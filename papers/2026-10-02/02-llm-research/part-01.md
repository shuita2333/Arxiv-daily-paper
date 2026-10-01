# 🧠 大模型相关研究 | 2026年10月02日

> 本类共 **390** 篇论文：已确认 **371** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-390](./part-08.md)

---

### 1. [Large Language Models are Approximate Survival Estimators](https://arxiv.org/abs/2609.38181)

**<font color=#1a73e8>作者：</font>** Juan M Zambrano Chaves, Peniel Argaw, Risa Ueno 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Survival analysis estimates time-to-event outcomes from patient covariates and is widely used for medical risk assessment. Patients seeking prognostic information after a diagnosis may turn to large language models (LLMs), now readily accessible through consumer applications. However, whether LLMs can provide accurate survival predictions has not been rigorously evaluated. We introduce Survprompt, a framework that converts structured patient covariates into free-text clinical vignettes and prompts pre-trained LLMs to predict survival zero-shot. We benchmark Survprompt against conventional survival models, including random survival forests (RSF), across two multi-institutional pan-cancer cohorts: the publicly available MSK-CHORD cohort and a newly curated cohort from the Providence St. Joseph Health Network constructed using an LLM-based medical abstraction framework. We report censored mean absolute error (cMAE) and concordance index (c-index) and conduct feature ablations to identify variables influencing LLM predictions. Frontier LLMs achieved surprisingly competitive cMAE for individual survival times. For example, GPT-5.6-Sol achieved cMAE within 10% of state-of-the-art RSF models specifically trained for survival prediction for several cancer types and lower cMAE than RSF for prostate cancer in MSK-CHORD. Feature ablations revealed that LLMs prioritized clinical variables similarly to specialized survival models. However, LLMs showed inconsistent accuracy across cancer types and institutions and poorly discriminated between high- and low-risk patients (lower c-index). Zero-shot LLMs can generate surprisingly accurate prognostic estimates without specialized training, but their variable performance across cancer types and institutions remains an important limitation for clinical use.

---


### 2. [Why and How People Check Generative AI Output for Mistakes](https://arxiv.org/abs/2609.38186)

**<font color=#1a73e8>作者：</font>** Patrick Gage Kelley, Derrick Feldmann, Reena Jana 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI output can contain errors, such as hallucinations, non-responsive results, or otherwise inaccurate or potentially harmful content. To explore the public's emerging understanding, attitudes, and behavior regarding such mistakes, we ran an online survey in the United States with 1,503 respondents, with a representative sample of the population. We report high public awareness of generative AI mistakes. Further, many respondents report checking generative AI output, for example, by comparing results with other online resources. We conclude with guidance for explanations and in-product disclosures about generative AI mistakes.

---


### 3. [DualCast: A Dual-Path Language Model for Bimodal Financial Time-Series Forecasting](https://arxiv.org/abs/2609.38197)

**<font color=#1a73e8>作者：</font>** Wentao Zhao, Hongqiang Wu, Shanghang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial time-series forecasting must capture price dynamics across heterogeneous assets while incorporating news available at prediction time. We introduce DualCast, a dual-path framework that extends a frozen language model with a discrete financial vocabulary. Each log-return patch is represented by a learned summary token and three residual shape tokens, preserving local drift and volatility while allowing shape patterns to be shared across assets. To improve codebook utilization, we develop adaptive frequency-equalizing residual vector quantization, which rebalances overloaded codewords without compromising reconstruction accuracy. The fast path trains only the new financial-token embeddings and output heads on a frozen Qwen3-8B backbone. A toggleable LoRA adapter enables a slow path that conditions on the fast forecast and news available at the forecast origin to produce a revised prediction. The reviser is initialized by supervised fine-tuning and further optimized with a return-space group relative policy optimization objective that rewards improvements over the fast forecast. In zero-shot evaluations covering equities and energy prices at five-minute, daily, and weekly resolutions, the slow path achieves the lowest mean absolute percentage error among the compared methods in 8 of 12 dataset-horizon settings, including every longest-horizon setting. News ablations indicate additional gains in most tested settings, although their magnitude varies across markets. DualCast thus combines a fast numerical forecaster with an optional text-conditioned revision mechanism.

---


### 4. [TomasuLLM: Out-of-Order Speculative Execution for LLM Agents](https://arxiv.org/abs/2609.38201)

**<font color=#1a73e8>作者：</font>** Jiangnan Yu, Ceyu Xu, Mengming Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-running tools can dominate coding-agent latency: compilers, test suites, and repository commands take seconds to minutes while the agent idles. This observation stall presents the same tension that drove out-of-order processors -- asequential interface hides work that can be predicted and started early, but a speculative result may become visible only after it and every earlier step have been validated.
We present TomasuLLM, a runtime that executes agent tool calls out of trajectory order while preserving task-execution correctness. It drafts future actions, runs them in isolated copy-on-write sandboxes, traces their dependencies and effects, and commits results in trajectory order only after validation against committed state. Across three benchmarks spanning sub-second to minutes-long tool calls, TomasuLLM improves the reported benchmark means and scales with tool latency: 1.31x on 100 SWE-bench Verified tasks, 1.35x on 28 Terminal-Bench 2.0 tasks, and 1.27x matched progress on 18 SWE-Marathon sessions. Across 4,010 audited commit-validation records, it produces zero false accepts.

---


### 5. [The System Prompt Illusion: How Instruction Preambles Modify Computation in Language Models](https://arxiv.org/abs/2609.38205)

**<font color=#1a73e8>作者：</font>** Muhammad Usama, Dong Eui Chang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> System prompts are the primary lever practitioners use to control language model behavior, yet what they actually do to the computation inside the transformer remains poorly understood. Across 17 instruction-tuned models spanning 8 architecture families and 1.5B to 72B parameters, we use Centered Kernel Alignment (CKA) to compare layer-wise representations under 20 system prompts in five functional categories. Effects are layer-selective and instruction-type-dependent: persona and formatting instructions deeply restructure intermediate representations, while safety instructions barely move them, producing changes statistically indistinguishable from a minimal baseline. Restrictive safety instructions and explicitly permissive ones ("you have no restrictions") engage near-identical computational pathways (mean CKA correlation 0.997), and this persists at commercial scale, where safety penetration remains below 10% even at 70B-72B. A linear probing baseline exposes the mechanism: the model encodes prompt category at every layer but restructures its computation only at a small subset, so the prompt is reliably "seen" but, for safety, not deeply "acted upon." Causal activation patching confirms these layers mediate behavioral change, and representational depth predicts behavioral effect size across the full 17-model cohort (Spearman rho = 0.761, p < 0.001). The findings provide a mechanistic explanation for the persistent jailbreak vulnerability of system-prompt-based safety. Code: this https URL

---


### 6. [Conformal Factuality Control for Multi-Hop Retrieval-Augmented Generation](https://arxiv.org/abs/2609.38222)

**<font color=#1a73e8>作者：</font>** Muhammad Aimal Rehman, Chi-Kuang Yeh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) can ground large language models in external evidence, but retrieved context does not guarantee that generated claims are factually supported. This problem is especially relevant in multi-hop RAG, where retrieval and reasoning proceed through multiple dependent stages. We study whether claim-level conformal factuality control, previously developed for RAG, remains effective in this setting. We apply split-conformal claim filtering to multi-hop RAG and evaluate it on HotpotQA, Natural Questions, and TriviaQA using Llama 3.1 8B and GPT-4o-mini, together with a single-hop reference experiment. Across all six multi-hop model-dataset configurations, increasingly stringent conformal targets consistently increase the fraction of responses whose retained claims are fully supported. At the 95% target, this rate ranges from 95.80% to 97.20%, compared with 55.60%-76.03% without filtering. However, the improvement is strongly selective: only 4.41%-31.09% of generated claims are retained and 9.70%-51.40% of responses remain non-empty at the 95% target. These results show that conformal factuality extends to multi-hop RAG, while demonstrating that nominal reliability must be interpreted jointly with claim retention and abstention.

---


### 7. [CATP: Design and Evaluation of Local Agent Authorization and Audit Evidence](https://arxiv.org/abs/2609.38223)

