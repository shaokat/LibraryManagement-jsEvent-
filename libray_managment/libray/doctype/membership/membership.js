// Copyright (c) 2016, Hasan and contributors
// For license information, please see license.txt



frappe.ui.form.on("Membership", "member_name",
    function(frm) {

        frappe.call({
            "method": "frappe.client.get",
            args: {
                doctype: "Libray Member",
                name: frm.doc.member_name
            },
            callback: function (data) 
            {
				console.log(data)
				frm.set_value('member_frist_name', data.message.frist_name),
				frm.set_value('member_last_name', data.message.last_name),
				frm.set_value('status', data.message.status),
				frm.set_value('email',data.message.email),
				frm.set_value('phone',data.message.phone)
				
            }
        })
    });