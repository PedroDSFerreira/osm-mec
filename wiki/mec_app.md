# MEC App


## MEC Apps
### Create a MEC App and a MEC App Descriptor
### Instantiate a MEC App
### Deploy a MEC App
### Update a MEC APP
### Terminate a MEC APP


## MEC App Descriptor Fields

- mec-appd
  - id (**_value_**: mandatory)
  - name (**_value_**: mandatory)
  - provider (**_value_**: mandatory)
  - soft-version (**_value_**: mandatory)
  - version (**_value_**: mandatory)
  - mec-version (**_value_**: mandatory) 
  - info-name (**_value_**: non-mandatory)
  - description (**_value_**: mandatory)

- virtual-compute
  - id (**_value_**: mandatory)
  - logical-node-reqs 
    - id (**_array_**: non-mandatory)
    - logical-node-requirement-details (**_value_**: non-mandatory)
      - key (**_array_**: non-mandatory)
      - value (**_value_**: non-mandatory)
  - request-additional-capabilities
    - name (**_array_**: non-mandatory)
    - support-mandatory (**_value_**: non-mandatory)
    - min-requested-additional-capability-version (**_value_**: non-mandatory) 
    - preferred-requested-additional-capability-version (**_value_**: non-mandatory)
    - target-performance-parameters 
      - key (**_array_**: non-mandatory)
      - value (**_value_**: non-mandatory)
  - compute-requirements
    - key (**_array_**: non-mandatory)
    - value (**_value_**: non-mandatory)

  - virtual-memory
    - mem-size (**_value_**: mandatory)
    - mem-oversubscription-policy (**_value_**: non-mandatory)
    - vdu-mem-requirements 
      - key (**_array_**: non-mandatory)
      - value (**_value_**: non-mandatory)
    - numa-enabled (**_value_**: mandatory)

  - virtual-cpu
    - architecture (**_value_**: non-mandatory)
    - cpu-count (**_value_**: mandatory)
    - cpu-clock (**_value_**: non-mandatory)
    - cpu-oversubscription-policy (**_value_**: non-mandatory)
    - vdu-cpu-requirements 
      - key (**_array_**: non-mandatory)
      - value (**_value_**: non-mandatory)
    - cpu-pinning
      - pinning-policy (**_value_**: non-mandatory)
      - pinning-rule
        - key (**_array_**: non-mandatory)
        - value (**_value_**: non-mandatory)

  - virtual-disk
    - id (**_value_**: non-mandatory)
    - size-of-storage (**_value_**: non-mandatory)
    - vdu-storage-requirements 
      - key (**_array_**: non-mandatory)
      - value (**_value_**: non-mandatory)
    - rdma-enabled (**_value_**: non-mandatory)
    - sw-image-id (**_value_**: non-mandatory)

- sw-image
  - id (**_value_**: mandatory)
  - name (**_value_**: mandatory)
  - version (**_value_**: mandatory)
  - checksum (**_value_**: mandatory)
  - container-format (**_value_**: mandatory)
  - disk-format (**_value_**: non-mandatory)
  - min-disk (**_value_**: non-mandatory)
  - min-ram (**_value_**: non-mandatory)
  - size (**_value_**: mandatory)
  - sw-image (**_value_**: mandatory)
  - operating-system (**_value_**: non-mandatory)
  - supported-virtualisation-environment (**_array_**: non-mandatory)

- virtual-storage:
  - id (**_array_**: mandatory)
  - type-of-storage (**_value_**: mandatory)
    - block-storage 
        - size-of-storage (**_value_**: mandatory) 
        - vdu-storage-requirements
            - key (**_array_**: non-mandatory)
            - value (**_value_**: non-mandatory)
        - rdma-enabled (**_value_**: non-mandatory)
        - sw-image-id (**_value_**: non-mandatory) 
    - object-storage
        - max-size-of-storage (**_value_**: non-mandatory) 
    - file-storage 
        - size-of-storage (**_value_**: non-mandatory) 
        - file-system-protocol (**_value_**: non-mandatory) 
        - int-virtual-link-id (**_value_**: non-mandatory) 
    - nfvi-maintenance-info
        - impact-notification-lead-time (**_value_**: non-mandatory) 
        - is-impact-mitigation-requested (**_value_**: non-mandatory)
        - supported-migration-time (**_value_**: non-mandatory)
        - max-undetectable-interruption-time (**_value_**: non-mandatory)
        - min-recovery-time-between-impacts (**_value_**: non-mandatory) 
        - max-number-of-impacted-instances
            - id (**_array_**: non-mandatory)
            - group-size (**_value_**: non-mandatory) 
            - max-number-of-impacted-instances (**_value_**: non-mandatory)

