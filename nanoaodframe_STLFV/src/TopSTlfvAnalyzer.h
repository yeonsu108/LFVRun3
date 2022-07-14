/*
 * TopSTlfvAnalyzer.h
 *
 *  Created on: April 9, 2020
 *      Author: Tae Jeong Kim 
 */

#ifndef TopSTlfvAnalyzer_H_
#define TopSTlfvAnalyzer_H_

#include "NanoAODAnalyzerrdframe.h"

class TopSTlfvAnalyzer: public NanoAODAnalyzerrdframe
{
	public:
		TopSTlfvAnalyzer(TTree *t, std::string outfilename, std::string year="", std::string syst="", std::string jsonfname="", string globaltag="", int nthreads=1);
		void defineCuts();
		void defineMoreVars(); // define higher-level variables from
		void bookHists();
        private:
                std::string _year;
                std::string _syst;

};



#endif /* TopSTlfvAnalyzer_H_ */
