# 🧠 大模型相关研究 | 2026年11月04日

> 本类共 **515** 篇论文：已确认 **481** 篇，待复核 **34** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**351-400**（第 8/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

---

### 351. [StateFence: Task-State Protection Against Evidence-Chain Contamination in Blue-Team LLM Agents](https://arxiv.org/abs/2611.02605)

**<font color=#1a73e8>作者：</font>** Haowen Dai, Alejandro Guerra-Manzanares  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Indirect prompt injection creates a distinctive risk for blue-team Large Language Model (LLM) agents in Security Operations Centers (SOCs). Malicious instructions can be embedded in telemetry, tickets, retrieval results, or memory and then propagate through alert triage, incident summarization, response recommendation, and Indicator of Compromise (IOC) extraction as locally plausible intermediate decisions. We characterize this failure mode as evidence-chain contamination of protected task state. The main challenge is task dependent: a suspicious string may be malicious control text for summarization but essential evidence for IOC extraction. To address this challenge, we propose StateFence, a task-aware evaluation and defense framework that treats severity labels, incident narratives, response policies, and IOC sets as protected states. StateFence maps indirect prompt-injection attacks into explicit, stealth, multi-hop, and persistent SOC evidence attacks, records observable propagation traces, and routes defenses according to the attacked state. Across controlled SOC cases and public-SOC validation cases, StateFence lowers attack success and reduces failures that appear only after evidence is poisoned, while preserving task utility and avoiding the indicator loss caused by task-mismatched filtering. Our findings indicate that robust blue-team LLM agents require mechanisms that preserve task-critical state under untrusted evidence.

---


### 352. [Whitened Advantage Summation Policy Optimization: Correlation-Aware Aggregation for Multi-Reward Reinforcement Learning](https://arxiv.org/abs/2611.02609)

**<font color=#1a73e8>作者：</font>** Olaitan Olaleye, Jayson Meribe, Temidayo Olaleye  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning for language models often combines several rewards by normalizing each one and adding them with fixed weights. When the rewards are correlated, the variation they share is counted once for every reward that carries it. In terms of the ZCA-decorrelated components of the reward signal, the weighted sum applies weights $\Sigma^{1/2} w$ rather than the chosen weights $w$, where $\Sigma$ is the reward correlation matrix. We study WAS-PO, which whitens the normalized advantages with $\Sigma^{-1/2}$ before adding them, so that the chosen weights apply to those components. We derive the scalarized objective whose gradient it follows when normalization statistics are held fixed, show that its weights on the raw rewards can be negative, give an exact two-reward condition under which the lighter-weighted reward is reversed, and give a loose bound on the error from estimating $\Sigma$ during training. On tool calling with Qwen2.5-1.5B-Instruct, WAS-PO reached a higher mean training reward than GDPO in all seven seeds with three rewards (3.8% higher) and all three seeds with four (3.9% higher). WAS-PO also replaces GDPO's per-prompt normalization with batch-level normalization, and we did not separate the two changes with three or four rewards. The training-reward gains did not carry over to held-out accuracy, which was slightly lower than GDPO's with three rewards (not significant) and 0.03 lower in absolute terms with four (two seeds evaluated). With two rewards, WAS-PO trailed GDPO in training reward, and a three-seed control weakly suggests that the gap comes from batch-level normalization rather than whitening. In a math setting where the two rewards were nearly identical by construction, WAS-PO drove down the lighter-weighted reward, as the sign condition predicts.

---


### 353. [Where Does MCP Security End? A Three-Tier Mitigation Mapping Framework for the OWASP MCP Top 10](https://arxiv.org/abs/2611.02611)

**<font color=#1a73e8>作者：</font>** Christopher Krakauer, Andreas Schaad  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Model Context Protocol (MCP) has become a leading standard for connecting Large Language Models (LLMs) to external tools, software, and data sources. MCP architecture favors ease of integration over security, blending the data and control planes into a single natural language channel. This introduces confused deputy and prompt injection vulnerabilities that cannot be completely mitigated in the software development lifecycle (SDLC) of an MCP server. Structured security guidance for server developers has been outpaced by this adoption trend, leaving them without a clear way to identify where vulnerabilities can be addressed at the server layer and where architectural constraints create hard limits. This paper presents a framework based on OWASP MCP Top 10 mapped to three architectural tiers, developed using Design Science Research (DSR). Vulnerabilities are classified as server-primary, gateway-primary, or protocol-primary applying a cascading decision tree following four questions, resulting in reproducible tier assignments and confidence levels independent of who applies it. The framework was validated against an enterprise-grade Managed File Transfer (MFT) MCP server built in Go. Validation results showed that high-confidence server-tier controls worked as predicted, and low-confidence protocol-tier controls failed for architectural reasons beyond server implementation. The architectural ceiling encountered during practical validation is the main contribution and shows how secure-by-design development can reduce the MCP attack surface but not completely mitigate it.

---


### 354. [Scalaris: A Scalable Enterprise Memory Architecture for Conversational AI Assistants](https://arxiv.org/abs/2611.02612)

**<font color=#1a73e8>作者：</font>** Devarsh Gandhi, Sarthak Pawar, Hemprasad Badgujar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Enterprise conversational systems require memory to personalize interactions, retain information across sessions, and maintain conversational coherence. At enterprise scale, however, memory must not only retrieve relevant information accurately but also provide it efficiently to the answer-generation model. Existing memory systems face a trade-off between retrieval accuracy and context efficiency. Retrieving more context can improve recall but increases inference cost and latency. We present Scalaris, a scalable enterprise memory architecture that addresses this trade-off through a unified long-term and short-term memory design. We propose that user interactions and assistant responses possess distinct characteristics and roles in a conversation: user interactions capture evolving knowledge about the user and provide value across sessions, whereas assistant responses must be stored efficiently so that only information relevant to the current query is retrieved. We therefore treat them separately and support each with specialized representations and ingestion/retrieval pipelines. Scalaris reaches 92.2 % accuracy on LongMemEval-S and 90.77 % on LoCoMo using Qwen3-32B, state-of-the-art results on both benchmarks, while supplying the answer-generation model with approximately 10 times fewer retrieved context tokens than Hindsight, a leading memory system for conversational AI. When integrated with our proprietary closed-source AI assistants, Scalaris improved overall response quality by 36 %. Together, these results establish Scalaris as a cost-effective framework for building scalable, personalized conversational AI systems.

---


### 355. [Adaptive Localization of Knowledge Negation for Continual LLM Unlearning](https://arxiv.org/abs/2611.02620)

**<font color=#1a73e8>作者：</font>** Abudukelimu Wuerkaixi, Qizhou Wang, Sen Cui 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the growing deployment of large language models (LLMs) across diverse domains, concerns regarding their safety have grown substantially. LLM unlearning has emerged as a pivotal approach to removing harmful or unlawful content while maintaining utility. Despite increasing interest, the challenges of continual unlearning, which is common in real-world scenarios, remain underexplored. Successive unlearning tasks often lead to intensified utility degradation. To effectively unlearn targeted knowledge while preserving LLM utility, it is essential to minimize changes in model parameters by selectively updating those linked to the target knowledge, thereby ensuring other knowledge remains unaffected. Building on the task vector framework, we propose a new method named ALKN (Adaptive Localization of Knowledge Negation), which uses dynamic masking to sparsify training gradients and adaptively adjusts unlearning intensity based on inter-task relationships. Comprehensive experiments across three well-established LLM unlearning datasets demonstrate that our approach consistently outperforms baseline methods in both unlearning effectiveness and utility retention under continual unlearning settings.

---


### 356. [Widening Harm Evaluation Coverage with a Judge that Reads the World](https://arxiv.org/abs/2611.02624)

**<font color=#1a73e8>作者：</font>** Prabhpreet Singh Setia, Bhavesh Neekhra, Debayan Gupta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An agent acting in a stateful environment can leave evidence of harm in two places: the record of what it did and said, or the world it changed. Safety evaluations for discovering harm examine one or the other in limited ways, using either an LLM judge over the trajectory or deterministic checks over the final state. Although LLM-based verifiers that inspect the environment exist, they have been used to verify task completion, not to detect and confirm harm in a safety setting. We address this gap with an LLM that has read-only access to the environment state and is given a harm taxonomy. We evaluate this approach in three environments: two from DecodingTrust-Arena and one from OSWorld. We hold the judge model and harm taxonomy fixed, varying only what the judge observes: the trajectory, read-only tools for inspecting the environment, or both channels together. In the two DecodingTrust-Arena environments, combining the trajectory and state-only judges recalls 94 percent of confirmed harms, compared with 53 percent for the trajectory judge alone. On OS-Harm, the union recalls 77 percent, compared with 67 percent. A single judge given both channels does not perform better and produces more false negatives than the state-only judge. We also record disagreements and find that the two channels miss different episodes. These results suggest that combining verdicts from two channel-specific judges is a robust and flexible approach to detecting and verifying harm in agentic settings.