- ext-cpd
  - id (**_array_**: non-mandatory)
  - k8s-cluster-net (**_value_**: non-mandatory)
  - virtual-network-interface-requirements
    - id (**_array_**: non-mandatory)
    - name (**_value_**: non-mandatory)
    - description (**_value_**: non-mandatory)
    - support-mandatory (**_value_**: non-mandatory)
    - network-interface-requirements 
      - key (**_array_**: non-mandatory)
      - value (**_value_**: non-mandatory)
    - niclo-requirements
      - id (**_array_**: non-mandatory)
      - logical-node-requirement-details
        - key (**_value_**: non-mandatory)
        - value (**_value_**: non-mandatory)
  - layer-protocol (**_array_**: non-mandatory)
  - cp-role (**_value_**: non-mandatory) 
  - description (**_value_**: non-mandatory)
  - trunk-mode (**_value_**: non-mandatory) 
  - security-group-rule-id (**_array_**: non-mandatory)
  - cp-protocol
    - associated-layer-protocol (**_array_**: non-mandatory)
    - address-data 
      - id (**_array_**: non-mandatory)
      - address-type (**_value_**: non-mandatory)
      - l2-address-data (**_value_**: non-mandatory)
      - l3-address-data
        - ip-address-assignment (**_value_**: non-mandatory)
        - ip-address-type (**_value_**: non-mandatory)
        - number-of-ip-addresses (**_value_**: non-mandatory)
        - floating-ip-activated (**_value_**: non-mandatory)
        - fixed-ip-address (**_value_**: non-mandatory)

- service-required
  - name (**_array_**: non-mandatory)
  - category
    - href (**_value_**: non-mandatory)
    - id (**_value_**: non-mandatory)
    - name (**_value_**: non-mandatory)
    - version (**_value_**: non-mandatory)
  - version (**_value_**: non-mandatory)
  - transport-dependencies
    - id (**_array_**: non-mandatory)
    - transport
      - name (**_value_**: non-mandatory)
      - description (**_value_**: non-mandatory)
      - type (**_value_**: non-mandatory)
      - protocol (**_value_**: non-mandatory)
      - version (**_value_**: non-mandatory)
      - security
        - oauth2-info
          - grant-types (**_array_**: non-mandatory)
          - token-endpoint (**_value_**: non-mandatory)
    - serializers (**_array_**: non-mandatory)
    - labels (**_array_**: non-mandatory)
  - requested-permissions (**_array_**: non-mandatory)

- service-optional
  - name (**_array_**: non-mandatory)
  - category
    - href (**_value_**: non-mandatory)
    - id (**_value_**: non-mandatory)
    - name (**_value_**: non-mandatory)
    - version (**_value_**: non-mandatory)
  - version
  - transport-dependencies
    - id (**_array_**: non-mandatory)
    - transport 
      - name (**_value_**: non-mandatory)
      - description (**_value_**: non-mandatory)
      - type (**_value_**: non-mandatory)
      - protocol (**_value_**: non-mandatory)
      - version (**_value_**: non-mandatory)
      - security 
        - oauth2-info
          - grant-types (**_array_**: non-mandatory)
          - token-endpoint (**_value_**: non-mandatory)
    - serializers (**_array_**: non-mandatory)
    - labels (**_array_**: non-mandatory)
  - requested-permissions (**_array_**: non-mandatory)

- service-produced
  - name (**_array_**: non-mandatory)
  - category
    - href (**_value_**: non-mandatory)
    - id (**_value_**: non-mandatory)
    - name (**_value_**: non-mandatory)
    - version (**_value_**: non-mandatory)
  - version (**_value_**: non-mandatory)
  - transports-supported
    - id (**_array_**: non-mandatory)
    - transport
      - name (**_value_**: non-mandatory)
      - description (**_value_**: non-mandatory)
      - type (**_value_**: non-mandatory)
      - protocol (**_value_**: non-mandatory)
      - version (**_array_**: non-mandatory)
      - security (**_array_**: non-mandatory)
        - oauth2-info
          - grant-types (**_array_**: non-mandatory)
          - token-endpoint (**_value_**: non-mandatory)
    - serializers (**_array_**: non-mandatory)
    - labels (**_array_**: non-mandatory)