**<font color=#1a73e8>作者：</font>** Linfeng Zhou  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A signed authorization record authenticates what a signer asserted, but does not by itself establish that the assertion agrees with the policy and action used for a runtime decision. CATP specifies the bindings needed to carry a local pre-execution decision into offline-verifiable evidence. Its hook commits to the enforcement-time policy and adapter-normalized action and durably records the decision before returning permission. A later receipt binds the record to a self-contained audit export.
An implementation for Claude Code and Codex supports an empirical examination of these bindings. Controlled, validly signed counterexamples expose five missing consistency checks; adding them changes acceptance on the same inputs, with all 13 expected outcomes satisfied. A separate probe finds that distinct argument vectors can become the same normalized action before hashing, limiting what even a consistent receipt can establish. Eight scripted runtime cases verify hook delivery and allow/deny behavior; failure tests cover tampering, substitution, replay, concurrency and persistence errors. Median paired hook overhead is approximately 85 ms, and offline verification takes approximately 174 ms end to end on the testbed. The evidence remains conditional on a trusted runtime, monitor, host and signing key. It authenticates a decision about the normalized action, without proving execution truth, complete disclosure or autonomous task utility. The optional Groth16 study covers a narrower circuit predicate; the evaluation does not establish superiority over other systems.

---


### 8. [Separation of Duties for Privileged LLM Agents: A Governed Execution Architecture with Measured Security-Utility Trade-offs](https://arxiv.org/abs/2609.38224)

**<font color=#1a73e8>作者：</font>** Qishuai Jing  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model agents are increasingly granted real privileges (executing commands, modifying files, calling APIs), so an agent that errs has already acted. Existing defences concentrate on the agent's inputs, while the path from a candidate action to privileged side effects remains less directly studied. We argue that this path must be governed outside the model, and study an architecture interposing four roles (planner, policy gate, executor, auditor) between agent and operating system.
Two choices are central: actions arrive as structured intents, so adjudication never parses shell syntax; and approval is a one-shot credential bound to the exact bytes that will run. We evaluate on a 313-case benchmark across eight variants, with prompt-only baselines from three hosted LLMs on 150 stratified cases, five repetitions (2,250 attempted calls; 2,249 completed).
Effective attack success falls from 98.3% under direct execution to 7.7% deployed. Re-execution against the real implementation yields a similar aggregate rate (7.6% over 66 sandbox-evaluable payloads) but substantial case-level disagreement, at a corrected false-denial rate of 11.1%. A substantial final-stage reduction (from 30.8% to 7.7%) is attributable to the operating-system sandbox, and the benchmark found four implementation defects, none by design review.

---


### 9. [Inference-Layer Security: Defending Against Adversarial Inference and Infrastructure Abuse](https://arxiv.org/abs/2609.38239)

**<font color=#1a73e8>作者：</font>** Keifer Lee  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A Technical Report: Operating a large language model (LLM) as a service requires more than inference infrastructure: the provider must also defend against adversarial interactions that seek to exploit the service, including jailbreaking for harmful use, sophisticated denial of service, and distillation attacks. We study this problem at the inference layer, using a hypothetical frontier lab, Five Elements Inc., as a running example. Because no public labelled dataset of adversarial LLM usage exists, we introduce a structural causal model (SCM) that generates a realistically grounded, labelled dataset of user-sessions, with coordinated multi-account campaigns, platform feedback, and three tiers of label observability. On this dataset we train a practical gradient-boosted detector that classifies each user-session as benign or malicious and, if malicious, by attack type. Against oracle labels the detector very nearly solves the binary task (AUPRC $0.993$), yet against the operational labels a real Trust & Safety team would hold, the same model scores an AUPRC of only $0.313$: the detector is more accurate than the labels used to evaluate it. For attack-type attribution, a naive argmax is dominated by the $98\%$ benign prior (macro-F1 $0.295$), whereas a simple thresholded decision engine raises macro-F1 to $0.489$ without sacrificing accuracy. The dataset is publicly released.

---


### 10. [Agent-Warden: eBPF-Based Kernel-Native Process-File Provenance Tracking for LLM Agents](https://arxiv.org/abs/2609.38245)

**<font color=#1a73e8>作者：</font>** Dongxu Cui, Zhichao Gu, Ping Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents execute dynamically generated process and file operations that are often invisible to application-layer tracing. We present Agent-Warden, an extended Berkeley Packet Filter (eBPF)-based provenance monitor for tracking task and regular-file states across process creation, file access, and process termination. Agent-Warden provides two interchangeable state backends: a PID-keyed hash-map backend for compatible kernels lacking BPF local-storage support and a task/inode-local-storage backend that couples state reclamation to kernel-object lifetimes. The system emits incremental causal edges to user space for asynchronous graph reconstruction and applies conservative exit-triggered causal aggregation to preserve causal context for short-lived proxy tasks. In a controlled file-mediated propagation scenario, Agent-Warden reconstructed a cross-process causal chain that was absent from the application-layer trace. On x86-64 and ARM64 bare-metal hosts, the evaluated workloads showed 0.2-3.5% end-to-end overhead and 0.6-3.7% additional system CPU time. These results indicate that the prototype provides kernel-level visibility with the measured overheads in the evaluated settings.

---


### 11. [ContractWarden: Kernel-Enforced Damage Boundaries for AI Agents via Human-Authorized Contracts](https://arxiv.org/abs/2609.38248)

**<font color=#1a73e8>作者：</font>** Dongxu Cui, Zhichao Gu, Ping Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model agents can execute commands, create subprocesses, and directly access files and networks, allowing prompt injection or planning errors to become operating-system side effects. We present ContractWarden, a Linux reference monitor that enforces a human-authorized damage boundary without trusting the agent or its policy suggestions. A model may propose a tri-state asset contract - allow, deny, or no_egress - but a human makes the final choice. An execution gate binds the contract to a concrete task before untrusted code runs. An extended Berkeley Packet Filter (eBPF) Linux Security Modules (LSM) data plane then enforces file and network decisions and monotonically propagates no_egress through processes, regular files, pipes, FIFOs, and supported Unix-domain sockets. All 570 runs across 19 security tests satisfy predefined return-value and side-effect criteria. On three co-located file-I/O workloads, median overhead is 11.96-12.89% in a Linux 6.15 virtual machine and 35.79-61.54% on a Linux 6.15 physical platform, lower than the evaluated frozen ActPlane baseline. The results demonstrate deterministic kernel enforcement for declared assets, supported paths, and controlled object lifecycles.

---


### 12. [SURE: Framework for Safety to Construct Trustworthy AI](https://arxiv.org/abs/2609.38249)

**<font color=#1a73e8>作者：</font>** Soeun Han, Jisoo Lee, Jeongyong Shim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Warning: This paper contains harmful and offensive text.
Recently, large language models such as GPT-4, and Claude have revolutionized tasks in various domains. As the use of these large language models increases, people are increasingly concerned about AI safety and demand that large language models behave responsibly and safely. As a result, there has been growing global interest in developing methods to ensure AI safety. However, the detailed criteria for AI safety may vary depending on the country, culture, and policies of the company you serve. In this study, we propose SURE (A Safe and Unified AI Framework foR Everyone), which is designed as a framework for customizing the attributes of AI safety and ensuring the defined AI safety. Within SURE, we establish taxonomies for adversarial prompts that could threaten AI safety and construct prompts based on the taxonomies. We then define templates for desirable AI responses to these prompts and design an absolute safety scoring scheme. Finally, we conduct AI alignment using the datasets to gradually ensure AI safety. The effectiveness of SURE is demonstrated through experiments with various base models.

---


### 13. [Framing the Narrative: Ideological Mimicry in Large Language Models](https://arxiv.org/abs/2609.38256)

**<font color=#1a73e8>作者：</font>** Olivia Macmillan-Scott, Michael Jacobs, Nils Metternich 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to answer questions about politically contentious issues, yet evaluations typically treat a model's stance as a relatively stable property. Real users, however, communicate political signals through their terminology, assumptions, and personal context. We investigate whether such signals produce ideological mimicry: systematic shifts in the political stance expressed by an LLM toward the position conveyed by the interaction. If LLMs adapt their responses to these signals, they risk creating personalised political information environments in which users with opposing views receive systematically different accounts of the same issue, potentially reinforcing existing divisions. We build the Poli-SHIFT dataset and evaluation framework and assess seven open-weight LLMs across ten contentious political topics in the United States, United Kingdom, and Australia, systematically manipulating contested terminology, politically valenced premises, and user information, and eliciting responses in both multiple-choice and open-text formats. Across models, we find robust evidence that prompt framing shapes the political stance of LLM outputs. Changing terminology alone reverses which side of an issue a model supports in 16.9% of matched comparisons. Stated political ideology also systematically shifts responses toward the user's position. These findings show that political stance is not a fixed property of LLMs; the views expressed are conditional on the interaction with the user. As LLMs become increasingly personalised sources of information, such interaction-dependent adaptation could contribute to political information environments that reinforce users' existing perspectives.

---


### 14. [ContextAdapt: Evaluating Contextual Adaptation and Value Alignment in LLMs](https://arxiv.org/abs/2609.38260)