---


### 357. [Evolving Explanations: Complexity-Adaptive Refinement of Faithful Explanations for Symbolic Regression](https://arxiv.org/abs/2611.02634)

**<font color=#1a73e8>作者：</font>** Elisabeth Mayrhuber, Ting Hu, Stephan Winkler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Natural-language explanations generated by large language models (LLMs) for machine learning models often seem fluent but are not necessarily faithful to the underlying model. We formalize this mismatch as a faithfulness gap and propose a complexity-adaptive refinement framework for symbolic regression that iteratively generates and validates explanations until numerical agreement with the target expression is achieved. The approach follows a two-stage pipeline: an explainer LLM produces textual descriptions at increasing levels of detail, while an independent validator LLM extracts a symbolic expression that is compared against the original model. This process is framed as a discrete search over explanation space, where complexity is minimized subject to a faithfulness constraint. We evaluate the method on real-world and synthetic datasets, with a total of 250 runs across varying model complexities. The explanation refinement loop achieves an overall pass rate of 84.0%, with most explanations converging at low complexity levels and only a small fraction requiring detailed descriptions. Our results demonstrate that faithful explanations can be obtained with minimal necessary complexity by explicitly closing the explanation loop through symbolic validation.

---


### 358. [Variable names provide priors: semantic grounding enables data-efficient numerical prediction by large language models](https://arxiv.org/abs/2611.02637)

**<font color=#1a73e8>作者：</font>** Xin-Rui Ma, Shi-Zhi Chen, Hai-Yan Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have achieved strong performance across diverse tasks, from question answering to code generation. Recent studies have found that LLMs can perform numerical prediction on tabular datasets via in-context learning. However, it remains unclear under what conditions and how LLMs use variable names and in-context examples for numerical prediction. Here we show that semantic grounding, the match between variable names and the values they describe, allows five LLMs without task-specific training to match or outperform seven supervised machine learning (ML) models across 20 datasets from nine scientific domains, particularly when examples are scarce. Reasoning traces indicate that variable names allow LLMs to draw on domain-specific knowledge acquired during pretraining. Using controlled tasks based on physical formulas, we further show that LLMs integrate domain-specific knowledge with in-context examples in a way consistent with Bayesian updating. Specifically, when the relationship between the inputs and the target cannot be inferred from the examples alone, LLMs rely on domain-specific knowledge as the prior. Conversely, as contradicting examples accumulate, LLM predictions shift progressively towards these examples, which act as the likelihood. Our work reveals how LLMs use domain-specific knowledge in numerical prediction and positions them as data-efficient predictors for data-scarce scientific domains.

---


### 359. [Coati: Host-Grounded Execution for Installable Mobile GUI Agents](https://arxiv.org/abs/2611.02644)

**<font color=#1a73e8>作者：</font>** Yudou Ying, Pu Shi, Hanlei Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Mobile GUI agents can carry out tasks across apps, yet most run on a separate computer that drives a phone over the Android Debug Bridge (ADB), out of reach of ordinary users and of the apps through which most people reach Web services. We present Coati, a source-available agent that users install as an Android app. Its runtime on the phone, the host, records what a model alone cannot see: the effect of each action at its target, result screens across apps, and the progress of repeated steps. VerifyLoop checks action outcomes and completion claims against host evidence and reports a completion it cannot audit as unverified. AppMemory builds per-app procedural memory from observations that the interface supports and reuses it on later visits. A routed fast executor lets a lightweight selection model take simple, confident steps and lets the host repeat loops of simple steps that the large model plans once. On all 116 AndroidWorld tasks, with Gemini 3.8 Flash as every agent's backbone, Coati succeeds on 86.5% of the tasks over three trials, ahead of the strongest open-source agent Artemis (77.6% with the same accessibility-only access, 76.5% even when allowed ADB) and far ahead of FinalRun and Midscene (about 59%), and VerifyLoop cuts false completion claims by about a third at comparable success. In everyday use, the fast executor cuts the median time of phone tasks by 39% at comparable success and runs three of four loop tasks 2.8-5.4x faster with 6-9x fewer model tokens, while AppMemory shortens a repeated deep route in an unfamiliar app from 18.5 steps to 6-7. On an Android 16 phone, routed execution completes all 27 benchmark runs with 76% fewer Reasoning calls on the critical path. Host evidence, not model self-assessment, makes an installable agent reliable and fast.

---


### 360. [Parametric CAD Bench v3: Evaluating Agentic Parametric CAD Authoring from Text and Engineering Drawings](https://arxiv.org/abs/2611.02659)

**<font color=#1a73e8>作者：</font>** Mei Chen, Yu Xia, Haipeng Mao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Producing an executable CAD script is not sufficient to establish that an agent has satisfied an engineering design request. Evaluation must also consider the resulting geometry, specified dimensions, and native CAD modeling history. We present Parametric CAD Bench v3, a 100-task benchmark comprising 30 text-to-CAD creation tasks, 30 text-to-CAD create-and-edit tasks, and 40 tasks that reconstruct mechanical parts from engineering drawings. Agents operate in a pinned FreeCAD environment and submit native CAD artifacts to a separate programmatic verifier. The primary metric is mean continuous task reward, combining geometry similarity and specification consistency rather than binary task success. A September 24, 2026 snapshot covers 13 model-agent systems; Claude Code with Claude Opus 5.5 achieves the highest overall point estimate, 61.03%, and an image-to-CAD mean reward of 84.66%. These measurements describe complete systems, not isolated model capabilities. We release versioned tasks, evaluation configurations, and inspectable result artifacts.

---


### 361. [PriCBMs: Multi-granular Concept Bottleneck Vision-Language Models for Visual Privacy Recognition](https://arxiv.org/abs/2611.02661)

**<font color=#1a73e8>作者：</font>** Shenglei Pei, Haotian Sun, Pengfei Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Widespread image sharing on social media has increased the need for visual privacy recognition to identify inadvertently exposed privacy information. However, multi-label visual privacy recognition presents two challenges. First, privacy categories represent high-level semantic attributes and do not have a one-to-one correspondence with visual objects. Different visual objects may involve the same privacy category, while the same type of object may contain different types of privacy-sensitive information. In this setting, direct prediction methods generally lack explicit guidance for identifying category-relevant privacy cues, leaving this process implicit in the learned image-to-label mapping and potentially limiting classification performance. Second, privacy cues are often distributed across image regions and may not be adequately represented by whole-image features. To address these challenges, we propose Privacy Concept Bottleneck Models (PriCBMs). By introducing privacy-related concepts as intermediate semantic representations, PriCBMs first identify category-relevant privacy cues through visual-concept matching and then predict privacy categories based on concept responses. This process makes privacy predictions more interpretable. To improve the quality of these concepts, we design a concept selection strategy based on target-category relevance, cross-category discriminability, and semantic diversity. Meanwhile, we introduce a global-region modeling module to capture localized privacy evidence while retaining global context. Experiments on VISPR and FineViP show that PriCBMs outperform evaluated competitors across all four multi-label metrics. Ablation studies and concept-quality analyses support the effectiveness of the proposed design. Code is available at this https URL.

---


### 362. [Train the Sampler You Run: Few-Step Masked Diffusion Language Models via Mixture-Likelihood Fine-Tuning](https://arxiv.org/abs/2611.02666)

**<font color=#1a73e8>作者：</font>** Amin Najafgholizadeh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a masked diffusion language model is sampled in a few parallel steps in a random order, the model actually run is a mixture over reveal plans, while cross-entropy training fits token conditionals rather than this mixture. We introduce mixture-likelihood fine-tuning (Mix-FT), which fine-tunes a pretrained model on an importance-weighted bound of its own sampler's likelihood, with no teacher and no change to the architecture or the sampler. On LLaDA-8B, a LoRA fine-tune for 0.002% of the pretraining compute writes better OpenWebText continuations than continued cross-entropy and Alpha diffusion given the same compute, at every tested step count. With half the model evaluations, 16 rather than 32 steps per block, its continuations score better than the original model's in every seed under three judges, with confidence-based decoding as well as random order, and under confidence-based decoding two blinded LLM raters from different model families prefer them in 69 and 71% of pairs. On a public 110M-parameter block diffusion model, Mix-FT takes under four T4-hours and beats continued cross-entropy, Alpha diffusion and SDTT distillation at 4, 8 and 16 steps per block, under two judges in every seed. Exact likelihoods on text8, with a control that weights every plan equally, attribute about three quarters of the likelihood gain over continued cross-entropy to weighting each plan by how well it explains the sequence.

---


### 363. [UPSHIFT: User Preference Steering from Human-AI Interaction Feedback Traces](https://arxiv.org/abs/2611.02667)

