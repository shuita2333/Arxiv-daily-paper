# 🔐 大模型安全相关研究 | 2026年06月10日

> 本类共 **25** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [MLingualFC: Evaluating Jailbreak Vulnerabilities in Multilingual Vision-Language Models](https://arxiv.org/abs/2606.07706)

**<font color=#1a73e8>作者：</font>** Rishabh Makwana, Mamta, Deeksha Varshney 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have demonstrated strong performance across multimodal tasks, yet their safety robustness remains an open challenge. While prior work has shown that structured visual prompts such as flowcharts can effectively jailbreak VLMs, existing studies are largely limited to English-centric settings. In this paper, we introduce MLingualFC, a multilingual multimodal benchmark designed to evaluate jailbreak vulnerabilities of VLMs across diverse languages using structured flowchart representations. MLingualFC encodes harmful instructions into flowchart images across five languages (Hindi, Punjabi, Spanish, Romanian, and German). We evaluate state-of-the-art multilingual VLMs, including Qwen2.5-VL, Gemma-4, and Pangea, under a black-box threat model. Our results reveal significant multilingual safety gaps. Flowchart-based attacks achieve high attack success rates (ASR) in case of Latin script languages, demonstrating that visual encoding of harmful content effectively bypasses safety alignment across languages. In contrast, non-Latin script languages such as Punjabi exhibit substantially lower ASR, suggesting potential limitations in visual text recognition rather than stronger safety alignment. These findings highlight that current VLM safety mechanisms fail to generalize across languages and modalities. Resources are available at this https URL

---


### 2. [Beyond Pass/Fail: Using Process Mining to Understand How LLMs Resist (and Fail) Red Team Attacks](https://arxiv.org/abs/2606.07833)

**<font color=#1a73e8>作者：</font>** Zvi Topol  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Standard AI red teaming evaluations reduce adversarial campaigns to a single binary outcome, attack success rate (ASR), not taking into account the sequential structure of how models resist or yield to attacks. We propose applying process mining, a discipline for discovering and analyzing process models from event logs, to red teaming traces. We conduct a controlled experiment pitting 60 HarmBench prompts against two LLMs, GPT-OSS 120B and Llama 3.3 70B, using 10 prompt mutation strategies over up to 110 attempts per prompt. From the resulting 8,575 scored events we extract Directly-Follows Graphs (DFGs) and state transition matrices that reveal structurally distinct defense profiles invisible to ASR alone: GPT-OSS exhibits a near-absorbing refusal state, while Llama presents multiple porous escape routes from refusal to getting successfully jailbroken. We further show that mutator effectiveness is asymmetric across models and that time-to-jailbreak distributions differ by an order of magnitude.

---


### 3. [Model Multiplicity for Adversarial Detection in Small Language Model Training on Edge Devices](https://arxiv.org/abs/2606.07857)

**<font color=#1a73e8>作者：</font>** Stefan Behfar, Richard Mortier  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rise of edge-based machine learning has enabled distributed adaptation of language models across mobile and IoT devices, offering privacy preservation and real-time responsiveness. However, distributed fine-tuning of language models on untrusted or heterogeneous edge nodes introduces new vulnerabilities. Compromised or unreliable devices can inject poisoned updates, leading to stealthy model manipulation or convergence degradation. Classical defenses such as robust aggregation or temporal anomaly detection operate on a single global model and are therefore limited in detecting coordinated or persistent poisoning. This work proposes a new system-level defense based on model multiplicity. Instead of maintaining one global model, the system rotates or concurrently trains multiple small language models (e.g., DistilGPT-2), each updated by independently sampled subsets of edge nodes. These models evolve under distinct training trajectories, creating multiple independent views of the same distributed population. Divergence between models quantified through gradient similarity, loss evolution, or parameter variance serves as a signal of anomalous or adversarial behavior. When one model deviates significantly from the ensemble mean, the system flags its contributing nodes for isolation or re-weighting. We implement this framework and evaluate it on edge-scale simulations of Small Language Model (SLM) training under varying heterogeneity and attack conditions. Results show that model multiplicity enables earlier and more reliable detection of poisoning compared to classical single-model defenses such as Flanders and Robust methods. Our findings demonstrate that diversity in model evolution can serve as a practical and effective defense mechanism for secure distributed learning on resource-constrained edge devices.

---


### 4. [Hallucination Cascade: Analyzing Error Propagation in Multi-Agent LLM Systems](https://arxiv.org/abs/2606.07937)

**<font color=#1a73e8>作者：</font>** Saeid Jamshidi, Arghavan Moradi Dakhel, Kawser Wazed Nafi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) generate fluent text but remain vulnerable to hallucinations, producing unsupported, inconsistent, and factually incorrect claims. Most prior work treats hallucination as a static property of isolated outputs. In multi-agent LLM systems, however, responses are exchanged across agents, revised through sequential stages, and reused as context for later reasoning. Hallucination, therefore, becomes a dynamic process shaped by interaction history, cascade depth, and model heterogeneity. This paper analyzes hallucination dynamics in multi-agent LLM cascades by tracking claim-level factual inconsistencies across sequential agent interactions. We conduct 500 cascade experiments across 10 knowledge domains using GPT-5.3, DeepSeek-V3, and LLaMA-3-70B-Instruct, yielding 1,250 evaluated responses. Results show that deeper cascades reduce the normalized hallucination score from 0.422 at the first agent to 0.272 at the final agent in 3-agent chains, with an amplification factor of 0.644, indicating net attenuation. This reduction is accompanied by a decline in factual accuracy from 0.789 to 0.769, revealing a trade-off between hallucination suppression and factual preservation. Transition-level analysis shows that each agent-to-agent refinement reduces hallucination by an average of 0.072, with small but consistent losses in factual consistency and response quality. Model-level results reveal reliability-efficiency trade-offs: LLaMA-3-70B-Instruct achieves the lowest hallucination score, whereas GPT-5.3 provides faster generation with a higher hallucination rate. Domain-level analysis shows that hallucination varies with topic complexity, with lower scores in well-grounded scientific domains and higher scores in more abstract domains.

---


### 5. [SGTO-MAS: Secure Gorilla Troops Optimization for Multi-Agent LLM Systems](https://arxiv.org/abs/2606.07940)

**<font color=#1a73e8>作者：</font>** Saeid Jamshidi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-agent large language model (LLM) systems offer strong capabilities for complex reasoning and decision-making, yet coordination across agents introduces error propagation, security risks, and inefficient use of resources. Existing methods often rely on heuristic, static strategies and lack a principled mechanism for balancing performance, security, and computational cost. This paper formulates multi-agent LLM coordination as a constrained optimization problem and proposes a security-aware method for adaptive agent selection. The method integrates trust modeling, risk-aware evaluation, and collective intelligence within a unified optimization objective. To solve the problem efficiently, we use a swarm-intelligence strategy inspired by Gorilla Troops Optimization (GTO), enabling adaptive coordination under varying threat conditions. Controlled experiments across 500 independent runs demonstrate the effectiveness of the proposed method. The system achieves a stable average performance score of 0.5281, with high consensus (0.8764), controlled risk (0.3000), and compact agent subsets averaging 4.04 selected agents. The optimization process converges efficiently, with an average runtime of 24.09 seconds per run and low score variability (standard deviation = 0.0173). Robustness analysis indicates graceful degradation under perturbations, with performance drops limited to 2.5% under agent removal and 5.3% under consensus disruption. These results show that effective multi-agent coordination can be achieved through structured optimization that jointly manages performance, security, and efficiency. The proposed method provides a practical security-aware solution for coordinating multi-agent LLM systems in complex adversarial settings.

---


### 6. [Collective Hallucination in Multi-Agent LLMs:Modeling and Defense](https://arxiv.org/abs/2606.07941)

**<font color=#1a73e8>作者：</font>** Saeid Jamshidi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hallucinations in large language models (LLMs) create heightened risks in multi-agent settings, where recursive agent interactions can propagate, reinforce, and amplify unsupported claims. This paper models hallucination as a system-level, time-evolving process across a network of interacting LLM agents, where nodes represent agents and edges encode information exchange. The proposed formulation captures how hallucinated claims diffuse through communication topologies, intensify under adversarial perturbations, and affect collective reliability across reasoning rounds. To suppress error propagation, we introduce an interaction-aware control method that combines confidence-weighted aggregation, adaptive impact regulation, external claim verification, and selective isolation of unreliable agents. Experiments on TruthfulQA and TriviaQA show that the proposed method reduces hallucination by up to 39.0% relative to undefended multi-agent reasoning, improves factual accuracy from 0.79 to 0.87, and increases semantic consistency from 0.75 to 0.84. Under adversarial conditions, the method limits hallucination amplification to 1.08, compared with 1.45 without adaptive control, maintaining stable collective behavior across recursive interaction rounds. These results indicate that hallucination in multi-agent LLM systems is governed by both individual model reliability and system-level interaction dynamics, including communication topology, confidence coupling, and recursive information flow.

---


### 7. [POISE: Position-Aware Undetectable Skill Injection on LLM Agents](https://arxiv.org/abs/2606.07943)

**<font color=#1a73e8>作者：</font>** Haochang Hao, Dehai Min, Zhifang Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills provide a lightweight mechanism for extending general-purpose agents, but their open format exposes them to skill-poisoning attacks. A practically dangerous injection must stay invisible: if executing the payload derails the user's legitimate task, the resulting failure signal invites inspection of the skill. We therefore evaluate attacks by Attack Success Rate, which requires the injected payload to execute and the user's task to still pass its verifier in the same trial. Prior skill-poisoning attacks face a reliability-stealth trade-off under this lens: YAML-header injections are reliably loaded but easily inspected, whereas stealthier body injections that place explicit malicious commands in the skill prose are less reliable because out-of-context commands invite the agent's own suspicion. We introduce POISE, a position-aware attack that compresses the trigger into a single, benign-looking body instruction, placing it at a feasible position and using a context-aware generator to blend it with nearby setup or prerequisite steps. On Skill-Inject with codex+gpt-5.2, POISE achieves an 89.3% ASR, 28.0 points above a random-placement body baseline and 2.6 points above a YAML-only baseline, while retaining the stealth advantage of body placement. That stealth is the decisive margin: because legitimate skill bodies naturally require privileged tool operations, LLM scanners are hyper-sensitive, falsely flagging 74.6% of clean skills on average across four judges and both benchmarks. Blending into these false alarms, POISE causes only 5.6% of poisoned variants to gain a new high-risk alert over their clean baselines, rendering current static defenses ineffective.

---


### 8. [RecurGuard: Runtime Monitoring for Reasoning-Token Consumption Attacks](https://arxiv.org/abs/2606.07968)

**<font color=#1a73e8>作者：</font>** Abid Aziz, Hafsa Binte Kibria  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reasoning-capable large language models can be induced to spend their generation budget on injected decoy tasks rather than answering the user's question, causing denial of service when no final answer is produced and denial of wallet when excess output tokens are billed. Input-side safety classifiers often miss these attacks because the injected prompts can appear syntactically benign. We build RecurGuard, a runtime monitor for detecting reasoning-chain consumption attacks when reasoning traces are exposed by the model. RecurGuard analyzes reasoning traces as they are generated and tracks three signals: recurrence rate, volume growth, and progress toward the user's query. If all three signals remain anomalous over three consecutive chunks, RecurGuard terminates generation early. We evaluate RecurGuard against OverThink and ExtendAttack across open-weight reasoning models and conduct adaptive stress tests on DS-R1-Qwen-7B. On this model, RecurGuard detects 99% of OverThink attacks and 92% of ExtendAttack instances while maintaining near-zero false positive rates on question answering, code generation, mathematics, and summarization. Adaptive evaluation reveals the limit of the defense: topical attacks retain 11.9x amplification with an approximately 50% joint miss rate, whereas full semantic evasion reduces amplification from 22.8x to 2.2x. When reasoning traces are unavailable, QDM provides a post-hoc fallback monitor based on the final output.

---


### 9. [Closing the Sim-to-Real Gap: An Evaluation Framework for Autonomous Cyber Defense Configuration of Commercial EDR](https://arxiv.org/abs/2606.08168)

**<font color=#1a73e8>作者：</font>** Kerri Prinos, Lilianne Brush  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Leading commercial endpoint detection and response (EDR) products have shifted from operator-configured rule sets to multi-component systems where autonomous AI components operate alongside, and increasingly in place of, operator-deployed policies. Autonomous defense agents using commercial EDR as their hardening tool are no longer tuning a passive tool, but a black-box autonomous system capable of making vendor-specific decisions. We present the first evaluation framework for autonomous defense agents hardening commercial EDR. We instantiate it in a Game of Active Directory (GOAD) lab with this http URL's NodeZero as the autonomous pentester and Microsoft Defender XDR as the EDR. We run a sample benchmark of defense agents with two large language model (LLM) backbones (Claude Sonnet 4.6 and Cisco Foundation-Sec-8B). We report three lessons learned that neither simulation nor open-source-EDR evaluation can surface: (i) commercial EDR telemetry is engineered for Security Operations Center (SOC) analyst workflows rather than scientific benchmarking; (ii) the importance of per-policy attribution to separate defense agent actions from autonomous EDR actions; and (iii) the EDR's autonomous behavior varies during the evaluation window. Together, these findings highlight a sim-to-real gap for enterprise defense and motivate evaluation methodology for benchmarking autonomous defense agents in environments with black-box, autonomous tools.

---


### 10. [Sample-Efficient LLM-Based Detection of Malicious Web Server Logs with Forensically Explainable Reasoning](https://arxiv.org/abs/2606.08649)

**<font color=#1a73e8>作者：</font>** Bernhard Kneip, Nhien-An Le-Khac, Hong-Hanh Nguyen-Le  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Forensic analysis of web server logs demands both accurate detection and human-readable explanations that can satisfy legal requirements. We present CEF-Log, a context-enhanced few-shot chain-of-thought prompting strategy for Large Language Models that addresses this dual requirement. CEF-Log embeds expert investigative methodology through a structured five-step reasoning template, enabling the model to learn \textit{how} to analyze logs rather than \textit{what} patterns to memorize. Experimental evaluation demonstrates that CEF-Log achieves an F1-score of 0.99 on the CSIC 2010 dataset using only four examples while providing a $10\times$ improvement in sample efficiency compared to other prompting-based methods. We also introduce ForenWebLog, a new dataset that incorporates real-world attacks and multi-step attack sequences for comprehensive evaluation. Qualitative analysis confirms that CEF-Log generates traceable, accurate explanations suitable for forensic documentation, addressing the critical "black-box" limitation of traditional machine learning approaches.

---


### 11. [Data Agents Under Attack: Vulnerabilities in LLM-Driven Analytical Systems](https://arxiv.org/abs/2606.08661)

**<font color=#1a73e8>作者：</font>** Kuncan Wang, Ziting Wang, Peizhuo Lv 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Data agents integrate LLM-driven reasoning with relational data access, executable analytical tools, and multi-step workflow orchestration, making them increasingly central to enterprise analytics. This integration introduces new security vulnerabilities across data resources, database execution, and agent reasoning, recombining concerns from database security and general-purpose LLM-agent security into failure modes that neither line of work captures on its own. To address this gap, we present a systematic security study of data agents. Our contributions are threefold. First, we develop a layered vulnerability framework that identifies eight data agent-specific risks across interpretation, execution, and policy layers. Second, we introduce an attack taxonomy organized by adversary goal, tactic, and technique, covering three goals, seven tactics, and fourteen techniques, and pair it with an LLM-driven payload generation pipeline grounded in real database schemas. Third, we evaluate these attacks on six systems, including four open-source data agents and two production cloud analytics services. Our experiments reveal substantial security vulnerabilities across current systems and yield four key takeaways.

---


### 12. [Evaluating Multimodal Steganalysis for Split-Payload Audiovisual Steganography](https://arxiv.org/abs/2606.08726)

**<font color=#1a73e8>作者：</font>** Prateek Paudel, Nitin Jha, Abhishek Parakh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The aim of steganography is to hide secret information inside ordinary media so that the existence of communication is hidden rather than encrypted. In audiovisual context, the availability of audio and video streams creates an opportunity to split a payload across these two modes thus, reducing the embedding burden on any single carrier. This paper evaluates whether such split-payload audiovisual steganography can help evade unimodal and multimodal steganalysis under synchronized and asynchronous embedding settings. We create audiovisual samples where the hidden message is divided between the audio and video tracks, and then test how well different detectors can identify them. The single mode detectors performs close to random guessing, thus showing the benefit of this hiding mechanism, while the multimodal model initially appears more effective. However, further checks show that this improvement mostly comes from the video stream, not from a true combined audio-video signal. Overall, the results suggest that splitting the payload across modalities can make detection harder, but multimodal detectors must be evaluated carefully to ensure they are learning the intended signal.

---


### 13. [Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops](https://arxiv.org/abs/2606.08960)

**<font color=#1a73e8>作者：</font>** Ziqian Zhong, Ivgeni Segal, Ivan Bercovich 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent benchmarks score submissions with outcome verifiers that are typically hand-written and brittle, leaving them open to reward hacking. We audit 1,968 tasks across five terminal-agent benchmarks and find 323 (16%) hackable by frontier models given only the task description. This corrupts both leaderboard rankings and RL training signal, yet the standard response is manual and reactive.
We introduce the hacker-fixer loop, a method for building exploit-resistant verifiers without per-task manual patching. The loop alternates three LLM agents: a hacker tries to pass the verifier without solving the task, a fixer patches the verifier to reject each discovered exploit, and a solver confirms the patched verifier still admits legitimate solutions. The loop iterates: each patch reshapes what the verifier rewards, surfacing the next exploit. We further add verifier access, and let patches transfer across tasks, to broaden the exploits the loop discovers.
On KernelBench, the loop drives the attack success rate from 62% to 0% on a held-out corpus of publicly reported exploits. We also find that weaker agents in the loop can defend against much stronger hackers: Gemini 3 Flash's loop drives the stronger Gemini 3.1 Pro and Claude Opus 4.7's attack success rate from 76% and 61% to 0% on KernelBench, and Gemini 3.1 Pro's from 39% to 17% on Terminal Bench across 77 tasks. We release Terminal Wrench (323 hackable environments, 3,632 hack trajectories) as a snapshot of the current attack surface, our patched verifiers, the exploits the loop discovered, and our implementation as a basis for future work.

---


### 14. [Document-Authored Control-Signal Impersonation: A Low-Cost Indirect Prompt Attack on RAG Safety Boundaries](https://arxiv.org/abs/2606.09005)

**<font color=#1a73e8>作者：</font>** Jianguo Zhu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) systems often serialize user queries, retrieved documents, metadata, system labels, and task instructions into one natural-language prompt. We study a source-authority boundary failure in this design: attacker-authored retrieved text can impersonate metadata, provenance, authority, or disclosure-policy signals that appear control-relevant to the model. We call this pattern Document-Authored Control-Signal Impersonation (DACSI). DACSI is a non-imperative, metadata-like payload subclass within indirect prompt injection. Its central lesson is simple: document-authored labels are data, not policy. Command-style injection asks the model to ignore, override, or violate policy; DACSI asks whether untrusted document text can be misattributed as an authorized control signal when RAG prompt rendering collapses trusted and untrusted text into the same natural-language channel.
We evaluate DACSI across six model settings, prompt-pressure levels, injection baselines, signal taxonomies, RAG-mediated pipelines, system-control probes, a source-authority attribution probe, and synthetic canary formats. We interpret the evidence by model regime rather than as six equal replications: DeepSeek V4 Pro and Qwen3.5-397B provide the cleanest positive lift, DeepSeek V4 Flash is a high-susceptibility setting, GPT-5.5 and Gemini 3.1 Pro Low are strong-boundary probes with selected residual risks, and GLM-4.7 is a saturated leakage boundary case. Across these regimes, DACSI warrants separate evaluation because it uses a command-free metadata/provenance/policy surface, follows a RAG-specific source-authority path, and responds to source/channel separation. The source-authority probe is behavioral attribution evidence, not proof of an internal mechanism.

---


### 15. [Context-Fractured Decomposition Attacks on Tool-Using LLM Agents: Exploiting Artifact Provenance Gaps](https://arxiv.org/abs/2606.09084)

**<font color=#1a73e8>作者：</font>** Xiaofeng Lin, Yukai Yang, Daniel Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool-using LLM agents interact with the world through actions that persist state in artifacts (e.g., workspace files or logs). Consequently, jailbreak defenses must reason about cross-step composition rather than isolated text. Yet most existing attacks and defenses, including ``multi-turn'' jailbreaks such as Crescendo and Tree of Attacks,still assume a single contiguous conversation visible to the defender. This assumption breaks down in real agent pipelines, where enforcement is fragmented across tools, modules, and time, and where artifact provenance is often not tracked. We operationalize a deployment failure mode for tool-using LLM agents, the \emph{provenance gap}, and study reproducible triggers for it: \emph{Context-Fractured Decomposition} (CFD), a family of cross-context multi-step jailbreaks that preserve benign-looking intermediate artifacts from an early interaction and elicit harmful behavior much later, potentially in a different agent instance or workflow stage, via individually innocuous tool actions whose risk emerges only under delayed artifact-mediated composition. We instrument the failure mode with trace-level diagnostics and outline a verifiable mitigation direction (provenance lineage tagging). Across agent-system jailbreak benchmarks, CFD improves success rates by up to 28.3 percentage points over state-of-the-art baselines, even against strong single-turn judges. Disclaimer: This paper contains examples of harmful or offensive language.

---


### 16. [Unveiling Privacy Risks in Multi-modal Large Language Models: Task-specific Vulnerabilities and Mitigation Challenges](https://arxiv.org/abs/2606.09125)

**<font color=#1a73e8>作者：</font>** Tiejin Chen, Pingzhi Li, Kaixiong Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Privacy risks in text-only Large Language Models (LLMs) are well studied, particularly their tendency to memorize and leak sensitive information. However, Multi-modal Large Language Models (MLLMs), which process both text and images, introduce unique privacy challenges that remain underexplored. Compared to text-only models, MLLMs can extract and expose sensitive information embedded in images, posing new privacy risks. We reveal that some MLLMs are susceptible to privacy breaches, leaking sensitive data embedded in images or stored in memory. Specifically, in this paper, we (1) introduce MM-Privacy, a comprehensive dataset designed to assess privacy risks across various multi-modal tasks and scenarios, where we define Disclosure Risks and Retention Risks. (2) systematically evaluate different MLLMs using MM-Privacy and demonstrate how models leak sensitive data across various tasks, and (3) provide additional insights into the role of task inconsistency in privacy risks, emphasizing the urgent need for mitigation strategies. Our findings highlight privacy concerns in MLLMs, underscoring the necessity of safeguards to prevent data exposure. Our dataset and code can be found here.

---


### 17. [Steganography Without Modification: Hidden Communication via LLM Seeds](https://arxiv.org/abs/2606.09135)

**<font color=#1a73e8>作者：</font>** Felix Mächtle, Jonas Sander, Sebastian Berndt 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We demonstrate that widely deployed Large Language Model (LLM) inference stacks harbor a steganographic channel that requires no modification to model weights, sampling code, or output distributions. The channel exploits a structural property of deterministic decoding: pseudo-random number generators (PRNGs) used in inverse-transform sampling produce a seed-dependent sequence of token-level probability intervals that can be reconstructed from the generated text alone. A sender encodes a secret message in the PRNG seed before generation; a receiver reconstructs the intervals and recovers the seed, and thus the hidden payload, by exhaustive search over the seed space.
We formalize two operational modes. In the known-prompt setting, sender and receiver share the prompt, enabling exact interval reconstruction and perfect seed recovery via forced alignment. In the unknown-prompt setting, only the generated text is available; approximate interval reconstruction combined with a maximum-hit-count scoring strategy still permits reliable recovery from sufficiently long outputs.
Extensive experiments across six model families and five heterogeneous text domains show that, in the known-prompt setting, full 32-bit seed recovery from the complete 2^32 candidate space achieves up to 100% accuracy, depending on model and text domain, within 300 tokens and under 35 seconds on a single GPU. In the unknown-prompt setting, recovery reaches near-perfect accuracy at 600-800 tokens in about 12 seconds. We further analyze the influence of prompting strategies, tokenization ambiguities, and sampling hyperparameters on channel reliability. Moreover, we discuss several applications of our results: First, it allows for the steganographic transmission of 32 bits, but also shows that ignorance of the prompt is not a valid security assumption.

---


### 18. [PrivCode++: Latent-Conditioned Differentially Private Code Generation for Comprehensive Guarantees](https://arxiv.org/abs/2606.09145)

**<font color=#1a73e8>作者：</font>** Zheng Liu, Chen Gong, Terry Yue Zhuo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models fine-tuned on instruction-code pairs may memorize and subsequently leak sensitive training data. Existing differentially private (DP) code generation methods primarily protect code snippets while assuming prompts are public, which fails in realistic scenarios where prompts may also contain sensitive information. When prompts cannot be explicitly learned or used during generation, code synthesis suffers from severe utility degradation as well as reduced diversity and fidelity. To address these challenges, we propose PrivCode-Plus, the first work to explore DP code generation where both prompts and code snippets are considered sensitive in LLM fine-tuning. PrivCode-Plus introduces a two-stage DP framework with a Privacy-Free Latent Conditioning module, enabling effective DP fine-tuning and data synthesis without direct access to sensitive prompts or code. Extensive experiments show that PrivCode-Plus achieves substantially higher utility than baselines, remains competitive with the method with relaxing privacy assumptions, and provides stronger privacy guarantees.

---


### 19. [Pretrained, Frozen, Still Leaking: Auditing Cross-Encoder Attribute Transfer in EEG Foundation Models](https://arxiv.org/abs/2606.09189)

**<font color=#1a73e8>作者：</font>** Jianwei Tai  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> EEG foundation-model releases are usually audited one endpoint at a time: raw-reconstruction, membership inference, identity linkage, or DP-SGD on the downstream head. We audit the same released embeddings under all four endpoints jointly, on BIOT, LaBraM, and EEGPT, and show that each single-endpoint audit clears releases that still leak spectral attributes. The decisive evidence is a cross-encoder transfer audit: a single ridge attribute decoder learned from one frozen encoder transfers, via a fitted linear bridge, to held-out-subject test splits of every other encoder, with subject-disjoint matched-control 95% CI lower bound at least 0.081 across all six BIOT/LaBraM/EEGPT directions. We prove a sufficient condition: two encoders sharing a nontrivial attribute-coordinate projector overlap beta admit a chained ridge bridge attacker with centered-gain lower bound sqrt(beta/(1+tau^2)) - eps_br - rho_0, and back-solve beta in [0.008, 0.198]. To turn the joint audit into a deployment-readable decision rule we introduce an audit-endpoint disagreement score (AEDS), prove sufficient conditions for its positivity, and bootstrap-calibrate it per cell; AEDS is positive in all eight matched-CI cells (BIOT/LaBraM/EEGPT on EEGMMI; LaBraM on Sleep-EDF, 54-channel LIMO, CHB-MIT pediatric scalp EEG) with p<0.001, while a head-level Carlini LiRA membership audit reaches AUC only 0.50-0.70. Standard defenses fail under audit: a Wiener-style noise-aware adaptive attacker, the LiRA audit, and DP-SGD at every utility-preserving epsilon in {4,8} leave the attribute channel essentially unchanged. The contribution is an audit framework that turns scattered single-endpoint defenses into a joint release decision, supported by a cross-encoder bridge theorem and adaptive-attacker, LiRA, and DP-SGD baselines; the audit licenses release-blocking, not raw-waveform exfiltration or held-out-subject identity recovery.

---


### 20. [Brain-Prompt Injection: A Route-Safety Audit for BCI-LLM Agents](https://arxiv.org/abs/2606.09315)

**<font color=#1a73e8>作者：</font>** Jianwei Tai  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> BCI-to-agent pipelines turn decoded neural activity into an authorization channel for tool-use agents, exposing a new attack surface we call \emph{brain-prompt injection}: signal-side perturbations, context-only injections, and adaptive dual-decoder attacks can all change the routed action while EEG-side or text-side monitors remain blind. Route safety in this stack depends on what the audit log can observe, not on decoder accuracy or agreement alone. We define a Route-Safety Audit Contract: a minimal log schema, denominator hierarchy, and endpoint specification, and prove an audit-schema separation theorem together with a C3 attacked-dependence decomposition; clean agreement and marginal robustness do not identify the joint term that controls C3 routing. As a calibration layer on top of the contract, we apply split-conformal calibration to a non-oracle EEG confirmation channel and report the resulting false-accept frontier under an explicit threat-archetype matrix. We instantiate the contract on EEGMMI native left/right command-control over 5{,}400 events, harmless tool stubs, and seed/case denominators. Provenance blocks C2 routes ($0.000$); agreement-plus-provenance routes C3 flips ($1.000$); confirmation-plus-provenance routes them ($0.000$). The conformal frontier reaches FAR $0.000$ at clean utility $0.150$ for $\alpha=.005$ and FAR $0.119$ at clean utility $0.452$ for $\alpha=.10$ under acquisition isolation; an attacker-controllable confirmation channel breaks the bound to $\approx\!1$. Subject-cluster bootstrap confirms these intervals on $60$ subjects; cross-architecture (TinyEEGNet, EEGNetV4) and capacity-sweep results show within-regime saturation. Mediation and confirmation reduce risk; they are not intent certificates.

---


### 21. [Now You (Still) See Me: Detecting Evasive Steganographic Payloads in LLMs](https://arxiv.org/abs/2606.09411)

**<font color=#1a73e8>作者：</font>** Charles Westphal, Timothy Douglas, Keivan Navaie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models can be fine-tuned to encode prompt-borne secrets into fluent, seemingly benign outputs. This creates a steganographic exfiltration risk that is difficult to detect with output-level steganalysis. Recent work proposes mechanistic detection using linear probes that recover the secret from internal activations. We show that this defense can be systematically evaded, but that detectability can be recovered through a targeted data-level intervention. First, we extend the detection setup to include a non-linear MLP probe. We then adversarially fine-tune steganographic trojans across five base models: Qwen3-8B, Llama-3.1-8B, Ministral-8B, Qwen3-14B, and Phi-4-14B. The resulting models retain $58$--$79\%$ exact-match secret recovery while evading both ridge and held-out MLP probes, with $1$--$8\%$ average capability degradation across six benchmarks. We then give an information-theoretic characterization of this evasion. Successful evasion preserves recoverability while reducing low-order extractability of the secret from the content-aligned representation, forcing the payload into synergistic interaction with residual degrees of freedom. This motivates a recontextualization dataset that restricts these residual degrees of freedom. On this distribution, both ridge and MLP detectability are restored across all five evasive trojans. Overall, our findings show that activation-based steganography detection is vulnerable to adaptive evasion, but also that theory-guided evaluation distributions can expose otherwise hidden payloads.

---


### 22. [SecureClaw: Clawing Back Control of LLM Agents](https://arxiv.org/abs/2606.09549)

**<font color=#1a73e8>作者：</font>** Yuhan Ma, Stefan Schmid  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool-using large language model (LLM) agents face two distinct security failures: unauthorized external actions and exposure of sensitive plaintext inside the runtime before any final output check can intervene. Existing defenses usually protect one boundary, either the planner/runtime or the action sink, and therefore do not by themselves secure both surfaces. We present SecureClaw, a dual-boundary architecture that places authorization at the effect sink and plaintext confinement at the read boundary. Sensitive reads pass through a trusted gateway that replaces raw values with opaque handles and, in the evaluated deployment, bounded summaries as an explicit declassification interface. Writes that change external state follow a PREVIEW$\rightarrow$COMMIT protocol in which only a trusted executor may commit the exact canonical request authorized by policy. The runtime can still plan over summaries and symbolic references, but cannot directly dereference secrets or perform side effects. Across AgentDojo, AgentLeak, and Agent Security Bench (ASB), SecureClaw is the only defense we evaluate in a common harness that simultaneously retains usable task utility and achieves 0\% attack success rate (ASR) on ASB, 0.64\% ASR on AgentDojo, and 3.23\% overall leak on AgentLeak's attacked parity lane, which measures final-output and internal-relay leakage.

---


### 23. [FuseFSS: Efficient Secure LLM Inference with Function Secret Sharing](https://arxiv.org/abs/2606.09551)

**<font color=#1a73e8>作者：</font>** Yuhan Ma, Yong Li, Stefan Schmid  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Two-server secure inference allows a client to query a hosted large language model (LLM) without revealing prompts or embeddings. Recent GPU systems based on function secret sharing (FSS) make linear layers efficient, but fixed-point nonlinearities and helper operations remain a bottleneck because each operator is typically implemented as a bespoke protocol with its own comparisons, wrap-around corrections, and preprocessing material. We present FuseFSS, a compiler that replaces per-operator protocol design with a single compilation pipeline. For each scalar fixed-point operator, a compact specification lists its interval partition, low-degree arithmetic pieces, and required predicate bits. The compiler emits two batched FSS evaluations on the public masked value: one packed comparison that returns all predicate bits, and one vector interval lookup that returns the active coefficients and constants. Compared to the current state-of-the-art FSS-based GPU secure inference, FuseFSS preserves accuracy while achieving a $1.24\times$--$1.50\times$ end-to-end speedup and reducing online communication by $9\%$--$16\%$ on BERT and GPT-style models; preprocessing is also lighter, with $14\%$--$23\%$ lower key-generation time and $20\%$--$24\%$ smaller keys.

---


### 24. [Observability for Delegated Execution in Agentic AI Systems](https://arxiv.org/abs/2606.09692)

**<font color=#1a73e8>作者：</font>** Abhinav Mishra, Kumar Sharad  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Delegation-scoped execution is not identifiable from standard observables: audit logs and execution traces can be identical under multiple incompatible delegation assignments. This gap is especially acute in LLM-based agentic systems, where agents dynamically select tools, vary execution sequences across runs for the same instruction, and spawn cooperating sub-agents. These dynamics fragment and interleave traces, making delegation-scoped reconstruction from causal structure alone structurally underdetermined. Although individual actions are authorized and logged, existing audit, tracing, and security schemas lack the semantics to reconstruct what actions occurred under a given delegation across heterogeneous systems. We focus on delegation-scoped attribution and access/share footprint reconstruction, not intent inference or reasoning reconstruction. We present an agent-aware observability substrate consisting of a lightweight gateway and a common information model that binds delegation context at execution time. This enables reliable cross-tool delegation-scoped reconstruction and direct forensic queries without heuristic time-window correlation.

---


### 25. [What the Eyes See, the LLMs Miss: Exploiting Human Perception for Adversarial Text Attacks](https://arxiv.org/abs/2606.09700)

**<font color=#1a73e8>作者：</font>** Qin Yang, Lu Malloy, Joshua Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-powered content moderation systems have become a critical defense against harmful online content. However, these systems primarily operate on tokenized text and largely ignore the visual cues that humans naturally rely on when interpreting content. We show that this discrepancy creates a fundamental perceptual mismatch: content that is readily recognized as harmful by humans can become effectively invisible to automated moderation systems. To study this vulnerability, we introduce a class of Human-Perceptible Adversarial Attacks (HPAA), in which harmful expressions are embedded into otherwise benign text through visually salient typographic manipulations. Our key insight is that typographic features, including spacing, visual emphasis, and spatial arrangement, can be strategically combined to preserve human recognition of harmful content while substantially reducing machine detectability. Operating in black-box settings with only a small query budget, our attack automatically generates evasive content without requiring model access or gradient information. We evaluate the attack across multiple datasets and ten deployed moderation systems, including commercial APIs and state-of-the-art open-source guardrails. Results reveal a striking gap between human and machine perception: with only three detector queries, generated attacks achieve over 86\% human recognition while maintaining detection rates below 1\% across the evaluated systems. We further conduct ablation studies to identify the typographic factors driving successful evasion, analyze why current moderation architectures fail to capture these signals, and discuss practical defenses. Our findings expose a fundamental blind spot in today's LLM-based moderation ecosystem and highlight need for moderation systems that reason about content in a manner more consistent with human perceptual understanding.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
