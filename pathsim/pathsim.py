#!/usr/bin/env python
import os
import sys
from StringIO import StringIO
from collections import defaultdict
import operator


class DBLPnetwork_PathSim:
    def __init__(self, author, venue, paper, relation):

        self.author_dict = {}
        self.venue_dict = {}
        self.paper_dict = {}
        self.relation_dict = defaultdict(list)
        self.author_paper_dict = defaultdict(list)
        self.paper_venue_dict = defaultdict(list)
        self.APV_dict = defaultdict(list)
        self.AV_dict = {}
        self.AA_dict_APVPA = {}
        self.AA_dict_APTPA = {}
        self.part1_AA_dict_APVPA = {}
        self.part1_AA_dict_APTPA = {}
        self.part2_AA_dict_APVPA = {}
        self.part2_AA_dict_APTPA = {}
        self._file_to_dict(author, venue, paper, relation)
        self._build_paths()
        self._build_APV_path()

    def _file_to_dict(self, author, venue, paper, relation):

        self._read_relation(relation)
        self._read_author(author)
        self._read_venue(venue)
        self._read_paper(paper)

    def _read_relation(self, relation):

        with open(relation) as r:
            for line in r:
                (key, val, none) = line.split()
                self.relation_dict[key].append(val)

        print "Relation Length : %d" % len(self.relation_dict)

    def _read_author(self, author):

        with open(author) as a:
            for line in a:
                splitLine = line.split()
                self.author_dict[splitLine[0]] = ' '.join(splitLine[1:])

        print "Author Length : %d" % len(self.author_dict)

    def _read_venue(self, venue):

        with open(venue) as v:
            for line in v:
                splitLine = line.split()
                self.venue_dict[splitLine[0]] = ' '.join(splitLine[1:])
        print "Venue Length : %d" % len(self.venue_dict)

    def _read_paper(self, paper):

        with open(paper) as p:
            for line in p:
                splitLine = line.split()
                self.paper_dict[splitLine[0]] = ' '.join(splitLine[1:])
        print "Paper Length : %d" % len(self.paper_dict)

    def _build_paths(self):

        for paperid, ids in self.relation_dict.iteritems():
            if self.paper_dict.has_key(paperid):
                paper = self.paper_dict.get(paperid)
            else:
                break

            for i in ids:
                # Build author paper path in the author_paper_dict
                if self.author_dict.has_key(i):
                    author = self.author_dict.get(i)
                    self.author_paper_dict[author].append(paper)
                # Build paper venue path in the venue_paper_dict 
                elif self.venue_dict.has_key(i):
                    venue = self.venue_dict.get(i)
                    self.paper_venue_dict[paper].append(venue)

        print "author-paper Length : %d" % len(self.author_paper_dict)
        print "paper_venue Length : %d" % len(self.paper_venue_dict)

    def _build_APV_path(self):

        for author, papers in self.author_paper_dict.iteritems():
            for paper in papers:
                # Build APV path (author_paper_venue)
                if self.paper_venue_dict.has_key(paper):
                    venues = self.paper_venue_dict.get(paper)
                    for venue in venues:
                        # APV path
                        self.APV_dict[author].append((paper, venue))
                        # AV path
                        if (self.AV_dict.has_key((author, venue))):
                            val = self.AV_dict.get((author, venue)) + 1
                            self.AV_dict[(author, venue)] = val
                        else:
                            self.AV_dict[(author, venue)] = 1

    def _find_venues_for_an_author(self, an_author):

        ret_dict = {}
        for venueid, venuename in self.venue_dict.iteritems():
            if (self.AV_dict.has_key((an_author, venuename))):
                ret_dict[venuename] = self.AV_dict.get((an_author, venuename))
        return ret_dict

    def get_self_to_self(self, num_paths):
        return int(num_paths) * int(num_paths)

    def build_AA_dict_APVPA(self, an_author):

        venuedict = self._find_venues_for_an_author(an_author)
        venuelist = venuedict.keys()
        fullvenuelist = self.venue_dict.values()

        fenzi = {}
        fenmu = {}

        for (author, venue), num_to_author in self.AV_dict.iteritems():
            fenzi.setdefault(author, 0)
            fenmu.setdefault(author, 0)
            self.part2_AA_dict_APVPA.setdefault(author, 0)
            self.part1_AA_dict_APVPA.setdefault(author, 0)

            if venue in fullvenuelist:
                # num_from_an_author = venuedict.get(venue)
                # an_author_self_paths = self.get_self_to_self(num_from_an_author)

                author_self_paths = self.get_self_to_self(num_to_author)

                self.part2_AA_dict_APVPA[author] = fenmu[author] + author_self_paths
                fenmu[author] = fenmu[author] + author_self_paths

            if venue in venuelist:
                num_from_an_author = venuedict.get(venue)

                self.part1_AA_dict_APVPA[author] = 2.00 * (fenzi[author] + num_from_an_author * num_to_author)
                fenzi[author] = fenzi[author] + num_from_an_author * num_to_author

        # print self.part2_AA_dict_APVPA
        # print self.part1_AA_dict_APVPA

        for author in self.author_dict.values():
            self.AA_dict_APVPA[author] = self.part1_AA_dict_APVPA[author] / (
            self.part2_AA_dict_APVPA[an_author] + self.part2_AA_dict_APVPA[author])
        '''if author == 'Mary':
                #print num_from_an_author,num_to_author,an_author_self_paths,author_self_paths
            print self.AA_dict_APVPA[author]'''
        # print self.AA_dict_APVPA

        return self.AA_dict_APVPA

    def find_top_10_similar_authors_APVPA(self, an_author):

        self.build_AA_dict_APVPA(an_author)
        sorted_AA_dict_APVPA = sorted(self.AA_dict_APVPA.items(), key=operator.itemgetter(1), reverse=True)[:10]
        ret_list = []
        for key, value in sorted_AA_dict_APVPA:
            ret_list.append(key)
        print sorted_AA_dict_APVPA
        return ret_list

    def print_dict(self, dict):

        for key, value in dict.iteritems():
            print key + ':' + str(value)

    def print_dict_tuple_key(self, dict):
        for (k1, k2), value in dict.iteritems():
            print k1 + "," + k2 + ":" + str(value)

    def print_defaultdict(self, dict):

        for key, values in dict.iteritems():
            print key + ':' + ', '.join(values)

    def print_defaultdict_tuple_value(self, dict):

        for line in dict.iteritems():
            print line
            # print key + ':' + ', '.join(str(i) for i in values)


def main():
    dblp = DBLPnetwork_PathSim('author.txt', 'venue.txt', 'paper.txt', 'relation.txt')

    print "============Top 10 using APVPA for Mike================="
    ADlist_APVPA = dblp.find_top_10_similar_authors_APVPA("Mike")

    for author in ADlist_APVPA:
        print author


if __name__ == "__main__":
    main()