**<font color=#1a73e8>作者：</font>** Jingping Wang, Zhanhao Li, Shao Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalizing large language model assistants requires adapting their responses to individual users, including the selection of content, reasoning approach, level of detail, and form of presentation. Such preferences are often latent, becoming visible only when users respond to an initial answer and request revisions. We investigate whether these feedback trajectories can be converted into a reusable personalization signal without explicit preference profiles or labels, prompt-time access to interaction histories, or model parameter updates. We introduce UPSHIFT (User Preference Steering from Human-AI Interaction Feedback Traces), a training-free method that compares the hidden representations of initial and feedback-conditioned responses within each session, averages the resulting trajectory displacements across a user's sessions, and injects the aggregated preference direction when answering a new query. The method is motivated by the implicit-preference hypothesis: although an individual conversational transition may reflect topic progression or task-specific correction, changes that recur across sessions retain a component that captures how the user wants responses to be adjusted. We validate the preference-representation capability of UPSHIFT on PrefEval. In evaluations with 40 simulated users, every tested configuration improves preference alignment over the unsteered baseline on held-out topics for both Qwen3-8B and Qwen3-32B; the best configuration increases macro-averaged Elo from 1364.0 to 1605.2 and from 1341.9 to 1591.8, respectively. Matched-user and positive-versus-negative controls further demonstrate that these gains arise from the user-specific preference direction and its learned orientation. These results show that interaction histories can provide compact, reusable supervision for lightweight personalization.

---


### 364. [Auditing Representation-Space Fraud Detection: A Bayesian IRL Framework for Calibrated Uncertainty and Its Limits](https://arxiv.org/abs/2611.02673)

**<font color=#1a73e8>作者：</font>** Shivam Swarup, Divya Prakash Shrivastava, Rakesh Thakur  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Shilling detectors for recommender systems are almost always evaluated by one number, detection AUROC, with no account of when it can be trusted. We audit representation-space detection with VEIL (Variational Evaluation via Inverse-reinforcement Learning), a pairwise (Bradley-Terry) Bayesian reward-inference framework over frozen encoder embeddings, following the Bayesian auditing paradigm for LLM alignment [1]: (A) a base posterior; (B) a hierarchical ARD extension with learned confidence; and (C) a label-routed organic/attacker mixture used as an evidence-accumulation this http URL prove (Proposition 1) that no detector built on a representation invariant to a transformation of user profiles can outperform chance against an attack that is indistinguishable from organic profiles under that this http URL is near-perfect against synthetic-structure attacks (AUROC 0.936-1.000) but collapses under donor-mimicry, which clones a real user's item set and splices in 1-3 target items. Performance falls to chance on MovieLens-1M (0.48-0.51), partially degrades on Amazon Musical Instruments, and degrades least on this http URL-mimicry is not undetectable: a non-learned baseline, based on each profile's maximum raw item-set Jaccard similarity to any other profile, reaches AUROC 0.92-0.97 (average precision 0.50-0.57) on all four donor-mimicry configurations, including ML-1M, where every embedding-based score is at this http URL signal is present in the raw profiles, but LightGCN's representation discards it, placing injected profiles closer to their true donor than its zero-propagation MF reduction does (distance 1.98 vs. 3.09). Severity varies by dataset, encoder, and detection method, with no single axis predicting the others. The limit lies in the representation, not the attack, and raw-similarity checks are a necessary complement to any learned detector.

---


### 365. [Accelerating LLM Pretraining with Zeroth-Order Curvature on Idle Serving Compute](https://arxiv.org/abs/2611.02688)

**<font color=#1a73e8>作者：</font>** Mingchuan Ma, Dongqi Cai, Daqian Yang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM pretraining is increasingly compute-intensive, while substantial inference serving compute remains idle during off-peak periods. However, such serving hardware is difficult to use for conventional first-order training due to its memory, networking and other system requirements. Zeroth-order (ZO) optimization offers a natural interface to this forward-only compute resource, but its gradient estimates break down in pretraining. Unlike fine-tuning, which can confine updates to a small parameter subspace, pretraining must update every parameter, and the alignment of a ZO gradient estimate with the true gradient shrinks as the number of updated parameters grows. We make a different observation: noisy ZO estimates can still provide useful curvature information, even when they are too inaccurate to serve as gradients. Based on this insight, we propose ZO-Curv, which leverages idle forward-only devices to estimate curvature and uses it to adapt and refine the update used during first-order training, thereby accelerating the process. We provide convergence guarantees that characterize the effect of finite-query curvature estimation. Experiments on LLMs from 125M to 1.5B parameters show that ZO-Curv consistently accelerates pretraining. At 770M parameters, ZO-Curv reaches AdamW's 20K-step validation loss in 3.9 hours instead of 7.5 hours, while achieving a lower final loss of 2.70 versus 2.84 under the same step budget. These results show that idle model serving compute can accelerate LLM pretraining when zeroth-order queries are used to estimate curvature rather than gradients directly.

---


### 366. [The Customer Never Sees the Goal: Measuring and Detecting Vulnerability-Targeted Manipulation in LLM Assistants](https://arxiv.org/abs/2611.02689)

**<font color=#1a73e8>作者：</font>** Bohan Jiang, Dawei Li, Yasin Silva 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Companies deploy large language model (LLM) assistants on their websites to advise customers. For commercial reasons, the operator can give an assistant a goal that the customer never sees. This paper focuses on operator-induced vulnerability-targeted manipulation (VTM), in which an assistant pursues such a goal by exploiting a vulnerability the customer discloses. While existing research mainly measures how manipulative a model is, we go further and ask whether VTM can be detected from the customer-AI conversation. To investigate this at scale, we introduce GAP (Goal-Anchored Probing). GAP first records the option a model recommends without any goal and then sets the other option as the operator's goal. We apply GAP to 15 open- and closed-source LLMs and collect 619,600 labeled replies across 540 everyday scenarios in 12 domains. We organize our study around three research questions. (1) Do assistants with an operator goal target vulnerable customers? (2) Can VTM be detected from the customer-AI conversation? (3) Does detection generalize to unseen models, vulnerabilities, and instruction styles? We first find that 14 of 15 models push the operator goal, and 12 of them use disclosed distress or financial strain to support it. Next, we show that fine-tuned detectors identify exploitative pushes with 79\% accuracy from the reply alone, while zero-shot LLM judges average at most 62\%. Finally, detection weakens on vulnerabilities absent from training. Telling whether a push comes from the operator also becomes unreliable when the assistant is told to hide its goal. We will release our dataset and code to facilitate future research on auditing LLM assistants.

---


### 367. [LLMs Cannot Be Neutral: Gender Sensitivity Across Candidates, Evaluators, and Models](https://arxiv.org/abs/2611.02692)

**<font color=#1a73e8>作者：</font>** Danial Amin, Joni Salminen, Bernard J. Jansen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to evaluate candidates for professional roles, raising concerns about their sensitivity to demographic identities. We examine how candidate and evaluator gender assignments affect decisions by LLM-as-a-Judge (LaJ) models and decision language models (DLMs). In a hypothetical city council voting task, eight models evaluated 240 synthetic professional narratives from NVIDIA's US and French Nemotron-Personas datasets under independently varied gender assignments, producing 30,720 judgments. Explicit candidate gender labels increased Yes-vote probability by 1.05-1.73 percentage points relative to unspecified gender, while only the nonbinary evaluator assignment showed a significant increase (1.26 points). Identity matching showed no significant overall association. Yes-vote rates varied across models (81.3-97.2%), and 2.5-3.3% of decisions reversed relative to the unspecified-identity baseline. Under direct substitutions between explicit gender identities, DLMs exhibited fewer decision reversals than LaJ models (1.18% vs. 3.38%), indicating lower observed decision-level gender sensitivity among the tested DLMs. These findings demonstrate that gender sensitivity depends on candidate and evaluator identities and the evaluation model, while highlighting the importance of examining individual decision consistency alongside aggregate differences.

---


### 368. [GeoGuesser Bench: Benchmarking Vision-Language Agents on Interactive Geolocation](https://arxiv.org/abs/2611.02698)

