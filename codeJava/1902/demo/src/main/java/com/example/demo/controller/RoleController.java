package com.example.demo.controller;

import com.example.demo.models.Role;
import com.example.demo.services.RoleService;
import lombok.AllArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@AllArgsConstructor
@RequestMapping("role")
public class RoleController {
    @Autowired
    private final RoleService roleService;

    @PostMapping
    public Role postRole(@RequestBody Role role) {
        return roleService.addNewRole(role);
    }

    @GetMapping
    public List<Role> getAllRole() {
        return roleService.getAllRole();
    }

    @GetMapping(path = "{id}")
    public Role getRoleById(@PathVariable String id) {
        return roleService.getRoleById(id);
    }

    @PutMapping(path = "{id}")
    public Role putRole(@RequestBody Role role, @PathVariable String id) {
        return roleService.editRole(role, id);
    }

    @DeleteMapping(path = "{id}")
    public String deleteRole(@PathVariable String id) {
        return roleService.deleteRole(id);
    }
}
