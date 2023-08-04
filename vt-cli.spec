# Generated by go2rpm 1.9.0
%bcond_without check

# https://github.com/VirusTotal/vt-cli
%global goipath         github.com/VirusTotal/vt-cli
Version:                0.14.0
%global tag             0.14.0

%gometa -f


%global common_description %{expand:
VirusTotal Command Line Interface.}

%global golicenses      LICENSE
%global godocs          doc AUTHORS README.md man/vt.md man/vt_analysis.md\\\
                        man/vt_collection.md\\\
                        man/vt_collection_attack_techniques.md\\\
                        man/vt_collection_autogenerated_graphs.md\\\
                        man/vt_collection_comments.md\\\
                        man/vt_collection_create.md\\\
                        man/vt_collection_delete.md\\\
                        man/vt_collection_domains.md\\\
                        man/vt_collection_files.md\\\
                        man/vt_collection_ip_addresses.md\\\
                        man/vt_collection_owner.md\\\
                        man/vt_collection_references.md\\\
                        man/vt_collection_relationships.md\\\
                        man/vt_collection_remove.md\\\
                        man/vt_collection_rename.md\\\
                        man/vt_collection_sigma_rules.md\\\
                        man/vt_collection_stats.md\\\
                        man/vt_collection_subscribed_users.md\\\
                        man/vt_collection_subscription_preferences.md\\\
                        man/vt_collection_threat_actors.md\\\
                        man/vt_collection_update.md man/vt_collection_urls.md\\\
                        man/vt_collection_yara_rulesets.md\\\
                        man/vt_completion.md man/vt_domain.md\\\
                        man/vt_domain_caa_records.md\\\
                        man/vt_domain_cname_records.md\\\
                        man/vt_domain_collections.md\\\
                        man/vt_domain_comments.md\\\
                        man/vt_domain_communicating_files.md\\\
                        man/vt_domain_downloaded_files.md\\\
                        man/vt_domain_graphs.md\\\
                        man/vt_domain_historical_ssl_certificates.md\\\
                        man/vt_domain_historical_whois.md\\\
                        man/vt_domain_immediate_parent.md\\\
                        man/vt_domain_memory_pattern_parents.md\\\
                        man/vt_domain_mx_records.md\\\
                        man/vt_domain_ns_records.md man/vt_domain_parent.md\\\
                        man/vt_domain_references.md\\\
                        man/vt_domain_referrer_files.md\\\
                        man/vt_domain_related_attack_techniques.md\\\
                        man/vt_domain_related_comments.md\\\
                        man/vt_domain_related_references.md\\\
                        man/vt_domain_related_threat_actors.md\\\
                        man/vt_domain_relationships.md\\\
                        man/vt_domain_resolutions.md\\\
                        man/vt_domain_siblings.md\\\
                        man/vt_domain_soa_records.md\\\
                        man/vt_domain_subdomains.md man/vt_domain_urls.md\\\
                        man/vt_domain_user_votes.md man/vt_domain_votes.md\\\
                        man/vt_download.md man/vt_file.md\\\
                        man/vt_file_analyses.md man/vt_file_behaviours.md\\\
                        man/vt_file_bundled_files.md\\\
                        man/vt_file_carbonblack_children.md\\\
                        man/vt_file_carbonblack_parents.md\\\
                        man/vt_file_ciphered_bundled_files.md\\\
                        man/vt_file_ciphered_parents.md man/vt_file_clues.md\\\
                        man/vt_file_code_blocks.md man/vt_file_collections.md\\\
                        man/vt_file_comments.md\\\
                        man/vt_file_compressed_parents.md\\\
                        man/vt_file_contacted_domains.md\\\
                        man/vt_file_contacted_ips.md\\\
                        man/vt_file_contacted_urls.md\\\
                        man/vt_file_distributors.md\\\
                        man/vt_file_dropped_files.md\\\
                        man/vt_file_email_attachments.md\\\
                        man/vt_file_email_parents.md\\\
                        man/vt_file_email_senders.md\\\
                        man/vt_file_embedded_domains.md\\\
                        man/vt_file_embedded_ips.md\\\
                        man/vt_file_embedded_urls.md\\\
                        man/vt_file_execution_parents.md\\\
                        man/vt_file_graphs.md man/vt_file_hash_collisions.md\\\
                        man/vt_file_itw_domains.md man/vt_file_itw_ips.md\\\
                        man/vt_file_itw_urls.md\\\
                        man/vt_file_memory_pattern_domains.md\\\
                        man/vt_file_memory_pattern_ips.md\\\
                        man/vt_file_memory_pattern_urls.md\\\
                        man/vt_file_overlay_children.md\\\
                        man/vt_file_overlay_parents.md\\\
                        man/vt_file_pcap_children.md\\\
                        man/vt_file_pcap_parents.md\\\
                        man/vt_file_pe_resource_children.md\\\
                        man/vt_file_pe_resource_parents.md\\\
                        man/vt_file_references.md\\\
                        man/vt_file_related_attack_techniques.md\\\
                        man/vt_file_related_references.md\\\
                        man/vt_file_related_threat_actors.md\\\
                        man/vt_file_relationships.md\\\
                        man/vt_file_screenshots.md\\\
                        man/vt_file_sigma_analysis.md\\\
                        man/vt_file_similar_files.md\\\
                        man/vt_file_submissions.md\\\
                        man/vt_file_urls_for_embedded_js.md\\\
                        man/vt_file_user_votes.md man/vt_file_votes.md\\\
                        man/vt_group.md man/vt_group_privileges.md\\\
                        man/vt_group_privileges_grant.md\\\
                        man/vt_group_privileges_revoke.md man/vt_hunting.md\\\
                        man/vt_hunting_notification.md\\\
                        man/vt_hunting_notification_delete.md\\\
                        man/vt_hunting_notification_list.md\\\
                        man/vt_hunting_notification_list_delete.md\\\
                        man/vt_hunting_ruleset.md\\\
                        man/vt_hunting_ruleset_add.md\\\
                        man/vt_hunting_ruleset_delete.md\\\
                        man/vt_hunting_ruleset_disable.md\\\
                        man/vt_hunting_ruleset_enable.md\\\
                        man/vt_hunting_ruleset_list.md\\\
                        man/vt_hunting_ruleset_notification_emails.md\\\
                        man/vt_hunting_ruleset_rename.md\\\
                        man/vt_hunting_ruleset_setlimit.md\\\
                        man/vt_hunting_ruleset_update.md man/vt_init.md\\\
                        man/vt_iocstream.md man/vt_iocstream_delete.md\\\
                        man/vt_iocstream_list.md man/vt_ip.md\\\
                        man/vt_ip_collections.md man/vt_ip_comments.md\\\
                        man/vt_ip_communicating_files.md\\\
                        man/vt_ip_downloaded_files.md man/vt_ip_graphs.md\\\
                        man/vt_ip_historical_ssl_certificates.md\\\
                        man/vt_ip_historical_whois.md\\\
                        man/vt_ip_memory_pattern_parents.md\\\
                        man/vt_ip_references.md man/vt_ip_referrer_files.md\\\
                        man/vt_ip_related_attack_techniques.md\\\
                        man/vt_ip_related_comments.md\\\
                        man/vt_ip_related_references.md\\\
                        man/vt_ip_related_threat_actors.md\\\
                        man/vt_ip_relationships.md man/vt_ip_resolutions.md\\\
                        man/vt_ip_urls.md man/vt_ip_user_votes.md\\\
                        man/vt_ip_votes.md man/vt_man.md man/vt_meta.md\\\
                        man/vt_monitor.md man/vt_monitor_analyses.md\\\
                        man/vt_monitor_comments.md man/vt_monitor_delete.md\\\
                        man/vt_monitor_deletedetails.md\\\
                        man/vt_monitor_download.md man/vt_monitor_list.md\\\
                        man/vt_monitor_owner.md\\\
                        man/vt_monitor_relationships.md\\\
                        man/vt_monitor_setdetails.md man/vt_monitor_upload.md\\\
                        man/vt_monitorpartner.md\\\
                        man/vt_monitorpartner_analyses.md\\\
                        man/vt_monitorpartner_comments.md\\\
                        man/vt_monitorpartner_download.md\\\
                        man/vt_monitorpartner_items.md\\\
                        man/vt_monitorpartner_list.md\\\
                        man/vt_monitorpartner_relationships.md\\\
                        man/vt_retrohunt.md man/vt_retrohunt_abort.md\\\
                        man/vt_retrohunt_delete.md man/vt_retrohunt_list.md\\\
                        man/vt_retrohunt_matches.md man/vt_retrohunt_start.md\\\
                        man/vt_scan.md man/vt_scan_file.md man/vt_scan_url.md\\\
                        man/vt_search.md man/vt_search_content.md\\\
                        man/vt_url.md man/vt_url_analyses.md\\\
                        man/vt_url_collections.md man/vt_url_comments.md\\\
                        man/vt_url_communicating_files.md\\\
                        man/vt_url_contacted_domains.md\\\
                        man/vt_url_contacted_ips.md\\\
                        man/vt_url_downloaded_files.md\\\
                        man/vt_url_embedded_js_files.md man/vt_url_graphs.md\\\
                        man/vt_url_http_response_contents.md\\\
                        man/vt_url_last_serving_ip_address.md\\\
                        man/vt_url_memory_pattern_parents.md\\\
                        man/vt_url_network_location.md\\\
                        man/vt_url_redirecting_urls.md\\\
                        man/vt_url_redirects_to.md man/vt_url_references.md\\\
                        man/vt_url_referrer_files.md\\\
                        man/vt_url_referrer_urls.md\\\
                        man/vt_url_related_attack_techniques.md\\\
                        man/vt_url_related_collections.md\\\
                        man/vt_url_related_comments.md\\\
                        man/vt_url_related_references.md\\\
                        man/vt_url_related_threat_actors.md\\\
                        man/vt_url_relationships.md man/vt_url_submissions.md\\\
                        man/vt_url_urls_related_by_tracker_id.md\\\
                        man/vt_url_user_votes.md man/vt_url_votes.md\\\
                        man/vt_user.md man/vt_user_privileges.md\\\
                        man/vt_user_privileges_grant.md\\\
                        man/vt_user_privileges_revoke.md man/vt_version.md

