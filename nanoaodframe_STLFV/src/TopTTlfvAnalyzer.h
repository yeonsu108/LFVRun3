/*
 * TopTTlfvAnalyzer.h
 *
 *  Created on: April 9, 2020
 *      Author: Tae Jeong Kim 
 */

#ifndef TopTTlfvAnalyzer_H_
#define TopTTlfvAnalyzer_H_

#include "NanoAODAnalyzerrdframe.h"

class TopTTlfvAnalyzer: public NanoAODAnalyzerrdframe
{
	public:
		TopTTlfvAnalyzer(TTree *t, std::string outfilename, std::string year="", std::string syst="", std::string jsonfname="", string globaltag="", int nthreads=1);
		void defineCuts();
		void defineMoreVars(); // define higher-level variables from
		void bookHists();
        private:
                std::string _year;
                std::string _syst;

};



#endif /* TopTTlfvAnalyzer_H_ */
