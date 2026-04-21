# 🔐 大模型安全相关研究 | 2026年04月22日

> 本类共 **22** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [CAMP: Cumulative Agentic Masking and Pruning for Privacy Protection in Multi-Turn LLM Conversations](https://arxiv.org/abs/2604.16521)

**<font color=#1a73e8>作者：</font>** Aman Panjwani  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The deployment of Large Language Models in agentic, multi-turn conversational settings has introduced a class of privacy vulnerabilities that existing protection mechanisms are not designed to address. Current approaches to Personally Identifiable Information (PII) masking operate on a per-turn basis, scanning each user message in isolation and replacing detected entities with typed placeholders before forwarding sanitized text to the model. While effective against direct identifier leakage within a single message, these methods are fundamentally stateless and fail to account for the compounding privacy risk that emerges when PII fragments accumulate across conversation turns. A user who separately discloses their name, employer, location, and medical condition across several messages has revealed a fully re-identifiable profile - yet no individual message would trigger a per-turn masker. We formalize this phenomenon as Cumulative PII Exposure (CPE) and propose CAMP (Cumulative Agentic Masking and Pruning), a cross-turn privacy protection framework for multi-turn LLM conversations. CAMP maintains a session-level PII registry, constructs a co-occurrence graph to model combination risk between entity types, computes a CPE score after each turn, and triggers retroactive masking of conversation history when the score crosses a configurable threshold. We evaluate CAMP on four synthetic multi-turn scenarios spanning healthcare, hiring, finance, and general conversation, demonstrating that per-turn baselines expose re-identifiable profiles that CAMP successfully neutralizes while preserving full conversational utility.

---


### 2. [TWGuard: A Case Study of LLM Safety Guardrails for Localized Linguistic Contexts](https://arxiv.org/abs/2604.16542)

**<font color=#1a73e8>作者：</font>** Hua-Rong Chu, Kuan-Chun Wang, Yao-Te Huang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety guardrails have become an active area of research in AI safety, aimed at ensuring the appropriate behavior of large language models (LLMs). However, existing research lacks consideration of nuances across linguistic and cultural contexts, resulting in a gap between reported performance and in-the-wild effectiveness. To address this issue, this paper proposes an approach to optimize guardrail models for a designated linguistic context by leveraging a curated dataset tailored to local linguistic characteristics, targeting the Taiwan linguistic context as a representative example of localized deployment challenges. The proposed approach yields TWGuard, a linguistic context-optimized guardrail model that achieves a huge gain (+0.289 in F1) compared to the foundation model and significantly outperforms the strongest baseline in practical use (-0.037 in false positive rate, a 94.9\% reduction). Together, this work lays a foundation for regional communities to establish AI safety standards grounded in their own linguistic contexts, rather than accepting boundaries imposed by dominant languages. The inadequacy of the latter is reconfirmed by our findings.

---


### 3. [A Survey on the Security of Long-Term Memory in LLM Agents: Toward Mnemonic Sovereignty](https://arxiv.org/abs/2604.16548)

**<font color=#1a73e8>作者：</font>** Zehao Lin, Chunyu Li, Kai Chen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Research on large language model (LLM) security is shifting from "will the model leak training data" to a more consequential question: can an agent with persistent, long-term memory be continuously shaped, cross-session poisoned, accessed without authorization, and propagated across shared organizational state? Recent surveys cover memory architectures and agent mechanisms, but fewer center the epistemic and governance properties of persistent, writable memory as the reason memory is an independent security problem.
This survey addresses that gap. Drawing on cognitive neuroscience and the philosophy of memory, we characterize agent memory as malleable, rewritable, and socially propagating, and develop a memory-lifecycle framework organized around six phases -- Write, Store, Retrieve, Execute, Share, Forget/Rollback -- cross-tabulated against four security objectives: integrity, confidentiality, availability, governance. We organize the literature on memory poisoning, extraction, retrieval corruption, control-flow hijacking, cross-agent propagation, rollback, and governance, and situate representative architectures as determinants of which phases are explicitly governable.
Three findings stand out: the literature concentrates on write- and retrieve-time integrity attacks, while confidentiality, availability, store/forget, and benign-persistence failures remain sparsely studied; no published architecture covers all nine governance primitives we identify; and using LLMs themselves for memory security remains sparse yet essential.
We unify these under mnemonic sovereignty -- verifiable, recoverable governance over what may be written, who may read, when updates are authorized, and which states may be forgotten -- arguing future secure agents will be differentiated not only by recall capacity, but by memory governance quality.

---


### 4. [SafeLM: Unified Privacy-Aware Optimization for Trustworthy Federated Large Language Models](https://arxiv.org/abs/2604.16606)

**<font color=#1a73e8>作者：</font>** Noor Islam S. Mohammad, Uluğ Bayazıt  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in high-stakes domains, yet a unified treatment of their overlapping safety challenges remains lacking. We present SafeLM, a framework that jointly addresses four pillars of LLM safety: privacy, security, misinformation, and adversarial robustness. SafeLM combines federated training with gradient smartification and Paillier encryption for privacy, integrates defenses against training and inference-time attacks, employs contrastive grounding with calibrated decoding to reduce hallucinations, and introduces alignment-aware binarized aggregation to enhance robustness while maintaining bounded reconstruction quality. Across benchmarks on factuality, toxicity, and membership inference, SafeLM achieves 98.0% harmful content detection accuracy, reduces communication by 96.9%, and lowers gradient inversion PSNR from 31.7 dB to 15.1 dB. Ablations show that each component contributes independently, whereas their integration yields a strong privacy utility efficiency trade-off for deploying trustworthy LLMs.

---


### 5. [Benign Fine-Tuning Breaks Safety Alignment in Audio LLMs](https://arxiv.org/abs/2604.16659)

**<font color=#1a73e8>作者：</font>** Jaechul Roh, Amir Houmansadr  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Prior work shows that fine-tuning aligned models on benign data degrades safety in text and vision modalities, and that proximity to harmful content in representation space predicts which samples cause the most damage. However, existing analyses operate within a single, undifferentiated embedding space -- leaving open whether distinct input properties drive the vulnerability differently. Audio introduces a structurally richer problem: a benign sample can neighbor harmful content not only through what is said but through how it sounds, even when its words are entirely innocuous. We present the first systematic study of benign fine-tuning safety in Audio LLMs, evaluating three state-of-the-art models with a proximity-based filtering framework that selects benign audio by embedding-space distance to harmful content. By decomposing proximity into semantic, acoustic, and mixed axes using external reference encoders alongside each model's own internal encoder, we show that benign fine-tuning elevates Jailbreak Success Rate (JSR) from single digits to as high as 87.12%. Crucially, the dominant vulnerability axis and the relative risk of audio versus text fine-tuning are both architecture-conditioned -- determined by how each model's encoder and projector transform audio into the LLM's input space. We propose two defenses: filtering training data to maximize distance from harmful embeddings, and a textual system prompt at inference, both reducing JSR to near-zero without architectural modification. Our mechanistic analysis on two architectures reveals that fine-tuning selectively suppresses the late-layer refusal circuit while the frozen encoder preserves representations, and that even the suppression pattern is architecture-conditioned, mirroring the behavioral asymmetries across modalities. Safety degradation from benign fine-tuning is a qualitatively distinct risk in Audio LLMs.

---


### 6. [Surgical Repair of Insecure Code Generation in LLMs](https://arxiv.org/abs/2604.16697)

**<font color=#1a73e8>作者：</font>** Gustavo Sandoval, Brendan Dolan-Gavitt, Siddharth Garg  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models write production code, and yet they routinely introduce well-known vulnerabilities. We show that this is not a knowledge deficit: the same models that generate insecure code, correctly identify and explain the vulnerability when asked directly, this is a gap we call the Format-Reliability Gap. Mechanistic analysis reveals the cause: security representations are encoded from the earliest layers but remain computationally inert until the final layer, where format-compliance demands compete with them. Because the failure is localized to a single layer, per-vulnerability steering vectors reduce insecure generation by up to 74% with negligible overhead. The mechanism and the fix generalize across five models, three architecture families, and six vulnerability types, suggesting insecure code generation is an interpretability problem, not a training artifact.

---


### 7. [SafeDream: Safety World Model for Proactive Early Jailbreak Detection](https://arxiv.org/abs/2604.16824)

**<font color=#1a73e8>作者：</font>** Bo Yan, Weikai Lin, Yada Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-turn jailbreak attacks progressively erode LLM safety alignment across seemingly innocuous conversation turns, achieving success rates exceeding 90% against state-of-the-art models. Existing alignment-based and guardrail methods suffer from three key limitations: they require costly weight modification, evaluate each turn independently without modeling cumulative safety erosion, and detect attacks only after harmful content has been generated. To address these limitations, we first formulate the proactive early jailbreak detection problem with a new metric, detection lead, that measures how early an attack can be detected before the LLM complies. We then propose SAFEDREAM, a lightweight world-model-based framework that operates as an external module without modifying the LLM's weights. SAFEDREAM introduces three components: (1) a safety state world model that encodes LLM hidden states into a compact safety representation and predicts how it evolves across turns, (2) CUSUM detection that accumulates weak per-turn risk signals into reliable evidence, and (3) contrastive imagination that simultaneously rolls out attack and benign futures in latent space to issue early alarms before jailbreaks occur. On three multi-turn jailbreak benchmarks (XGuard-Train, SafeDialBench, SafeMTData) against 8 baselines, SAFEDREAM achieves the best detection timeliness across all benchmarks (1.06-1.20 turns before compliance) while maintaining competitive false positive rates and outperforming baselines in detection quality.

---


### 8. [Visual Inception: Compromising Long-term Planning in Agentic Recommenders via Multimodal Memory Poisoning](https://arxiv.org/abs/2604.16966)

**<font color=#1a73e8>作者：</font>** Jiachen Qian  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The evolution from static ranking models to Agentic Recommender Systems (Agentic RecSys) empowers AI agents to maintain long-term user profiles and autonomously plan service tasks. While this paradigm shift enhances personalization, it introduces a vulnerability: reliance on Long-term Memory (LTM). In this paper, we uncover a threat termed "Visual Inception." Unlike traditional adversarial attacks that seek immediate misclassification, Visual Inception injects triggers into user-uploaded images (e.g., lifestyle photos) that act as "sleeper agents" within the system's memory. When retrieved during future planning, these poisoned memories hijack the agent's reasoning chain, steering it toward adversary-defined goals (e.g., promoting high-margin products) without prompt injection. To mitigate this, we propose CognitiveGuard, a dual-process defense framework inspired by human cognition. It consists of a System 1 Perceptual Sanitizer (diffusion-based purification) to cleanse sensory inputs and a System 2 Reasoning Verifier (counterfactual consistency checks) to detect anomalies in memory-driven planning. Extensive experiments on a mock e-commerce agent environment demonstrate that Visual Inception achieves about 85% Goal-Hit Rate (GHR), while CognitiveGuard reduces this risk to around 10% with configurable latency trade-offs (about 1.5s in lite mode to about 6.5s for full sequential verification), without quality degradation under our setup.

---


### 9. [False Security Confidence in Benign LLM Code Generation](https://arxiv.org/abs/2604.17014)

**<font color=#1a73e8>作者：</font>** Xiaolei Ren  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Prior work has demonstrated that functionally correct yet vulnerable outputs arise systematically in threat-oriented settings, where adversarial or implicit channels are used to induce security failures in code agents and automated patching workflows. This note introduces a complementary but distinct framing: False Security Confidence (FSC), which studies the same surface phenomenon from a measurement-first perspective in ordinary, non-attack-framed generation tasks. Our interest is not in whether attacks can produce such outputs, but in how frequently and in what forms they appear absent explicit attack pressure, and whether conventional functional evaluation reliably detects them. We formalize FSC rate as the prevalence of security failure within the set of functionally correct outputs, distinguish it from prior joint functional-security metrics such as SAFE and outcome-driven evaluation frameworks such as CWEval, define a three-ecosystem task view for studying how FSC manifests across general-purpose programming, deployment-context tasks, and security-explicit programming, and identify FSC-hard as a practically important refinement layer in which static analyzers miss vulnerabilities that remain dynamically triggerable. This technical report is intentionally scoped as a framework statement rather than a full empirical paper: its purpose is to establish terminology, measurement boundaries, and study design commitments for subsequent large-scale evaluation.

---


### 10. [HarmChip: Evaluating Hardware Security Centric LLM Safety via Jailbreak Benchmarking](https://arxiv.org/abs/2604.17093)

**<font color=#1a73e8>作者：</font>** Zeng Wang, Minghao Shao, Weimin Fu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The integration of large language models (LLMs) into electronic design automation (EDA) workflows has introduced powerful capabilities for RTL generation, verification, and design optimization, but also raises critical security concerns. Malicious LLM outputs in this domain pose hardware-level threats, including hardware Trojan insertion, side-channel leakage, and intellectual property theft, that are irreversible once fabricated into silicon. Such requests often exploit semantic disguise, embedding adversarial intent within legitimate engineering language that existing safety mechanisms, trained on general-purpose hazards, fail to detect. No benchmark exists to evaluate LLM vulnerability to such domain-specific threats. We present the HarmChip benchmark to assess jailbreak susceptibility in hardware security, spanning 16 hardware security domains, 120 threats, and 360 prompts at two difficulty levels. Evaluation of state-of-the-art LLMs reveals an alignment paradox: They refuse legitimate security queries while complying with semantically disguised attacks, exposing blind spots in safety guardrails and underscoring the need for domain-aware safety alignment.

---


### 11. [Systematic Capability Benchmarking of Frontier Large Language Models for Offensive Cyber Tasks](https://arxiv.org/abs/2604.17159)

**<font color=#1a73e8>作者：</font>** Tyler H. Merves, Michael H. Conaway, Joseph M. Escobar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present, to our knowledge, the most comprehensive cross-model evaluation of LLM agents on offensive cybersecurity tasks, benchmarking 10 frontier models from 7 providers on all 200 challenges of the NYU CTF Bench. Building on the D-CIPHER multi-agent framework, we extend it with multi-provider backend support, a custom Kali Linux environment with over 100 pre-installed penetration testing tools, and runtime tool-discovery agents. Through a controlled factorial study, we find that the Kali Linux environment yields a +9.5 percentage-point improvement over Ubuntu, while auto-prompting and category-specific tips often degrade performance in well-equipped environments. Among models, Claude 4.5 Opus achieves the highest solve rate (59%), followed by Gemini 3 Pro (52%), with Gemini 3 Flash offering the best cost-efficiency at $0.05 per solve. Asymmetric planner/executor model assignments provide no meaningful benefit while coherent same-model configurations consistently outperform mixed-tier pairings. Our results indicate that environment tooling and model selection emerge as the strongest drivers of performance, whereas prompt engineering interventions show diminishing or negative returns in well-equipped environments. Reported performance reflects both model reasoning ability and compatibility with agent tooling and API integration.

---


### 12. [Bit-Flip Vulnerability of Shared KV-Cache Blocks in LLM Serving Systems](https://arxiv.org/abs/2604.17249)

**<font color=#1a73e8>作者：</font>** Yuji Yamamoto, Satoshi Matsuura  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Rowhammer on GPU DRAM has enabled adversarial bit flips in model weights; shared KV-cache blocks in LLM serving systems present an analogous but previously unexamined target. In vLLM's Prefix Caching, these blocks exist as a single physical copy without integrity protection. Using software fault injection under ideal bit targeting, we characterize worst-case severity and identify three properties: (1) Silent divergence - 13 of 16 BF16 bit positions produce coherent but altered outputs, indistinguishable from legitimate responses without a clean baseline. (2) Selective propagation - only requests sharing the targeted prefix are affected. (3) Persistent accumulation - no temporal decay occurs, so cumulative damage grows linearly with subsequent requests. Together, these constitute a threat profile distinct from weight corruption: silent divergence and selective propagation enable detection evasion; persistent accumulation then proceeds unchecked, yielding damage amplification bounded only by how long the block remains cached. A checksum-based countermeasure detects any single-bit corruption at scheduling time, bounding cumulative damage to one batch independent of the block's cache lifetime, with negligible overhead. These results argue for integrity protection of prefix blocks before end-to-end exploitation is demonstrated.

---


### 13. [GuardPhish: Securing Open-Source LLMs from Phishing Abuse](https://arxiv.org/abs/2604.17313)

**<font color=#1a73e8>作者：</font>** Rina Mishra, Gaurav Varshney, Doddipatla Sesha Sahithi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid adoption of open-source Large Language Models (LLMs) in offline and enterprise environments has introduced a largely unexamined security risk like susceptibility to adversarial phishing prompts under static safety configurations. In this work, we systematically investigate this vulnerability through GuardPhish, a large scale multi-vector phishing prompt dataset comprising 70,015 samples spanning web, email, SMS, and voice attack scenarios derived from real world campaigns. Using a deterministic five model ensemble for labeling, we achieve near perfect inter model agreement (Fleiss kappa = 0.9141), with residual disagreements resolved through expert adjudication. By evaluating eight open-source LLMs under fully offline inference conditions, we uncover a substantial enforcement gap like models that correctly identify phishing intent with detection rates up to 96% nevertheless generate actionable phishing content from identical prompts, with attack success rates reaching 98.5% in voice-based scenarios. These findings demonstrate that intent classification alone does not guarantee generative refusal in the absence of dynamic guardrails. To mitigate this risk, we train transformer based classifiers on GuardPhish, achieving up to 98.27% accuracy as modular pre-generation filters deployable without modifying the underlying generative model. Our results highlight a critical weakness in current open-source LLM deployments and provide a reproducible foundation for strengthening defenses against phishing and social engineering attacks.

---


### 14. [Terminal Wrench: A Dataset of 331 Reward-Hackable Environments and 3,632 Exploit Trajectories](https://arxiv.org/abs/2604.17596)

**<font color=#1a73e8>作者：</font>** Ivan Bercovich, Ivgeni Segal, Kexun Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We release Terminal Wrench, a subset of 331 terminal-agent benchmark environments, copied from the popular open benchmarks that are demonstrably reward-hackable. The data set includes 3,632 hack trajectories and 2,352 legitimate baseline trajectories across three frontier models (Claude Opus 4.6, Gemini 3.1 Pro, GPT-5.4). Each entry preserves the original task definition alongside full attack trajectories that show how the verifier was bypassed. It also includes cases where the task was not solved as intended. The tasks span system administration, machine learning, software engineering, and security challenges; the exploits range from simple output spoofing to stack-frame introspection, standard-library patching, and rootkit-style binary hijacking. Crucially, these exploits are specific to each task, rather than the evaluation harness, making them harder to patch. We also present a monitorability study in which hack trajectories are sanitized or stripped of reasoning traces and then scored by an LLM judge, showing that detection degrades meaningfully when chain-of-thought is removed (AUC drops from 0.97 to 0.92). The data set is publicly available at this https URL.

---


### 15. [SDLLMFuzz: Dynamic-static LLM-assisted greybox fuzzing for structured input programs](https://arxiv.org/abs/2604.17750)

**<font color=#1a73e8>作者：</font>** Yihao Zou, Tianming Zheng, Futai Zou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fuzzing has become a widely adopted technique for vulnerability discovery, yet it remains ineffective for structured-input programs due to strict syntactic constraints and limited semantic awareness. Traditional greybox fuzzers rely on mutation-based strategies and coarse-grained coverage feedback, which often fail to generate valid inputs and explore deep execution paths. Recent advances in large language models (LLMs) have shown promise in improving input generation, but existing approaches primarily focus on seed generation and largely overlook the effective use of runtime feedback. In this paper, we propose SDLLMFuzz, a dynamic-static LLM-assisted greybox fuzzing framework for structured-input programs. Our approach integrates LLM-based structure-aware seed generation with static crash analysis, forming a unified feedback loop that iteratively refines test inputs. Specifically, we leverage LLMs to generate syntactically valid and semantically diverse inputs, while extracting rich semantic information from crash artifacts (e.g., core dumps and execution traces) to guide subsequent input generation. This dynamic-static feedback mechanism enables more efficient exploration of complex program behaviors. We evaluate SDLLMFuzz on the Magma benchmark across multiple structured-input programs, including libxml2, libpng, and libsndfile. Experimental results show that SDLLMFuzz significantly outperforms traditional greybox fuzzers and LLM-assisted baselines in terms of bug discovery and time-to-bug. These results demonstrate that combining semantic input generation with feedback-driven refinement is an effective direction for improving fuzzing performance on structured-input programs.

---


### 16. [A Quasi-Experimental Developer Study of Security Training in LLM-Assisted Web Application Development](https://arxiv.org/abs/2604.17763)

**<font color=#1a73e8>作者：</font>** Mohammed Kharma, Ahmed Sabbah, Radi Jarrar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper presents a controlled quasi-experimental developer study examining whether a layer-based security training package is associated with improved security quality in LLM-assisted implementation of an identity-centric Java Spring Boot backend. The study uses a mixed design with a within-subject pre-training versus post-training comparison and an exploratory between-subject expertise factor. Twelve developers completed matched runs under a common interface, fixed model configuration, counterbalanced task sets, and a shared starter project. Security outcomes were assessed via independent manual validation of submitted repositories by the first and second authors. The primary participant-level endpoint was a severity-weighted validated-weakness score. The post-training condition showed a significant paired reduction under an exact Wilcoxon signed-rank test ($p = 0.0059$). In aggregate, validated weaknesses decreased from 162 to 111 (31.5\%), the severity-weighted burden decreased from 432 to 267 (38.2\%), and critical findings decreased from 24 to 5 (79.2\%). The largest reductions were in authorization and object access (53.3\%) and in authentication, credential policy, and recovery weaknesses (44.7\%). Session and browser trust-boundary issues showed minimal change, while sensitive-data and cryptographic weaknesses showed only marginal improvement.
These results suggest that, under the tested conditions, post-training runs reduce validated security burden in LLM-assisted backend development without modifying the model. They do not support replacing secure defaults, static analysis, expert review, or operational hardening.

---


### 17. [Understanding Secret Leakage Risks in Code LLMs: A Tokenization Perspective](https://arxiv.org/abs/2604.17814)

**<font color=#1a73e8>作者：</font>** Meifang Chen, Zhe Yang, Huang Nianchen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Code secrets are sensitive assets for software developers, and their leakage poses significant cybersecurity risks. While the rapid development of AI code assistants powered by Code Large Language Models (CLLMs), CLLMs are shown to inadvertently leak such secrets due to a notorious memorization phenomenon. This study first reveals that Byte-Pair Encoding (BPE) tokenization leads to unexpected behavior of secret memorization, which we term as \textit{gibberish bias}. Specifically, we identified that some secrets are among the easiest for CLLMs to memorize. These secrets yield high character-level entropy, but low token-level entropy. Then, this paper supports the biased claim with numerical data. We identified that the roots of the bias are the token distribution shift between the CLLM training data and the secret data. We further discuss how gibberish bias manifests under the ``larger vocabulary'' trend. To conclude the paper, we discuss potential mitigation strategies and the broader implications on current tokenizer design.

---


### 18. [TitanCA: Lessons from Orchestrating LLM Agents to Discover 100+ CVEs](https://arxiv.org/abs/2604.17860)

**<font color=#1a73e8>作者：</font>** Ting Zhang, Yikun Li, Chengran Yang 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software vulnerabilities remain one of the most persistent threats to modern digital infrastructure. While static application security testing (SAST) tools have long served as the first line of defense, they suffer from high false-positive rates. This article presents TitanCA, a collaborative project between Singapore Management University and GovTech Singapore that orchestrates multiple large language model (LLM)-powered agents into a unified vulnerability discovery pipeline. Applied in open-source software, TitanCA has discovered 203 confirmed zero-day vulnerabilities and yielded 118 CVEs. We describe the four-module architecture, i.e., matching, filtering, inspection, and adaptation, and share key lessons from building and deploying an LLM-based vulnerability discovery solution in practice.

---


### 19. [RAVEN: Retrieval-Augmented Vulnerability Exploration Network for Memory Corruption Analysis in User Code and Binary Programs](https://arxiv.org/abs/2604.17948)

**<font color=#1a73e8>作者：</font>** Parteek Jamwal, Minghao Shao, Boyuan Chen 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated remarkable capabilities across various cybersecurity tasks, including vulnerability classification, detection, and patching. However, their potential in automated vulnerability report documentation and analysis remains underexplored. We present RAVEN (Retrieval Augmented Vulnerability Exploration Network), a framework leveraging LLM agents and Retrieval Augmented Generation (RAG) to synthesize comprehensive vulnerability analysis reports. Given vulnerable source code, RAVEN generates reports following the Google Project Zero Root Cause Analysis template. The framework uses four modules: an Explorer agent for vulnerability identification, a RAG engine retrieving relevant knowledge from curated databases including Google Project Zero reports and CWE entries, an Analyst agent for impact and exploitation assessment, and a Reporter agent for structured report generation. To ensure quality, RAVEN includes a task specific LLM Judge evaluating reports across structural integrity, ground truth alignment, code reasoning quality, and remediation quality. We evaluate RAVEN on 105 vulnerable code samples covering 15 CWE types from the NIST-SARD dataset. Results show an average quality score of 54.21%, supporting the effectiveness of our approach for automated vulnerability documentation.

---


### 20. [Committed SAE-Feature Traces for Audited-Session Substitution Detection in Hosted LLMs](https://arxiv.org/abs/2604.18179)

**<font color=#1a73e8>作者：</font>** Ziyang Liu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hosted-LLM providers have a silent-substitution incentive: advertise a stronger model while serving cheaper replies. Probe-after-return schemes such as SVIP leave a parallel-serve side-channel, since a dishonest provider can route the verifier's probe to the advertised model while serving ordinary users from a substitute. We propose a commit-open protocol that closes this gap. Before any opening request, the provider commits via a Merkle tree to a per-position sparse-autoencoder (SAE) feature-trace sketch of its served output at a published probe layer. A verifier opens random positions, scores them against a public named-circuit probe library calibrated with cross-backend noise, and decides with a fixed-threshold joint-consistency z-score rule. We instantiate the protocol on three backbones -- Qwen3-1.7B, Gemma-2-2B, and a 4.5x scale-up to Gemma-2-9B with a 131k-feature SAE. Of 17 attackers spanning same-family lifts, cross-family substitutes, and rank-<=128 adaptive LoRA, all are rejected at a shared, scale-stable threshold; the same attackers all evade a matched SVIP-style parallel-serve baseline. A white-box end-to-end attack that backpropagates through the frozen SAE encoder does not close the margin, and a feature-forgery attacker that never runs M_hon is bounded in closed form by an intrinsic-dimension argument. Commitment adds <=2.1% to forward-only wall-clock at batch 32.

---


### 21. [AgenTEE: Confidential LLM Agent Execution on Edge Devices](https://arxiv.org/abs/2604.18231)

**<font color=#1a73e8>作者：</font>** Sina Abdollahi, Mohammad M Maheri, Javad Forough 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents provide powerful automation capabilities, but they also create a substantially broader attack surface than traditional applications due to their tight integration with non-deterministic models and third-party services. While current deployments primarily rely on cloud-hosted services, emerging designs increasingly execute agents directly on edge devices to reduce latency and enhance user privacy. However, securely hosting such complex agent pipelines on edge devices remains challenging. These deployments must protect proprietary assets (e.g., system prompts and model weights) and sensitive runtime state on heterogeneous platforms that are vulnerable to software attacks and potentially controlled by malicious users.
To address these challenges, we present AgenTEE, a system for deploying confidential agent pipelines on edge devices. AgenTEE places the agent runtime, inference engine, and third-party applications into independently attested confidential virtual machines (cVMs) and mediates their interaction through explicit, verifiable communication channels. Built on Arm Confidential Compute Architecture (CCA), a recent extension to Arm platforms, AgenTEE enforces strong system-level isolation of sensitive assets and runtime state. Our evaluation shows that such multi-cVMs system is practical, achieving near-native performance with less than 5.15% runtime overhead compared to commodity OS multi-process deployments.

---


### 22. [Different Paths to Harmful Compliance: Behavioral Side Effects and Mechanistic Divergence Across LLM Jailbreaks](https://arxiv.org/abs/2604.18510)

**<font color=#1a73e8>作者：</font>** Md Rysul Kabir, Zoran Tiganj  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open-weight language models can be rendered unsafe through several distinct interventions, but the resulting models may differ substantially in capabilities, behavioral profile, and internal failure mode. We study behavioral and mechanistic properties of jailbroken models across three unsafe routes: harmful supervised fine-tuning (SFT), harmful reinforcement learning with verifiable rewards (RLVR), and refusal-suppressing abliteration. All three routes achieve near-ceiling harmful compliance, but they diverge once we move beyond direct harmfulness. RLVR-jailbroken models show minimal degradation and preserve explicit harm recognition in a structured self-audit: they are able to identify harmful prompts and describe how a safe LLM should respond, yet they comply with the harmful request. With RLVR, harmful behavior is strongly suppressed by a reflective safety scaffold: when a harmful prompt is prepended with an instruction to reflect on safety standards, harmful behavior drops close to the baseline. Category-specific RLVR jailbreaks generalize broadly across harmfulness domains. Models jailbroken with SFT show the largest collapse in explicit safety judgments, the highest behavioral drift, and a substantial capability loss on standard benchmarks. Abliteration is family-dependent in both self-audit and response to a reflective safety scaffold. Mechanistic and repair analyses further separate the routes: abliteration is consistent with localized refusal-feature deletion, RLVR with preserved safety geometry but retargeted policy behavior, and SFT with broader distributed drift. Targeted repair partially recovers RLVR-jailbroken models, but has little effect on SFT-jailbroken models. Together, these results show that jailbreaks can produce vastly different properties despite similar harmfulness, with models jailbroken via RLVR showing remarkable similarity to the base model.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