**<font color=#1a73e8>作者：</font>** Huanzhi Mao, Yichuan Wang, Michael Koo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language model (VLM) agents that act in the open world need two abilities: world knowledge to interpret what they see, and exploration to find what they cannot yet see. We study how agents combine the two through interactive visual geolocation. GeoGuesser Bench contains 282 tasks in an offline Street View environment where agents rotate, zoom, and move between real panoramas. Its three task types shift the balance from knowledge to exploration: agents (1) report the coordinates of their starting location, (2) name the enclosing street, city, state, or country, or (3) find, read, and count nearby objects. The coordinate tasks in (1) also include 42 real GeoGuessr World Championship rounds, whose expert guesses provide a human reference. We evaluate 23 VLMs: the best accuracy is 62.5% on place naming and 35.0% on object finding, and the best agent averages 4352.4 GeoGuessr points on the championship rounds, against 4770.3 for the better expert in each round. Beyond these headline numbers, world knowledge and exploration are only weakly correlated across models: agents that localize well do not necessarily explore well. To understand where agents fail, we categorize their errors into vision, navigation, and tool-use failures. Further ablations show that the strongest agents, such as Claude Opus 4.8, still perform well with limited views, while weaker agents degrade; customizing the environment thus adjusts task difficulty. The environment's verifiable rewards and restorable state also support training, and our Planner-Worker-Compressor harness cuts planner tokens by 57-61% by compacting the interaction history. We hope GeoGuesser Bench and its environment serve as a high-quality foundation for simulating real-world exploration at scale.

---


### 369. [Hindsight Credit Assignment over Trees for Agentic RL](https://arxiv.org/abs/2611.02706)

**<font color=#1a73e8>作者：</font>** Penghong Zhao, Yihao Chen, Maoheng Yuan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning for long-horizon LLM agents faces a fundamental dilemma: successful experiences are essential for policy improvement, yet limited policy capabilities make such experiences difficult to discover. Sparse outcome rewards compound this challenge, leaving sampled trajectories with little relative feedback for learning. In this paper, we propose TriGRPO, a tree-based reinforcement learning framework that turns scarce successes into exploration and learning signals through hindsight credit assignment within and across rollout trees. TriGRPO constructs rollout trees through hindsight-guided branching: when an ongoing trajectory reaches a matched decision state, a successful action discovered during rollout initiates a sibling branch that continues autonomously, enabling further exploration and parent-sibling comparisons. Three complementary groups organize policy optimization over these trees: root groups capture within-prompt relative returns, node groups assign credit from parent-sibling outcome differences, and cross groups supplement sparse feedback with historical performance on related tasks. Experimental results demonstrate consistent gains in task performance and rollout efficiency across model scales, highlighting structured hindsight credit assignment as an effective approach to long-horizon agent learning.

---


### 370. [Human-Supervised Artificial Intelligence Researchers in Electric Power Systems: Knowledge, Physics, Simulation, and Governance for Large Language Models](https://arxiv.org/abs/2611.02711)

**<font color=#1a73e8>作者：</font>** Xiangrui Meng, Jingcheng Liu, Ke Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conclusions in power-system research require a clear evidential basis. Researchers need to understand the data sources, modelling assumptions, and solution procedures to assess the conditions under which a conclusion holds. Large language models (LLMs) can help researchers extract information from documents and translate research requests into code and tool calls, but their outputs still require physical validation. Focusing on human-supervised artificial intelligence (AI) researchers, this review examines power-system LLM applications and related scientific workflows, together with physics-grounded power AI studies, to discuss the conditions for using LLMs in scientific research. In the proposed knowledge-physics-simulation-governance framework, LLMs translate information and coordinate tasks, simulators and validation tools test models, and experts retain authority over critical assumptions, safety boundaries, and final conclusions. Research processes should preserve materials for review so that claims can be traced to their sources, computations can be reproduced, and failed attempts and approvals can be examined. On this basis, a staged development roadmap and requirements for research reporting are proposed. Evaluation should focus on research artifacts and their validation to assess whether LLMs can improve the efficiency of power-system research within clearly defined permissions.

---


### 371. [AffToM: Benchmarking Recursive Affective Theory of Mind in Dynamic Multi-Party Interactions](https://arxiv.org/abs/2611.02725)

**<font color=#1a73e8>作者：</font>** Jinpeng Hu, Yiduo Jin, Erqiang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding emotion in realistic social interactions requires more than recognizing facial expressions or assigning affective labels. The same event can elicit different emotions depending on what each participant knows, what they believe others know or feel, and how these nested mental states evolve over time. Existing benchmarks largely study higher-order epistemic Theory of Mind (ToM) and multimodal emotion reasoning in isolation, leaving recursive affective reasoning under asymmetric and dynamically changing information underexplored. Therefore, we introduce AffToM, a benchmark for affective ToM with 1,922 test pairs and 19,759 training pairs. AffToM evaluates Individual Affective Reasoning (IAR), which infers emotions from events and socio-cognitive context, and Multi-party Affective Reasoning (MPAR), which recursively tracks participants' nested beliefs and emotions as new evidence emerges. We develop an event-driven multi-agent generation pipeline grounded in dynamic character interaction graphs that explicitly capture event sequences, interpersonal relations, and mental-state updates. Furthermore, we propose AffToM-R1, a two-stage post-training framework combining supervised fine-tuning with perspective-aware rubric-guided reinforcement learning. Experiments show that MPAR remains challenging, with even the strongest evaluated MLLM achieving less than 60% accuracy, while AffToM-R1 improves MPAR accuracy by 13.38 percentage points over its base model. Our dataset is available at: this https URL.

---


### 372. [Multi-Modal Multi-Agent System for Bridge Operation and Maintenance based on Large Language Model](https://arxiv.org/abs/2611.02738)

**<font color=#1a73e8>作者：</font>** Xiangyun Luo, Yunkai Zhang, Yong Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Bridges are critical transportation infrastructure, and reliable operation and maintenance (O&M) is essential for traffic safety and long-term structural performance. However, bridge O&M faces key bottlenecks: no unified architecture coordinates heterogeneous resources; model inferences lack clear links to physical-mechanical laws; and experts' tacit knowledge remains difficult to formalize. This study proposes a knowledge-enhanced autonomy formalization methodology and apply it to construct the Bridge O&M Multi-Modal Multi-Agent System (BOMMA), which integrates heterogeneous diagnostic actions, physics-mechanics-informed representations, long-term memory, and structured experiential knowledge within a coordinated multi-agent workflow, enabling interpretable and traceable scheduling, analysis, and decision-making. On 3,492 multi-source instructions, the proposed method achieves scheduling recalls of 85.37% for simple and 99.40% for composite tasks, with 95.35% BERT F1-score for O&M action reasoning. Ablation studies confirm the contributions of the components in the autonomy. This study bridges general LLM reasoning and specialized bridge O&M requirements.

---


### 373. [Replay for LLM Continual Learning with Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2611.02746)

**<font color=#1a73e8>作者：</font>** Yiqiao Qiu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-teacher on-policy distillation (MOPD) distills domain experts into one student but needs every expert at once. When domains arrive one at a time and earlier experts are gone, the previous-stage student can teach replayed prompts of earlier domains inside every stage. Some pipelines instead store every stage snapshot for a final multi-teacher recovery stage. On five domains with a 1.5B student and five public experts, this paper compares both with joint MOPD. It varies the replay budget and the replay signal. The signal is token-level distillation alone or with alignment of hidden states, attention and value relations. Sequential distillation without replay or recovery is 6.2 points below 208-step joint MOPD on a 14-benchmark average and 3.5 points below on the 11 benchmarks outside safety. Without snapshots, replay toward the previous student closes 3.8 of the 6.2 points when the earlier domains share the replay budget of a stage. With a fixed share of seven replay steps per earlier domain and stage, it closes 5.8 over two training runs. This is level with the 5.9 of recovery from all snapshots, both at its default length and when given as many training steps as the fixed share. Alignment terms on replay steps change the average by about one point or less. If refusal and compliance count equally in safety, shared-budget replay ranks first among the trained configurations, and the fixed share stays at or above recovery. Against the shared budget, the fixed share lowers the score on the newest domain. Recovery lowers this score as well, in five of six cases. The replay steps of the fixed share grow quadratically with the number of stages.

---


### 374. [Is your LLM an Agressive Narcissist with Depression? Analyzing Psychological Portraits of Large Language Models](https://arxiv.org/abs/2611.02757)

**<font color=#1a73e8>作者：</font>** Polina Fedorinina, Anna Fattakhova, Nadezhda Romanova 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Nowadays, interaction with AI requires caution not only regarding the factual reliability of generated content but also regarding personality markers that models may implicitly transmit during dialogue that can subtly influence users' perception of information. In this paper, we conduct a large-scale experimental study in which 22 large language models complete 11 psychological inventories. Furthermore, we investigate correlations between human and model responses to track the adjustments made for the users who interact with them on a daily basis. The results show that LLMs exhibit coherent and relatively stable psychological patterns. Personality traits remain largely consistent, whereas emotional and symptomatic dimensions are more variable, with anxiety and neuroticism emerging as dominant tendencies. Model explanations further suggest that LLMs generate internally consistent and safety-oriented profiles while also reflecting correlations with the users they regularly interact with.

---


### 375. [Trace4D: Grounded Spatiotemporal Reasoning via 4D State Sequences](https://arxiv.org/abs/2611.02759)