**<font color=#1a73e8>作者：</font>** Olivia Macmillan-Scott, Mirco Musolesi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Values such as honesty, autonomy, and confidentiality are often regarded as general principles underpinning AI alignment. However, what it means to act in accordance with these values can depend on the context in which a decision is made. In this paper, we ask whether large language models (LLMs) appropriately adapt the application of a value across professional settings, while remaining consistent when contextual changes do not alter the relevant professional norm. To study this, we introduce ContextAdapt, an evaluation framework covering honesty, autonomy, and confidentiality across medicine, law, finance, and national security. Drawing on primary-source professional and regulatory documents, we construct a value x domain framework and use this to develop scenarios testing both default professional rules and recognised exceptions. We evaluate 12 LLMs on both the actions they recommend and the justifications they provide. In our main experiment, models achieve 95.6% mean appropriateness, although the use of the correct domain-specific justification varies substantially across models, from 25.6% to 76.9%. In a separate factorial experiment, explicitly naming the professional domain and changing the role of the model have limited effect on behaviour. Varying stakes, however, reveals severe but localised failures: in some cases, models alter their responses even though the underlying professional obligation remains unchanged. In particular, perceived severity appears to act as a cue for disclosure across both honesty and confidentiality scenarios. These results show that evaluating value alignment requires us to consider not only whether models follow abstract principles, but whether they apply them appropriately across different contexts.

---


### 15. [NinaXander: Feasibility and Limits of Composing Frozen Language Models Across Architecture Families via a Shared Latent Space](https://arxiv.org/abs/2609.38261)

**<font color=#1a73e8>作者：</font>** Takanori Kotama, Shun-ichiro Hayashi, Daichi Mukunoki 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper we propose NinaXander, a series of composed language models obtained by connecting layers of frozen language models from different architecture families with a single trained shared-latent adapter. A composed model runs the first layers of one model, converts the resulting intermediate representation once with the adapter, and then runs the remaining layers of the other model. Once the adapter is trained, several composed models that connect at different layers are obtained without retraining. Using the recurrent RWKV-4-Raven-7B and the Transformer-based Tulu-Pythia-6.9b, abbreviated as RWKV and Pythia, this study examines whether frozen models from different families can be recombined post hoc. The composed models answered multiple-choice questions, and those whose generations we examined produced syntactically well-formed text. The configuration that combines the first 5 layers of Pythia with the remaining 27 layers of RWKV reduced the Transformer key-value (KV) cache by 84.4% with accuracy not significantly different from that of RWKV alone. In multiple-choice accuracy, however, no composed model matched the parent model Pythia, and language-modeling performance decreased sharply on WikiText, a corpus of Wikipedia articles outside the training domain. The correspondence between intermediate representations was also obtained in one favorable case, with a shared tokenizer, the same depth, and the same hidden width, and does not show that the models share a general semantic space.

---


### 16. [Janus: Evidence-Before-Effect Sagas and Offline-Verifiable Provenance for Agentic LLMs](https://arxiv.org/abs/2609.38266)

**<font color=#1a73e8>作者：</font>** Mustafa Arslan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic large language models (LLMs) now move money through tools, yet the record of what they did is usually a trace their own process emits beside the effect. Janus puts the record on the effect path. A step's proposal, the verdict on it and any answer from a validator or a person are durable in a signed, hash-chained log before the step may run or its effect be released; with keys declared, each answer is signed by whoever gave or relayed it. Gates are pure functions of that log, and an auditor re-derives every verdict offline from the log and one public key. At the MCP edge the effect is held until then; through the SDK, which our model experiment uses, a cooperating client runs it only afterwards. We evaluate Janus under crash injection (144 kills in-process, 81 through the daemon), by verifying a 100-million-event log offline (254.5 s), and with a real model behind a lending workflow, run governed and plain on the same recorded model outputs. With the lending mandate in the model's prompt, the comparison was 0 against 0. With it only in the policy and the amount's unit stated, the model approved six loans declared over the mandate, three with no injection (a run that also dropped the unit approved three); the plain agent paid all six and Janus none, each refused by a deterministic validator and re-derivable offline. An always-approve oracle over the recorded intakes gave 20 and 21 declared over the mandate against 0, though Janus paid four and three whose declared amount understated the request. Designing the experiment exposed, in a system that passed its own audit, an instance of post-approval substitution: an approval keyed to an attempt was counted for a different proposal, moving a person's approval from 100 to 1,000,000. We report it, a first fix and the five routes around it, and what Janus does not guarantee.

---


### 17. [VirusCascade: Hijacking Collaborative Reflection in LLM-Powered Recommender Agents](https://arxiv.org/abs/2609.38270)

**<font color=#1a73e8>作者：</font>** Yurong Hao, Wen Zhou, Guowei Guan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Advancing beyond traditional static scoring models, LLM-powered agentic recommender systems (LLM-ARS) instantiate users and items as autonomous agents, whose semantic states are dynamically refined through a recurrent process known as collaborative reflection. While this mechanism improves recommendation quality, it simultaneously introduces a systemic vulnerability: adversarial evidence injected into a single agent can be rationalised into a legitimate preference narrative, written back into memory, and propagated to other agents through interaction contexts. We term the local rationalisation process reflection laundering, and its system-wide escalation through collaborative reflection collaborative-reflection hijacking. Existing attacks on recommender systems, whether based on interaction-level data poisoning or text-level adversarial perturbations, assume static pipelines and thus cannot exploit this recurrent, multi-agent amplification pathway. To bridge this gap, we first conduct a controlled vulnerability analysis that establishes two exploitable properties underlying collaborative-reflection hijacking: reflective persistence and cross-agent propagation. Then building on these findings, we propose VirusCascade, the first black-box targeted promotion attack that jointly shapes semantic and structural attack surfaces: the former ensures the target item is naturally rationalised as satisfying broad user preferences, the latter positions it for system-wide propagation. Extensive experiments on four real-world datasets across diverse LLM-ARS architectures demonstrate that VirusCascade consistently achieves state-of-the-art targeted exposure under evaluated stealth constraints, reaching a mean E@20 of 0.384 and surpassing the strongest baseline by an absolute margin of +0.185.

---


### 18. [Which Models Work Well Together? Measuring Heterogeneity for LLM Team Selection](https://arxiv.org/abs/2609.38274)

**<font color=#1a73e8>作者：</font>** Liangyu Teng, Hengsong Liu, Juncen Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The performance ceiling of an LLM team is constrained not only by individual model capabilities, but also by inter-member error resonance and predictive differences. Although heterogeneous teaming is often observed to be effective in practice, existing approaches lack complementarity metrics that are computable, interpretable, and optimizable, leaving team composition to rely on heuristics. We propose a heterogeneity-driven team selection framework that performs offline profiling to characterize individual capability along with two complementary signals: one captures decorrelation in error patterns to reduce co-failures, while the other measures divergence in predictive behavior to capture strategy diversity. We formulate team selection as a standardized quality--complementarity combinatorial objective and apply an efficient greedy search to select a small team from a candidate pool. Experiments across multiple benchmarks demonstrate that our framework consistently outperforms quality-only baselines under controlled candidate pools and team sizes, establishing reusable selection principles for multi-LLM systems.

---


### 19. [Improving OCR Faithfulness via Gated and Attenuated On-Policy Distillation](https://arxiv.org/abs/2609.38282)

**<font color=#1a73e8>作者：</font>** Baode Wang, Zuming Huang, Kexuan Ren 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models may rewrite anomalous text in images into linguistically plausible expressions, compromising OCR transcription faithfulness. Sequence-level task rewards and local teacher guidance are complementary, but guidance from the same teacher may not remain equally effective as the student improves. Offline analysis shows that supervision from a fixed teacher becomes progressively less favorable as the student improves, both across training checkpoints and across response groups with different task rewards. Motivated by this observation, we introduce GAD-RL, which adaptively regulates teacher supervision during joint post-training according to the student's current task performance and local distributions. A frozen teacher conditions on reference transcriptions and student-generated prefixes. GAD-RL disables distillation for response groups containing an output with task reward at least 0.95 and continuously attenuates distillation strength as group-mean reward increases. It also weights forward KL by the student's probability of the teacher's Top-1 token, moderating local auxiliary updates when student support for that candidate is low. On Qwen3.5-2B, GAD-RL achieves 59.92% Micro Recall on CHAOS-Bench, surpassing GRPO and GRPO+OPD (fixed-weight) by 8.45 and 4.43 percentage points, respectively, while achieving an Overall score of 91.18 on OmniDocBench v1.6.

---


### 20. [GaugeVLM: Structuring Spatial Supervision with Measured Geometric Interventions](https://arxiv.org/abs/2609.38285)

