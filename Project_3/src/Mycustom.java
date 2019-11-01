package org.myParser.lucene.search;
import org.apache.lucene.search.Query;
import org.apache.solr.common.params.DisMaxParams;
import org.apache.solr.common.params.ModifiableSolrParams;
import org.apache.solr.common.params.SolrParams;
import org.apache.solr.request.SolrQueryRequest;
import org.apache.solr.search.ExtendedDismaxQParser;
import org.apache.solr.search.ExtendedDismaxQParserPlugin;
import org.apache.solr.search.QParser;
import org.apache.solr.search.QParserPlugin;
import org.apache.solr.search.SyntaxError;
public class Mycustom extends ExtendedDismaxQParser{
	
	public Mycustom(String qstr, SolrParams localParams, SolrParams params, SolrQueryRequest req) {
		super(qstr, localParams, params, req);
		// TODO Auto-generated constructor stub
	}

	@Override
	public Query parse() throws SyntaxError {
		// TODO Auto-generated method stub
		return null;
	}

	
}
