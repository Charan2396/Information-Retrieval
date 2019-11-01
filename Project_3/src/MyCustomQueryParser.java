package org.myParser.lucene.search;

import org.apache.solr.common.params.DisMaxParams;
import org.apache.solr.common.params.ModifiableSolrParams;
import org.apache.solr.common.params.SolrParams;
import org.apache.solr.request.SolrQueryRequest;
import org.apache.solr.search.ExtendedDismaxQParser;
import org.apache.solr.search.ExtendedDismaxQParserPlugin;
import org.apache.solr.search.QParser;
import org.apache.solr.search.QParserPlugin;
public class MyCustomQueryParser extends ExtendedDismaxQParserPlugin {
	String[] fields= {"text_en", "text_de", "text_ru"};
	@Override
	  public QParser createParser(String qstr, SolrParams localParams, SolrParams params, SolrQueryRequest req) {
		ModifiableSolrParams newParams=new ModifiableSolrParams();
		if(qstr.contains("lang:en"))
		{
			fields[0]="text_en^2";
		}
		if(qstr.contains("lang:de"))
		{
			fields[1]="text_de^2";
		}
		if(qstr.contains("lang:ru"))
		{
			fields[2]="text_ru^2";
		}
		
		newParams.add(DisMaxParams.QF, fields);
		params=SolrParams.wrapAppended(params, newParams);
	    return new ExtendedDismaxQParser(qstr, localParams, params, req);
	  }
}
 
