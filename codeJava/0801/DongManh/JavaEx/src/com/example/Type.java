package com.example;

public enum Type {
    EXPERIENCE, FRESHER, INTERN;

    public String toString() {
        switch (this) {
            case INTERN: return "2";
            case FRESHER: return "1";
            case EXPERIENCE: return "0";
        }
        return null;
    }
}
