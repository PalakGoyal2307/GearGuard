from odoo import models, fields, api

class GearRequest(models.Model):
    _name = 'gear.request'
    _description = 'Maintenance Request'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    subject = fields.Char(string="Subject", required=True)
    description = fields.Text(string="Description")
    
    # Relations
    equipment_id = fields.Many2one('gear.equipment', string="Equipment", required=True)
    team_id = fields.Many2one('gear.team', string="Team")
    technician_id = fields.Many2one('res.users', string="Technician")
    
    # Logistics
    scheduled_date = fields.Date(string="Scheduled Date", default=fields.Date.context_today)
    duration = fields.Float(string="Duration (Hours)")
    
    request_type = fields.Selection([
        ('corrective', 'Corrective'),
        ('preventive', 'Preventive')
    ], string="Type", default='corrective')
    
    stage = fields.Selection([
        ('new', 'New'),
        ('progress', 'In Progress'),
        ('repaired', 'Repaired'),
        ('scrap', 'Scrap')
    ], string="Stage", default='new', group_expand='_expand_stages', tracking=True)

    # Hackathon "Must Have": Auto-Fill Team based on Equipment
    @api.onchange('equipment_id')
    def _onchange_equipment_id(self):
        if self.equipment_id:
            self.team_id = self.equipment_id.maintenance_team_id

    # Hackathon "Must Have": Scrap Logic
    def write(self, vals):
        if 'stage' in vals and vals['stage'] == 'scrap':
            for record in self:
                record.equipment_id.is_scrapped = True
        return super(GearRequest, self).write(vals)

    def _expand_stages(self, states, domain, order):
        return [key for key, val in type(self).stage.selection]