- feature-required
  - name (**_value_**: non-mandatory)
  - version (**_value_**: non-mandatory)

- feature-optional
  - name (**_value_**: non-mandatory)
  - version (**_value_**: non-mandatory)

- transport-dependencies
  - id (**_array_**: non-mandatory)
  - transport
    - name (**_value_**: non-mandatory)
    - description (**_value_**: non-mandatory)
    - type (**_value_**: non-mandatory)
    - protocol (**_value_**: non-mandatory)
    - version (**_value_**: non-mandatory)
    - security (**_value_**: non-mandatory)
      - oauth2-info
        - grant-types (**_array_**: non-mandatory)
        - token-endpoint (**_value_**: non-mandatory)
  - serializers (**_array_**: non-mandatory)
  - labels (**_array_**: non-mandatory)

- traffic-rule
  - id (**_array_**: non-mandatory)
  - filter-type (**_value_**: non-mandatory)
  - priority (**_value_**: non-mandatory)
  - traffic-filter
    - id (**_array_**: non-mandatory)
    - src-address (**_value_**: non-mandatory)
    - dst-address (**_value_**: non-mandatory)
    - src-port (**_value_**: non-mandatory)
    - dst-port (**_value_**: non-mandatory)
    - protocol (**_value_**: non-mandatory)
    - tag (**_value_**: non-mandatory)
    - uri (**_value_**: non-mandatory)
    - packet-label (**_value_**: non-mandatory)
    - src-tunnel-address (**_value_**: non-mandatory)
    - tgt-tunnel-address (**_value_**: non-mandatory)
    - tgt-tunnel-address (**_value_**: non-mandatory)
    - src-tunnel-port (**_value_**: non-mandatory)
    - dst-tunnel-port (**_value_**: non-mandatory)
    - qci (**_value_**: non-mandatory)
    - dscp (**_value_**: non-mandatory)
    - tc (**_value_**: non-mandatory)
  - action (**_value_**: non-mandatory)
  - dst-interface
    - id (**_array_**: non-mandatory)
    - interface-type (**_value_**: non-mandatory)
    - tunnel-info
      - tunnel-type (**_value_**: non-mandatory)
      - tunnel-dst-address (**_value_**: non-mandatory)
      - tunnel-src-address (**_value_**: non-mandatory)
    - src-mac-address (**_value_**: non-mandatory)
    - dst-mac-address (**_value_**: non-mandatory)
    - dst-ip-address (**_value_**: non-mandatory)

- dns-rule
  - id (**_array_**: non-mandatory)
  - domain-name (**_value_**: non-mandatory)
  - ip-address-type (**_value_**: non-mandatory)
  - ip-address (**_value_**: non-mandatory)
  - ttl (**_value_**: non-mandatory)

- latency
  - max-latency (**_value_**: non-mandatory)

- terminate-app-instance-op-config
  - min-graceful-termination-timeout (**_value_**: non-mandatory)
  - max-recommended-graceful-termination-timeout (**_value_**: non-mandatory)
  - vnf-parameters
    - key (**_array_**: non-mandatory)
    - value (**_value_**: non-mandatory)

- change-app-instance-state-op-config
  - min-graceful-stop-timeout (**_value_**: non-mandatory)
  - max-recommended-graceful-stop-timeout (**_value_**: non-mandatory)
  - vnf-parameters
    - key (**_array_**: non-mandatory)
    - value (**_value_**: non-mandatory)

- user-context-transfer-capability
  - stateful-application (**_value_**: non-mandatory)
  - user-context-transfer-support (**_value_**: non-mandatory)

- network-policy
  - steered-network (**_value_**: non-mandatory)
    - cellular-network (**_value_**: non-mandatory)
    - wifi-network (**_value_**: non-mandatory)
    - fixed-access-network (**_value_**: non-mandatory)

- artifacts
  - name (**_array_**: non-mandatory)
  - description (**_value_**: non-mandatory)
  - type (**_value_**: non-mandatory)
  - file (**_value_**: non-mandatory)



