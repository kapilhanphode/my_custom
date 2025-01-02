/** @odoo-module **/

import { ListController } from '@web/views/list/list_controller';
import { registry } from '@web/core/registry';
import { listView } from '@web/views/list/list_view';
import { useService } from "@web/core/utils/hooks";


export class CustomListController extends ListController {
    /**
     * Validate all the records selected
     */
     setup(){
        super.setup();
        this.orm = useService("orm");
        this.dialog = useService("dialog");
     }
     async onCustomReturnAction() {
        this.actionService.doAction({
            type: 'ir.actions.act_window',
            res_model: 'sale.order.template',
            views: [[false, 'form']],
            view_mode: "form",
            name: 'Custom',
            target: 'new',
            res_id: false,
//          context: {'default_record': record.id},
        });
    }
    async onCustomReturnFunction() {
        try {
            const result = await this.orm.call(
                        'sale.order',
                        'sale_list_view_button',
                        [null],
                        {}
            );

            if (result) {
                alert("Custom Button Clicked SuccessFully !!");
                return;
            }
        } catch (error) {
            console.error("Error in Custom Button   :", error);
        }
    }
}

registry.category('views').add('list_view_button', {
    ...listView,
    Controller: CustomListController,
    buttonTemplate: 'Custom.ListView.Buttons',
});