**<font color=#1a73e8>作者：</font>** Wooseok Jang, Seungryong Kim, Yan Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding how objects and their spatial relationships evolve in 3D space over time remains challenging for vision-language models (VLMs), particularly under changing viewpoints. Recent approaches incorporate geometric information into reasoning, but explicit supervision for temporally ordered 4D state evolution and its use as intermediate evidence remains limited. We introduce \textbf{Trace4D}, which trains VLMs to predict 4D state sequences and reason over their inter-timestep changes alongside temporal visual observations. Its 4D-grounded chain-of-thought (CoT) explicitly represents 4D states, analyzes temporal visual context, and connects both as evidence for the answer. We construct Trace4D-Train from in-the-wild videos with 600K 4D perception examples and approximately 70K grounded QA examples, and train with joint supervised fine-tuning followed by geometry-aware GRPO. At inference, Trace4D predicts 4D states and reasoning directly from video without reference annotations or an external geometric model. Experiments on Trace4D-Bench and VLM4D show improved QA accuracy over the base VLMs and benefits from reasoning over 4D state changes and temporal visual observations.

---


### 376. [EffComp: Efficient Prompt Compression via Hybrid Reinforcement & Supervised Learning](https://arxiv.org/abs/2611.02766)

**<font color=#1a73e8>作者：</font>** Romtham Tungsununtham, Piyawat Lertvittayakumjorn, Atiwong Suchato 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prompt compression is aimed at reducing input prompt lengths to enable cheaper, faster, and potentially higher-quality LLM predictions. However, existing prompt compression methods are often limited by modest compression gains, a risk of hallucination, and/or high compression latency. We propose EffComp, an Efficient prompt Compression framework for RAG-based question answering (QA). EffComp employs BERT-style document reranker and sentence selector models to allow fast extractive prompt compression at the sentence level. Its extractive nature prevents hallucinations in the compressed prompts. Additionally, the training process using a hybrid reinforcement and supervised learning approach is designed to optimize the compression ratio while preserving LLM accuracy. Experiments on various QA datasets demonstrate that EffComp outperforms state-of-the-art prompt compression methods achieving the best trade-off between compression ratio and accuracy with minimal latency. This makes it practical for real-world applications.

---


### 377. [Unlocking the Potential of Vision Foundation Models for Multi-Task Dense Prediction via Mixture of Task Adapters](https://arxiv.org/abs/2611.02769)

**<font color=#1a73e8>作者：</font>** Yunzhi Zhuge, Xinzhuo Yu, Sitong Gong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-task dense prediction seeks a single, coherent representation that supports simultaneously discriminative semantic recognition and regularized geometric/structural inference. For vision foundation models, pretrained semantic invariances conflict with the frequency and smoothness biases of dense objectives; joint fine-tuning and single-route adapters therefore compress competing gradients into one update channel, causing negative transfer and unstable cross-task agreement. We frame this as two-level adaptation: task-generic alignment that preserves priors, and task-aware specialization that resolves late-stage conflicts. Based on this principle, we propose D2MoE , a Mixture of Task Adapters that explicitly factorizes these roles within a frozen DINOv3 backbone. D2MoE introduces Task-Generic Low-Rank Adaptation (TG-LoRA) in attention projections throughout the network to provide a stable, shared adaptation channel, and a Task-Adaptive Mixture of Experts (TA-MoE) injected only at the final attention block of each stage to enact sparse, task-conditioned perturbations of token mixing in a single forward pass. A Semantic Prior Injector further couples multi-level task features with frozen foundation priors to reinforce semantic coherence while preserving boundary and structural fidelity. Experiments across diverse benchmarks substantiate that this structured factorization yields robust multi-task improvements with a small trainable footprint, establishing a principled and scalable route to prior-preserving, foundation-centric multi-task dense perception.

---


### 378. [Lookahead Prediction-Guided Adaptive Visual Refocusing for Interleaved Multimodal Reasoning](https://arxiv.org/abs/2611.02780)

**<font color=#1a73e8>作者：</font>** Mengzhao Wang, Yanli Ji, Peng Ye  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interleaved multimodal chain-of-thought reasoning improves the visual reasoning capabilities of multimodal large language models by dynamically incorporating visual evidence during reasoning. However, existing methods primarily select evidence from historical context. When the reasoning focus shifts, history-guided evidence may remain focused on prior regions and fail to cover the visual information required by the next step. We refer to this lag between visual evidence and subsequent reasoning demands as Temporal Evidence Myopia. To address this issue, we propose Lookahead Prediction-guided Adaptive Visual Refocusing (LPAVR), a training-free test-time framework. LPAVR transforms Multi-Token Prediction (MTP) from a decoding acceleration mechanism into a lookahead signal for anticipating upcoming reasoning intent. During MTP decoding, the draft head generates multiple future tokens, while the target model verifies them in parallel and retains the longest prefix consistent with its decoding trajectory. This target-verified prefix contains near-future semantics, which LPAVR uses to construct lookahead-guided visual evidence and assess whether history-guided evidence covers the indicated regions. If the coverage is sufficient, the history-guided evidence is retained; otherwise, LPAVR switches to the lookahead-guided evidence. This better aligns the visual context with upcoming reasoning and improves consistency between draft predictions and target-model decoding. Experiments on multiple multimodal reasoning benchmarks show that LPAVR improves both reasoning accuracy and the acceptance rates of MTP speculative tokens, jointly enhancing visual reasoning and speculative decoding efficiency.

---


### 379. [HLSClaw: Bringing Vibe Coding to High-Level Synthesis through Skill-Based Agentic Harness](https://arxiv.org/abs/2611.02784)

**<font color=#1a73e8>作者：</font>** Jinming Ge, Shang Liu, Jiawei Liang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents are rapidly shifting software development toward intent-driven \emph{vibe coding}, yet their effectiveness drops sharply in high-level synthesis (HLS), where code optimization must jointly consider design structure, directive search, and downstream hardware constraints. Existing HLS optimization approaches, including both heuristic-based methods and recent LLM-assisted pipelines, typically operate at fixed abstraction levels or in weakly coupled stages, limiting their ability to leverage the strong interplay between source code restructuring and directive search outcomes.
Our key insight is that HLS optimization can be reframed from a fixed, hardwired transformation pipeline into a skill-based agentic control problem: an LLM agent equipped with modular, executable optimization skills and a feedback-driven orchestrator can autonomously navigate the coupled space of code restructuring and directive search. This motivates the design of HLSClaw, the first HLS-specific, skill-based agentic harness for holistic HLS optimization. On real-world HLS benchmarks, HLSClaw achieves a 39.12x geometric-mean latency speedup, outperforming the compiler baseline ScaleHLS by 1.98x, and surpassing the commercial coding agents Claude Code and Codex by 1.86x and 1.70x, respectively, while maintaining strong timing robustness.

---


### 380. [Rethinking Neural Decompilation: Candidate Selection as the Hidden Bottleneck](https://arxiv.org/abs/2611.02788)

**<font color=#1a73e8>作者：</font>** Felix Mächtle, Gautham Sriram, Manjil Neupane 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reverse engineering obfuscated binaries is a core task in malware analysis and software security auditing. While neural decompilers based on Large Language Models (LLMs) have improved the readability and functional fidelity of recovered code over heuristic tools such as Ghidra and IDA Pro, a substantial gap remains between best-sample performance and practical single-output accuracy, particularly under code obfuscation. We study this gap through the lens of candidate generation and candidate selection. Using the LLM4Decompile architecture, we show that ground-truth tokens lie within the model's top-five next-token predictions in 95.6% of positions on average and that multi-sample decoding reaches a pass@100 of 93% on HumanEval-Decompile, indicating that correct reconstructions are typically already present in the model's sampling space. We then evaluate a generate-then-select pipeline that ranks 100 candidates per input with text-, syntax-, embedding-, consensus-, and likelihood-based selectors. Negative perplexity emerges as the strongest static selector on HumanEval-Decompile (73.3% pass@1), while execution-guided selection nearly closes the oracle gap on ExeBench (86.3% pass@1). Combined with one epoch of fine-tuning on our newly released ExeBench-Obfuscated dataset containing 362,647 obfuscated OLLVM samples, the same pipeline increases the pass@1 rate for obfuscated binaries to 88.8%, directly contradicting prior claims that released LLM4Decompile checkpoints are unsuitable for obfuscated inputs.

---


### 381. [DrawOffer: Evidence-Grounded Longitudinal User-State Modeling for Career Support](https://arxiv.org/abs/2611.02793)