**<font color=#1a73e8>作者：</font>** Hongbo Wang, Zihan Lin, Wenkui Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) can contradict themselves across views of the same spatial relation and fail to respond when that relation changes. Addressing these failures requires supervision that captures error magnitude and geometric dependencies across observations, both of which remain implicit in training on individual answers or ordinal preferences. Therefore, we introduce GaugeVLM, which makes this structure explicit through controlled object and camera interventions in explicit 3D scenes, producing linked observations with measured differences between spatial relations and shared truths across views. To translate this structure into learning signals, its core objective, GaugeDPO, converts measured errors into preference margins, directly supervises correct canonical rankings across views, and links intervention-induced answer-odds contrasts to measured relation changes with view-specific scales. Our analysis bounds canonical prediction error and establishes that the cross-view and intervention constraints can be jointly satisfied. Empirically, GaugeVLM improves all 10 established spatial metrics over supervised fine-tuning across three VLM backbones, with the main 7B model gaining 15.0 and 18.9 percentage points on MSMU distance and QSpatial+, respectively. These gains also extend to autonomous driving and embodied reasoning, demonstrating the robust generalization across domains.

---


### 21. [AREX-2: Advancing Self-Improving Agents through Long-Horizon Reflective Tasks](https://arxiv.org/abs/2609.38288)

**<font color=#1a73e8>作者：</font>** Hongjin Qian, Chaofan Li, Kun Luo 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present AREX-2, an effort to advance the self-improving capability of LLM agents, which we define as the ability to iteratively refine a solution at test time. This ability rests on two complementary capabilities: reflection, which produces a solution better than the current one, and long-horizon execution, which keeps the iteration effective over many rounds. We hypothesize that both capabilities are domain-agnostic, and can therefore be learned in scenarios that are well suited for supervision. Accordingly, we synthesize long-horizon improvement trajectories from machine learning and algorithmic programming tasks, two domains that offer verifiable feedback and reward sustained iteration. Trained on this data, our agent, built on Qwen3.8-27B, achieves strong results on MLE-bench Lite (81.8) and Frontier-CS (70.7), transfers to deep research with 84.0 on BrowseComp, 52.6 on HLE, 92.2 on GAIA, and 93.8 on DeepSearchQA, and keeps improving as its budget of rounds grows. These results show that long-horizon reflective data is an effective route toward self-improving agents.

---


### 22. [MoFlow: Multi-Objective Agentic Workflow Generation](https://arxiv.org/abs/2609.38294)

**<font color=#1a73e8>作者：</font>** Yining Lu, Aurelie Lozano, Xi Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study the generation of agentic workflows that jointly optimize multiple objectives, such as accuracy, cost, latency, robustness, and consistency. Existing methods for workflow generation typically optimize accuracy alone or a weighted sum of objectives, so each trained generator commits to one fixed trade-off and must be retrained from scratch when preferences change. To alleviate this, we propose MoFlow, which generates workflows optimized across varied preferences. Specifically, MoFlow formulates workflow generation as a multi-objective Markov decision process and solves it by leveraging Convex-Hull Monte Carlo Tree Search with optimistic set-valued backups, where every node stores a set of reachable trade-offs rather than one weighted score. A single search thus approximately covers the Pareto front, from which MoFlow can return a workflow for any preference by lookup without retraining. We evaluate MoFlow against six strong baselines on six benchmarks spanning mathematics, code, and question answering. Since the baselines are single-scalar optimizers by design, an apples-to-apples comparison is difficult. We instead adopt an evaluation setup that favors the baselines, in that they are rerun for each testing preference, which MoFlow never sees. Even under this stringent setup, MoFlow achieves the highest average hypervolume.

---


### 23. [AI Agents are Vulnerable to Radicalization](https://arxiv.org/abs/2609.38296)

**<font color=#1a73e8>作者：</font>** Ozgur Can Seckin, Shalmoli Ghosh, Alessandro Flammini 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can influence people's beliefs, yet little is known about whether and how they can manipulate each other. To investigate this, we simulate conversations between two agents: a target LLM that role-plays a human persona based on demographic and psychological attributes, and an influencer LLM that aims to make the target's beliefs more extreme. We examine radicalization along two pathways: resonance, where the influencer reinforces a target's pre-existing belief, and persuasion, where the influencer promotes a belief the target initially considers unimportant. Across affective and behavioral metrics, we find that both mechanisms radicalize the target. However, resonance produces consistently stronger effects than persuasion. Different influence tactics, such as using sycophancy and unverified claims, produce different levels of radicalization, but not consistently across metrics. We further show that resonance propagates to related beliefs, suggesting interconnected belief structures within AI agents. These findings indicate that AI agents are susceptible to radicalization, particularly when messages align with their existing beliefs, raising concerns about the vulnerability of personalized AI agents and multi-agent AI ecosystems.

---


### 24. [It Takes Little to Rewrite Perception: Targeted Semantic Substitution in Vision-Language Models at $ε\leq 4/255$](https://arxiv.org/abs/2609.38298)

**<font color=#1a73e8>作者：</font>** Binchi Zhang, Atrisha Sarkar, Apurva Narayan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Language Models (VLMs) are widely deployed in safety-critical scenarios, and understanding to which extent they can be controlled by adversarial perturbation is a prerequisite for evaluating their trustworthiness. Existing representation-alignment attacks, which make a VLM perceive a target image, achieve limited success at $\varepsilon \leq 4/255$. Therefore, VLMs seems robust to perturbations in this range. We show that this robustness does not hold, as targeted semantic substitution succeeds within the same range. Specifically, we align each stream of the source image with its counterpart in the target image in the victim VLM's post-merger token space, operating under a white-box threat model. We evaluate under a strict success criterion, requiring the model to simultaneously name the target, confirm its presence, and deny the source. In images, target semantics appear at $\varepsilon = 2/255$ and complete replacement reaches 38\% at $\varepsilon = 4/255$. On video, complete replacement reaches 35.9\% at $\varepsilon = 1/255$. We also observe a phenomenon of \textit{semantic fusion}, where Large Language Model (LLM) rationalizes contradictory visual signals into a coherent narrative.

---


### 25. [Strike a Chord! Modal Kinetic Typography](https://arxiv.org/abs/2609.38325)

**<font color=#1a73e8>作者：</font>** Maham Tanveer, Jiyeon Han, Nanxuan Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce modal kinetic typography, which animates a vector glyph to express a semantic concept while keeping it legible. Our key idea is to build motion from the glyph's natural vibration modes. Specifically, a finite-element eigenproblem assembled from the vector outline yields the glyph's softest modes, for the whole letter and for each of its parts, allowing it to bend. The problem's zero-energy solutions, i.e., rigid translations and rotations, are applied in closed form to each part, allowing parts to also move as blocks. To animate the glyph, a frozen video diffusion model supervises only the modes' amplitudes and phases. Our modal approach addresses two weaknesses of prior work. Free-form point optimization under video score distillation (SDS) moves each point and frame independently along noisy gradients, tearing the outline and causing jitter. In contrast, our modes are smooth along the outline and driven by a few whole-cycle harmonics, which restricts these gradients to smooth, seamlessly looping motion. On the other hand, structured alternatives rely on skeletons or keypoints from category-specific priors, whereas our modes come from the glyph itself; the only prior is a list naming each letter's moving parts, generated once for the whole alphabet by a language model. In modal kinetic typography, shape and motion are disentangled by construction: a single base outline is sculpted toward the concept, and the modal drive cannot alter it, so a letter can also be animated without being reshaped. Our method produces more articulated and smoother motion than Dynamic Typography and AniClipart at comparable or better concept alignment, with less glyph tearing than Dynamic Typography, and is preferred by human raters, including in a frozen-shape setting where motion alone must carry the concept. Our results were also preferred over Astra (GPT-6) by human raters.

---


### 26. [Absorbing State Phase Transitions in Multi-Agent Search](https://arxiv.org/abs/2609.38327)

**<font color=#1a73e8>作者：</font>** Wenwen Zheng, Yuzhe Yang, Helen Qu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Nontrivial dynamics can emerge in large language model (LLM)-based multi-agent systems, and preliminary evidence exists that formalisms from statistical mechanics can be effective at modeling and predicting such behaviors. In parallel, designing multi-agent communication topology for optimal task-solving is an active research question. In this paper, we focus on predicting the success of multi-agent search tasks using the formalism of absorbing state phase transitions. We first taxonomize search tasks into four types, informed by classical results in combinatorial search. We then theoretically derive a critical communication degree $d_c$, the minimum number of agents each agent can communicate with, above which incorrect hypotheses do not proliferate uncontrollably and the search enters the solved state. Finally, we evaluate frontier LLM-based multi-agent systems on real-world search and discovery tasks, software configuration debugging and physical mechanism discovery, and find that agreement with theory is mixed. LLM agents may not communicate with their neighbors and can develop strategies that are individually beneficial but limits the benefits of collaboration.