Name:           %{goname}
Release:        %autorelease
Summary:        VirusTotal Command Line Interface

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
for cmd in vt; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc doc AUTHORS README.md man/vt.md man/vt_analysis.md man/vt_collection.md
%doc man/vt_collection_attack_techniques.md
%doc man/vt_collection_autogenerated_graphs.md man/vt_collection_comments.md
%doc man/vt_collection_create.md man/vt_collection_delete.md
%doc man/vt_collection_domains.md man/vt_collection_files.md
%doc man/vt_collection_ip_addresses.md man/vt_collection_owner.md
%doc man/vt_collection_references.md man/vt_collection_relationships.md
%doc man/vt_collection_remove.md man/vt_collection_rename.md
%doc man/vt_collection_sigma_rules.md man/vt_collection_stats.md
%doc man/vt_collection_subscribed_users.md
%doc man/vt_collection_subscription_preferences.md
%doc man/vt_collection_threat_actors.md man/vt_collection_update.md
%doc man/vt_collection_urls.md man/vt_collection_yara_rulesets.md
%doc man/vt_completion.md man/vt_domain.md man/vt_domain_caa_records.md
%doc man/vt_domain_cname_records.md man/vt_domain_collections.md
%doc man/vt_domain_comments.md man/vt_domain_communicating_files.md
%doc man/vt_domain_downloaded_files.md man/vt_domain_graphs.md
%doc man/vt_domain_historical_ssl_certificates.md
%doc man/vt_domain_historical_whois.md man/vt_domain_immediate_parent.md
%doc man/vt_domain_memory_pattern_parents.md man/vt_domain_mx_records.md
%doc man/vt_domain_ns_records.md man/vt_domain_parent.md
%doc man/vt_domain_references.md man/vt_domain_referrer_files.md
%doc man/vt_domain_related_attack_techniques.md
%doc man/vt_domain_related_comments.md man/vt_domain_related_references.md
%doc man/vt_domain_related_threat_actors.md man/vt_domain_relationships.md
%doc man/vt_domain_resolutions.md man/vt_domain_siblings.md
%doc man/vt_domain_soa_records.md man/vt_domain_subdomains.md
%doc man/vt_domain_urls.md man/vt_domain_user_votes.md man/vt_domain_votes.md
%doc man/vt_download.md man/vt_file.md man/vt_file_analyses.md
%doc man/vt_file_behaviours.md man/vt_file_bundled_files.md
%doc man/vt_file_carbonblack_children.md man/vt_file_carbonblack_parents.md
%doc man/vt_file_ciphered_bundled_files.md man/vt_file_ciphered_parents.md
%doc man/vt_file_clues.md man/vt_file_code_blocks.md man/vt_file_collections.md
%doc man/vt_file_comments.md man/vt_file_compressed_parents.md
%doc man/vt_file_contacted_domains.md man/vt_file_contacted_ips.md
%doc man/vt_file_contacted_urls.md man/vt_file_distributors.md
%doc man/vt_file_dropped_files.md man/vt_file_email_attachments.md
%doc man/vt_file_email_parents.md man/vt_file_email_senders.md
%doc man/vt_file_embedded_domains.md man/vt_file_embedded_ips.md
%doc man/vt_file_embedded_urls.md man/vt_file_execution_parents.md
%doc man/vt_file_graphs.md man/vt_file_hash_collisions.md
%doc man/vt_file_itw_domains.md man/vt_file_itw_ips.md man/vt_file_itw_urls.md
%doc man/vt_file_memory_pattern_domains.md man/vt_file_memory_pattern_ips.md
%doc man/vt_file_memory_pattern_urls.md man/vt_file_overlay_children.md
%doc man/vt_file_overlay_parents.md man/vt_file_pcap_children.md
%doc man/vt_file_pcap_parents.md man/vt_file_pe_resource_children.md
%doc man/vt_file_pe_resource_parents.md man/vt_file_references.md
%doc man/vt_file_related_attack_techniques.md man/vt_file_related_references.md
%doc man/vt_file_related_threat_actors.md man/vt_file_relationships.md
%doc man/vt_file_screenshots.md man/vt_file_sigma_analysis.md
%doc man/vt_file_similar_files.md man/vt_file_submissions.md
%doc man/vt_file_urls_for_embedded_js.md man/vt_file_user_votes.md
%doc man/vt_file_votes.md man/vt_group.md man/vt_group_privileges.md
%doc man/vt_group_privileges_grant.md man/vt_group_privileges_revoke.md
%doc man/vt_hunting.md man/vt_hunting_notification.md
%doc man/vt_hunting_notification_delete.md man/vt_hunting_notification_list.md
%doc man/vt_hunting_notification_list_delete.md man/vt_hunting_ruleset.md
%doc man/vt_hunting_ruleset_add.md man/vt_hunting_ruleset_delete.md
%doc man/vt_hunting_ruleset_disable.md man/vt_hunting_ruleset_enable.md
%doc man/vt_hunting_ruleset_list.md
%doc man/vt_hunting_ruleset_notification_emails.md
%doc man/vt_hunting_ruleset_rename.md man/vt_hunting_ruleset_setlimit.md
%doc man/vt_hunting_ruleset_update.md man/vt_init.md man/vt_iocstream.md
%doc man/vt_iocstream_delete.md man/vt_iocstream_list.md man/vt_ip.md
%doc man/vt_ip_collections.md man/vt_ip_comments.md
%doc man/vt_ip_communicating_files.md man/vt_ip_downloaded_files.md
%doc man/vt_ip_graphs.md man/vt_ip_historical_ssl_certificates.md
%doc man/vt_ip_historical_whois.md man/vt_ip_memory_pattern_parents.md
%doc man/vt_ip_references.md man/vt_ip_referrer_files.md
%doc man/vt_ip_related_attack_techniques.md man/vt_ip_related_comments.md
%doc man/vt_ip_related_references.md man/vt_ip_related_threat_actors.md
%doc man/vt_ip_relationships.md man/vt_ip_resolutions.md man/vt_ip_urls.md
%doc man/vt_ip_user_votes.md man/vt_ip_votes.md man/vt_man.md man/vt_meta.md
%doc man/vt_monitor.md man/vt_monitor_analyses.md man/vt_monitor_comments.md
%doc man/vt_monitor_delete.md man/vt_monitor_deletedetails.md
%doc man/vt_monitor_download.md man/vt_monitor_list.md man/vt_monitor_owner.md
%doc man/vt_monitor_relationships.md man/vt_monitor_setdetails.md
%doc man/vt_monitor_upload.md man/vt_monitorpartner.md
%doc man/vt_monitorpartner_analyses.md man/vt_monitorpartner_comments.md
%doc man/vt_monitorpartner_download.md man/vt_monitorpartner_items.md
%doc man/vt_monitorpartner_list.md man/vt_monitorpartner_relationships.md
%doc man/vt_retrohunt.md man/vt_retrohunt_abort.md man/vt_retrohunt_delete.md
%doc man/vt_retrohunt_list.md man/vt_retrohunt_matches.md
%doc man/vt_retrohunt_start.md man/vt_scan.md man/vt_scan_file.md
%doc man/vt_scan_url.md man/vt_search.md man/vt_search_content.md man/vt_url.md
%doc man/vt_url_analyses.md man/vt_url_collections.md man/vt_url_comments.md
%doc man/vt_url_communicating_files.md man/vt_url_contacted_domains.md
%doc man/vt_url_contacted_ips.md man/vt_url_downloaded_files.md
%doc man/vt_url_embedded_js_files.md man/vt_url_graphs.md
%doc man/vt_url_http_response_contents.md man/vt_url_last_serving_ip_address.md
%doc man/vt_url_memory_pattern_parents.md man/vt_url_network_location.md
%doc man/vt_url_redirecting_urls.md man/vt_url_redirects_to.md
%doc man/vt_url_references.md man/vt_url_referrer_files.md
%doc man/vt_url_referrer_urls.md man/vt_url_related_attack_techniques.md
%doc man/vt_url_related_collections.md man/vt_url_related_comments.md
%doc man/vt_url_related_references.md man/vt_url_related_threat_actors.md
%doc man/vt_url_relationships.md man/vt_url_submissions.md
%doc man/vt_url_urls_related_by_tracker_id.md man/vt_url_user_votes.md
%doc man/vt_url_votes.md man/vt_user.md man/vt_user_privileges.md
%doc man/vt_user_privileges_grant.md man/vt_user_privileges_revoke.md
%doc man/vt_version.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
