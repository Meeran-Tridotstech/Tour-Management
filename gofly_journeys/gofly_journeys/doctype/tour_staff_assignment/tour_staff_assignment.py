import frappe
from frappe.model.document import Document

class TourStaffAssignment(Document):

    def on_update(self):
        self.update_travel_plan_guide()

    def update_travel_plan_guide(self):
        if not self.booking or not self.guide_id:
            return

        # 🧩 Find the Travel Plan record with the same booking
        travel_plan_name = frappe.db.get_value("Travel Plan", {"booking": self.booking}, "name")

        if travel_plan_name:
            # ✅ Update its guide field with the current guide_id
            frappe.db.set_value("Travel Plan", travel_plan_name, "guide", self.guide_id)
            frappe.msgprint(f"Guide updated in Travel Plan {travel_plan_name}")
        else:
            frappe.msgprint("⚠️ No Travel Plan found for this booking.")