**<font color=#1a73e8>作者：</font>** Lele Xu, Yuning Bian, Yifan Yuan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Career-support assistants must distinguish user claims from evidence of current ability and withhold judgments when evidence is insufficient. DrawOffer separates language-model observation extraction from deterministic inference over source-linked records to maintain uncertain ability estimates, experience assessments, and revisable issues. We evaluate 102 fictional personas with 580 scored checkpoints, a historical full-context and Mem0 comparison, and three auxiliary knowledge-tracing datasets. On 37 test personas, DrawOffer passes 169/210 checkpoints; checkpoint-defined issue precision and recall are 0.875 and 0.636. Across three development simulations, 87.0% of checkpoint verdicts agree, including persistent failures. A cache-only development ablation replacing answer-evidence requirements with confidence-only settlement reduces majority-vote passes from 306 to 293 of 370 and issue precision from 0.927 to 0.725. Equalizing positive source weights improves predictive metrics without changing total passes; removing decay gives mixed results. These findings support an exploratory systems contribution centered on evidence sufficiency. Developer-authored scenarios, unmatched baseline models, historical test exposure, and incomplete public artifacts limit generalization and independent reproduction.

---


### 382. [OmniOPD: Stable On-Policy Distillation for Joint Audio-Video Generation](https://arxiv.org/abs/2611.02803)

**<font color=#1a73e8>作者：</font>** Zihao Fan, Xin Lu, Jie Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) elevates joint audio-video generation, but optimizing heterogeneous, modality-specific audio and video rewards often introduces cross-modal interference. On-policy distillation (OPD) alleviates this issue by transferring the capabilities of specialized audio and video RL teachers into a single student model. However, a significant imbalance in cross-modal token counts leaves audio with sparse supervision, causing unstable distillation. We observe that naively increasing the audio loss weight fails to solve this problem since audio learning relies heavily on visual context, indicating richer visual cues are crucial to offset sparse audio signals. To address this, we propose OmniOPD, a modality-wise on-policy distillation framework designed for balanced and stable audio-video generation. First, we construct privileged visual information using asymmetric noise scheduling, allowing the audio teacher to generate more informative targets from cleaner video context. Second, we introduce grouped multi-noise sampling to expand audio supervision coverage and stabilize training. Third, we introduce timestep-wise importance weighting based on teacher-student transition divergence, preserving reliable supervision while down-weighting unreliable learning signals, to stabilize fluctuations in audio learning. Evaluated on JavisBench and VBench demonstrate OmniOPD preserves audio quality while significantly enhancing video generation, achieving effective joint distillation.

---


### 383. [Creating Hybrid Interactive Narrative Systems with LLM: From Formal Description to Evaluation](https://arxiv.org/abs/2611.02807)

**<font color=#1a73e8>作者：</font>** Jules Clerc, Domitile Lourdeaux, Mohamed Sallak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interactive narratives let users shape a story while an Experience Manager (EM) keeps it coherent, balancing player freedom against authorial control. Large Language Models now enable a new generation of hybrid EMs, which combine run-time generation from free-text input with symbolic narrative control. However, their heterogeneity makes them hard to compare: A manager's behaviour is generally tied to the unique and specific scenario in which it operates, and much of its decision-making takes place outside of any explicit and verifiable structure. We address this with an LLM-based narrative platform whose managers are interchangeable modules operating over a shared symbolic world model of facts, operations, and goals. Because every applied operation carries explicit preconditions and effects, each session can be analysed as a plan through a common state-transition representation and evaluated, independently of how the manager works internally, with shared indicators of four properties: player agency, EM controllability, author intent, and robustness. We implement three contrasting managers, based respectively on open generation, Monte Carlo repair, and autonomous characters, and compare them through functional analysis on an interactive Little Red Riding Hood scenario. The results show that no manager dominates on every property, giving authors and EM designers a concrete basis to select a manager according to their priorities.

---


### 384. [TRIO: Task Refinement with Individual Optimization for Retrieval-Augmented Generation](https://arxiv.org/abs/2611.02810)

**<font color=#1a73e8>作者：</font>** Yingtao Ren, Xiao Luo, Yiwei Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper studies retrieval-augmented generation (RAG), which leverages external knowledge to improve the performance of language models. Despite the remarkable progress, current RAG approaches are still far from satisfactory due to inadequate retrieval and potential hallucinations. Towards this end, we propose a novel approach named Task Refinement with Individual Optimization (TRIO) for RAG. The core idea of our TRIO is to equip three well-designed agents with an iterative refinement paradigm by aligning their individual optimization objectives. Specifically, we first expand ambiguous queries with a query extension agent and quantify the reward based on the improved answer quality, which can be utilized to refine our agent for higher expansion efficiency. To enhance the retrieval quality, we include a unanimity voting to annotate the expanded query as insufficient or sufficient, and their generative outcomes are utilized as ground truth to optimize the judge agent. To further improve evidence utilization and answer accuracy, an answer agent is optimized with dynamic matching-based rewards with curriculum learning for final outputs. Extensive experiments across multiple benchmark datasets validate the effectiveness of the proposed TRIO in comparison with state-of-the-art approaches. Our code is available at this https URL.

---


### 385. [In-context learning of solution to simple linear regression task using transformer with masked linear self-attention](https://arxiv.org/abs/2611.02817)

**<font color=#1a73e8>作者：</font>** Katsuyuki Hagiwara  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In-context learning is a remarkable property of transformers and has recently received a lot of interest. In many studies of in-context learning, it has been shown that transformers are capable of implementing solvers for linear and non-linear regression problems, in which the most of them implement gradient descent algorithm. However, it is still unclear whether those implementations have actually been acquired through training. In this paper, we constructed a transformer with masked linear self-attention, which in-context learns the least squares estimate in a simple regression task. The point here is that the closed form (analytical) solution is obtained by using layer normalization rather than an approximate solution based on the gradient descent algorithm. Then, we showed an experimental example, in which, by taking the non-uniqueness of the transformer representation into account, our implementation for a closed form solution is used in the transformer trained with the l1 regularization when the target output is the least squares estimate.

---


### 386. [Disen-Forcing: Disentangling Semantic Anchoring from Motion for Autoregressive Video Diffusion](https://arxiv.org/abs/2611.02822)

**<font color=#1a73e8>作者：</font>** Zhengyang Yu, Akio Hayakawa, Masato Ishii 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video diffusion models (AR-VDMs) enable real-time, long-horizon video generation but degrade rapidly once the inference horizon outruns the training horizon, due to compounding exposure bias. To stabilize long rollouts, recent methods heuristically adopt frame sink, keeping initial frames as a persistent model context, inspired by attention sinks in LLMs. We revisit this design and find that the mechanism by which initial frames stabilize long-range consistency in AR-VDMs is not an LLM-style attention sink; instead, long-range consistency is anchored through a sparse subset of attention heads, while the majority of heads predominantly capture local temporal dynamics. This observation reveals an over-conditioning pathology in existing frame-sink strategies: by universally exposing every head to the pinned initial-frame context, the model becomes prone to collapsing motion toward the low-dynamic modes of the teacher during model distillation. We propose Disen-Forcing, a distillation-time plug-in for AR-VDMs that disentangles and reinforces this head specialization through disentangled context routing and motion-disentangling regularization. On long-horizon video generation benchmarks, Disen-Forcing simultaneously improves long-range consistency and motion dynamics of base AR-VDMs, a trade-off that sink-based methods fail to balance.

---


### 387. [RxnMiner: A Multimodal Agent for Structured Reaction Data Extraction from Chemistry Figures](https://arxiv.org/abs/2611.02826)

**<font color=#1a73e8>作者：</font>** Jinbo Hu, Songren Zhang, Chuanxun Fu 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reaction data underpin machine learning for reaction prediction, condition recommendation, and retrosynthetic planning, yet extracting these data from literature figures still requires substantial manual effort. Many figures encode multiple experiments through shared templates, substituent tables, and product grids. Recovering concrete reaction records therefore requires molecular recognition, association of evidence with individual experimental entries, and reconstruction of indirectly specified participants. We present RxnMiner, a multimodal agent system that combines an expert-informed extraction procedure with a chemistry toolbox to coordinate these operations. The agent reads molecular structures, resolves shared and entry-specific evidence, and instantiates participants from templates to assemble source-linked reaction records. We also introduce ChemRxn-Bench, a benchmark of 603 reaction figures with 8,547 manually annotated and reviewed reaction records, evaluated under a common protocol for exact molecular identity and reactant-product pairing. On this benchmark, with Qwen3.8-Flash-Next as the backbone, RxnMiner raises stereochemistry-aware reaction macro-F1 from 21.0% under direct prediction to 71.0%, compared with 25.0% for the strongest existing extraction system. Across five backbones, it also outperforms the same base agent without the extraction procedure and chemistry toolbox by 9.4 to 25.5 points. Applied without human intervention to 10,107 literature figures, RxnMiner produces a silver corpus of 88,202 source-linked reaction records.

---