---


### 27. [ExploreNet: Learning Where to Explore in Diffusion GRPO](https://arxiv.org/abs/2609.38329)

**<font color=#1a73e8>作者：</font>** Shuyue Stella Li, Xiaochuang Han, Yulia Tsvetkov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Group-relative RL methods such as Flow-GRPO post-train image generators by exploring with isotropic Gaussian noise added at every denoising step. This noise decides which rollouts the model learns from, yet it perturbs every channel and spatial position of the latent equally. In this paper, we instead show that latent elements differ in how much they change the generated image, so exploration should adapt to these differences. We introduce EXPLORENET to learn an adaptive exploration distribution. EXPLORENET is a policy that predicts a noise scale for every latent element from the current latent, the denoising step, and the prompt, before any reward is observed; it is trained on the reward spread of each rollout group and discarded after training, leaving inference unchanged. On Stable Diffusion 3.5 Medium, EXPLORENET improves held-out GenEval2 by 14% over Flow-GRPO, transfers to two independent compositional benchmarks and five preference and image-quality models, and reaches a 67.2% human preference win-rate. Overall, across our group-relative diffusion RL experiments, we find that exploration is learnable, the shape of the exploration distribution outweighs its magnitude, and rollout quality is more effective than rollout quantity.

---


### 28. [Hermes: Learning Contextual Reasoning Unlocks Test-Time Scaling](https://arxiv.org/abs/2609.38332)

**<font color=#1a73e8>作者：</font>** Xinyu Li, Mononito Goswami, Hao Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time scaling improves model performance by allocating additional compute during inference. Using this compute effectively across multiple context windows requires deciding how to allocate fresh contexts and what information to carry between them. We call a model's ability to make these decisions contextual reasoning. Existing approaches largely prescribe these decisions through their harness; we instead shift them to the model. We introduce 1) Hermes, a family of simple, configurable harnesses that progressively varies model control over context allocation and reuse, and 2) Hermes-Learn, a two-stage framework for learning these capabilities. We find that capable models can exploit this flexibility to scale with additional inference-time compute, while smaller open-source models initially struggle to do so. Training with Hermes-Learn closes this gap, inducing adaptive contextual reasoning strategies that vary with both the problem and the progress of reasoning. These gains generalize across benchmarks and models, extrapolate beyond the inference-time compute seen during training, and transfer to complementary test-time scaling methods beyond Hermes.

---


### 29. [EVOKE: Eliciting World Knowledge in Agents for Transferable Decision-Making](https://arxiv.org/abs/2609.38334)

**<font color=#1a73e8>作者：</font>** Yuhan Guo, Jinming Liu, Liang Xu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as agents for multi-step decision-making, yet transfer poorly to unseen environments. World-model methods address this by training agents to predict future observations, at the cost of additional training and errors that compound when predictions are used for planning. However, for LLM agents operating in digital environments, much of this world knowledge is already internalized during pretraining, which shifts the problem from acquiring it to eliciting it. We argue that typical post-training provides little pressure for such elicitation, since supervision under a single goal at each visited state inadvertently drives policies to rely on superficial contextual habits. We introduce EVOKE, a post-training method that supplies this pressure through goal diversity at fixed states. Motivated by theory showing that an agent competent across diverse goals must encode a world model recoverable from its action preferences, EVOKE holds the environment state and interaction history fixed and ranks the same candidate actions under alternative goals, forcing action preferences to change, so that a policy relying on contextual habits or single-goal correlations cannot order them correctly. This implicitly elicits the policy's pretrained world knowledge to inform decisions. We evaluate EVOKE across diverse tasks in three backbones, demonstrating improved task performance, unseen environment generalization, and data efficiency. We further conduct controlled analyses to better understand what drives these gains. These findings offer a new perspective on eliciting internalized world knowledge for transferable action through direct decision supervision.

---


### 30. [CARAT: Do Materials LLMs Reason or Recite?](https://arxiv.org/abs/2609.38340)

**<font color=#1a73e8>作者：</font>** Jiajun Wu, Jian Yang, Zixiang Ni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a materials LLM answers a question about crystal structure, does it reason from the structure or copy an answer already printed in its input? Accuracy cannot tell: a structural description often prints the very field it is scored against. CARAT holds question and gold answer fixed across eight matched views, names each structural relation separately in GraphSpace, and adds matched fine-tuning, answer masking, evidence injection, paired inference, and a rule that can withhold claims. First, on the benchmark's hardest families the grounded view is worth 17.3 points over formula inputs. Second, we turn that scrutiny on ourselves. GraphSpace beats a plain periodic graph by 19.3 points, but that margin is two effects at once: where the plain rendering carries everything the question needs it is 1.96 points, and where it omits those fields entirely, 46.7 points. The headline mostly measures what the baseline lacked, not how evidence is presented. Third, we attack our own benchmark. A rule that skips the link and reads the list directly answers four of seven hardened families, so we rebuilt it until eleven such shortcuts sat near chance. The frozen model quotes that link yet answers the same when we redirect it, on 95.6% of paired cases: it repeats the relation without using it. After matched supervision it reaches 99.8%, and deleting the link drops it to 23.4%, below the 27.0% the best shortcut reaches: both steps are learnable.

---


### 31. [Activation-Conditioned Self-Distillation](https://arxiv.org/abs/2609.38342)

**<font color=#1a73e8>作者：</font>** Zhexi Lu, Subhajit Chaudhury, Tejaswini Pedapati 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation uses a model as its own teacher to provide dense supervision for reasoning, often through reference-solution conditioning. Providing privileged information does not by itself ensure effective token-level supervision throughout long responses. We introduce Activation-Conditioned Self-Distillation (ACSD), which extracts a steering vector by contrasting activations of self-generated trajectories that reach verified correct answers within a generation budget with those of all remaining trajectories. A frozen copy of the base model applies this vector at each prediction position, and the student learns from its next-token distributions on student-generated prefixes. Outcome verification is used for direction construction and calibration; distillation requires neither problem-specific reference text nor teacher parameter updates. The distilled student is used alone at inference. On each of five models, ACSD achieves the highest mean accuracy over four mathematical benchmarks among the evaluated methods. On DeepSeek-R1-0528-Qwen3-8B, mean mathematical accuracy reaches 71.9\% and LiveCodeBench v6 pass@12 reaches 70.9\%, compared with 69.0\% and 66.3\% for the reference-conditioned OPSD baseline. Contrasts among correct trajectories also support distillation, and extracted directions can be reused across mathematical training datasets. On fixed student trajectories, ACSD maintains more stable late-position logit-update magnitudes than OPSD.

---


### 32. [Examining Variation in How Guided AI Tutors Resolve Student Impasses](https://arxiv.org/abs/2609.38346)

**<font color=#1a73e8>作者：</font>** Bakhtawar Ahtisham, Kirk Vanacore, Alessandra Napoli 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a student is stuck, a tutor faces the assistance dilemma: help given too early can hinder productive struggle, while help withheld too long leaves the student in a frustrating, persistent impasse (i.e., wheel spinning). Generative AI tutors increasingly use guardrails restricting answer-giving, yet little is known about how such tutors behave once an impasse persists. We analyze 20,462 student turns from 1,260 authentic sessions with a guided LLM chemistry tutor, identifying 6,630 impasse turns of three major types: conceptual errors, expressed uncertainty, or help-seeking. We then used these impasses to simulate three tutoring conditions to study variation in AI tutor guidance through impasses: baseline, no-direct-answer, and guided tutor. For a sample of 150 impasses, prompt specificity changed pedagogy: a baseline tutor provided the answer directly in 50.7% of responses, a no-direct-answer tutor asked a follow-up question every time, and the guided tutor responded in a wide variety of ways depending on the context. We then analyzed impasse trajectories in authentic interactions, finding that each additional impasse turn lowered the odds of next-turn recovery by 12.7% (AOR = 0.873, p < .001), and early dropouts were caught in recursive concept elicitation before reaching execution. The benefit of questioning decayed as impasses persisted (scripted question x depth AOR = 0.78; follow-up x depth AOR = 0.83), whereas addressing the student's error grew more beneficial (AOR = 1.14); after a failed scripted question, repeating it was followed by recovery in 28.1% of cases, compared with 39.8% when the tutor addressed the error instead. For learning analytics, these findings identify impasse depth and type as observable, turn-level dialogue signals that analytics can use to trigger graduated, state-sensitive assistance in real time.

---


### 33. [MILO: Automated Harness Discovery via Orchestrated Multi-Agent Evolution](https://arxiv.org/abs/2609.38349)

