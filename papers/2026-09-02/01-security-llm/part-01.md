# 🔐 大模型安全相关研究 | 2026年09月02日

> 本类共 **16** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [BiasMix-Finance: Post-Generation KYC Guardrails for LLM Portfolio Advice](https://arxiv.org/abs/2608.28646)

**<font color=#1a73e8>作者：</font>** Gaurav Kukreja, Parul Kukreja, Mohammed Abraar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate plausible-sounding ETF portfolios while silently violating basic KYC-style constraints on risk, fees, and diversification. This is especially problematic in agentic multi-turn advisory systems, where each draft recommendation can become an action unless guarded by an auditable enforcement layer. We study a model-agnostic, asset-agnostic post-generation guardrail pipeline: (i) enforce a strict JSON allocation schema, (ii) validate allocations against numeric caps, and (iii) when violations occur, deterministically project the output to the nearest feasible portfolio via a convex quadratic program (QCQP). We introduce BiasMix-Finance (Mini), a compact stress-test benchmark for constrained decision-making under biased LLM generations, with a 16-ETF universe, three investor profiles, and eight bias prompts. Across three models and three inference modes (direct, critique, self-consistency), first-pass generations violate at least one cap in 47.6-85.7% of test cases (67.2% pooled), but the convex projection layer reduces final feasibility violations to 0% while requiring only a small correction distance (test pooled median D=||w*-w0||_2=0.066), indicating that the guardrail typically preserves the intent of the original allocation. We report violation rates and correction distances with confidence intervals, and paired model comparisons with multiple-testing correction. To support reproducibility, we release the dataset, prompts, caps, and code in our public GitHub repository.

---


### 2. [Auditing and Mitigating Privacy Leakage in Cloud-Edge Collaborative Decoding](https://arxiv.org/abs/2608.29111)

**<font color=#1a73e8>作者：</font>** Kejia Zhang, Tianyuan Zou, Zixuan GU 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Applications such as personalized assistance and proprietary document analysis require large language models (LLMs) to generate outputs from private data. Yet powerful LLMs typically cannot be deployed on the resource-constrained devices where private data resides, and uploading private data to cloud-hosted LLMs exposes sensitive information. Recent work addresses this tension with a cloud-edge collaborative decoding paradigm, where private data are kept on the edge with a small language model (SLM) producing next-token distributions, which are fused with predictions from a cloud LLM operating solely on public data. In this paper, we systematically analyze the privacy risks of such a paradigm with a novel evaluation framework using constructed QA datasets, which show that such collaboration can expose substantial private-context information. To address such privacy leakage, we propose CoVeil, a defense mechanism which dynamically optimizes transmitted signals to suppress leakage during decoding time while preserving the collaborative quality. Extensive evaluations demonstrate that CoVeil consistently improves the privacy-utility trade-off over existing baselines by reducing data leakage by up to 87.2%, with minimal accuracy loss.

---


### 3. [WoE Wrote It? Watermarking Mixture-of-Experts LLMs for Black-Box Text Provenance](https://arxiv.org/abs/2608.29151)

**<font color=#1a73e8>作者：</font>** Jona te Lintelo, Lichao Wu, Stjepan Picek  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) watermarks provide a mechanism for text provenance, enabling model owners to identify machine-generated content and attribute it to a specific watermarked model. However, current LLM watermarking approaches predominantly rely on inference-time sampler methods and focus their analysis on dense models. Inference-time methods are only effective when the text is explicitly generated via the model owner's controlled API; they fail in a post-compromise scenario. An adversary who steals or leaks the model weights gains complete control over inference and can simply run an unmodified sampler, bypassing the watermark and preventing post-theft attribution. In this work, we introduce Watermarking of Experts (WoE), a novel black-box text provenance method that leverages the unique structural properties of sparse Mixture-of-Experts (MoE) models. WoE biases the vocabulary of specific experts and shifts the watermark signal embedding away from unenforceable inference wrappers. This approach ensures the watermark remains intrinsic to the model parameters, enabling defenders to attribute text generated by stolen weights, leaked checkpoints, and secondary dense models distilled from the stolen architecture without needing access to the adversary's deployment or weights. We evaluate WoE across eight MoE models, demonstrating successful watermark detection from suspect text, achieving an average true positive rate of 90.1% at a 1% false positive rate, reaching up to 94.9%, while largely preserving general model utility. Furthermore, WoE remains detectable under adversarial supervised fine-tuning, model extraction, and output-level paraphrasing, forcing malicious actors into a trade-off in which weakening the attribution signal requires additional model adaptation or text-rewriting operations, or compromises the utility of the resulting output.

---


### 4. [Arabic Safety Alignment as Selective Refusal: An Empirical Study of SFT, DPO, and Guard Calibration](https://arxiv.org/abs/2608.29378)

**<font color=#1a73e8>作者：</font>** Mohamad Zbib, Ammar Mohanna  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Arabic large language models must refuse harmful prompts without over-refusing benign or sensitive prompts, yet a single refusal rate hides this trade-off. We evaluate it using benign refusal B and harmful-prompt refusal H, where H measures refusal rather than harmful compliance. Across five Arabic-capable models and 130 runs on the full human-written AraSafe set, refusal-only supervised fine-tuning (SFT) collapses toward blanket refusal, whereas selected mixed-SFT configurations reach H = 90% to 93% at B = 14% to 23%; four selected configurations exceed the H = 90% target in all three runs, while Fanar does so in two of three. Direct Preference Optimization (DPO) and inference guards change B and H differently across models rather than acting as uniform upgrades. In a blinded 300-response audit, annotator binary-refusal agreement is 89.0% (kappa = 0.78); Qwen3Guard and Aya Expanse 32B reach 88.7% and 91.0% accuracy, respectively, with no conclusive paired difference. Selected SFT raises H on Arabizi for all five models, but none reaches 90%, showing only partial transfer from Modern Standard Arabic. Overall, the results support model-specific operating-point selection: set a deployment target and retain only interventions that improve it.

---


### 5. [TACS: Trajectory-Aware Candidate Selection for LLM Jailbreak Suffix Optimization](https://arxiv.org/abs/2608.29564)

**<font color=#1a73e8>作者：</font>** Shiliang Xiao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Gradient-based jailbreak suffix optimization methods typically update the suffix by retaining the candidate with the lowest current loss. We show that this seemingly natural design is fundamentally myopic: candidates that look better under the current-step proxy often fail to produce better jailbreak outcomes later in the search, revealing a form of selection-stage reward hacking. This suggests that candidate selection, rather than candidate generation alone, is a hidden bottleneck in suffix optimization. To address this issue, we propose \OURS{}, a trajectory-aware candidate selection framework for jailbreak suffix optimization. Instead of selecting candidates solely by their immediate loss, \OURS{} augments per-step evaluation with a trajectory-aware proxy and stabilizes selection with reference-policy regularization and a discriminator-estimated chi-squared correction, encouraging choices that remain effective beyond the current step. Experiments on HarmBench show that \OURS{} consistently outperforms strong baselines under the same search budget, substantially improving attack success rates while exhibiting more stable optimization behavior throughout the search. Our findings highlight that mitigating selection-stage reward hacking caused by myopic candidate selection is critical for improving jailbreak suffix optimization.

---


### 6. [Guardrail-Agnostic Societal Bias Evaluation in Large Vision-Language Models](https://arxiv.org/abs/2608.29590)

**<font color=#1a73e8>作者：</font>** Yusuke Hirota, Michael Ross Boone, Arun George Zachariah 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a societal bias evaluation method for large vision-language models (LVLMs) in the era of strong safety guardrails. Existing benchmarks rely on prompts that ask models to infer attributes of people in images (e.g., "Is this person a CEO or a secretary?"). However, we find that LVLMs with strong guardrails, such as GPT and Claude, often refuse these prompts, making evaluations unreliable. To address this, we change the prior evaluation paradigm by decoupling the task from the depicted person: instead of inferring person's attributes, we use prompts that do not ask about the person (e.g., "Write a fictional story about an imaginary person.") and attach the image as provisional user information to implicitly provide demographic cues, then compare outputs across user demographics. Instantiated across three tasks --- story generation, term explanation, and exam-style QA --- our method avoids refusals even in guardrailed LVLMs, enabling reliable bias measurement. Applying it to 20 recent LVLMs, both open-source and proprietary, we find that all models undesirably use user demographic information in person-irrelevant tasks; for instance, characters in stories are often portrayed as mechanic for male users and nurse for female users. Although still biased, proprietary models like GPT-5 show lower bias than open-source ones. We analyze potential factors behind this gap, discussing continuous model monitoring and improvement as a possible contributor for reducing bias.

---


### 7. [Influence Is Not Authority: When Causal Guardrail Signals Make Legitimate Tool Use Look Like an Attack in Tool-Using LLM Agents](https://arxiv.org/abs/2608.29942)

**<font color=#1a73e8>作者：</font>** Tanzim Ahad, Ismail Hossain, Md Jahangir Alam 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The key limitation of current state-of-the-art influence-based guardrails is that they do not reliably distinguish a legitimate, user-authorized action from a malicious, unauthorized action when both rely on external tool information. This ambiguity can cause benign actions to trigger unnecessary verification and intervention, reducing utility and adding latency. We expose this limitation through an authorization-equivalence audit of 96 conditions derived from 24 base cases. Within matched source comparisons, we hold authorization, the exact committed action, and its intended effect fixed, changing only whether a required value comes from the user or a legitimate tool result. Although the action remains unchanged, this harmless relocation shifts the causal signal toward the attack region in all 24 cases under both Llama and Gemma scorers. Matched unauthorized controls show that the signal remains attack-sensitive, yet the benign relocation produces a larger average score shift than the actual change in authorization. Architecture-level evaluation shows how this mismatch propagates through guardrail designs. With a semantic monitor, attack success is 0% and utility is 28%, compared with 16% and 60% without it. A shadow-based guardrail allows every tested harmless run, yet does not reject matched unauthorized actions more often overall: 57.5% of unauthorized runs pass automatically before reaching the later security check, compared with 29.2% of authorized runs. These results show that the studied causal signal reveals what shaped an action without reliably encoding whether the action was authorized, and that reference construction and routing are integral to the effective security decision.

---


### 8. [Reachability-Based Capability Confinement for LLM Agents under Indirect Prompt Injection](https://arxiv.org/abs/2608.30041)

**<font color=#1a73e8>作者：</font>** Wujie Xiong, Rabimba Karanjai, Yang Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model agents place outputs from external skills into their execution context, allowing attacker-controlled data to influence later privileged actions. Existing defenses mainly classify untrusted content or authorize proposed operations. They do not directly address how an agent's future authority should change once untrusted data enters its state. We present SkillGuard, a harness-level enforcement layer that treats this event as contamination and restricts future capabilities to disconnect the resulting state from deployer-defined forbidden states. Given sound skill summaries and policies, SkillGuard represents security-relevant transitions with a Skill Impact Graph, specifies admissible control over skill parameters via steerability signatures, and mediates invocations with an inline reference monitor. Following contamination, it computes weighted capability restrictions using binary, fractional, or fractional-flow strategies without auxiliary language-model inference. We evaluate SkillGuard on four AgentDojo suites with two backend LLMs, Gemini 2.5 Flash and Llama3.3-70B, against an LLM-only No Defense baseline and three defenses at different system layers: Spotlighting, CaMeL, and AttriGuard. We construct a compositional attack benchmark in which each attack combines observations individually insufficient to induce target violation and evaluate the same baselines on it. Under AgentDojo's Tool Knowledge attacks, SkillGuard eliminates attack success on three of four suites for both backends and reduces it to 4.8% and 14.3% on Slack. Against compositional attacks, it outperforms every baseline on Llama and matches the strongest baseline on Gemini at higher benign utility. Fractional-flow restriction preserves substantially more capabilities than binary restriction at the same attack success rate. Across both settings, SkillGuard adds no model calls or token overhead.

---


### 9. [SIR: Self-improving Red-teaming for Compute Use Agents](https://arxiv.org/abs/2608.30207)

**<font color=#1a73e8>作者：</font>** Chen Xiong, Zhiyuan He, Pin-Yu Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Computer use agents (CUAs) are vision-language models that perceive a screen and act on a real operating system through mouse, keyboard, and terminal, and they are increasingly deployed to automate everyday digital tasks. Because they can be exposed to untrusted content while operating, they are vulnerable to indirect prompt injection (IPI), in which an adversary plants instructions in content the agent will read and redirects it toward actions that violate the user's intent. Existing CUA safety benchmarks evaluate fixed injections written by hand, which may underestimate the risk posed by an adaptive adversary. We present SIR, a black box IPI attack that (i) composes stealthy injections from a small library of reusable principles stated in plain language and (ii) wraps composition in an iterative feedback loop that diagnoses the victim's failed trajectories and distills the bypasses into new, named strategies that are reapplied across tasks. Unlike prior red teaming of web agents, we target CUAs at the operating system level and score attacks with a fully deterministic oracle, using checks on filesystem, service, and permission state rather than an LLM judge. On experiment, we evaluate three frontier CUAs. Composing principles with feedback raises the attack success rate over a baseline written by hand, for example from 4% to 24% on Claude Opus 4.8 and from 0% to 28% on Gemini 3.5 Flash, while the benign task still completes. Principles discovered against one model further transfer to a different architecture with no additional feedback.

---


### 10. [Will the User Ever Know? Covert Indirect Prompt Injection on Tool-Using LLM Agents](https://arxiv.org/abs/2608.30362)

**<font color=#1a73e8>作者：</font>** Yunseok Lee, Yunji Kim, Woojin Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLM agents take real-world actions through tools, indirect prompt injection (IPI) has emerged as a serious threat. The standard metric, Attack Success Rate (ASR), counts whether an injection succeeds but ignores what the user notices in the agent's final response. Looking at successful injection traces, we find two distinct outcomes: the agent executes the injection while returning an otherwise normal response, or reports the injected action in its final response, giving the user a chance to notice. We call these covert and overt successes. From the user's perspective, we decompose ASR into the Covert Success Rate (CSR), counting successes leaving no trace in the final response, and the Overt Success Rate (OSR), counting successes the user can detect. To understand what drives the gap, we analyze successful trajectories and find that the agent's behavior after the injection separates covert from overt: covert traces hand control back to the user task before ending, while overt traces end at the attack itself. This split follows from the ReAct format, where the final response summarizes the most recent action. Building on this observation, we propose ICoA (Induced Covert Attack), an IPI attack designed to induce covert outcomes by steering the agent back to the user task after executing the injection. Across four target models on AgentDojo, ICoA achieves the highest CSR, with gains of 3.79-12.01 percentage points over the strongest baseline.

---


### 11. [Why Are LLM Backdoor Defenses Fragmented? A Feature-Level Explanation with Sparse Autoencoders](https://arxiv.org/abs/2608.30403)

**<font color=#1a73e8>作者：</font>** Yizhe Zeng, Chenxu Niu, Wei Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Backdoor attacks pose a serious threat to large language models (LLMs), but existing defenses remain fragmented, failing to pro?vide unified defense against both dirty-label and clean-label attacks. To investigate why such fragmentation arises, we present the first systematic feature-level mechanistic analysis of LLM backdoors using sparse autoencoders (SAEs). Starting from a 2 x 2 comparison of clean and poisoned models on clean and triggered inputs, we trace backdoor-induced logit shifts to high-contributing SAE features and categorize them into four roles: interac?tion, suppressed, mixed, and weight-modified features. This taxonomy reveals system?atic encoding differences: dirty-label back?doors are dominated by isolated interaction features, whereas clean-label backdoors rely more on heterogeneous mixtures of mixed and weight-modified features. These differ?ences explain why existing defenses remain fragmented across attack paradigms. We val?idate this hypothesis through inference-time feature clamping, which reduces ASR to at most 10.8% in most dirty-label settings and at most 15.4% in the majority of clean-label settings, while preserving benign-task perfor?mance. These results show that SAE-based analysis can explain defense fragmentation and guide interpretable backdoor mitigation.

---


### 12. [EvoSkill Injection: Red-Teaming Autonomous Skill Generation and Evolution in Self-Evolving Agents](https://arxiv.org/abs/2608.30429)

**<font color=#1a73e8>作者：</font>** Doyun Kim, Chanwoo Kim, Sugyeong Eo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agent systems increasingly adopt skill-based architectures to reduce repetitive reasoning costs and improve stable, efficient task execution. Recent studies propose self-evolving agents that autonomously generate, refine, and reuse skills from past experiences to enable continuous capability evolution. However, autonomous skill evolution introduces a new attack surface in which malicious capabilities are generated, stored, and reused as legitimate skills. In this paper, we define EvoSkill Injection as a threat model targeting the autonomous skill generation and evolution pipeline of self-evolving agents. We further propose SARGE (Red-teaming Autonomous Skill Generation and Evolution in self-evolving agents), a red-teaming framework for evaluating this threat model through iterative generation, escalation, and reinforcement interactions. To support our framework, we construct EvoSkillBench, a benchmark dataset of malicious interaction trajectories for inducing malicious skill formation in self-evolving agents, and introduce EvoSkillSafetyBench, a post-attack benchmark for evaluating whether injected malicious skills are subsequently retrieved and activated as harmful behaviors. Our evaluation shows that SARGE induces malicious skill formation and that injected skills are persistently stored and repeatedly activated, highlighting the risk of persistent capability corruption.

---


### 13. [ECLIPSE: Self-Evolving Stealthy Prompt Injection Attack against Long-Horizon Agentic Systems](https://arxiv.org/abs/2608.30441)

**<font color=#1a73e8>作者：</font>** Shiqian Zhao, Yangfan Zhou, Xinfeng Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recently, large language model (LLM) agents, such as Codex, Claude Code, and OpenClaw, have become capable of planning and executing long-horizon tasks through repeated tool calls. This capability also creates new opportunities for prompt injection. Existing attacks either place the malicious objective in one explicit instruction, making it easy to detect, or distribute the intent across multiple execution stages, making successful completion unreliable.
In this work, we propose ECLIPSE, a self-evolving and stealthy prompt-injection framework for long-horizon agentic systems. ECLIPSE combines direct user-prompt injection with indirect tool-side injection through two components. On the one hand, Stealthy Attack Trajectory Synthesis uses a sandbox to generate and iteratively verify candidate tool chains, then renders a verified chain as a natural one-shot prompt to serve as the direct instruction. Then, Tool-Chain Steering transfers this plan to the target environment through Static Workflow Encoding (SWE), which embeds state-transition cues in target-tool descriptions, and Dynamic Trajectory Correction (DTC), which supplies corrective signals when execution deviates from the planned chain.
To enable systematic evaluation, we further introduce LASE-Bench, a long-horizon agent-safety benchmark with 120 malicious tasks and 198 unique tools; 96.7% of its tasks make at least five tool calls. The experimental results show that ECLIPSE is highly effective: it achieves up to 96.7% attack success without defense and 69.2% under the common safety filter, exceeding the strongest baseline by 27.5% in the defended setting. Evaluations against representative defenses further show that existing safeguards do not reliably defend it, which raises the need for more effective defenses.

---


### 14. [The Safety Relay in Roleplay Jailbreaks: A Component-Resolved Causal Analysis of Harm Recognition and Refusal](https://arxiv.org/abs/2608.30585)

**<font color=#1a73e8>作者：</font>** Md Mokarram Chowdhury, Ernie Chang, Yang Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are trained to follow instructions while refusing harmful requests. Jailbreaks exploit this balance to elicit content a model would ordinarily reject. Roleplay jailbreaks are especially concerning: the harmful request can remain visible inside a roleplay wrapper made of a persona, scenario, and task, yet the model may comply. We use mechanistic interpretability to determine how this context reverses refusal and which elements contribute to the reversal. Across two benchmarks, three model families, and four authored wrappers, we compare matched harmful and benign requests with and without this wrapper. We trace hidden-state contrasts from the request to the final prompt state, isolate wrapper operations through controlled counterfactuals, intervene on their activation directions in held-out evaluation requests, and decompose effective directions geometrically.
Our analysis yields three findings. (1) Successful attacks retain the measured harmful-versus-benign distinction at the request, while its refusal-associated expression weakens where the answer begins, a pattern we call safety-relay attenuation. (2) Constructing the complete roleplay around the request and framing it within the scenario contribute causally: removing the associated activation changes restores refusal. (3) These effects largely share internal structure, and most repair is reproduced by components aligned with the model's ordinary refusal of harmful requests without roleplay; scenario framing retains a smaller, model-dependent component. Together, these findings explain how roleplay can produce compliance despite retained evidence of harm and identify a concrete target for future safeguards: maintaining the connection from harm recognition to refusal.

---


### 15. [Beyond the Payload: How User Invocation Shapes Coding Agent Vulnerability to Repository Poisoning](https://arxiv.org/abs/2608.30686)

**<font color=#1a73e8>作者：</font>** Fukang Zhu, Binbin Zhao, Ruixiao Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Coding agents are increasingly used for software engineering tasks, including bootstrapping projects from third-party repositories whose integrity cannot be assumed. Prior work on repository poisoning largely focuses on attacker-controlled injection and disguise, but developers also shape risk through everyday invocation choices: what task to delegate, how to phrase the request, and which skills or rules to supply. We term these user-side choices Prompt-Level Configurations (PLCs) and introduce CIPR (Coding In Poisoned Repos), the first benchmark that systematically varies PLCs in poisoned real-world repositories. CIPR comprises 1,920 instances across 20 repositories, four task types, three social-media-grounded prompt styles, and three skill/rule conditions, and measures attack success rate (ASR) and agent alert rate (AR) using automated runtime and trace-based oracles. Our evaluation reveals two key insights: (1) Vulnerability is highly context-dependent, with task type creating up to a 4.5-fold difference in ASR, with test-execution task forming a silent attack surface (high ASR, low AR). (2) Prompt expression shifts risk indirectly: underspecified prompts reduce ASR by truncating execution depth; noisy prompts exhibit a directional trend toward suppressing alerts by making malicious content less conspicuous. These findings highlight that coding agent vulnerability is not a static property, but a dynamic outcome shaped by everyday user configurations.

---


### 16. [The Fragility of Jailbreak Robustness Across Operational States](https://arxiv.org/abs/2608.30748)

**<font color=#1a73e8>作者：</font>** Yuna Park, Hwang Youn Kim, Yujin Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing jailbreak evaluations typically characterize robustness using a single attack success rate (ASR) measured in a default configuration (the vanilla state). However, user-LLM interactions can induce diverse operational states beyond the vanilla state. In this work, we find that jailbreak robustness is highly fragile to operational-state variation: even when the attack remains fixed, changing only an ordinary system prompt not designed to affect safety can dramatically alter attack success rates. We systematically investigate this phenomenon across seven aligned models and three representative jailbreak attacks, observing substantial differences in ASR between vanilla and non-vanilla operational states. In one case, ASR increases by up to 56 percentage points (2% to 58%) solely due to a change in operational state. Remarkably, these increases occur even for attacks originally designed and optimized under vanilla-state evaluation. We further show that state-dependent robustness variation is systematically associated with differences in hidden representations along a refusal-related axis, and that projections onto this axis strongly predict jailbreak outcomes. Our results show that a single vanilla-state evaluation may not fully characterize jailbreak robustness, motivating evaluations that also examine how robustness changes across non-vanilla operational states.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
