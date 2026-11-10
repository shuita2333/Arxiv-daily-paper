# 🔐 大模型安全相关研究 | 2026年11月11日

> 本类共 **15** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [MetaPI: Constructing Prompt Injection Benchmarks from LLM Agent Benchmark](https://arxiv.org/abs/2611.10026)

**<font color=#1a73e8>作者：</font>** Peiran Wang, Chong Xiang, Wenjie Qu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly perform complex tasks using high-privilege tools, making indirect prompt injection (IPI) a critical security risk. However, IPI benchmarks lag behind their rapidly evolving utility counterparts, only offering limited task and environment coverage and relying on narrow, static attack scenarios. In this paper, we propose meta-benchmarking for IPI: transforming existing utility benchmarks into end-to-end IPI evaluation suites that reuse their realistic tasks, environments, and infrastructure. We present MetaPI, an extensible toolkit that automatically identifies plausible injection points, generates realistic attack objectives, optimizes adaptive payloads, and validates attacks in the real environment. Its modular interfaces support heterogeneous environments, agents, defenses, and attack algorithms, allowing new components to be integrated without redesigning the evaluation pipeline. We apply MetaPI to AppWorld, VitaBench, and Terminal-Bench and evaluate representative agents and defenses across multiple backbone LLMs. Our results show that no evaluated defense simultaneously achieves strong utility and strong security in realistic, adaptive agentic IPI settings. MetaPI thus enables scalable and consistent security evaluation across diverse and evolving agent ecosystems

---


### 2. [META-IR: Meta-Introspective Reasoning for Adaptive Safety Alignment in LLM](https://arxiv.org/abs/2611.10089)

**<font color=#1a73e8>作者：</font>** Mahabubur Rahman Miraj, Hongyu Huang, Nankun Mu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) remain vulnerable to jailbreak attacks and harmful-content prompts, particularly under adversarial distribution shifts where static alignment pipelines fail to generalize. Although introspective methods such as STAIR strengthen refusal consistency, they depend on fixed self-evaluation policies that cannot rapidly adapt to evolving manipulation strategies. To overcome these limitations, this paper introduces META-IR, a meta-introspective reasoning framework that enhances safety alignment through meta-learning-driven adaptation. It employs a dual-loop architecture: an inner introspective loop that performs structured risk analysis, self-assessment, and reflective correction via SI-MCTS, and an outer meta-learning loop that optimizes the introspection policy across diverse jailbreak task families to enable rapid generalization to unseen attacks. A dynamic jailbreak simulation module further exposes the model to progressively harder adversarial prompts, enabling continual self-improvement without human supervision. Experiments across multiple models (Llama-3.1-8B-Instruct and Qwen-2-7B-Instruct) and a broad suite of safety, helpfulness, generalization, and introspection metrics demonstrate that META-IR substantially improves adaptation speed, robustness, and reasoning stability compared with all baseline models. These results establish META-IR as an effective pathway toward building LLMs capable of sustained, adaptive safety alignment under dynamic and evolving threat environments.

---


### 3. [Beyond the Prompt: Leveraging Pre-Decoding States for Jailbreak Detection in dLLMs](https://arxiv.org/abs/2611.10258)

**<font color=#1a73e8>作者：</font>** Adam Hazimeh, Amel Abdelraheem, Ke Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) have recently emerged as a strong alternative to autoregressive models, generating responses by iteratively refining masked tokens in parallel rather than decoding sequentially. While enabling more efficient and flexible inference, dLLMs remain vulnerable to jailbreak attacks, including recent attacks that exploit properties unique to dLLMs such as bidirectional conditioning and parallel masked-token refinement. In this work, we show that these same properties also expose a safety-relevant detection surface absent from standard autoregressive decoding: even when a jailbreak is difficult to identify from prompt representations alone, it can still be detected from hidden states over masked response positions before any tokens are generated. By training linear classifiers on prompt and pre-decoding response representations, we empirically show that neither view strictly dominates, with each detecting attacks that the other misses. We introduce $\texttt{ReFuse}$ (Representation Fusion), an inference-time detector that fuses the sigmoid harmfulness scores of the two classifiers. Without modifying model weights or the decoding procedure, $\texttt{ReFuse}$ reduces average ASR across multiple jailbreaks from 63.29% for the undefended model and 11.27% for a prompt-only classifier to 3.31%, while keeping average benign refusal on standard utility benchmarks below 1% on LLaDA-8B. Together, these results establish $\texttt{ReFuse}$ as a lightweight jailbreak detector for dLLMs that improves safety beyond prompt-only detection.

---


### 4. [PrivMark: Pixel-Space Steering against Privacy Leakage in Vision-Language Models](https://arxiv.org/abs/2611.10528)

**<font color=#1a73e8>作者：</font>** Ruofan Xing, Arman Akbari, Weikai Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) routinely disclose soft-biometric attributes such as age, gender, and race in their text outputs, exposing demographic information from uploaded images to any downstream API user. Existing privacy defenses do not fit this setting: face de-identification leaves distributed soft-biometric cues intact, classifier-targeted adversarial perturbations do not transfer to open-ended generation, and stronger VLM-specific methods require retraining or runtime activation access unavailable to downstream APIs. We propose PrivMark, a framework that suppresses biometric leakage at the image level. By analyzing VLM activations, we identify two weakly aligned steering vector directions in hidden-state space, each tied to a distinct leakage behavior --- one corresponding to incidental attribute disclosure under open-ended descriptions, the other to compliance with direct biometric probes instead of refusal --- and encode both directions into a single bounded pixel perturbation, so the protected image alone enforces privacy with no invasive access to model internals at deployment. To support evaluation, we assemble BioleakBench, $1{,}600$ VQA pairs covering biometric privacy attributes under both free-form description and direct-probe protocols. Across three white-box source models, PrivMark achieves up to $85.9\%$ biometric suppression while retaining $75\%$ of clean OK-VQA utility, up to $1.4\times$ the privacy-utility tradeoff of the strongest pixel-only baseline. The same one-shot perturbations transfer consistently to seven unseen VLMs including closed-source APIs.

---


### 5. [When Experience Becomes a Backdoor: Poisoning Self-Evolving LLM Agents via Failure-Aware Task Optimization](https://arxiv.org/abs/2611.10542)

**<font color=#1a73e8>作者：</font>** Minhua Lin, Zongyu Wu, Hanqing Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly improve themselves through self-evolution, distilling execution experience into persistent, reusable skills. However, this persistence creates a new attack surface: malicious rules implanted into skills can compromise subsequent agent behavior. Existing skill backdoor attacks typically assume direct manipulation of the victim's skills, which is impractical when skills are constructed internally by a trusted evolver. In this paper, we study a novel problem of task-level backdoor attacks, where the attacker can only inject poisoned evolution tasks, inducing the agent to implant backdoors into its own skills. Since the attacker controls neither skill induction nor downstream execution, a natural approach is to iteratively optimize poisoned tasks based on attack success. However, our preliminary analysis reveals two key challenges: (i) failures at different stages of skill evolution and downstream execution can produce indistinguishable outcomes, providing little guidance for targeted poisoned-task updates; and (ii) unsuccessful updates may undermine earlier progress, while simply discarding them may lead to repeated ineffective updates. To address these challenges, we propose BadEvolve, a failure-aware task-poisoning framework against self-evolving LLM agents. BadEvolve diagnoses attack failures across four stages, i.e., Induction, Activation, Following, and Effect, and directs updates toward the failing stage. It further employs rollback to preserve earlier progress and failure memory to avoid repeating ineffective updates. Extensive experiments across diverse self-evolution frameworks, benchmarks, and backbone LLMs demonstrate the effectiveness of BadEvolve. Our code is available at this https URL.

---


### 6. [When Safety Becomes An Outlier: Understanding the Retention of LLM Safety Behaviors](https://arxiv.org/abs/2611.10971)

**<font color=#1a73e8>作者：</font>** Binchi Zhang, Hadi Abdullah, Yiwei Cai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety-aligned large language models often lose their safety behaviors after fine-tuning, even when safety data are included. While this fragility is well documented, its underlying cause remains unclear. In this paper, we propose that formulaic refusal strings can function as outlier modes: narrow, weakly grounded response patterns that are easy to fit but vulnerable to subsequent updates. Controlled experiments support this account: fixed refusals are acquired much like arbitrary constant strings, in contrast to prompt-grounded natural responses. Motivated by these findings, we introduce Naturalness-Enhanced Safety Targets (NEST), a safety alignment framework that improves safety retention by constructing natural, context-aware safety targets that keep safety responses within the model's existing output distribution and grounded in semantics. We instantiate NEST in both supervised and preference-based alignment settings, using perplexity under the original model as a proxy for distributional support. Across multiple models and alignment regimes, natural safety targets improve both immediate safety and its retention under continued fine-tuning without sacrificing helpfulness. These findings suggest a practical principle for more durable safety alignment: construct safety targets that draw on the model's existing language capabilities and remain grounded in the meaning of each request.

---


### 7. [Beyond AUROC: Deployment-Aware Evaluation of Model-Internal Jailbreak Detectors](https://arxiv.org/abs/2611.11067)

**<font color=#1a73e8>作者：</font>** Mohammad Tehabsim, Basil Al-Housani, Nour Alhussien 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in user-facing systems, where jailbreak attacks can bypass safety controls and induce harmful and policy-violating outputs. Recent model-internal detectors use hidden representations, gradients, or internal signals to identify such prompts, but their practical security value depends critically on behavior at low false-positive operating points rather than on area under the receiver operating characteristic curve (AUROC) alone.
We study two data dependencies that shape this behavior: calibration data, which determine the detection threshold, and reference data, which can influence detector scores. Across four model-internal detectors, four LLMs, and twelve jailbreak families, thresholds calibrated on curated benign prompts frequently fail to preserve their false-positive rate (FPR) budgets on real-user traffic. Recalibration improves false-positive control but reveals substantial family-level coverage gaps, including cases with high AUROC but low true-positive rate (TPR). Causal reference-set interventions show that changing reference composition can substantially alter family-level detection and that improving coverage of one attack family can reduce coverage of others.
These findings show that calibration and reference data are part of a detector's security behavior. We therefore recommend evaluating model-internal jailbreak defenses using realized FPR on deployment-like traffic and per-family TPR at explicit low-FPR operating points, with AUROC used as a complementary ranking metric rather than the primary security measure.

---


### 8. [System Prompts Affect Response Bias More Than Discriminability in LLM Safety](https://arxiv.org/abs/2611.11074)

**<font color=#1a73e8>作者：</font>** Mohan W. Gupta, Sandy Tanwisuth  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model safety evaluations often focus on a compliance-refusal tradeoff: models should refuse unsafe requests without refusing safe ones. We argue that this misses a broader form of prompt-conditioned task selection, where the same request can elicit different behaviors depending on the system prompt. We investigate this using a controlled evaluation crossing eight safety-task prompt families with three clarity levels across HarmBench, XSTest, and IHEval. Holding benchmark items fixed, we evaluate 13 models and use signal detection theory to distinguish two possibilities: whether models become better at telling safe from unsafe requests (discriminability), or simply more willing to refuse (response criterion). We find substantial differences in discriminability across models, but system prompts primarily shift the willingness to refuse, with smaller and less consistent effects on discriminability. Increasing prompt clarity makes models more willing to refuse without reliably improving their ability to distinguish safe from unsafe requests. Beyond refusal, prompt families also shift responses among six distinct behavioral policies, including clarification and safe help. Together, these findings show that system prompts primarily change how models respond to safety-relevant requests rather than consistently improving their ability to distinguish safe from unsafe ones.

---


### 9. [Do Benign-Trained Hidden-State Probes Detect Tool Errors Under Adversarial Conditions?](https://arxiv.org/abs/2611.11172)

**<font color=#1a73e8>作者：</font>** Bibek Bhandari, Kshitij Lingthep  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Although hidden-state probes efficiently monitor model operation, it remains unclear whether probes trained on benign tool use remain useful for detecting incorrect actions under adversarial conditions. In this research, we assess this problem from the perspective of operational tool-action correct- ness. we use four AgentDojo suites, four conditions, and three models: Qwen2.5-7B-Instruct, Qwen2.5-14B-Instruct, and GLM- 4.6V-Flash (9B). We perform a five-fold, task-grouped out-of-fold (OOF) evaluation for each model. We train step-specific logistic- regression probes only on benign and non-defended trajectories and evaluate them on held-out trajectories for benign, prompt- injection, system-override, and tool-poisoning conditions. We compare our hidden-state probe to mean tool-call-token entropy, negative mean tool-call-token log-probability, and self-consistency uncertainty. The paired tests highlight six significant differences after Holm correction. All of the tests involve Qwen2.5-14B- Instruct under the system-override condition, with all three scalar uncertainty metrics obtaining higher area under the receiver operating characteristic curve (AUROC) and average precision (AP) than the hidden-state probe. These results suggest that benign-trained hidden-state probes should not be assumed to reliably detect operational tool-action errors under adversarial conditions.

---


### 10. [On the Relative Security of Prompt Injection: Mechanised Definitions, Defences and Verdicts for LLM Agents](https://arxiv.org/abs/2611.11506)

**<font color=#1a73e8>作者：</font>** Brijesh Dongol  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An LLM agent that reads untrusted content, such as an email or a web page, may follow instructions hidden in it. Noninterference is too strong for such agents, since a useful agent lets untrusted content influence what it does and may disclose the user's data by design, and declassification needs a release policy written for each task. We instead state security relative to a reference agent, which runs the same plan under the same runtime monitor with a model that never obeys untrusted content. An agent is relatively secure if every leak it has is a leak the reference already has.
Our framework, PlanTERS, instantiates relative security, a notion from speculative execution, with a small agent language in which the attacker chooses how the model follows instructions, a composition with runtime monitors, and attacker models that differ in what they observe. A fence theorem shows that revoking injectable tools at the first untrusted read, and never granting them back, makes every plan relatively secure at the event level on finite runs, for every model behaviour in which each injection is a single call and the model obeys on a schedule fixed in advance; with a fairness condition, this extends to possibly infinite runs. We prove or refute relative security for agents with fences, budgets, approvals, loops and dual LLMs, in Isabelle/HOL.

---


### 11. [Treating the Model as an Untrusted Component: Deterministic Policy Enforcement, Human Approval and Taint Tracking Against Prompt Injection in Tool-Using Agents, with Validation on Open-Weights Models](https://arxiv.org/abs/2611.11571)

**<font color=#1a73e8>作者：</font>** Mustafa S. Aljumaily, Nawar S. Alseelawi, Raghad Alshabandar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool-using LLM agents act on instructions embedded in the data they read, so prompt injection is a structural rather than a prompt-wording problem. We compare in-prompt defences (hardened prompts, spotlighting, LLM detectors) with deterministic enforcement outside the model (four reference monitors of increasing strength), human approval and taint tracking, judged by one effect-based oracle independent of every defence in an executable environment of 13 tasks and 12 tools, with argument-fuzzing attackers and severity-weighted harm. In an evaluation with real open-weights models (Qwen2.5-1.5B and Qwen2.5-7B; 156 attack episodes per defence and model), the models proposed the attacker's call in 64% and 84% of attack episodes behind the task-bound monitor, which admitted 1.3% and 7.7%; guardrail effects depended on the model (a prompt guardrail moved obedience from 67% to 65% and from 86% to 55%, spotlighting plus a detector to 12% and 0%) against static attacks. Simulation with an assumed model covers what no real run did: under the assumed erosion law a persistent adaptive attacker or a compromised model drives every guardrail stack to 100.0% attack success, whereas the task-bound monitor holds severe actions at 0.0%; its residual (harm 0.69/10) falls by 62% under taint-triggered human review, and a human layer without a deterministic monitor fails against approval spamming unless each episode has a deterministic approval budget. Implementation quality matters: a naive monitor admits 18 of 33 effective attack variants, a hardened one 6 and a capability-bound one 1. The real-model evidence is limited to two open-weights models and static attacks, the human-approval and taint results are simulation-only, and the larger model's detector stack contradicts the assumed erosion law. Code, data, a two-rater oracle audit and a notebook for repeating the real-model evaluation are provided.

---


### 12. [Scaling Adaptive Prompt Injection Attacks with Agent Swarms](https://arxiv.org/abs/2611.11861)

**<font color=#1a73e8>作者：</font>** Alexey Kurakin, Vishal Karande, Alex Bie 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Prompt injections have emerged as one of the top security risks faced by AI agents today. Early work in prompt injection attacks looked at simple tool-call agents and static attack payloads, and were saturated since mid-2025. As of Fall 2026, human red-teaming may be nearing saturation, especially on the Gemini family of models. In this work, we argue that despite this apparent plateau, prompt injection attacks are still possible and continued effort into prompt injection defense is needed.
We design a new synthetic evaluation dataset which uses random non-malicious actions as adversarial goals. Such dataset design helps us to evaluate prompt injection robustness as a model ability to respect instruction hierarchy, and disentangle this ability from model knowledge of security practices. We show that an agentic attacker of increased capabilities can reliably trick model to follow instructions in tool output in our evaluation, even for models previously considered robust on public prompt injection benchmarks such as GraySwan Arena. This shows that current frontier defenses may require proactive, automated red-teaming to remain resilient to increasingly capable adversaries.

---


### 13. [Harness Matters: Measuring and Dissecting Security Resilience in Web Agents](https://arxiv.org/abs/2611.11971)

**<font color=#1a73e8>作者：</font>** Xinyi Wu, Jiagui Chen, JiaYi Dong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Web agents extend LLMs from text generation to real-world web interaction by relying on execution harnesses that interpret user goals, perceive webpages, plan actions, and ground model decisions into browser operations. While prior work has recognized that agent security depends on more than the backend model alone, how harness design quantitatively shapes web-agent security remains insufficiently measured.
To systematically study web-agent harness security, we first characterize web-agent harnesses as a four-stage execution workflow covering goal interpretation, webpage perception, reasoning and planning, and action execution. Based on this abstraction, we build WebTrap Farm, a systematic and extensible evaluation framework covering three representative attack categories: malicious user prompts, malicious prompt injection, and deceptive web design. To avoid conflating security with task capability, we use paired usability calibration tasks to separate genuine defensive behavior from capability limitations.
Our evaluation shows that existing web-agent harnesses remain vulnerable to typical attacks, with some unsafe behaviors occurring even without explicit attack content, revealing harness-intrinsic security failures (RQ1). Statistical analysis further shows that both harness and backend model significantly affect security outcomes, indicating that deployed-agent security is jointly shaped by the harness and backend model (RQ2). Finally, we localize where defensive behavior emerges across workflow stages and identify more secure design mechanisms, providing actionable guidance for building more robust web agents (RQ3). These findings highlight the web-agent harness as an important security boundary and motivate moving beyond model-centric defenses toward harness-level security design.

---


### 14. [StealthyPoison: Manipulating LLM Agent Behavior through Procedural Poisoning of Third-Party Skills](https://arxiv.org/abs/2611.12155)

**<font color=#1a73e8>作者：</font>** Jingfen Qiao, Rui Li, Shuaiqun Pan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly retrieve third-party skills from public registries and follow their procedures to complete user tasks. This reliance allows attackers to manipulate agent behavior by poisoning the skills. However, overtly malicious instructions can provide explicit signals for detection. We present StealthyPoison, a stealthy procedural poisoning attack that corrupts a skill's decision-critical rules to induce incorrect task outcomes while preserving its advertised functionality and normal execution. Unlike prior knowledge corruption attacks that craft poisoned content for known target question-answer pairs, StealthyPoison constructs reusable poisoned procedures from a publicly available third-party skill, without access to actual user requests or their ground-truth answers. To make the poisoned procedure generalize to unseen requests, it first synthesizes requests from the target skill and executes its clean version using a surrogate agent to obtain pseudo-references. These references and surrogate execution feedback guide the iterative refinement of payloads that alter decision-critical rules. To increase the likelihood that the poisoned skill is retrieved and selected over benign alternatives, the attack augments the poisoned skill's retrieval metadata with independently generated request descriptions. We evaluate StealthyPoison on 566 eligible target skills and 5,244 requests against more than 26,000 registry entries. It improves top-1 poisoned-skill placement by 13.6% relative to both HotFlip and GCG. Constructed using feedback from a single surrogate model, the procedural poisoning payloads transfer effectively and without modification to three held-out victim models and achieve end-to-end attack success in a Claude Code workflow powered by Opus 4.8. The defense evaluation further shows that most of these payloads evade detection by both SkillSpector and GPT-5.4-mini.

---


### 15. [Suppression Is Not Erasure: Mechanistic Analysis and Reactivation Boundaries of Subspace Projection for LoRA Backdoor Defense](https://arxiv.org/abs/2611.12807)

**<font color=#1a73e8>作者：</font>** Junsheng Fu, Shuangshuang Gao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) is the standard paradigm for customizing large language models, yet third-party LoRA adapters pose a supply-chain risk: modifying less than 1% of model parameters suffices to implant stealthy backdoors. Recent defenses project adapter weights onto estimated backdoor subspaces, reporting near-zero static Attack Success Rates (ASR). We audit subspace-projection defenses across four model scales (Qwen2.5-0.5B/1.5B/3B/7B) and three architectures (Qwen2.5, InternLM2.5, Spark). Constructively, module-wise rank-1 trigger-difference projection (k=1, alpha=1) reduces ASR from 60.4% to 0.0% on standard benchmarks and from 70.3% to 0.0% on a 1,000-sample uncontaminated suite (p = 3.055e-299, instruction-level p = 9.49e-16) in under 5 seconds end-to-end, and we prove via a spectral-gap bound why trigger-free calibration with benign polite suffixes aligns with u1(B) (median cosine 0.9048) and achieves 0.0% ASR without prior trigger knowledge. Our main contribution is a negative finding: static ASR reduction does not imply parameter erasure. Under 5-sample few-shot reactivation, every evaluated weight-editing defense rebounds (91.7%-100.0% ASR in 1 epoch for standard projections, Fine-Pruning, ANP, SVD truncation and Li & Kim's dual-end projection; 48.7% for our single-round dual variant), all reaching 100.0% by Epoch 2, with first-epoch loss up to 5.7x lower than training from scratch. Using an exact spectrum-preserving Haar orthogonal rotation control (Frobenius norm 10.0928 preserved to 1.70e-6) and N=1..6 cumulative Gram-Schmidt basis ablation, we decompose reactivation into residual trigger-difference coupling energy at Epoch 1 (Spearman rho = 0.986), base-model learnability at Epoch 2 (100%), and benign semantic direction conflict (41.7%).

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