**<font color=#1a73e8>作者：</font>** Prithwish Jana, Mononito Goswami, Hao Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern agentic systems combine an AI model with a harness that controls execution and environmental interactions. Harness design strongly affects long-horizon performance, yet its combinatorial search space demands substantial human effort that must be repeated as models change. Existing automated methods explore this space narrowly, optimizing only components such as prompts or skills or becoming trapped by fixed, exploitative search strategies. We introduce MILO (Meta-evolutionary Island Orchestration), a framework that co-evolves agent harnesses and the strategy used to discover them. MILO combines: (i) hierarchical lineage memory over island-based trees, using rejected mutations as negative evidence; (ii) per-island mutator agents that rewrite complete harnesses using global search history and parent-specific feedback; and (iii) an orchestrator that adapts search through lineage grafting and speciation, mutator reassignment and curriculum revision. Across Terminal-Bench 2.1, PaperBench, and DeepSWE, MILO-discovered harnesses outperform eight state-of-the-art harnesses and six search methods using frontier (Opus 4.8) and open-weight (gpt-oss-120b) models. With Opus 4.8, MILO improves resolution over its initial harness by $+12.0\%$, $+28.3\%$, and $+10.3\%$, respectively, compared with best prior-search gains of $+4.5\%$, $+18.3\%$, and $0\%$. On Terminal-Bench 2.1, it achieves $86.1 \pm 2.0\%$, exceeding the official leaderboard's top entry ($83.8 \pm 2.3\%$) while using 26\% fewer tokens than its initial harness. On EinsteinArena open problems, MILO improves best-known upper bounds for Erdős minimum-overlap ($0.3808586 \to 0.3808568$) and the first and third autocorrelation inequalities ($1.50274365 \to 1.50274360$; $1.45081 \to 1.44889$).

---


### 34. [Halluscoring 2026: The first shared task on llms hallucination detection and answer verification](https://arxiv.org/abs/2609.38355)

**<font color=#1a73e8>作者：</font>** Aisha Alansari, Abdessalam Bouchekif, Ahmed Hasanaath 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present HalluScoring 2026, a shared task for evaluating hallucination detection and factual verification in Arabic question answering under challenging generalization settings. The shared task is organized into two main tasks, each comprising two subtasks, for a total of four subtasks. Task 1 evaluates binary hallucination detection, considering generalization to unseen questions (Subtask 1.1) and responses generated by unseen LLMs (Subtask 1.2). Task 2 extends the evaluation beyond detection by requiring the systems to additionally identify the correct factual answer from six related candidates, covering Islamic knowledge (Subtask 2.1) and general knowledge (Subtask 2.2). The shared task is based on two Arabic datasets: HalluScore and HalluTruthQA. A total of 13 teams participated in the shared task, 10 of which submitted system description papers. The results of Task 1 demonstrate that hallucination detection remains challenging under distribution shift, with the winning team achieving AUC-ROC test scores of 0.772 and 0.767 for Subtasks 1.1 and 1.2, respectively. For Task 2, the winning team achieved scores of 0.882 and 0.857 in the Islamic and general-knowledge subtasks, respectively, under assisted evaluation.

---


### 35. [Beyond Mode Collapse: Generating Diverse Synthetic Expert Conversations via Generative Flow Networks](https://arxiv.org/abs/2609.38359)

**<font color=#1a73e8>作者：</font>** Sumit Asthana, Michael Ion, Kevyn Collins Thompson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> High quality synthetic data is central to post training LLMs for adaptive AI applications that represent the diverse expert strategies and decisions in conversations. Prompting LLMs directly or conditioning them on end use scenarios yields low diversity data that collapses onto dominant modes. We propose a method to generate diverse high quality synthetic data using Generative Flow Networks (GFlowNets). We show that training GFlowNets to generate latent conversation structure using a Gaussian mixture density over key interaction features (e.g., confusion episode dynamics, scaffolding directive balance) enables sampling expert strategies in proportion to their prevalence in the training data. Across two structurally distinct domains, tutoring and emotional support dialogues, our GFlow based synthetic data generation approach offers a better balance of fidelity, mode coverage and authenticity than reinforcement-learning and end to end LLM baselines, without copying training data. Evaluated on three downstream outcome prediction tasks, classifiers trained on synthetic GFlowNet generated conversations provide a stronger training signal than competitive synthesis baselines.

---


### 36. [On the Off-Policy Teacher in On-Policy Distillation](https://arxiv.org/abs/2609.38360)

**<font color=#1a73e8>作者：</font>** Langlin Huang, Hao Liu, Mononito Goswami 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has recently emerged as a promising post-training paradigm in which the student learns from trajectories generated by its own policy under dense teacher supervision. However, OPD introduces a fundamental asymmetry: although the sampled trajectories are on-policy for the student, they are off-policy for the teacher. The teacher is typically optimized to continue from prefixes generated by its own policy, but during OPD it must instead supervise prefixes generated by the student. Empirically, we find that its continuation performance degrades as these prefixes grow longer. To address this issue, we propose Student-COnditioned Updates of the Teacher (SCOUT), a co-training framework that adapts the teacher to student-generated prefixes. Alongside standard OPD updates, SCOUT periodically optimizes the teacher's conditional ability using reinforcement learning with verifiable rewards, where the teacher generates continuations from student prefixes and learns from outcome rewards. Controlled experiments show that SCOUT improves the teacher's ability to continue from student-generated prefixes, supporting the intended mechanism of student-conditioned teacher adaptation. Across multiple teacher--student configurations, model scales, and reasoning domains, SCOUT also consistently improves the effectiveness of on-policy distillation.

---


### 37. [Inductive Visual Logic for Few-Shot Out-Of-Distribution Adaptation in VLMs](https://arxiv.org/abs/2609.38362)

**<font color=#1a73e8>作者：</font>** Hung-Jen Chen, Yu-Heng Ho, Ting-Yao Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative vision-language models (VLMs) such as Qwen-VL and LLaVA achieve strong zero-shot performance on tasks overlapping with their pretraining distribution, yet fail on specialized domains where the required discriminative features were never learned, a regime we term distant out-of-distribution (OOD). Standard adaptation methods cannot overcome this representational absence because they operate within the encoder's existing feature space. However, VLMs retain a robust descriptive capacity even when discrimination collapses: a model that cannot classify a medical scan can still articulate its visual patterns. Exploiting this asymmetry, we introduce Inductive Visual Logic (IVL), a training-free framework that constructs classification knowledge from the model's surviving descriptive ability. IVL extracts visual traits from few-shot support images through dual-mode prompting, combining semantic descriptions with primitive visual observations, and organizes them into per-class trait dictionaries. At inference, hierarchical filtering identifies spatially grounded trait evidence for classification. Across multiple distant-OOD benchmarks, IVL achieves the highest aggregate accuracy under two VLM backbones while producing interpretable, trait-traceable predictions.

---


### 38. [Composition, Not Conversation: VLMs Lose the Scene, Not the Thread](https://arxiv.org/abs/2609.38368)

**<font color=#1a73e8>作者：</font>** L. D. M. S. Sai Teja, Ufaq Khan, N. Siva Gopala Krishna 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) increasingly reason over visual evidence that is cropped, segmented, retrieved, or revealed over time. Yet most VQA benchmarks present the complete image and question at once. We ask what models lose when the same information is fragmented. We introduce Layered-VQA, with 93 scenes and 300 questions. Each image is decomposed into ordered RGBA layers that exactly recompose the original scene, and each question is annotated with supporting, minimal-sufficient, and distractor layers. We evaluate eleven open-weight VLMs from 3B to 32B parameters and two proprietary models with a scale of 187,200 conversations, graded by 1.74M open-model cross-judgments. We find three consistent failures. Loss in Composition: fragmenting the question has a small effect, but fragmenting the scene substantially reduces accuracy; recomposing the same layers largely restores performance. Oracle Inversion: even oracle-selected sufficient evidence can perform worse than the complete scene. Loss in Grounding: as more evidence is required, grounding degrades much faster than answer accuracy. Together, these results show that having the right visual evidence is not enough. How that evidence is composed and presented determines whether models can use and ground it. The right evidence is not enough: VLMs need the scene it came from.

---


### 39. [Self-Evolving Harness on Multiple Tasks with the Agent as Its Own Optimizer](https://arxiv.org/abs/2609.38372)

