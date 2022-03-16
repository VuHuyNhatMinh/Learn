package com.example.demo;

import lombok.AllArgsConstructor;
import lombok.Data;
import org.springframework.data.mongodb.core.mapping.Document;

@Data
@AllArgsConstructor
public class Address {
    private String country;
    private String postCode;
    private String city;
}
