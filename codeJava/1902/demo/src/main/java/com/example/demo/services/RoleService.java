package com.example.demo.services;

import com.example.demo.models.Role;
import com.example.demo.repository.RoleRepository;
import lombok.AllArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
@AllArgsConstructor
public class RoleService {

    @Autowired
    private final RoleRepository roleRepository;

    // POST method: add new role to DB
    public Role addNewRole(Role role) {
        return roleRepository.insert(role);
    }

    // GET method: get all roles in DB
    public List<Role> getAllRole() {
        return roleRepository.findAll();
    }

    // GET method: get a role by id
    public Role getRoleById(String id) {
        Optional<Role> role = roleRepository.findById(id);
        if (role.isPresent()) {
            return role.get();
        } else {
            return null;
        }
    }

    // PUT method: edit a Role by id
    public Role editRole(Role update, String id) {
        Optional<Role> role = roleRepository.findById(id);
        if (role.isPresent()) {
            return roleRepository.save(update);
        } else {
            return null;
        }
    }

    // DELETE method: delete a Role by id
    public String deleteRole(String id) {
        Optional<Role> role = roleRepository.findById(id);
        if (role.isPresent()) {
            roleRepository.deleteById(id);
            return "success";
        } else {
            return null;
        }
    }
}
