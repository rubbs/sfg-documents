import logging
from sfg_letter import SfgLetter

logger = logging.getLogger('sfg')

class SfgTermination(object):


    def create_termination(self, data):
        logger.info('create_termination')
        term = SfgLetter();

        return term.get_pdf();
