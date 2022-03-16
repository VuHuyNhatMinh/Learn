package com.example.demo.models;

import lombok.AllArgsConstructor;
import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Data
@AllArgsConstructor
@Document("role")
public class Role {
    @Id
    String id;
    String name;
    Long createTime;
    Long lastUpdateTime;
}