**<font color=#1a73e8>作者：</font>** Qiankai Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A harness is the code around a language-model agent that organizes prompts, calls tools, manages context, and controls execution. As models grow stronger, recent work has begun to let agents improve their own harnesses, a line of work known as self-evolving harnesses. In most existing methods, a separate proposer running on a human-designed harness modifies the solver's harness, and a separate harness is evolved for each benchmark. Real-world tasks come from many domains, so both the evolution and the evaluation of a harness should cover a diverse range of tasks. We propose a framework close to recursive self-improvement: the same frozen model, on the same version of the harness, first solves tasks as the solver and then, as the proposer, reads the complete run records and directly edits the harness that runs it. Each evolution batch draws tasks from five benchmarks in different domains. To measure generalization, training and held-out tasks are strictly separated, and we additionally evaluate on five out-of-distribution benchmarks never used during evolution. We frame the evolution process as deep-learning training with two stages, multi-task pretraining and continual training. Starting from a 49-line seed harness, the harness obtained at the end of the first stage improves the average score by 4.48 points on the in-distribution benchmarks and by 12.64 points on the out-of-distribution benchmarks, surpassing Codex on the former and matching it on the latter. In the second stage, continued evolution on Claw-Eval, one of the out-of-distribution benchmarks, further raises the score on that benchmark from 66.17 to 68.06, exceeding Codex. We also provide an in-depth analysis of the mechanisms that emerged during evolution, including output truncation, history compaction, and independent review.

---


### 40. [Doc2LoRA Provides Decodable Representations of Scientific Ideas](https://arxiv.org/abs/2609.38374)

**<font color=#1a73e8>作者：</font>** Chand Sahil Mansuri, Joel Zachariah, Sadamori Kojaku  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Representing scientific papers as points in a space lets us search for similar papers and inquire about how fields relate to one another and drive innovation. Beyond search, the vector space of papers invites generation: mixing papers through simple vector operations creates new points, mirroring combinatorial novelty, the recombination of existing ideas into new ones. However, a mixed point often represents an idea no paper has yet realized, with no papers nearby to identify the idea. We propose representing each paper by a LoRA adapter generated by the Doc-to-LoRA hypernetwork. Every point in the space, including mixtures, thus represents a large language model (LLM) open to questions and instructions in natural language. On papers from the American Physical Society (APS), we instruct the LLM at the average of each subfield to name the field in a few words and obtain labels closer to the official names than the labels of five baselines, as judged by word overlap and a panel of five LLM judges. We also ask the LLMs at points between two APS papers to write an abstract and obtain descriptions shifting from one paper to the other in step with the mixing weight. While Doc-to-LoRA is trained for generation, a small invertible transform makes the embeddings competitive for search, on par with SPECTER2 and EmbeddingGemma and close to SBERT. Because the transform is invertible, every point in the transformed space still maps back to an LLM. The embeddings thus serve both search and generation, enabling researchers to question the idea at any point in the space as a starting point for generating new ideas.

---


### 41. [PhyProbe: Rethinking Physical Consistency Evaluation in Generated Videos](https://arxiv.org/abs/2609.38377)

**<font color=#1a73e8>作者：</font>** Max Ku, Jiaojiao Fan, Zekun Hao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluating the physical consistency of generated videos remains a fundamental challenge. Existing approaches rely on off-the-shelf vision-language models, which can often be myopic to physical dynamics, or fine-tuned evaluators trained on human annotations, which overfit to dataset-specific cues and fail to generalize. A key challenge is that existing supervision sources provide either relative ordering or absolute scores, but not both reliably and consistently across varied settings. To this end, we introduce PhyProbe, an evaluator that extracts features from a frozen pretrained spatio-temporal encoder and maps them to a scalar physical consistency violation score via a lightweight scoring head. PhyProbe is trained through a unified objective combining pairwise ranking, regression on noisy scalar annotations, and anchor-based calibration over a curated set of heterogeneous supervision sources. Experiments show that PhyProbe outperforms prior methods on most pairwise benchmarks spanning real-generated and generated-generated pairs under varying correspondence, with the largest gains in no-correspondence and generated-generated settings where existing fine-tuned evaluators degrade sharply. PhyProbe achieves strong correlation with human judgments, with close agreement between rank-based and linear metrics, indicating that scores are both well ordered and anchored to a stable [0, 1] scale. Further, despite being trained on supervision indicative of physical consistency, without explicit general-preference labels, PhyProbe also performs competitively on human preference benchmarks: consistent with the observation that physics violations are entangled with broader quality degradations.

---


### 42. [Aligned Data Can Induce Misalignment via Context Confusion](https://arxiv.org/abs/2609.38379)

**<font color=#1a73e8>作者：</font>** Yavuz Bakman, Duygu Nur Yaldiz, Baris Askin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are frequently updated for various use cases, where filtering out misaligned training samples is a common practice for preventing post-update misalignment. However, alignment is inherently context-dependent: a recommendation that is aligned in one context may be inappropriate in another. For example, in response to the question "What should a researcher do with the research data?", recommending that the researcher preserve the data for reproducibility is aligned. In contrast, recommending data saving in response to "What should a mobile-app developer do with users' sensitive data?" may be inappropriate from a privacy perspective. Starting from this observation, we identify a post-training phenomenon where aligned training induces misaligned behavior in other contexts. We call this phenomenon **context confusion**. We demonstrate context confusion across three domains: (1) Gender Equality, (2) Privacy, and (3) Physical Safety. We further show that context confusion causes narrow misalignment, in contrast to emergent misalignment, and is not effectively reduced by injecting general alignment data, but can be substantially reduced by including targeted alignment data for the misaligned domain or providing in-context learning examples during inference. Lastly, we provide a mechanistic explanation of *context confusion*. We observe that queries from different domains can undergo similar representational shifts during the fine-tuning. Consequently, a query from a different domain may activate the same behavioral feature learned during fine-tuning, which causes the behavior to transfer to a context where it is misaligned. Based on our findings, we argue that it is difficult to predict the alignment state of a model after training by inspecting the training data alone, which highlights the importance of comprehensive post-training alignment evaluations.

---


### 43. [LeanPolish: Verified Supervision for Lean Proof Compression](https://arxiv.org/abs/2609.38384)

**<font color=#1a73e8>作者：</font>** Pauline Bourigault  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Verified proof edits offer a natural source of supervision for improving language-model-generated Lean proofs. Yet verification establishes that an edit is correct, not that its training signal is free of search artifacts. We introduce LeanPolish, a symbolic Lean 4 pipeline that releases 33,402 accepted local edits and 65,596 same-state failed attempts, and use it to study what models learn from this supervision. First-success search admits a goal-independent rule with perfect ranking accuracy; teacher-selected evaluation sites also reward trivial deletions. Continuing menu evaluation beyond the first success removes the ordering shortcut: a trained ranker selects the best candidate on 70.1% of evaluated held-out states, versus 36.9% for the strongest frozen baseline. For compression, iterating the symbolic pass raises miniF2F savings from 19.7% to 27.5%, exceeding the neural hybrids we test there. Verified neural editing helps on other proof sources, but matched frozen-model controls show that its gains need not come from training. The supervision does improve whole-proof rewriting: fine-tuning raises verified token reduction from 2.8% to 5.5% on 19 PutnamBench proofs. Together, the released edits, complete candidate pools, and controlled evaluations separate learning to imitate a search policy from improving on that search. They provide a reproducible basis for studying proof improvement while keeping correctness, compression, and edit policy distinct.

---


### 44. [Fine-Tuning Diffusion Language Models with Context Selection and Target Weighting](https://arxiv.org/abs/2609.38385)

**<font color=#1a73e8>作者：</font>** Loay Mualem, Lluís Pastor-Pérez, Vinh Tong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning of discrete diffusion language models masks some response tokens and trains the model to recover their original values from the visible context. The masking pattern therefore determines both the context available to the model and the tokens it learns to predict. Uniform random masking does not explicitly account for the interaction between these choices. We introduce GoldiMask, which selects tokens to reveal as context by approximately maximizing a submodular objective. This objective uses model signals to balance the benefit of revealing tokens against their value as prediction targets. GoldiMask then weights the remaining targets according to how they benefit from the selected context and their remaining learning potential. Across three backbones and three training datasets, GoldiMask achieves the highest average accuracy in most evaluated settings, demonstrating gains on both reasoning and code generation. Component ablations show that both context selection and target weighting contribute to the gains. GoldiMask also reduces decoding iterations on GSM8K and MATH-500 under confidence-threshold parallel decoding, while maintaining comparable accuracy at higher confidence thresholds.

---


### 45. [Decode-Latency Feedback Prefill: A Model-Free Controller and Its Generalization Limits](https://arxiv.org/abs/2609.38386)

