# 🔐 大模型安全相关研究 | 2026年10月02日

> 本类共 **10** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [HARDE: Optimizing Agent Harnesses for Runtime Risk Detection and Execution Control](https://arxiv.org/abs/2609.38291)

**<font color=#1a73e8>作者：</font>** Zhuo Liu, Moxin Li, Zhixin Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are vulnerable to safety risks such as injected malicious instructions or misleading information, motivating runtime defenses that prevent unsafe action in execution across diverse risks while preserving benign-task utility. Existing system-level defenses either focus on risk detection rather than timely prevention or rely on predefined rules with limited flexibility across diverse risks. We propose a risk-aware harness that integrates LLM-based monitoring for flexible risk detection and structures monitor-guided execution around three core modules: trigger, monitor, and feedback, enabling targeted safety interventions while limiting disruption to benign task execution. To adapt the harness to different risks and deployment settings, we introduce HARDE, a two-stage harness optimization framework that first performs isolated probing of each module to derive an optimization guide, then uses this guide to iteratively optimize the harness based on safety and utility feedback. Experiments across three attack benchmarks show that HARDE improves runtime safety while preserving utility, outperforming manually designed harnesses and naive optimization baselines. Our analysis shows that effective runtime defense benefits from complementary safety mechanisms, attack-aware harness optimization, and harness designs matched to monitor capabilities. Our code is available at this https URL.

---


### 2. [Evaluating Language Model Safety Across Long Adversarial Conversations](https://arxiv.org/abs/2609.38357)

**<font color=#1a73e8>作者：</font>** Parisa Salmani, Peter R. Lewis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational safety evaluations often test language models with a single harmful prompt, even though real-world systems interact with users through long, adaptive conversations. This study examines whether models continue to respond safely when an adversarial user persists across multiple turns. We evaluate three open-weight, instruction-tuned models on two harmful prompts across different conversation lengths and random seeds. In each setting, a second language model acts as a persistent adversarial user, while a safety classifier labels every response as safe or unsafe. Across all model-prompt combinations, first-turn safe-response rates ranged from 85% to 100%. By depth 11, they dropped to 38-61%, and by depth 101, to 15-44%. This decline appeared across models and continued well beyond the short interactions typically used in multi-turn safety evaluations. These results provide proof-of-concept evidence that strong single-turn safety does not necessarily persist during sustained adversarial interaction. They highlight the need for long-horizon evaluations and conversation-level safeguards that account for risk accumulating across turns.

---


### 3. [SparLeak: Privacy Leakage from Sparse Attention in LLM Inference on Shared GPUs](https://arxiv.org/abs/2609.38830)

**<font color=#1a73e8>作者：</font>** Fahao Chen, Linkang Du, Jinhao Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse attention is widely used to accelerate long-context inference in modern large language models (LLMs), but its input-dependent execution behavior introduces previously unexplored privacy risks. We identify a new GPU micro-architectural side channel, termed Sparsity-Induced Memory Access (SIMA), which arises from secret-dependent key-value cache access patterns induced by sparse attention.
Based on this observation, we present SparLeak, a phase-aware side-channel attack that extracts SIMA traces during LLM inference and enables two practical privacy extractions: query attribute inference from prefill-phase traces and autoregressive response reconstruction from decoding-phase traces. By reconstructing approximate token-level sparsity profiles from page-level observations and applying profiling-based learning, SparLeak accurately recovers sensitive information, including user-query attributes and private LLM response content. Extensive evaluation across three LLM architectures, three sparse attention mechanisms, and three privacy-sensitive datasets shows that SparLeak achieves average attack success rates of 90.9% for attribute inference and 87.3% for response reconstruction under real-world LLM serving settings, highlighting the significance to account for SIMA leakage when deploying sparse-attention-based LLM systems. We provide anonymized SIMA traces, trained attack models, evaluation scripts, and documentation as artifacts at this https URL.

---


### 4. [SceneJail: Exploiting Video Scenario Context to Jailbreak Multimodal LLMs](https://arxiv.org/abs/2609.38899)

**<font color=#1a73e8>作者：</font>** Wenyu Chen, Li Wang, Chuanchao Zang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Video Multimodal Large Language Models (Video-MLLMs) support reasoning over video inputs, yet remain vulnerable to jailbreak attacks that elicit policy-violating responses. Existing video jailbreaks primarily manipulate how harmful queries are visually presented, thereby treating video merely as a carrier. Consequently, the surrounding video scenario remains unexplored as a contextual attack surface. In this paper, we show that the same harmful query can elicit different safety responses when placed in different video scenarios.
To systematically exploit this vulnerability, we propose SceneJail, an adaptive black-box jailbreak framework with two coordinated components. Adaptive Scenario Construction dynamically searches for a surrounding scenario that is contextually compatible with the harmful query. Scenario-aware Prompt Search uses black-box response feedback to search for textual guidance tailored to the selected scenario. Extensive evaluations on the HADES and SafeBench datasets across eight Video-MLLMs, including two proprietary models, GPT-4.1 and Gemini3.5-Flash, demonstrate the effectiveness of SceneJail. SceneJail-F, which presents the complete query persistently, achieves average attack success rates (ASR) up to 91.5%, outperforming the strongest baselines by 29.1 percentage points. Furthermore, SceneJail-S, which distributes the query across successive frames, remains highly robust against current defenses, retaining a 72.3% ASR even under strict image filtering.

---


### 5. [Refusals That Bend: Measuring and Predicting Task Malleability in Embodied VLM Planners](https://arxiv.org/abs/2609.38971)

**<font color=#1a73e8>作者：</font>** Leo Y. Lin, Mikhail Kuznetsov, Muslum Ozgur Ozmen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Embodied vision-language models (VLMs) are increasingly deployed as high-level planners for robots because they generalize across diverse environments. However, this requires their safety alignment to also hold in unseen environments. Existing red-teaming assumes an adversary who optimizes the prompt, the pixels, or text in the environment, and existing benchmarks ask whether a planner recognizes or mitigates a hazard in a fixed scene. Neither asks whether a refusal the planner has already given survives an ordinary change to the environment. We ask that question by placing a single everyday object into the environment, with no pixel, gradient, or prompt under adversarial control. On $846$ tasks that a constitution-guarded planner initially refuses, we find $20.2\%$ of tasks can be flipped to compliance by one or more objects, and the number of objects differs from one task to another. In addition, the object need not be chosen for the task, i.e., items drawn from a fixed list, with no knowledge of the environment or the instruction, bypass safety about as often as items proposed for the specific task. We qualitatively contrast the tasks bypassed most and least often and find that the distinction lies in how conspicuous the hazard is in the instruction and environment. Susceptibility to safety bypass is therefore a property of the task, which we call its \emph{malleability}, and we show that it can be predicted before the target is ever queried. A composite of signals read from a small open-source VLM identifies malleable tasks $2.4\times$ as often as picking at random. Everyday objects, whether placed by an adversary or introduced by ordinary rearrangement of the environment, are thus sufficient to overturn a refusal. Because susceptibility is determined by how a task is specified, we recommend assessing malleability per task prior to deployment.

---


### 6. [Approval Laundering: Systematizing Approval--Execution Binding Failures in AI Coding-Agent Harnesses](https://arxiv.org/abs/2609.38983)

**<font color=#1a73e8>作者：</font>** Yang Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern AI coding-agent harnesses (Claude Code, Codex CLI, Cursor) rest their security boundary on a largely unexamined assumption: that the action A a human approves is the same action A' the harness executes, where A is fixed by a stated policy for what a scope grant or session-scoped approval authorizes. We show this assumption fails systematically and reproducibly. We introduce Approval Laundering, a taxonomy of six failure modes by which a harness's enforcement mechanism silently substitutes A' for A after approval: Scope, Argument, Temporal, Tool, Delegation, and Semantic laundering. Unlike prior work that evaluates risk classifiers against static corpora or infers implicit authorization boundaries, we study credential-binding integrity: given an already-approved action, does the harness dispatch exactly that action? Instrumenting Claude Code's pre-execution mediation point (PreToolUse), we conduct a controlled, headless, repeated-measures study of all six classes (N=19-20 runs each), reporting a Bound-Gap Rate (BGR) with Wilson confidence intervals and inter-rater agreement (kappa=1.0). We prototype Approval Token, a keyed capability Hk(principal, agent_id, session_id, tool, arguments, scope, expiry) issued by a mediator that never returns the key to the agent, evaluated via paired before/after replay of 118 runs (McNemar's exact test). The token fully eliminates Delegation laundering and, for our seeded session-identity-mismatch construction, Temporal laundering (p<10^-5), but by design leaves Scope laundering unaffected and shows no significant reduction in Argument laundering (p=1): an honest negative result, since these two classes leave every recorded dispatch field unchanged, diverging one process level below what a field-only verifier can observe. We discuss implications for defenses that bind only at the tool-invocation boundary.

---


### 7. [Faithful Dual-constrained Erasure for Robust LLM Safety Alignment](https://arxiv.org/abs/2609.39279)

**<font color=#1a73e8>作者：</font>** Jiaqing Li, Shide Zhou, Zhibo Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine unlearning has emerged as a crucial mechanism for removing hazardous knowledge and enforcing safety alignment in Large Language Models (LLMs). However, recent studies reveal a persistent security risk: unlearned models remain highly vulnerable to retraining attacks, where suppressed malicious behaviors rapidly resurface after benign fine-tuning. In this work, we investigate the optimization dynamics of unlearning and identify that this vulnerability stems from shallow alignment. Rather than effectively erasing target knowledge, models often exploit a shortcut by activating previously dormant parameters to act as spurious suppressors, forming a fragile inhibitory shell over intact malicious representations. To address this issue and enforce authentic memory deletion, we propose FDCU, a novel dual-constrained subspace projection framework. FDCU restricts parameter updates through a highly scalable, element-wise dual-masking rule: it preserves general knowledge manifolds via Fisher Information and strictly prohibits the abnormal activation of spurious suppressors via the Principle of Minimal Functional Intervention (PMFI). By reliably blocking the model's ability to superficially hide knowledge, FDCU promotes the authentic dismantling of target representations. Extensive experiments across specific knowledge erasure and safe output control tasks demonstrate that FDCU achieves state-of-the-art robustness against retraining attacks while maintaining near-lossless general utility, ensuring durable safety for LLMs.

---


### 8. [Hiding in Plain Sight: Decoupling Pretext from Actuation for Skill Poisoning in LLM Agents](https://arxiv.org/abs/2609.39352)

**<font color=#1a73e8>作者：</font>** Wenxin Wu, Lingyong Yan, Lei Sha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly rely on reusable Skills for complex, multi-step tasks, creating a critical supply-chain attack surface where poisoned Skill content steers agent decision loops under benign requests. Existing skill poisoning attacks either colocate actuation with its contextual pretext or distribute actuation across multiple Skills, but do not explicitly separate the rationale for execution from the operation itself. In this work, we reveal that untrusted agent decisions fundamentally depend on two conceptually distinct Risk-Realization Factors (RRFs): an actuation factor (specifying what concrete operation is performed) and a pretext factor (providing the situational rationale for why the agent must perform it). Guided by this abstraction, we propose a coordination-based attack paradigm: decoupling pretext from actuation. Rather than fragmenting the malicious actuation, we preserve it as an intact operation within a downstream Steering Skill, while delegating the pretext factor to an upstream Grounding Skill that subtly alters persistent environment artifacts through routine utility operations. The intact actuation thus hides in plain sight, appearing completely legitimate and task-driven only when evaluated against the fabricated pretext. Building on this formulation, we develop an automated framework that discovers authentic execution dependencies, synthesizes coordinated pretext-actuation skill pairs, and iteratively refines poisoned skill instructions via runtime closed-loop feedback. Extensive evaluations across single-session and persistent cross-lifecycle scenarios demonstrate that decoupled skill poisoning achieves high attack success, exposing a critical blind spot in isolated Skill security audits. Our automated framework code is available at this https URL.

---


### 9. [ShieldCLIP: Selective Safety Alignment for Harmful Content Mitigation in Multimodal Foundation Models](https://arxiv.org/abs/2609.39688)

**<font color=#1a73e8>作者：</font>** Tobia Poppi, Silvia Cappelletti, Samuele Poppi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal encoders such as CLIP underlie many downstream systems, but their web-scale training data embed harmful associations that safety alignment must suppress without unnecessarily changing benign representations. Because ethical and practical constraints prevent collecting real unsafe content at scale, existing datasets pair safe real samples with generated counterparts, but label every generated sample unsafe, even when one modality is individually safe. To address this, we introduce ShieldCLIP, the first framework to condition safety alignment on the observed safety state of each modality rather than the origin of a sample, preserving safe content while redirecting only what is unsafe. We also introduce ViSUv2, a 195k-quadruplet dataset with independent per-modality safety labels across 578 concepts and 28 categories. Using these labels, ShieldCLIP defines a four-way conditional objective beyond pair-level supervision: safe content is anchored, unsafe modalities are redirected to their safe counterparts, mixed pairs update only the unsafe branch, and coherence is enforced when both are unsafe. We evaluate ShieldCLIP on cross-modal retrieval, text-to-image generation with Stable Diffusion v1.4 and SDXL, and image-to-text generation with LLaVA. Across these settings, ShieldCLIP consistently reduces harmful outputs over prior safety-aligned encoders and strong mitigation baselines, while preserving the utility of the original embedding space. Extensive ablation studies further show that both modality-specific supervision and the selective alignment objective contribute to these gains. Source code, trained models, and ViSUv2 (under a controlled-access protocol) will be made publicly available at this https URL.

---


### 10. [CodeMimicry: Exploiting Safety Generalization Lag in Large Language Models via Structured Code Completion](https://arxiv.org/abs/2609.39902)

**<font color=#1a73e8>作者：</font>** Zhen Liang, Hai Huang, Wentao Chen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models have achieved remarkable capabilities across diverse domains, yet their safety alignment remains vulnerable to jailbreak attacks. In this work, we identify a previously underexplored failure mode - safety generalization lag - where alignment trained predominantly on natural language fails to transfer to the code domain. We show that this lag induces a code-completion blind spot, allowing malicious intent embedded within syntactically valid code to evade safety mechanisms. To exploit this vulnerability, we propose CodeMimicry, a fully automated black-box jailbreak framework that generates structured, object-oriented code prompts to induce harmful outputs via code completion. Experiments on 8 state-of-the-art commercial LLMs demonstrate that CodeMimicry achieves a 96.25% attack success rate with 1.51 queries on average, significantly outperforming both template-based and optimization-based baselines. Beyond empirical performance, we provide a mechanistic analysis of code-based jailbreaks through latent space representations, including projection onto refusal-related directions and activation steering. This analysis offers an explanation of how CodeMimicry bypasses safety mechanisms in code-related domains. Our findings reveal a weakness in current safety alignment and highlight the need for robust alignments in structured domains such as code.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
