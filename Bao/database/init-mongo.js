db = db.getSiblingDB('employee_db');  // Chọn cơ sở dữ liệu employee_db

// Tạo các collection cơ bản nếu cần
db.createCollection('campaigns');
db.createCollection('employees');
db.createCollection('results');

// Thêm dữ liệu mẫu vào các collection
db.campaigns.insertMany([
  { name: "Campaign 1", startDate: new Date(), endDate: new Date(new Date().setDate(new Date().getDate() + 10)) },
  { name: "Campaign 2", startDate: new Date(), endDate: new Date(new Date().setDate(new Date().getDate() + 20)) }
]);

db.employees.insertMany([
  { id: "E001", name: "John Doe" },
  { id: "E002", name: "Jane Smith" }
]);

db.results.insertMany([
  { employeeId: "E001", campaignName: "Campaign 1", startDate: new Date(), endDate: new Date(new Date().setDate(new Date().getDate() + 10)), distance: 10 },
  { employeeId: "E002", campaignName: "Campaign 2", startDate: new Date(), endDate: new Date(new Date().setDate(new Date().getDate() + 20)), distance: 15 }
]);