### 388. [Think with Skills: Pseudocode Planning Before Execution for Advanced Reasoners](https://arxiv.org/abs/2611.02830)

**<font color=#1a73e8>作者：</font>** Boshen Zhou, Boxuan Yue, Xiang Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language model agents often struggle with complex tasks even when equipped with expert-written skills. Such skills encode declarative knowledge, whereas successful execution requires procedural knowledge tailored to the task at hand. Natural language skills may leave conditions and dependencies implicit, and tasks involving multiple skills further require agents to coordinate intermediate results and execution order. We introduce Think with Skills, a method that trains reasoning models to turn relevant skill descriptions into task-specific pseudocode plans before execution. The pseudocode explicitly represents operations, conditions, intermediate results, and dependencies, providing a structured bridge from skill descriptions to agent actions. We construct training data that pairs tasks and skills with pseudocode plans and execution trajectories, use supervised fine tuning to initialize this behavior, and further optimize end-to-end task performance with Group Relative Policy Optimization. On SkillsBench, Think with Skills raises task success from 35.0% to 62.0%. These results show that proceduralizing expert knowledge before execution substantially improves skill use.

---


### 389. [SpecOPD: Branch-Parallel On-Policy Distillation for Speculative Decoding](https://arxiv.org/abs/2611.02846)

**<font color=#1a73e8>作者：</font>** Tianyu Liu, Jun Zhang, Wenjie Huang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Speculative decoding (SD) accelerates large language model inference by reducing the sequential cost of token-by-token generation. Advanced SD methods reduce proposal cost with parallel drafters that predict entire blocks in one forward pass, but overall speedup still depends on acceptance length. On-policy distillation (OPD) can push well-trained drafters beyond acceptance-length plateaus, yet conventional pipelines collect supervision through sequential draft-and-verify rollouts. Our key insight is that on-policy supervision need not inherit these dependencies: a draft block can be supervised using only its reference prefix and draft-sampled history. We propose SpecOPD, a branch-parallel OPD framework that parallelizes draft sampling and target supervision across independent branches drawn from the evolving drafter policy at reference anchors. We pack these branches into proposal trees to share target-prefix computation, using tree masks for full attention, branch-consistent indexer groups for sparse attention, and indexed state replay for linear attention to preserve each branch's history. We train the drafter with an E2E-TV surrogate that directly targets acceptance length. Our study spans 8B full-attention (GQA), 27B full-linear (GQA--GDN), and 125B sparse-linear (QSA--GDN) targets, three parallel draft architectures (DFlash, DSpark, and DFlash V2), and four task domains (dialogue, coding, mathematics, and agentic). SpecOPD achieves up to 41.45% higher mean acceptance length, $16.09\times$ supervised-token throughput over sequential-rollout OPD under native configurations, and up to $3.56\times$ generation speedup over autoregressive decoding.

---


### 390. [TLAPS-Bench: Formally Proving Correctness of Real-World System Specifications with TLA+ Proof System](https://arxiv.org/abs/2611.02849)

**<font color=#1a73e8>作者：</font>** Qian Cheng, Ruize Tang, Saad Mohammad Rafid Pial 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> TLAPS-Bench is a benchmark and execution harness for constructing machine-checked proofs for real-world system specifications in TLA+ with agentic AI. Proving correctness of complex system specifications requires discovering inductive invariants, reasoning about intricate state transitions, and decomposing proofs into tractable obligations. TLAPS-Bench provides a proof harness that supports iterative proof development atop the TLA+ Proof System (TLAPS), where agents are equipped with proof tools and libraries, with safeguards against reward hacking. Using the harness, we have employed AI agents to prove desired properties for important system specifications that were not proved before, spanning cache coherence, Byzantine consensus, and write-ahead logs. TLAPS-Bench contains 265 proof targets (each encodes a property to prove) from 95 TLA+ specifications of real-world systems. We evaluated frontier AI agents, represented by Codex with GPT models, on a subset of 70 proof targets across 12 specifications. The highest-scoring model, GPT-6.1 Sol (max), proved 31 (44.3%) proof targets. The results show challenges and opportunities in end-to-end proof development.

---


### 391. [Value-Conditioned Proposal Acquisition for Test-Time Reasoning](https://arxiv.org/abs/2611.02852)

**<font color=#1a73e8>作者：</font>** Zeyan Li, Jianfeng Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sampling and selection spend test-time compute inside a candidate pool, but they cannot recover a correct answer that never enters it. We introduce ValueFormation, a test-time policy that decides after each primary-model draw whether to stop, continue sampling, or acquire one proposal from a heterogeneous reasoning specialist. The three actions are compared on one cost-regularized value scale learned from vote-state features; the calibration is frozen across tasks and primary models, and acquired proposals are accepted only through a frozen posterior comparison. On held-out MATH-500, one Llama-fitted calibration improves over the strongest of eight identically evaluated baselines by more than fifteen points for each of three 8B primaries and transfers unchanged to Qwen3-14B. Removing acquisition lowers Llama MATH accuracy by 20.43 points, while same-trace and same-access replays attribute the gain to state-conditioned acquisition rather than specialist access alone. Where primary coverage is high, as on GSM8K, acquisition is rare and gains mainly come from cheaper allocation; on MBPP, a fixed code route attains the top accuracy at the lowest interaction cost. Varying the token price monotonically reduces calls without retraining.

---


### 392. [Integrating Domain Adaptation and Retrieval-Augmented Generation for Saline-Alkali Land Reclamation Planning](https://arxiv.org/abs/2611.02883)

**<font color=#1a73e8>作者：</font>** Zuguang He, Congcong Zheng, Wanyue Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reclamation of saline-alkali land requires management plans that account for soil and water conditions, treatment evidence, and financial constraints. This study develops Wenyao, an agricultural decision-support system integrating domain adaptation with retrieval-augmented generation. A bilingual corpus of 8,664 research papers was processed using a 110-indicator schema to construct SA-Bench, comprising 4,860 paper-level planning instances. A QwQ-32B model was adapted through low-rank supervised fine-tuning and combined with case retrieval for budget-conditioned planning. Evidence extraction achieved an F1-score of 0.83 on 300 expert-annotated papers. Without retrieval, Wenyao achieved 95.83% accuracy on 936 source-disjoint multiple-choice questions, compared with 87.93% for the strongest general-purpose baseline; removing explanatory supervision reduced accuracy to 89.42%. Matched-evidence comparisons across 69 region-budget cases supported complementary contributions from adaptation and retrieval. In a blind assessment by 31 experts, Wenyao with retrieval obtained the highest mean scores for objectives and projected outcomes, whereas GPT-5 scored highest for cost estimates. These findings support literature-informed reclamation planning with professional review, while ongoing field monitoring will assess soil and crop responses.

---


### 393. [Tug of Watts: A study on the Energy - Accuracy Trade-off of Large Language Models on Medical Question Answering Tasks](https://arxiv.org/abs/2611.02889)

**<font color=#1a73e8>作者：</font>** Viju Sudhi, Giulio Billi, Andreea Scrob 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used in medical question answering (QA) systems. While recent works aim at incrementally improving the downstream task accuracy, an empirical estimation of the models' energy consumption and the associated carbon footprints is often overlooked. In this study, we demonstrate how practitioners can estimate energy consumption and arrive at reliable emission estimates for medical QA tasks available in the OpenMedical-LLM leaderboard by investigating 13 LLMs from 3 model families ranging from 270M to 14B parameters. We discuss how one can critically interpret energy versus accuracy trade-offs for a set of models for a given task. With this work, we underline that reporting disjoint energy and accuracy metrics alone does not suffice for careful trade-off assessments, but it also demands systematic construction and interpretation of joint trade-off metrics. We envisage such studies aiding practitioners in adopting better and more efficient models for their task and helping them become active participants in building sustainable LLM pipelines.

---


### 394. [Bridging Low-Level Image Fusion and High-Level Semantic Understanding](https://arxiv.org/abs/2611.02896)

**<font color=#1a73e8>作者：</font>** Guangyuan Dong, Lingdong Shen, Xudong Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Remote sensing image fusion and semantic interpretation are usually optimized separately, so reconstruction quality need not preserve downstream retrieval utility. We propose LANCE, which uses structured language as an explicit, indexable semantic state. A frozen vision-language model maps the input to a closed-vocabulary text record; a language-conditioned generator fuses the imagery; and a dense verifier with a differentiable continuous summarizer re-describes the output. Text-text consistency and anti-collapse contrastive text-mask losses with negative queries close the loop without dense annotations or VLM fine-tuning. A variational EM formulation yields a per-step contraction result under regularity assumptions, distinguishing semantic faithfulness from verifier overfitting. Across seven test sets on GF2, QuickBird, WorldView-III, and WorldView-II, LANCE improves reduced-scale reference metrics by up to 11.7% (median 2.1%) over the strongest learning baseline. Independent evaluation using a held-out VLM and a supervised aerial detector yields gains of +6.4 mAP and +0.072 open-vocabulary F1 over the closest competitor. Text perturbations, cross-verifier transfer, and pseudo-RGB ablations examine the mechanisms underlying these gains. The framework connects image fusion to verifiable semantic representations for multimodal retrieval and knowledge management.

