from odoo import models, fields, api

class GearEquipment(models.Model):
    _name = 'gear.equipment'
    _description = 'GearGuard Equipment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Equipment Name", required=True, tracking=True)
    serial_number = fields.Char(string="Serial Number")
    purchase_date = fields.Date(string="Purchase Date")
    location = fields.Char(string="Physical Location")
    
    # Links to other Odoo modules
    department_id = fields.Many2one('hr.department', string="Department")
    employee_id = fields.Many2one('res.users', string="Assigned Employee")
    
    # Links to our own modules
    maintenance_team_id = fields.Many2one('gear.team', string="Maintenance Team")
    technician_id = fields.Many2one('res.users', string="Default Technician")
    
    # Smart Button Logic
    request_count = fields.Integer(compute='_compute_request_count', string="Request Count")
    is_scrapped = fields.Boolean(string="Is Scrapped", default=False, tracking=True)

    def _compute_request_count(self):
        for record in self:
            record.request_count = self.env['gear.request'].search_count([('equipment_id', '=', record.id)])

    def action_view_requests(self):
        return {
            'name': 'Maintenance Requests',
            'type': 'ir.actions.act_window',
            'res_model': 'gear.request',
            'view_mode': 'kanban,tree,form',
            'domain': [('equipment_id', '=', self.id)],
            'context': {'default_equipment_id': self.id},
        }