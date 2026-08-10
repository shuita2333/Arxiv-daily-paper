# 🔐 大模型安全相关研究 | 2026年08月10日

> 本类共 **9** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [WorldMark: A Plug-and-Play World Knowledge Interface for Cross-Host Language Model Watermarking](https://arxiv.org/abs/2608.06416)

**<font color=#1a73e8>作者：</font>** Song Xiao, Yuqi Yuan, Yanshuo Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Watermarking traces the provenance of text produced by large language models by embedding statistically detectable signals during decoding. Existing schemes fall into logits-based, sampling-based, entropy-aware, and adaptive-strength families, yet all of them place watermark signals according to local token statistics. In the open-ended text-generation settings evaluated in this work, local statistics may provide insufficient guidance for placing robust watermark signals. We introduce WorldMark, a plug-and-play interface that uses World Knowledge Memory (WKM) to organize semantic and episodic knowledge in a memory graph, converts the retrieved knowledge into a token-level knowledge saliency score, and adjusts the strength of a host watermark through Asymmetric Knowledge Modulation (AKM). WorldMark requires no backbone retraining and introduces no additional detector-side model or parameter. On the primary C4 evaluation, the complete WorldMark interface improves clean and attacked detection across three adaptive-strength host variants while slightly reducing perplexity. Additional pilot experiments on C4 and OpenGen show that direct memory conditioning transfers across multiple watermark families but can be unstable without saliency-aware modulation. WorldMark requires no additional detector-side model or parameter and introduces negligible overhead under the primary protocol.

---


### 2. [CyberForge: Verified Vulnerability Injection at Repository Level for Cybersecurity Agent Training](https://arxiv.org/abs/2608.06471)

**<font color=#1a73e8>作者：</font>** Amine Lbath, Manan Suri, Aurelien Delaitre 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Despite recent advances, frontier large language model (LLM) agents remain limited in discovering and patching complex vulnerabilities in real-world software. Generally available agents can already aid attackers, who only need to find one exploitable weakness, while defenders must continuously identify and patch all vulnerabilities across fast-growing codebases. Stronger defensive agents would help close this gap, yet the scarcity of security training data with reproducible build and execution environments remains a bottleneck.
We present CyberForge, a framework that synthesizes executable, repository-level security training data by injecting vulnerabilities into real C/C++ projects. It validates each instance dynamically: the injected build must pass the project's unit tests, and generated proof-of-vulnerability (PoV) must trigger on the injected build and not on the clean one. CyberForge is not limited by the availability of disclosed vulnerabilities, therefore it can scale in comparison to data augmentation techniques which rely on historic CVE data. The resulting corpus holds 1034 validated vulnerabilities across 80 projects and 63 weakness categories, with edit locality similar to real CVE patches under a real-versus-real noise floor. Fine-tuning on trajectories collected over this corpus improves SEC-bench patch repair by +3.3 to +14.7 points, in all six configurations of three model scales and two teachers, with the 31B student reaching its GPT-5.4-mini teacher, 72.7% against 74.0%. These gains generalize out of distribution to PatchEval, a corpus containing other programming languages, where every configuration also improves and the 31B student passes its teacher.

---


### 3. [From Documentation to Zero-day Vulnerabilities: LLM-Driven Fuzzing of JavaScript Engines in PDF Readers](https://arxiv.org/abs/2608.06641)

**<font color=#1a73e8>作者：</font>** Suyue Guo, Stijn Pletinckx, Tianle Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing fuzzers for PDF readers rely on simple test cases that involve only individual API calls, leading to limited coverage and potentially missing vulnerabilities that require sequences of API calls. To address these limitations, we propose PDFuzzer, a novel PDF engine fuzzer that automatically generates complex and meaningful API call sequences. PDFuzzer first uses a Large Language Model (LLM) to construct context-free grammars and infer the relationships between individual API calls from specifications extracted from JavaScript API manuals and execution traces. Based on the grammars and relationships, PDFuzzer employs a constraint solver to generate concrete API call sequences for fuzzing. Our experiments show that PDFuzzer significantly outperforms state-of-the-art PDF fuzzers (TypeOracle, Favocado, and Cooper) and LLM-based fuzzers (Fuzz4All, naive LLM) on three mainstream PDF readers: Adobe Acrobat Reader, Foxit PDF Reader, and PDF-XChange Editor. PDFuzzer achieves up to 48% higher coverage than existing tools and identifies 31 zero-day vulnerabilities in these readers, from information leakage to arbitrary code execution. Our ablation study validates the necessity of each component, including LLMs, which achieve high accuracy across all pipeline stages (93-98%). We disclosed all vulnerabilities to the vendors via a coordinated vulnerability disclosure process and received bug bounties.

---


### 4. [CyberLLM: A Multi-Agent LLM Framework for Autonomous Detection and Guarded Response in Automotive Cybersecurity](https://arxiv.org/abs/2608.06651)

**<font color=#1a73e8>作者：</font>** Nenad Petrovic, Oussama Jeddou, Feres Ben Fraj 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software-Defined Vehicles (SDVs) expand the automotive attack surface across source code, runtime logs, and deployment topologies, while safety constraints forbid autonomous agents from acting without oversight. This paper presents CyberLLM, a multi-agent, LLM-orchestrated framework that autonomously detects vulnerabilities and executes remediations under a formal, runtime safety guard. Detection combines a deterministic layer (regex rules, AST analyzers, and topology graph checks) with an LLM refinement pass, so a high-recall floor is complemented by high-precision reasoning. A decision agent aggregates findings, tags them with a human-centric asset taxonomy, and selects a tiered response, ratcheting its confidence with signed cross-session memory and re-planning feedback. Every action is validated against four contextual security properties and an independent action-alignment oracle before it is allowed to run, and refused actions trigger escalation and re-planning. A symmetric attack pipeline generates and replays exploits so both sides can be exercised on the same scenarios. On an independent, ground-truthed benchmark of nine original automotive ECU modules in C, C++, and Rust seeding 47 layered vulnerabilities plus clean controls, the always-on deterministic layer covers 34\% of the labeled vulnerabilities at perfect precision, and adding the grounded LLM refinement and completeness passes roughly doubles coverage to about 70\% (F1 $0.83$) while producing zero false positives on the clean controls. The results indicate that LLM agents can perform useful autonomous cyber-defense when wrapped in a deterministic, auditable safety envelope.

---


### 5. [Policy-Masked Private Experts: Auditable and Reversible Capability Access Control in Sparse MoE Models](https://arxiv.org/abs/2608.06690)

**<font color=#1a73e8>作者：</font>** Zhuoheng Huang, Mukesh Singh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Most language-model access controls regulate behavior while leaving the same computation available to every request. We study a different systems question: can trusted authorization determine which newly trained parameters are reachable by the forward pass? Policy-Masked Private Experts freezes a pretrained sparse Mixture-of-Experts (MoE) model, trains a disjoint expert branch, and selects the public or private pool before top-k routing. The resulting claim is narrow but testable: under the declared trusted computing base (TCB), an unauthorized request executes no private expert. It does not imply that the public model lacks the same semantic capability.
We test this separation between execution control and task utility in Qwen3-30B-A3B and DeepSeek-V2-Lite. Three Qwen BF16 seeds update all 32 private experts while the public fingerprint remains unchanged. Across 64 adversarial scenarios and 96 deny/fail-closed events, unauthorized private execution is zero; independent hooks exactly match 11,616 routed private rows and allow-deny-allow recovery is exact. On two prospectively frozen Qwen benchmarks, the private branch improves exact tool use by 5.0 percentage points (pp) (five versus zero discordances; one-sided Holm p = 0.03125, corresponding two-sided exact p = 0.0625) and 21.3 pp (percentile-bootstrap 95% CI [13.3, 29.3], Holm p = 0.000031). Three arm-blinded model evaluators retain a positive external effect of 18.7 pp (95% CI [9.3, 28.0]). A parameter-matched Lora has similar external utility, but a post-hoc request gate leaves 1,225 adapter calls under deny; the disjoint expert branch leaves none. DeepSeek reproduces the route invariant and gains 27.0 pp. A valid sealed evaluation is near-neutral. These results support auditable, reversible control over a trained parameter path, while showing that useful transfer remains distribution dependent.

---


### 6. [Retrieval-Constrained Policy Optimization for Attack Technique Extraction from Cyber Threat Intelligence](https://arxiv.org/abs/2608.06778)

**<font color=#1a73e8>作者：</font>** Jiayun Zhang, Junshen Xu, Zejun Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mapping cyber threat intelligence (CTI) text to MITRE ATT&CK techniques is essential for structured threat analysis, yet manual annotation is costly and does not scale. The ATT&CK taxonomy comprises several hundred attack techniques, and a single CTI passage may describe multiple techniques, making accurate and complete extraction challenging. Existing automated approaches fall short in different ways: multi-label classifiers struggle with severe class imbalance and the large label space, while LLM-based methods--retrieval pipelines and fine-tuned generators--optimize token-level objectives that treat technique annotation as sequence generation rather than set prediction, lacking direct supervision on whether the predicted technique set is correct and complete. We propose TTP-R1, a two-stage framework that combines retrieval-augmented supervised fine-tuning (SFT) with reinforcement learning using verifiable rewards (RLVR). A hybrid retriever first narrows the large label space to a candidate set, and a fine-tuned LLM learns to select the correct techniques. We then apply Group Relative Policy Optimization with a decomposed reward that directly supervises the precision, recall, and output format of the predicted technique set. Across four CTI benchmarks, TTP-R1 achieves the best average F1, improving sub-technique-level F1 by 7.4 percentage points over Claude Sonnet 4.5 with retrieval augmentation, while running 28x faster when served as an 8B-parameter model on a single GPU.

---


### 7. [LoRAScan: Detecting Backdoor Prompts in Low-Rank Adapters for Large Language Models via Down-Projection Activation Spikes](https://arxiv.org/abs/2608.06795)

**<font color=#1a73e8>作者：</font>** Doniyorkhon Obidov, Honggang Yu, Xiaolong Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) enables efficient specialization and distribution of large language models through compact adapters. However, untrusted adapters introduce a supply-chain threat: a backdoored adapter can cause a model to generate harmful content, malicious code, political propaganda, or covert advertisements when an input contains a hidden trigger. Adapter-agnostic defenses merge the adapter with the base model, which dilutes backdoor signals and reduces detection performance. Existing adapter-aware methods do not address how to safely use a potentially backdoored adapter. Instead, they either train a defensive adapter to repair a backdoored base model, addressing the inverse problem rather than securing the adapter itself, or rely on a classifier that flags the entire adapter as suspicious and requires separate mitigation. These methods overlook the distinct latent-space signatures produced by trigger-bearing inputs in backdoored adapters.
We introduce LoRAScan, the first adapter-aware defense that detects and rejects trigger-bearing inputs at inference time without modifying adapter parameters. Our key observation is that a small subset of LoRA insertion sites, approximately 5%, remains stable across clean inputs but exhibits highly concentrated spikes in LoRA down-projection activations when a trigger is present. LoRAScan identifies these low-variance insertion sites before model deployment and monitors them during inference. Across standard LLM backdoor benchmarks, LoRAScan rejects approximately 98.49 of malicious inputs with a small error rate on clean inputs, outperforming existing defenses across diverse evaluation settings.

---


### 8. [SynChain: Inducing Computer-Use Agent Systems to Construct Their Own Attack Chains](https://arxiv.org/abs/2608.06862)

**<font color=#1a73e8>作者：</font>** Fuyao Zhang, Jiaming Zhang, Che Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Computer-use agents~(CUAs) have transformed large language models into persistent execution systems capable of generating, storing, and reusing artifacts like skills and memory entries. However, existing security defenses largely treat attacks as externally triggered or temporally bounded, leaving a critical gap in addressing how compromise can propagate internally through an agent's own persistent state. We reveal that malicious influence can be covertly embedded into the structural redundancies of autonomously synthesized artifacts, allowing it to survive internal state updates and bypass standard vetting mechanisms. To formalize this threat, we introduce SynChain, a self-synthesized attack paradigm utilizing persistence-aware directed supervised fine-tuning to induce agents to create poisoned yet benign-looking artifacts. To systematically evaluate this propagation, we construct CUAChain, a dataset comprising 30 benign task chains and three attack objectives. SynChain enables dormant payloads to seamlessly reactivate in future workflows as trusted context, operating entirely without new malicious exogenous inputs. Extensive experiments on OpenClaw, Codex, and Claude Code under four defense settings demonstrate that SynChain achieves high attack success and outperforms adapted baselines, proving that securing CUAs requires provenance-aware reasoning over cross-task execution trajectories.

---


### 9. [When Context Bites: Detecting RAG Poisoning via Document-Level Attention Collapse](https://arxiv.org/abs/2608.06947)

**<font color=#1a73e8>作者：</font>** Yingtao Ren, Ziyi Zhao, Yiwei Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) is indispensable for enhancing large language models. However, RAGs are increasingly susceptible to poisoning attacks, in which adversarial documents are injected to manipulate generator outputs. Previous methods rely on output-side signals such as perplexity and consistency checks to detect such attacks. Nevertheless, our analysis reveals that deliberate attacks often induce false confidence, where poisoned outputs exhibit even lower perplexity than benign ones, rendering uncertainty-based detection ineffective. To address this challenge, we explore the internal dynamics of the generator and identify a distinctive signature termed \textit{Attention Collapse}. Unlike the dispersed attention in benign generations, attacked generations exhibit a decrease in entropy as attention concentrates on poisoned documents. Building on these findings, we propose \texttt{D-SCAN} (Document-level Signal Collapse Analysis), a lightweight detection framework that monitors attention dynamics to identify attacked generations. Extensive experiments on multiple attack benchmarks demonstrate the effectiveness of our method. Moreover, D-SCAN can detect attacks even when they fail to alter the final answer. Code is available at this https URL.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