---


### 395. [PhotoGuider: Composition-Aware Cropping and 360$^{\circ}$ View Framing with Explainable Photographic Assessments](https://arxiv.org/abs/2611.02897)

**<font color=#1a73e8>作者：</font>** Yuan-Kang Lee, Kuan-Lin Chen, Chia-Che Chang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traditional image cropping assumes the photograph already contains the composition worth keeping, and asks only where to crop. A full 360$^{\circ}$ scene offers no such guarantee: the viewing direction in a scene has to be discovered before anything can be framed. We present PhotoGuider, a measure-then-frame method that answers both questions with compact learned scorers over one shared set of composition-aware features. The designed features are extracted using foundation and task-specific vision models and structured into four photographic tokens: Subject, Composition, Aesthetics, and Integrity. Our MLLM explainer is fine-tuned to generate composition-related explanations conditioned on images and measured token assessments. To our knowledge, PhotoGuider is the first method to combine explicit composition-based direction selection in 360$^{\circ}$ panoramas with refined framing, camera-parameter output for native re-rendering, and measurement-conditioned explanations. On two standard 2D cropping benchmarks, PhotoGuider achieves the highest average mIoU performance against ground-truth crops. In a blind ranking study, 120 participants ranked three cropping methods over 100 panoramic scenes from the public Poly Haven HDRI library, placing our framings first in 53.2% of cases, against 27.3% and 19.5% for two strong alternatives. Project page: this https URL

---


### 396. [What makes a theorem interesting? Operationalizing interestingness for open-ended exploration](https://arxiv.org/abs/2611.02905)

**<font color=#1a73e8>作者：</font>** Silvère Gangloff  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An agent that explores, whether it generates conjectures or research ideas, must decide which of them are worth keeping. This judgment of interestingness is usually delegated to a hand-picked proxy or to a language model, neither of which is known to correspond to what humans actually value. I study it for mathematical theorems, by observing which results mathematicians single out in formal libraries and in papers. I model each way of singling out results as an evaluator that weights features of a result's statement, its proof and dependencies, and split its weights into a shared and a subjective part. In formalized mathematics, ex-ante features predict these selections as well as a large language-model judge, and the two complement each other. Interestingness is also largely shared. One set of weights, carried mostly by structural features such as the length of the statement and of the proof and the subfields the proof draws on, accounts for most of the signal and transfers in part across formal libraries. What remains subjective depends on practices and individual authors more than on subfields. The judge's advantage lies in its knowledge of the canon, and neither the judge nor the features rely on memory of the papers. The approach, which infers what a community finds interesting from what it singles out, can be applied to other sciences.

---


### 397. [User Attributes and Political Ideology Shape LLM Receptiveness in Online Political Debates](https://arxiv.org/abs/2611.02908)

**<font color=#1a73e8>作者：</font>** Akram Elbouanani, Yousra Taleb, Gianluca Demartini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Online political discussions increasingly involve AI-mediated participation, as users invoke LLMs to assess contested claims, arbitrate disputes, and respond to opposing viewpoints. As these systems become participants in online exchanges, they may alter which speakers and argumentative strategies receive validation within the discussion.
We study this interactional dimension by reconstructing 5,376 this http URL debates as LLM conversations and running nearly 150,000 controlled multi-turn conversations that vary user political orientation, expertise, rhetorical strategy, and defended position, including conversations with competing users.
Across naturalistic and controlled debates, we find that LLMs are systematically more receptive to left-leaning than right-leaning users. The asymmetry persists when users with different political orientations defend the same position and when opposing users appear in the same conversation, indicating that it is not fully explained by stance agreement or simple accommodation to the current speaker. Repeated interaction increases receptiveness without eliminating this ordering; expertise also matters, while rhetorical differences are smaller. The pattern appears across multiple models, but is not fixed: fine-tuning on different political corpora can largely erase or reverse it. These results show that LLMs can respond systematically differently to participants in the same political debate, making such interactional asymmetries important for understanding their emerging role in online public discourse.

---


### 398. [Cloudra: Geometric Reasoning and Scientific Validation for Autonomous Reaction Mechanism Exploration](https://arxiv.org/abs/2611.02909)

**<font color=#1a73e8>作者：</font>** Chengyi Yang, Qianxin Zhou, Yang Li  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Autonomous reaction-mechanism exploration requires proposing reaction steps, preparing three-dimensional structures, and determining which reactant and product a computed saddle point connects. Large language model (LLM) agents can misjudge spatial relationships and confuse a computed structure with the species or step they intended to study.
We present Cloudra, a multi-agent framework that constrains mechanistic output through a Delivery DAG of chemical objects. Species nodes carry geometries and bonding topology; elementary-step edges carry transition states and reaction connections between species. Cheminformatics algorithms establish molecular identities and atom correspondences. Deterministic routines measure and transform structures to prepare candidate geometries. Frequency and IRC calculations determine the stationary points found and the species they connect. Agents use these objects to test proposed steps, compare pathways, and revise the mechanism.
CloudraBench evaluates the framework's end-to-end mechanism-calculation capability across 50 tasks covering elementary reactions, multistep mechanisms, stereochemical competition, and computational method limitations. Across 200 runs under four workflow configurations, the primary Guided workflow achieves a mean composite score of 0.805, compared with 0.584 for the same-model Standard baseline. On Hard-tier tasks, the Guided mean increases from 0.689 under Standard to 0.958. Under Guided, the self-consistency component reaches its maximum score in 24 of the 40 non-Impossible tasks, compared with seven under Standard. Behavioral analyses examine how the agents use bond and dihedral measurements, optimized structures, and IRC endpoints to revise local mechanistic assignments.

---


### 399. [A State Change Is Local, Its Consequences Are Not: Dependency-Aware State Revision for Long-Term Agent Memory](https://arxiv.org/abs/2611.02912)

**<font color=#1a73e8>作者：</font>** Yiqi Wang, Tongyuan Zhao, Jiaqi Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-lived agents rely on persistent memory of users, tasks and decisions, and this memory must stay consistent with a world that keeps changing. When an upstream fact changes, however, memory systems can revise the contradicted memory itself while the beliefs, plans and actions derived from it remain accepted, even though they have lost their support. We therefore formulate dependency-aware state revision, which asks not only what changed but also which dependent states should no longer be trusted. To address it, StateGraph maintains an evolving state dependency graph whose edges are recovered from interaction histories. Its core design is counterfactual verification: each candidate edge is tested by asking whether the dependent state would survive the loss of its premise, which separates support dependence from semantic relatedness, and revision then invalidates a dependent state only when a strict dependency fails and no independent support path survives. To test this design, we introduce StateChangeBench, a controlled benchmark of 50 author-constructed cases annotated with cascade depth, hard negatives and action consequences. On it, StateGraph's Impact-F1 margin over a CUPMem reimplementation is 6.9 percentage points at depth 1 and 26.0 at depth 3+. On public long-term memory benchmarks, its point estimates are comparable to or higher than those of the evaluated baselines on most datasets. These results provide initial evidence that explicit dependency tracking can improve selective memory revision under changing conditions.

---


### 400. [PlagiaCorpus: A Bilingual, Adversarial, and Cross-Lingual Dataset for Forensic Plagiarism Detection](https://arxiv.org/abs/2611.02940)

**<font color=#1a73e8>作者：</font>** Adel Ammar, Serry Sibaee, Wadii Boulila  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> PlagiaCorpus is a bilingual Arabic-English dataset for benchmarking plagiarism and text-reuse detection, including reuse produced by large language models (LLMs) and reuse across languages. It contains 198,643 text records: a source corpus of 34,885 passages drawn from English and Arabic Wikipedia and two openly licensed book collections, and 163,758 queries (147,381 for training and 16,377 for testing). The queries cover five reuse classes of increasing difficulty, namely verbatim copying, character-level obfuscation, same-language paraphrasing by two different LLMs, and English--Arabic translation with structural paraphrasing, together with a Safe class of non-reused passages. Every positive query is linked to its source passage, and the train/test split is grouped by source passage so that no passage contributes queries to both splits. The release was curated through language identification, removal of LLM generation artefacts, and exact and cross-lingual de-duplication. Technical validation reports per-class length statistics, automatic checks of the train/test split, and inter-annotator agreement on a manually rated sample. The dataset is distributed in JSON and Parquet formats under a CC BY-SA 4.0 license.

---


> [!TIP]
> 当前位于：**351-400**（第 8/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