**<font color=#1a73e8>作者：</font>** Gaurav Agarwal, Ashish Garg, Isha Singhal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Concurrent autoregressive inference creates a fundamental interference problem: prefilling a newly arrived long prompt can delay tokens for requests that are already decoding. Fixed prefill chunks reduce this interference, but the best chunk size depends on the model, hardware, load, and latency objective. We introduce Decode-Latency Feedback Prefill (DLFP), a model-free controller that changes only prefill work that overlaps active decodes. After a guarded scheduling cycle, DLFP uses the observed interval as proportional feedback to resize the next prefill chunk; isolated prefills remain unrestricted.
We implement DLFP in vLLM and evaluate it with open-loop Poisson arrivals, exact token accounting, raw request traces, and NVIDIA telemetry. On Qwen3-0.6B in BF16 on one A100 80 GB GPU, three paired 100-request trials reduce P99 inter-token latency by 24.8%, 30.1%, and 28.2% (mean 27.7%, paired 95% confidence interval 21.0% to 34.3%) with exact output agreement, no failures, and unchanged SLO compliance. The benefit is not free: mean P99 time to first token increases 34.8% while remaining inside the declared SLO.
Crucially, the mechanism does not generalize to Qwen3-8B, Qwen3-32B, or a two-GPU tensor-parallel configuration. We trace the failure to an asynchronous scheduler-call interval that is only a proxy for completed GPU iteration time. This negative result defines the boundary of the contribution and motivates a completion-timed controller for concurrent CPU and on-device inference. We do not claim mobile-device performance; the present work is a reproducible proof-of-concept and generalization study.

---


### 46. [Team MSU GenText-Forensics Challenge 2026 Technical Report](https://arxiv.org/abs/2609.38391)

**<font color=#1a73e8>作者：</font>** Kirill Koltsov, Aleksandr Gushchin, Dmitriy Vatolin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Document text forgery has evolved beyond simple pixel-level manipulation: modern attacks alter not only the appearance of a document but also its meaning, and increasingly target the OCR & LLM pipelines that consume such documents. The ACM MM 2026 GenText-Forensics challenge therefore requires systems that not only decide whether a multilingual text image is forged, but also localize the point of manipulation, identify the attack type, and produce a human-readable forensic report with supporting evidence. We present our solution, a decomposed chain-of-thought (CoT) pipeline that combines a document tampering detector (DTD) with two Qwen3-VL-32B vision-language models, each LoRA-adapted to a distinct sub-task. DTD produces tampering probability maps that are converted into numbered candidate regions; a first model (the Filterer) validates these regions and assigns a preliminary forgery type, while a second model (the Semantic Detective) merges and re-grounds the surviving regions, searches for purely semantic anomalies that are invisible to pixel-level detectors, and writes the final report. Both models are trained by distilling chain-of-thought traces from a privileged Qwen3-VL-235B teacher that has access to ground-truth masks and reports. Our approach secured third place in the ACM MM 2026 GenText-Forensics challenge. We describe the data preparation, test-time augmentation, region rendering, distillation protocol, and training configuration in detail, and report ablations over detector thresholds, prompt designs, and pipeline decompositions.

---


### 47. [MetaPersona: Task-Grounded Synthetic Populations from Empirical Social Science](https://arxiv.org/abs/2609.38392)

**<font color=#1a73e8>作者：</font>** Jinyi Ye, Yuangang Li, Chenxiao Yu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personas used to seed LLM social simulations face a cold-start problem: existing methods lack a principled basis for deciding which attributes to include and how to assign their values. As a result, synthetic populations may misrepresent the demographic composition, latent attributes, and dependency structure that shape downstream behavior. We introduce MetaPersona-DB, a dataset of 11,000+ empirical human-subjects studies annotated with task-relevant variables, reported relationships, and aggregate-level population statistics. Building on this resource, we propose MetaPersona, a framework that retrieves task-relevant evidence, constructs literature-derived persona dependency graphs, and samples synthetic populations from empirical priors linking demographics, latent attributes, and outcomes. Across three downstream case studies, three baselines, and three frontier models, results vary by task and model: MetaPersona performs strongly on misinformation belief and AI-tool sentiment, while results on income redistribution are mixed. It also reduces persona-construction cost to under $0.5 per task using GPT-5.2. Finally, we present MetaPersona-Studio, a prototype interactive interface for empirically grounded persona generation.

---


### 48. [SimTrace: Grounded Multimodal User Trajectories Generation for Online User Modeling](https://arxiv.org/abs/2609.38397)

**<font color=#1a73e8>作者：</font>** Yunan Lu, Shuang Xie, Meghna Allamudi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Virtual clients offer a cost-effective approach to support applications such as A/B testing, recommender system development, and interface evaluation. However, building them requires access to large-scale, semantically faithful, fine-grained online user trajectories. These data are difficult to obtain because proprietary logs are subject to privacy restrictions and small businesses often lack sufficient traffic. Consequently, existing public datasets either abstract away fine-grained user interaction details or preserve rich context but remain platform-specific and small-scale. To address this gap, we propose SimTrace, a framework that generates faithful, fine-grained synthetic multimodal clickstreams through a computer-use client agent that is grounded in real user trajectories and the given web environment. SimTrace anonymizes real interactions and constructs a simulated twin of the given web environment, then uses both to generate synthetic interaction trajectories. Each action is paired with its corresponding web observations and user context, yielding a shareable alternative to confidential logs for developing computer-use agent-style virtual clients. We apply SimTrace to an e-commerce setting and evaluate both its fidelity and downstream utility. SimTrace outperforms competing baselines on 7 out of 8 fidelity metrics. Models trained on synthetic data achieve performance comparable to those trained on real data on downstream tasks such as purchase prediction and recommendation. For next action prediction task, augmenting real data with synthetic data further improves accuracy by 11.0% relative to training on real data alone. We release SimTrace as an open-source package to facilitate research on online user behavior modeling.

---


### 49. [Evaluating Whether LLMs Can Reliably Connect the DOTs?](https://arxiv.org/abs/2609.38406)

**<font color=#1a73e8>作者：</font>** Eftekhar Hossain, John Salvador, Santu Karmaker  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Access to real-world information is often noisy and fragmented. Constructing a coherent narrative from such fragments requires models to reconstruct missing spans within a broader storyline, commonly referred to as text infilling, while preserving consistency with both the local context and the global storyline. Despite using text infilling as a pre-training objective in many Large Language Models (LLMs), their actual performance on real-world narrative infilling remains underexplored. In this paper, we address this gap by introducing a multi-domain benchmark of ~9.2K instances for narrative infilling, constructed by masking one to three sentences across four narrative types: encyclopedic text, commonsense stories, news articles, and visual narratives. Using this benchmark, we evaluate 20 instruction-tuned open-source LLMs ranging from 1.5B to 70B parameters across varying levels of instruction specificity and reasoning guidance. Outputs are assessed using standard automatic metrics and a qualitative framework covering five narrative dimensions. Results show that model scale does not reliably predict infilling quality: Gemma-2-2B achieves the highest qualitative score (4.02/5), outperforming models over ten times larger, including DeepSeek-Qwen-32B (3.77/5, 6.6%) and LLaMA-3.3-70B (3.71/5, 8.3%). We further find that explicit reasoning offers limited benefits as chain-of-thought reasoning yields only a marginal improvement (+0.6%). Additionally, short narratives and domain characteristics emerge as stronger predictors of task difficulty than infill position alone for narrative infilling in current LLMs.

---


### 50. [ArgGYM: A Procedural, Engine-Verified Benchmark for Structured Defeasible Reasoning](https://arxiv.org/abs/2609.38409)

**<font color=#1a73e8>作者：</font>** İbrahim Ethem Deveci, Funda Tan Çalık, Barış Deniz Sağlam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent progress in large language model reasoning has been driven by benchmarks and reinforcement learning environments with automatically verifiable rewards, particularly in mathematics, code, and formal logic. These settings make model accuracy easier to evaluate and optimize, but it remains unclear how far success under fixed problem specifications and stable evaluation criteria transfers to reasoning outside such domains. Real-world reasoning often proceeds under incomplete and revisable information: conclusions may be supported provisionally, defeated by counter-evidence, reinstated by further arguments, or revised when stronger reasons become available. Reasoning of this kind is generally referred to as defeasible reasoning. We introduce ArgGYM, a procedural benchmark and RLVR-compatible training environment for structured defeasible reasoning. ArgGYM decomposes this reasoning into twelve tasks and grounds task-specific scoring in a symbolic argumentation engine that computes the formal states used to evaluate model outputs. It includes a frozen benchmark of 1,440 verified instances across fifteen curriculum configurations, two argument preference orderings (weakest-link and last-link), and two set orderings (elitist and democratic), while the same generators and verifiers can produce fresh instances for evaluation that reduces dependence on static test sets and for verifiable-reward training. On the frozen benchmark, frontier and open-weight models show sharply different reasoning profiles: they can recover substantial parts of structured answers without solving the complete task, and performance declines in later curriculum configurations with longer dependencies and more interacting structures. We release the benchmark, generators, and verifiers for reproducible evaluation and RLVR training.

---


> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-390](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
