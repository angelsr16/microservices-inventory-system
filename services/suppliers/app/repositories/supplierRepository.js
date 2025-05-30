const pool = require("../db");

class SupplierRepository {
    async getAll() {
        const { rows } = await pool.query("SELECT * FROM suppliers ORDER BY name")
        return rows;
    }

    async getById(id) {
        const { rows } = await pool.query("SELECT * FROM suppliers WHERE id = $1", [id])
        return rows[0]
    }

    async create(){
        
    }
}