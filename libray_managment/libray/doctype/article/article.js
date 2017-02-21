// Copyright (c) 2016, Hasan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Article', {

	onload:function(frm)
	{
		frm.set_query('article',function()
		{
			return{
				filters:[
					{"has_variant":1}
				]
			}
		});



		/*frm.add_fetch('article', 'article_name', 'article_name')
		frm.add_fetch('article', 'language', 'language')*/
	},
	article:function(frm)
	{

		 frappe.call({
            "method": "frappe.client.get",
            args: {
                doctype: "Templete Article",
                name: frm.doc.article
            },
            callback: function (data) 
            {
				console.log(data)
				frm.set_value('article_name', data.message.article_name)
				
            }
        })
	},

	refresh: function(frm) {


	}
});
