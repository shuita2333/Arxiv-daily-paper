# 🔐 大模型安全相关研究 | 2026年07月30日

> 本类共 **13** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Multimodal User Authentication Method via Fusion of Keystroke Dynamics and Glove-Based Hand Kinematics](https://arxiv.org/abs/2607.24747)

**<font color=#1a73e8>作者：</font>** Issei Hyakuda, Lei Jing  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Although keystroke dynamics are cost-effective behavioral biometrics, their practical deployment is hindered by susceptibility to environmental variations. To address this, we propose a robust multimodal authentication framework that augments traditional keystroke dynamics using 19-dimensional hand kinematics. Features are captured using a bespoke data glove equipped with 10 piezoresistive pressure sensors and a 9-axis IMU. A hybrid CNN-LSTM architecture effectively fuses these heterogeneous time-series streams. To ensure real-world applicability, we implemented a rigorous "unseen" evaluation protocol: the model was trained on a desktop keyboard using data from 1 target user and 8 "known" impostors, but evaluated on a laptop keyboard (cross-domain) against the target and an "unknown" impostor excluded from training. Averaged over five trials, the multimodal method achieved a mean Equal Error Rate (EER) of 2.12% for individual 600-ms authentication events (Window 1). Crucially, aggregating scores over 10 events (6 seconds) using a temporal smoothing window yielded perfect authentication (0.00% EER). While our ablation study showed IMU kinematics alone achieved equivalent performance in a static laboratory, error analysis confirmed that pressure and IMU sensors, despite strong physical correlation, possess distinct sensitivities to error factors. Fusing these modalities establishes a vital fail-safe against real-world vulnerabilities like spatial spoofing and environmental noise, highlighting that combined physical traits provide much stronger biometric discrimination than timing features alone.

---


### 2. [The Mirage of LLM Guardrails: A Case Study in AI-Assisted Medical Note Manipulation](https://arxiv.org/abs/2607.24859)

**<font color=#1a73e8>作者：</font>** Davis Yadav, Amulya Yadav  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid deployment of large language models (LLMs) in healthcare settings makes the reliability of their built-in guardrails against malicious queries a question of urgent practical consequence. Yet the robustness of these mechanisms against deliberate misuse (in the healthcare context) remains poorly understood. In this paper, we investigate this question empirically, using AI-assisted medical note manipulation as a concrete case study. We make four novel contributions. First, we develop a reproducible manipulation pipeline that takes publicly available seed medical note templates and use commercial LLMs to produce customized manipulated notes by substituting patient names, provider identities, dates, and medical conditions across multiple model families, input formats, and prompt phrasings. Second, we conduct a systematic empirical evaluation of LLM guardrail robustness for medical note manipulation. Our experimental results reveal substantial weaknesses and inconsistencies in contemporary commercial LLM guardrails, including low refusal rates for several model families. Third, we utilize a combination of automated metrics and human annotation-based metrics to assess the correctness of requested manipulations. Fourth, we conduct a user-study to assess the believability of manipulated medical notes, finding that the best manipulations are visually indistinguishable from original documents to human raters. Finally, we discuss implications for responsible guardrail design in LLMs, AI safety policies, and the broader ethics of deploying LLMs in healthcare settings.

---


### 3. [Early Detection of Distributed Backdoors in Multi-Agent LLM Systems: A Characterization Study](https://arxiv.org/abs/2607.24893)

**<font color=#1a73e8>作者：</font>** Diego Fernandez Arias, Dev Prashant Mistry, Ren Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems can be attacked by a payload that no single agent ever holds in full: a poisoned tool hides encrypted fragments in its observations, spreads them across several agents, and an external step reassembles and executes them after the run. Per-step safety checks that judge each action in isolation may fail to recognize the complete distributed payload. We investigate how early such an attack can be detected while the run is still unfolding, and how robustly it can be caught once its most obvious cues are stripped away. We build a working instance on a hierarchical multi-agent system, run it under benign and attacked conditions across five language models and two task domains, and record when each fragment is injected and when the payload is assembled and executed. Detection is a race against assembly. Before the first fragment is injected, attacked and benign runs are indistinguishable; once injection begins, a prefix detector flags $99.3\%$ of successful attacks with a median of five steps remaining and a $10.3\%$ safe-run false-positive rate. Because assembly occurs only after the run, these alarms arrive in time to abort nearly every successful attack. We then measure how much of that warning rests on removable surface cues of the attack rather than on its distributed structure. Generic zero-shot and behavior-trained detectors provide almost no warning at all; the detectors that do work lean in part on removable surface cues, chiefly the ciphertext's length and entropy, and once the entropy cue is removed from the payload and the length features from the detector, detection arrives later and transfers poorly across domains, though a fine-tuned model recovers some of the loss.

---


### 4. [TYPO: Instruction-Dense Visual Jailbreaks against Commercial Closed-Source Image-Generation Models](https://arxiv.org/abs/2607.24897)

**<font color=#1a73e8>作者：</font>** Meng Xie, Li Zeng, Hangtao Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent commercial image-generation models can generate high-quality images with readable text (e.g., posters, infographics, and manuals), attracting considerable attention. Yet we first show that this same capability also introduces a previously unreported safety vulnerability: these systems may refuse to generate harmful text directly, yet permit the same content when rendered as text within generated images, i.e., safety alignment does not reliably transfer from textual outputs to text embedded in images. In this paper, unlike existing visual jailbreaks against image-generation models, which primarily induce models to generate harmful visual objects or scenes, we introduce the concept of instruction-dense visual jailbreaks, in which image-generation models produce detailed, readable, and actionable harmful instructions within images. Such outputs can amplify harm because the rendered instructions can be readily read and widely spread. To instantiate this threat, we propose TYPO, a black-box framework that exploits this safety gap by automatically generating adversarial TYPOgraphy prompts, which covertly steer image-generation models to express harmful intent as highly legible, typographically structured text. Specifically, TYPO decomposes prompt generation into two channels: a textual channel for reframing the target intent, and a visual channel for specifying its presentation form. We formulate these two channels as a dual-channel textual-visual strategy space and optimize candidate strategy combinations through an adaptive combinatorial search. Extensive experiments across four commercial models (i.e., GPT-Image-2, Nano Banana Pro, Qwen-Image-2, and Seedream 5.0 Lite) show that TYPO substantially outperforms nine representative jailbreak attacks by 50.2% in ASR on average, while incurring an average query cost of only $0.04.

---


### 5. [ALIBI: Adaptive Agentic Attacks on LLM-Based Vulnerability Detectors via Adversarial Code Comments](https://arxiv.org/abs/2607.24964)

**<font color=#1a73e8>作者：</font>** Zixuan Wu, Cristina Nita-Rotaru  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed for security-sensitive tasks such as vulnerability detection and code review. Their reliance on natural-language context embedded in source code exposes a previously underexplored attack surface: adversarial comments that can influence a detector's reasoning without changing program behavior. We study LLM-based vulnerability detectors against a new adversary: a coding agent that implements new functionality, deliberately introduces vulnerabilities, and strategically inserts adversarial source-code comments to evade detection.
We present ALIBI, an automated adaptive black-box attack framework that generates and iteratively refines adversarial comments using detector reasoning and feedback. We transform real-world vulnerability-fixing commits into coding tasks and evaluate four representative LLM-based vulnerability detectors, ranging from specialized open-weight reasoning models to frontier multi-agent systems. All evaluated detectors are highly vulnerable: attack success rates exceed 90% across 125 real-world null-pointer dereference vulnerabilities, reaching 100% on one system. The framework also generalizes beyond this vulnerability class. Adversarial comments steering detector reasoning or fabricating external tool results prove most effective, while iterative refinement based on detector feedback further increases attack success. Finally, prompt-level defenses provide limited robustness against adaptive attacks, whereas architectural isolation and pre-detector comment sanitization substantially improve resilience. Our findings expose a fundamental attack surface in current LLM-based vulnerability detectors and motivate security-aware designs that carefully calibrate trust between natural-language context and program evidence.

---


### 6. [Decision-Level Hijacking: Injecting Cognitive Bias into Large Language Models via Bit-Flip Attacks](https://arxiv.org/abs/2607.25227)

**<font color=#1a73e8>作者：</font>** Yu Yan, Jiahao Chen, Siqi Lu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have been widely applied in high-stakes decision-making scenarios such as corporate strategy, and users are increasingly relying on their outputs. However, the deep integration of open-source model sharing ecosystems with LLM-powered critical decision-making applications also introduces critical risks: if an attacker can manipulate the model's cognitive stance, they can indirectly influence the judgments and actions of downstream decision-makers. This paper defines such threats as decision-level hijacking. Existing attacks fail to achieve targeted cognitive manipulation without triggering prohibited content or degrading model functionality. To fill this gap, this paper reveals that Bit-Flip Attacks (BFAs) can serve as an attack vector for inducing decision-level hijacking, requiring no real-time interaction or control over the training process, and only a minimal number of weight bits need to be flipped after deployment to achieve stealthy, low-cost, and persistent cognitive manipulation. Therefore, we propose CogBias, a cognitive bias injection framework for LLMs. CogBias converts subjective preferences into optimization signals via a differentiable sentiment evaluator, uses a multi-objective loss to jointly constrain multiple dimensions, and constructs BitScout to locate critical bits, achieving targeted cognitive intervention under an ultra-sparse flip budget. Experiments on Llama-3.2-3B, Mistral-7B, and Qwen2.5-14B, as well as on the commercial recommendation and controversial factual topic scenarios, demonstrate that flipping only a small number of bits stably induces significant stance shifts on target topics, while the impact on non-target tasks and overall output distribution is limited. This work demonstrates that minute perturbations to low-level weight data suffice to undermine the high-level value alignment of LLMs.

---


### 7. [Hybrid Analysis for Secure MCP Tool Use in LLM Agents](https://arxiv.org/abs/2607.25297)

**<font color=#1a73e8>作者：</font>** Ping He, Yuexiang Xie, Yaliang Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid development of large language model (LLM) agents has enabled their broad adoption across diverse real-world tasks. To standardize interactions between LLM agents and external environments, Model Context Protocol (MCP) tools have emerged as a de facto standard and have been widely integrated into these systems. However, the use of MCP tools also introduces new safety risks, as LLM agents can be induced to perform malicious or unauthorized actions. Although prior work has proposed defenses for securing tool use in LLM agents, most methods rely on static analysis, i.e., inspecting prompts and generated outputs, which limits the defense effectiveness and robustness. To address these limitations, we propose MTGuard, a hybrid analysis-based defense framework designed to safeguard the use of MCP tools in LLM agents by leveraging lifecycle-aware static-dynamic co-analysis. Extensive evaluation demonstrates that MTGuard effectively mitigates multiple categories of harmful tool use across different LLM agents while maintaining performance on benign user tasks.

---


### 8. [Architectural Backdoors in Vision-Language Model Supply Chains via Representation Steering](https://arxiv.org/abs/2607.25479)

**<font color=#1a73e8>作者：</font>** Maria Rosaria Briglia, Igor Maljkovic, Antonio Emanuele Cinà 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vision--Language Models (VLMs) are increasingly deployed through a model supply chain in which pretrained checkpoints, architecture definitions, text encoders, and exported computation graphs are distributed by third parties and reused across downstream services. This reuse model creates a security-critical trust boundary: VLM deployments inherit not only learned parameters but also executable behavior encoded in shared model artifacts. In this paper, we show that a malicious provider can exploit this trust boundary by embedding architectural backdoors into VLM supply chains through representation steering. Our attack introduces dormant steering logic into the model architecture through a trigger-gated additive modification of an intermediate representation, without poisoning training data, controlling downstream fine-tuning, or modifying prompts at deployment time. When the trigger is absent, the modification reduces to zero and the model follows its normal computation, preserving clean utility. When the trigger is present, a steering direction shifts the internal representation toward an attacker-defined objective. We evaluate the attack across multiple VLM families and downstream tasks, including visual question answering, text-to-image generation, retrieval, and semantic response biasing. The results show that the proposed architectural steering backdoor compromises integrity, safety enforcement, and ranking fairness while preserving normal behavior on clean inputs. We further show that shared VLM artifacts can carry dormant steering logic against downstream services, and we propose an auditing defense that inspects the executable logic distributed with model artifacts rather than only their learned weights.

---


### 9. [Mapping CVEs to MITRE ATT&CK Techniques: A Curated Gold-Set Classifier and the Limits of LLM-Assisted Label Expansion](https://arxiv.org/abs/2607.25572)

**<font color=#1a73e8>作者：</font>** Cédric Bonhomme, Alexandre Dulaunoy  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present a reproducible pipeline for mapping Common Vulnerabilities and Exposures (CVEs) to MITRE ATT&CK Enterprise techniques from free-text vulnerability descriptions. Rather than relying on the CWE->CAPEC->ATT&CK derivation chain, whose table-expansion artifacts we quantify, we train a multi-label classifier on a curated gold dataset of 1,207 CVEs from expert MITRE Center for Threat-Informed Defense mappings. The resulting model approximately doubles recall@5 compared with a zero-shot embedding-similarity baseline and improves every ranking metric. We then investigate whether LLM-assisted labeling can extend the gold dataset. Initial experiments suggest contradictory conclusions: a single run indicates degraded performance, while averaging over five random seeds suggests a small gain. However, an independent replication and an expansion-size study (100--984 additional CVEs) show that the apparent improvement is an evaluation artifact. LLM-generated labels, with approximately 0.39 agreement with expert annotations, provide no reliable improvement at any expansion size and reduce rare-technique coverage at around 1,000 added CVEs (macro-F1 decreases by 0.04). The root cause is evaluation noise. Selecting checkpoints on a small test split effectively maximizes over many noisy evaluations, producing recall@5 differences of up to 0.05 between otherwise identical runs. Using a corrected protocol based on validation-split checkpoint selection, the gold-only model achieves recall@5 of (0.673 \pm 0.019), and repeating the decisive experiment confirms the null result for LLM expansion. A final scaling study shows that additional expert-curated data consistently improves performance, whereas LLM-labeled data does not, indicating that the classifier is limited by label quality rather than dataset size. All datasets, models, code, and training logs are publicly released.

---


### 10. [Stemma: Induced Decision Regions Reveal LLM Provenance](https://arxiv.org/abs/2607.25880)

**<font color=#1a73e8>作者：</font>** Keyu Zhang, Vadim Safronov, Andrew Martin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM provenance testing asks whether a suspect LLM belongs to the same lineage as a source. Existing black-box methods largely infer this relationship from response-level characteristics, but these characteristics may shift under adaptation or deployment even when the underlying meaning remains unchanged, weakening the reliability of provenance evidence. To address this limitation, we introduce induced decision regions by mapping open-ended outputs into a finite decision space, thereby abstracting away surface-form variation and reframing provenance testing as measuring the inheritance of decision regions. Empirical analysis shows that the source's induced regions are preserved more strongly in related models than in unrelated models. Building on this signal, we propose Stemma, a practical black-box LLM fingerprinting method that operationalises stability, robustness, and specificity as complementary probe-selection principles for reliably estimating induced decision region inheritance. Across 770 source-suspect pairs drawn from 56 public checkpoints and spanning diverse model-weight transformations, Stemma achieves 0.967 AUC and 87.8% TPR at 1% FPR, substantially outperforming four representative baselines. It further achieves 0.995 AUC and 93.5% TPR at 1% FPR on 1,260 pairs covering 91 deployment instances, demonstrating robustness to diverse inference-time deployment settings.

---


### 11. [From Role Prompt to Infinite Thinking: Exploiting Persona Conditioning for Inference Cost Attacks in LLMs](https://arxiv.org/abs/2607.25936)

**<font color=#1a73e8>作者：</font>** Zhiyi Mou, Wangze Ni, Tianfang Xiao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly deployed in real-world applications, making inference efficiency and service reliability critical concerns due to their substantial computational costs. However, the autoregressive generation mechanism of LLMs enables malicious prompts to manipulate generation behaviors, inducing excessive token generation that amplifies computational consumption and threatens service efficiency. Existing methods mainly rely on adversarial suffixes or explicit extension instructions, which introduce detectable behaviors and limit their applicability. In this paper, we reveal a previously unexplored vulnerability caused by persona consistency in LLMs, where models maintain assigned roles and reproduce corresponding behaviors even when they result in inefficient reasoning and excessive generation. Based on this observation, we propose RolePlay, a task-aware dynamic persona alignment framework that constructs adaptive personas to naturally induce inefficient yet semantically coherent behaviors for inference cost amplification. Extensive experiments across multiple LLMs and diverse task datasets demonstrate that RolePlay consistently outperforms existing inference extension methods, achieving an average token amplification of up to \bm{$7.64\times$} and a maximum token amplification ratio of \bm{$207.64\times$}. Our findings identify persona conditioning as a new attack surface for LLM inference efficiency and offer a new perspective on computational cost amplification.

---


### 12. [\textsc{IH-Benchmark}: A Conflict-Centered Benchmark for Instruction-Hierarchy Robustness in LLM Applications](https://arxiv.org/abs/2607.25987)

**<font color=#1a73e8>作者：</font>** Conor McCauley, Zeliang Kan, Jason Martin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> When a language model receives conflicting instructions from different priority levels, which one does it actually follow? This question lies at the heart of reliable LLM deployment. Existing benchmarks answer this only partially, often focusing on a single hierarchy edge or adapting public datasets with limited tool-use coverage. We present IH-Benchmark, a conflict-centered benchmark for instruction-hierarchy robustness across direct system-user conflicts (S>U) and tool-mediated user-tool (U>T) conflicts. IH-Benchmark is built from a human-authored taxonomy of 44 constraint families across generic, health, finance, retail, and coding settings, and evaluates scenarios with a uniform binary pass/fail protocol combining a predicate DSL with category-scoped LLM judges. Across 37 evaluated models, hierarchy compliance ranges from 98.2% to 20.5%. We find that strong S>U compliance is not a reliable proxy for U>T robustness: several models preserve system constraints under direct user conflict but degrade sharply when conflicting instructions appear in tool outputs. Constraint hardening also reveals a split between models: some failures are largely fixed by stronger warnings, while others persist across all strictness levels. Finally, the most revealing failures are often subtle rather than overtly dangerous; models resist unauthorized purchases or bulk ticket closure more reliably than injected disclaimers or small factual distortions. These results suggest that instruction-hierarchy robustness is not a single capability, but a set of behaviors that must be evaluated across conflict surfaces, constraint types, and attack presentations.

---


### 13. [Does Runtime Topology Context Improve LLM-Generated Kubernetes Security Patches?](https://arxiv.org/abs/2607.25995)

**<font color=#1a73e8>作者：</font>** Farooq Shaikh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Kubernetes is central to the cloud-native ecosystem, orchestrating containerised workloads. Recent work suggests that large language models (LLMs) can automate cluster security remediation, generating configuration patches from Kubernetes Security Posture Management (KSPM) findings without human authoring. Such systems, however, prompt the model with each finding in isolation from the live service call graph, assuming general hardening knowledge suffices. This assumption breaks down whenever a patch must preserve a runtime service dependency invisible to the model: an otherwise compliant fix then carries a destructive functional blast radius, crashing downstream callers or silently severing call edges across the cluster. Whether live cluster context improves patch correctness has not been measured under controlled conditions across multiple dependency classes. We introduce KuTIE (Kubernetes Topology Intelligence Engine), which builds a live cluster context from Istio call edges, Trivy KSPM findings, and the service-account bindings a workload reads, and conditions LLM patch generation on it. It is evaluated on VulnCare, a purpose-built 36-deployment, four-namespace healthcare cluster with 31 injectable findings across seven dependency classes, each labelled by topology dependence against cluster ground truth. Across 248 trials, topology context raises topology-dependent patch correctness from 11.1% to 78.0% ($\Delta = 0.669$), a gap that holds for every model and for six of seven classes, from credential and network-policy ($\Delta = 0.95$) to role-based access control ($\Delta = 0.31$); a topology-independent control exhibits no such effect ($\Delta = 0.0$), isolating the result from generic prompt enrichment. Supplying the live service-call graph and the service-account bindings it exposes thus improves remediation of topology-dependent findings well beyond scanner-only context.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
