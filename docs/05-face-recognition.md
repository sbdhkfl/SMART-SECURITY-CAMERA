# 05 - Local Face Recognition

## Design

Face recognition is performed on the Orange Pi, not by a cloud service.

The system keeps a local enrollment database and supports a configurable number of people. The default project configuration allows 50 people and can be changed.

## Enrollment

Each person should have multiple samples captured with small changes in angle and expression. Multiple samples are more useful than relying on one photograph.

## Recognition

The pipeline will:
1. detect faces
2. generate a face representation
3. compare it with enrolled representations
4. apply a configurable threshold
5. return a known label or unknown

## Safety and privacy

Recognition is not perfect. Lighting, camera angle, motion, occlusion, and similar-looking faces can cause false matches or missed matches. The system should treat recognition as an automation signal, not proof of identity.

Face data should remain local and should be deletable by the owner.
