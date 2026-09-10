# 🧠 大模型相关研究 | 2026年09月11日

> 本类共 **148** 篇论文：已确认 **136** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-148](./part-03.md)

---

### 1. [World-Time Compute with Verified Code World Models](https://arxiv.org/abs/2609.09163)

**<font color=#1a73e8>作者：</font>** James Schwoebel, Ingrida Semenec, Jenia Rousseva 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLMs generalize across a domain only after seeing many real, labeled examples, which most domains lack. We study a way to manufacture it cheaply. When a domain's dynamics can be written as code, one template instantiates into many world models: executable, verifiable programs over symbolic state, each an inexhaustible source of exactly-labeled trajectories. Fine-tuning an LLM on trajectories through many such worlds, which we call world-time compute, a training-time analogue of test-time compute, lifts generalization to held-out worlds it never trained on (synthesized world families). Gains are largest where capability is scarcest: +29 points at 0.5B; the largest model's lift is within noise, consistent with saturation. Labels can be trusted because the worlds are verified code: synthesized-then-checked dynamics are exact over 20-step rollouts and answer 10x out-of-distribution probes exactly (100%), whereas per-step LLM and MLP predictors compound error and collapse. Unlike domain randomization, each world is independently authored and verified; a corrupted-label control shows label exactness, not task variety, drives the gains. On real benchmarks (ARC-AGI grids, List Functions, CLRS) the same lever holds as per-world test-time training. On List Functions the harder cross-world form holds: one adapter trained on 128 disjoint worlds reaches 40% on held-out worlds versus 6% for a corrupted-label control (+34 points, CI [29, 39]). The gain is a saturating regularity, not a law: largest for few-step reasoning and small/weak models, fading for long chains, perception-induced tasks, and saturated tasks; cross-task transfer is weak without shared skill. Worlds are authored and served by OpenWorld, a zero-dependency framework (companion paper). Scope: symbolic state; pixel-native domains remain territory of learned models. All code, recipes, and this manuscript regenerate from one repository.

---


### 2. [X-CoSD: Communication-Efficient Cross-Vocabulary Collaborative Speculative Decoding](https://arxiv.org/abs/2609.09166)

**<font color=#1a73e8>作者：</font>** Jaeduk Lee, Wan Choi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper investigates collaborative speculative decoding (CoSD), a distributed large language model (LLM) inference framework in which an on-device small language model (SLM) drafts candidate tokens and a server LLM verifies them. Existing CoSD methods assume a shared vocabulary between the SLM and the LLM and incur substantial communication load because residual resampling requires token distribution exchange between the user device and the edge server. To address these limitations, we propose cross-vocabulary CoSD (X-CoSD), a lossless and communication-efficient CoSD framework for heterogeneous SLM-LLM vocabularies. X-CoSD is built on hybrid resampling (HR), which splits residual resampling across the common-vocabulary region on the device and the LLM-only region on the server, so that distribution transmission is required only for the common-vocabulary region. We further propose X-CoSD-E, an enhanced variant based on server resampling with device verification (SR-DV), in which the server sends only replacement candidates sampled from the server LLM and their corresponding probabilities for local verification at the device. We prove that both X-CoSD and X-CoSD-E preserve the server LLM distribution, and experiments show that they significantly improve token generation speed while maintaining generation quality comparable to that of the server LLM.

---


### 3. [Evidence-Order Calibration for Selective Visual Reasoning under Progressive Loss of Question-Critical Evidence](https://arxiv.org/abs/2609.09184)

**<font color=#1a73e8>作者：</font>** Muhamathu Ameer Ali Aacaas Muhamath  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language model (VLM) confidence may change in aggregate when visual evidence is degraded while remaining structurally inconsistent within individual examples. We study answer-level reliability along five-step, question-conditioned evidence-loss trajectories. Using a frozen Qwen2.5-VL-3B-Instruct model, we construct 176 accepted GQA-derived trajectories (880 masking conditions) by progressively masking scene-graph-localized question-critical regions. Native sequence confidence has an evidence monotonicity violation rate (EMVR) of 0.436, and 92.0% of trajectories contain at least one adjacent violation. A matched non-critical-region control shows that full critical masking reduces accuracy by 28.2 percentage points, compared with 0.6 points for equally sized non-critical masks; the paired difference is 27.6 points (95% CI [20.0, 34.7]). We train a lightweight post-hoc reliability head on frozen hidden states, sequence confidence, and entropy. Adding evidence-order supervision to binary cross-entropy (BCE) reduces masking EMVR from 0.330 to 0.303 (paired difference -0.027, 95% CI [-0.044, -0.010]). The same mask-trained objective reduces EMVR from 0.449 to 0.402 on held-out question IDs under unseen local Gaussian blur (difference -0.0468, 95% CI [-0.0739, -0.0199]). AUROC, Brier, and AURC differences between the two learned heads are statistically inconclusive, and native confidence remains stronger for selective-risk ranking. The results separate evidence-order consistency from conventional correctness discrimination rather than establishing generic confidence superiority.

---


### 4. [OpenDiscoveryTrace: Process Traces for Evaluating AI Scientist Workflows](https://arxiv.org/abs/2609.09203)

**<font color=#1a73e8>作者：</font>** Aayam Bansal, Keertan Balaji  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing benchmarks for autonomous AI scientists evaluate only final outputs---generated code, hypotheses, or papers---yet discard the reasoning process by which those outputs were obtained. This makes it impossible to audit scientific methodology, diagnose failure modes, or distinguish systematic reasoning from fortunate guessing. We present \textbf{OpenDiscoveryTrace}, a public dataset of 558 complete AI scientific agent trajectories that captures how models reason, not just what they produce. Each trajectory records a structured 9-field-per-step trace---including thoughts, tool calls, observations, errors, revision triggers, and self-reported confidence---as models execute 124 scientific tasks spanning drug discovery, materials science, genomics, and scientific literature analysis. The dataset covers seven models: three frontier models (GPT-5.4, Claude Opus 4.6, and Gemini 3.1 Pro; 124 trajectories each, fully balanced across domains and difficulty levels) and four open-weight models (Qwen2.5-7B, Mistral-7B-v0.3, Phi-3.5-mini, and Qwen2.5-1.5B; 30 each), plus 60 live-retrieval variant trajectories. Pilot analysis on 363 LLM-judged trajectories reveals that process traces expose behavioral differences invisible to output-only evaluation: all three frontier models achieve comparable success rates (84--89%), yet Claude Opus 4.6 produces 30$\times$ more errors than GPT-5.4 (2.5 vs. 0.08 per trajectory, $p < 0.0001$, Cliff's $\delta = 0.613$), with qualitatively different error profiles---66.7% tool misuse for Claude versus 83.6% reasoning errors for GPT-5.4. We define five benchmark tasks with baselines from logistic regression, random forests, LSTMs, and Transformer models. The dataset, trace schema, agent harness, and benchmark definitions are publicly available under CC BY 4.0 to support research on process-level evaluation, scientific agent auditing, and AI governance.

---


### 5. [MLLMs Hallucinate when Information Distribution Drifts in Synergy Heads](https://arxiv.org/abs/2609.09206)

**<font color=#1a73e8>作者：</font>** Meng'en Qin, Junye Chen, Jucheng Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) often struggle with hallucinations, thus hindering their reliable practical applications. Existing attention-based mitigation methods mainly rely on indirect signals (e.g., attention weights) that fail to accurately reflect the actual information shift underlying hallucination generation. In this paper, we propose HEAL, Head-lEvel information disentAnglement and caLibration for identifying and mitigating hallucinations. HEAL first employs causal noise intervention on multi-head outputs to filter out causally redundant heads. Subsequently, it disentangles information distribution within the remaining heads via the counterfactual Difference-in-Differences, categorizing heads into four types. Through analysis, we observe: hallucinations happen when information distribution drifts away from a healthy equilibrium in synergy heads, not strongly correlated with the quantity or strength of modality-specific heads. Motivated by this insight, HEAL injects dynamic information calibration factors into the value vectors of synergy heads, and actively regulates visual-language dependencies, steering the output distribution towards factual evidence. Extensive experiments demonstrate that HEAL effectively reduces hallucinations across multiple MLLMs, offering a simple and interpretable pathway to enhance model trustworthiness.

---


### 6. [AgentHijack: Visual Patch Attacks on Multimodal Computer-Use Agents](https://arxiv.org/abs/2609.09212)

**<font color=#1a73e8>作者：</font>** Zhihao Liu, Hongyu Sun, Zhiyuan Fu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper presents an end-to-end evaluation framework for image-triggered command injection against computer-use agents (CUAs). The goal is to test whether a local visual patch can induce verifiable environmental consequences along the full chain of screenshot input, VLM generation, action parsing, and environment execution. We train and deploy patches on author-controlled GitHub Pages pages and a locally deployed CSDN clone, and evaluate them in real environments across five open-source or publicly available GUI-agent or vision-language-model (VLM) backends. Our experiment aggregates 600 instance-level online cases, with T-ASR, TAPR, and E2E-ASR reaching 84.5%, 47.0%, and 20.3%, respectively. Trajectory analysis further shows that in some successful cases the agent first executes a malicious terminal command and then continues the original benign task. These results indicate that optimized local visual signals can affect not only VLM outputs but also propagate through the execution pipeline of open CUAs and create real environmental risk.

---


### 7. [Scores Alone Do Not Prove Discovery: The Discovery Certification Protocol for Auditing AI Research Agents](https://arxiv.org/abs/2609.09219)

**<font color=#1a73e8>作者：</font>** Jingjie Ning, Shanshan Zhong, Xiaochuan Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> AI research agents combine prior knowledge, public sources, and experimental feedback to produce useful results. The Discovery Certification Protocol (DCP) turns claims about these results into executable recovery and feedback tests. Gate 1 validates useful improvement on sealed evaluation. Gate 2 gives matched agents the registered starting information and observed Web content while withholding the target research history. Every valid method reaching the numerical target supplies a recovery witness and triggers the Core veto. DCP Core requires adequate controls, zero observed recoveries, and a finite-sample bound on recovery in one fresh registered episode. Optional Gate 3 measures the average effect of truthful feedback relative to a specified neutral policy from a shared checkpoint. DCP Evidence adds this effect after independent null calibration and a registered effect margin. Two controlled audits exercise the complete protocol in SQLite optimization and virtual catalyst control under different models. Each produced zero recoveries in 96 episodes, with an upper bound of 0.0468. Each paired study yielded 30 truthful recoveries and zero neutral recoveries, with passing 60-pair null studies. Additional cases exercise Core, recovered, and audit-incomplete decisions. A deterministic, LLM-free verifier reproduces the decisions from frozen evidence. DCP provides a common evidence language for useful outcomes, alternative routes, and feedback effects across AI research.

---


### 8. [Subagents vs Agent Skills: Executing Reusable Knowledge for Long-Horizon Agentic Tasks](https://arxiv.org/abs/2609.09233)

**<font color=#1a73e8>作者：</font>** Wasu Top Piriyakulkij, Rachel Lawrence, Alicia Curth 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How can language model agents effectively leverage libraries of reusable knowledge to solve long-horizon tasks? Recent work has increasingly focused on agent skills: reusable capabilities represented as skill packages, i.e., multi-file bundles containing instructions, scripts, and other resources that help agents perform specific tasks. Agent skills are typically executed by loading their skill instructions into an agent's context and relying on the agent to follow them. As task horizons grow, however, this approach becomes increasingly brittle, because reasoning quality degrades as more information accumulates in the context window. We investigate an alternative approach in which skill packages are instead invoked as subagents. Rather than loading skill instructions into the main context, subagent execution spawns fresh context windows dedicated to solving individual subtasks. We show that subagent execution outperforms agent-skill execution when skill packages expose clear input-output contracts and their instructions encode the procedural knowledge needed to fulfill those contracts. The tradeoff is additional communication overhead, as extra tokens are required to coordinate between the main agent and its subagents. Our results show that the benefit of reusable knowledge depends not only on its content, but also on how it is organized and invoked.

---


### 9. [Scaling Post-Training Ternarisation to Qwen3-8B Capability Retention, Reproduction, Lossless Packing, and Packed Execution](https://arxiv.org/abs/2609.09240)

**<font color=#1a73e8>作者：</font>** Anirudh Malik, M Sparsh Mehra, Poojith Devan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ultra-low-bit language models promise reductions in storage and memory traffic, but a nominal "1.58-bit" label does not specify the deployed representation or its execution cost. We study a scale-up of an aggressive post-training conversion pipeline from Qwen3-4B to Qwen3-8B.
The conversion uses KOTMS rotation, E2M-ATQ adaptive ternarisation, and GPTQ-style error compensation in a weight-only A16 configuration. We do not claim these algorithms as new. Our contribution is the end-to-end scale-up characterisation: an external reproduction gate, matched 4B/8B capability analysis, cross-corpus perplexity, effective-bit accounting, lossless lattice-aware packing, and direct packed execution.
The 8B model reaches a three-corpus perplexity ratio of 1.361x, with WikiText-2, C4, and PTB ratios of 1.318x, 1.393x, and 1.371x. On eight zero-shot tasks at n = 500, mean accuracy is 64.6% versus 72.4% for FP16, corresponding to 78.5% chance-corrected retention and a 7.8-point absolute cost. The matched 4B run retains 69.6%, yielding an 8.9-point 8B advantage.
The packed checkpoint is 8.24 GiB and preserves the recorded perplexity to measurement precision. Direct packed execution reaches 15.52 tokens/s in 7.35 GiB, while a preliminary packed GEMV remains slower than FP16 cuBLAS. The result is a validated scale-up baseline: model size improves robustness to aggressive post-training discretisation, actual serialisation is solved for the measured artefact, and direct execution is feasible, while broader seeds, calibration distributions, and kernel optimisation remain open.

---


### 10. [Distribution-Consistent Inference for Dynamic Sparse Mixture-of-Experts](https://arxiv.org/abs/2609.09241)

**<font color=#1a73e8>作者：</font>** Dohyeon Kim, Bedionita Soro, Sung Ju Hwang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures have emerged as a powerful paradigm for scaling model capacity while preserving efficient inference in large foundation models. However, most MoE models use a fixed top-$k$ expert selection policy, assigning the same expert budget to every token even when fewer experts may be sufficient. Inference-time dynamic top-$k$ routing can reduce computation without retraining, but existing methods often overlook the distributional shift caused by deviating from the training-time routing configuration. We show that reducing the number of activated experts consistently increases the RMS scale and variance of SMoE outputs, inducing a representation mismatch that contributes to downstream performance degradation in addition to the loss of expert capacity. To address this correctable component, we propose Layer-wise Distribution Alignment (LDA), a lightweight inference-time correction that uses layer-wise calibration statistics to align reduced-routing representations with the default configuration. Across multiple SMoE LLMs, benchmarks, and routing strategies, LDA recovers much of the performance lost induced by the distributional shift under reduced routing while preserving sparse-inference efficiency with negligible overhead.

---


### 11. [StochBench: A Domain-Specific Benchmark for Stochastic Processes in Lean](https://arxiv.org/abs/2609.09264)

**<font color=#1a73e8>作者：</font>** Idan Davidovich, Debargha Ganguly, Vikash Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Leading benchmarks for formal theorem proving with large language models are small collections drawn from competition math, such as the IMO and Putnam, that poorly represent field-specific applications. We introduce StochBench, a Lean 4 benchmark of 450 graduate stochastic-processes problems at varying abstraction levels, each paired with its natural-language source. Addressing a field underrepresented in Mathlib, it covers finite and countable Markov chains, renewal processes, random walks, martingales, stopping times, queues, Brownian motion, stochastic calculus, weak convergence, and Poisson and continuous-time Markov processes. Our Opus 4.8-based agent achieves a 34.9% proof rate (157/450) under a 15-minute per-problem limit. StochBench better represents domain-specific applied mathematics while remaining challenging for advanced provers.

---


### 12. [Video-MOPD: Multi-Teacher On-Policy Distillation for Video Understanding](https://arxiv.org/abs/2609.09300)

**<font color=#1a73e8>作者：</font>** Zhenxin Qin, Peng Shi, Cong Han 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video understanding demands a convergence of complementary capabilities across perception, temporal understanding, and complex reasoning, which are difficult to jointly optimize within a single model. We introduce Video-MOPD-8B, an open-weight model dedicated to video understanding tasks. To fundamentally enhance its capabilities, we conduct targeted reinforcement learning (RL) optimization across three core domains: video temporal grounding (VTG), general video comprehension, and video STEM reasoning. We then unify their complementary capabilities via Multi-Teacher On-Policy Distillation (MOPD), which consolidates expert knowledge by supervising student-generated trajectories with routed teacher feedback. We further introduce Reliability-Aware Informative Sampling (RAIS), which selects examples with consistently reliable teacher supervision and large teacher-student performance gaps. Together, these components enable Video-MOPD-8B to achieve coordinated and comprehensive performance gains across diverse video understanding tasks. Extensive experiments on comprehensive benchmarks covering general video understanding, temporal grounding, video reasoning, and video STEM tasks demonstrate that Video-MOPD-8B achieves state-of-the-art performance among existing models at a comparable scale. The trained model weights are available at this https URL.

---


### 13. [Early Epistemic Settlement in AI-Assisted Writing](https://arxiv.org/abs/2609.09332)

**<font color=#1a73e8>作者：</font>** Han-yu Wang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> A language model can resolve a writer's current organizing problem while the construction needed for her own resolution remains unfinished. I call this early epistemic settlement. The supplied organization meets every demand then governing the passage, yet proceeding from it can displace work through which the writer would have changed those demands or become able to form further organizations. I distinguish the coordination needed to complete an already formable organization from construction that changes which organizations are formable in the first place. Settlement in the first case changes the relative work still required to bring available organizations to sufficiency. In the second, it can remove the need for the work through which another organization would become formable. Even when supplied resolution and continued construction leave the same visible qualification, different dependencies in the writer's inquiry may support different later organizations. Model suggestions can also contribute to this development when writers work through them while the problem remains unresolved. In theoretical and exploratory writing, the relations developed in reaching local adequacy help determine what the writer can later defend or develop. A sound judgment that the present passage is sufficient can therefore make further inquiry dispensable before that generative work has occurred.

---


### 14. [Where Does the Human End? Creative Agency with Generative AI across Five Years of Chinese Digital Painting](https://arxiv.org/abs/2609.09333)

**<font color=#1a73e8>作者：</font>** Yibo Meng, Ruiqi Chen, Shuheng Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As generative AI enters creative work, practitioners must decide where AI assistance ends and human authorship begins. Human-agent interaction (HAI) research has examined AI as a tool, collaborator, consultant, and competitor. The longitudinal problem is how these roles are revised as systems become more capable, public, and economically embedded. We report a five-year interview study with 17 Chinese digital painters, based on annual semi-structured interviews from 2021 to 2025. Participants described recurring but non-uniform patterns of protective resistance, pragmatic task delegation, and, for some, reflective agency repartitioning. Early resistance protected observation, originality, signature, and ownership from AI. Later delegation placed AI in bounded tasks such as references, backgrounds, rough sketches, and client-facing drafts. By 2025, some participants built hybrid workflows around human-only zones, while others described fatigue, precarity, or difficulty locating a remaining human role. Peer norms, emotional climates, and production pressures shaped which delegations felt useful, acceptable, or exhausting. Copyright, authorship, and creative labor remained recurring limits on what participants were willing to delegate. We frame these accounts as longitudinal agency partitioning, the situated work of deciding which stages, responsibilities, values, and claims remain human in creative human-agent interaction. We discuss design implications for revisable agency-boundary controls, provenance scaffolds, and community-facing authorship norms.

---


### 15. [Osprey: Target-agnostic Pre-training Makes Stronger Drafters in Speculative Decoding](https://arxiv.org/abs/2609.09338)

**<font color=#1a73e8>作者：</font>** Fengxiang Bie, Yuqing Jian, Yifan Yu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding is critical for accelerating LLM inference. However, the speedup is fragile: drafters are typically trained against a narrow distribution for a single target model, and their acceptance rate collapses under workload shifts. This is a striking inversion of modern LLM development, where target models are valued precisely for the broad generalization they acquire through large-scale pretraining. We argue that the natural remedy, pretraining, has been hard to apply to drafters because existing recipes are target-specific: the drafter consumes the target's hidden states and is distilled on the target's logits, so pretraining must be repeated for each target. We introduce Osprey, which instead bootstraps drafters from off-the-shelf pretrained small language models, treating broad pretraining as a reusable, target-agnostic asset and reducing per-target work to a lightweight adaptation step. Realizing this requires overcoming two challenges: small LMs are far deeper than a latency-bound drafter can afford, and their pretrained computation must remain intact while the drafter learns to ingest target hidden states and emit tokens in the target's vocabulary. Osprey addresses both by pruning to a shallow backbone, restoring its language-modeling capability with target-agnostic next-token pretraining, and adapting it to each target through vocabulary alignment, zero-initialized QKV expansion, and distillation from the target model's output distribution. Empirically, a single pretrained Osprey backbone transfers across targets and improves mean acceptance length by 16.1% for Qwen3-8B, 21.2% for Llama-3.3-70B-Instruct, and 22.7% for the 229B MiniMax-M2.5 (with 17.5% higher tokens per second), with the largest gains on out-of-domain and multilingual data. Our code is available at this https URL.

---


### 16. [SWORD: Wikidata-based Distortions Reveal Hidden Cross-Lingual Inconsistencies in LLM Factual Error Rejection](https://arxiv.org/abs/2609.09349)

**<font color=#1a73e8>作者：</font>** Sanghyeok Park, Minji Kang, Hosung Kwak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern LLMs demonstrate impressive multilingual performance, yet standard benchmarks primarily reward selecting correct answers rather than evaluating genuine factual understanding. We introduce Systematic Wikidata-based Object-Relation Distortion (SWORD), a benchmark that evaluates whether models consistently reject factual errors across languages. SWORD generates syntactically well-formed but factually incorrect statements in eight widely spoken languages through controlled perturbations of Wikidata triples, ranging from random entity substitutions to semantically plausible property-based selections. Our distortion-based evaluation surfaces two critical insights that remain entirely obscured by conventional benchmarks. First, models counterintuitively achieve higher accuracy on semantically plausible distortions than on nonsensical random substitutions, suggesting reliance on distributional familiarity rather than genuine factual verification. Second, models exhibiting comparable baseline accuracy across languages show substantial performance degradation specifically on (East) Asian languages when presented with distorted statements, with cross-lingual performance gaps reaching up to 28 percentage points (49\% relative reduction) in some models. These findings demonstrate that multilingual factual reasoning involves asymmetric capabilities that aggregate accuracy metrics systematically obscure.

---


### 17. [Auditable Emergency Triage for Maternal and Newborn Care in India](https://arxiv.org/abs/2609.09356)

**<font color=#1a73e8>作者：</font>** Shobhit Jagga, Aman Dalmia, Niharika Priyadarshini 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> At Noora Health, our nurses answer more than 50,000 medical queries per month on our WhatsApp-based service that provides caregivers with on-demand support. Their most time-critical task is emergency triage: deciding which queries need immediate in-person attention. To support them, we built a system that uses a large language model (LLM) to classify whether a message is an emergency and provide a rationale for interpretability. But the system was opaque: analyzing mistakes meant reading reasoning chains for each message, which is infeasible at our scale. Prompt changes meant re-running a full evaluation to prevent regressions, which was both costly and operationally challenging. Clinicians follow a decision tree to make this call, but it was never documented or passed to the model, which relied on a flat list of danger signs. To address these issues, we decomposed triage into two steps: an LLM extracts canonical symptoms and patient context from the query using a clinician-authored vocabulary, and a deterministic rule engine captures the scenarios that indicate an emergency. We show that the new system raised recall from 0.565 to 0.810 and F1 from 0.606 to 0.702, with structured rules driving most of the accuracy gains while the decomposition provides auditability: clinical experts can inspect each stage of the new system to see whether the query was mistranslated, symptoms were incorrectly extracted, patient context was wrongly inferred, or the necessary rules were missing. They can add new rules independently without causing regressions and avoid running costly evaluations. Since deployment, the new system has triaged 152,421 patient queries and flagged 28,535 (18.7%) as emergencies. The over-escalation rate has been 17.8%, without any increase in missed emergencies. Clinicians have also added 48 new rules since deployment, evidence of the faster correction loop we set out to build.

---


### 18. [Do LLMs Make More Mistakes If They Do Not Believe the Input Data?](https://arxiv.org/abs/2609.09363)

**<font color=#1a73e8>作者：</font>** Peter Kochelka, Aleš Manuel Papáček, Vojtěch Dvořák 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are prone to hallucinating or misinterpreting facts, which impairs their usability in retrieval-augmented generation or data-to-text systems. We analyse how faithfulness of LLMs to provided context depends on how plausible they perceive the context to be (context-memory conflict). To better identify error patterns, we make use of the increased difficulty of non-English and low-resource language text generation and input data based on local knowledge, only partially captured in models' parametric knowledge. We let the models generate text in English, Czech, Slovak and Upper Sorbian from factual (FA), counterfactual (CFA) and fictional (FI) RDF triples containing local Czech and Slovak data. Contrary to our expectations, we observe only a weak context-memory conflict on the human-annotated sample. For Kimi K3 as an LLM judge, which agrees well with human annotations on the sample, counterfactual inputs receive only slightly lower faithfulness scores than factual ones (-0.05 on a 1-5 scale). We also find that a suboptimal choice of LLM judge would lead to overestimating the strength of the context-memory conflict.

---


### 19. [Agentic Web Accessibility Auditing: Authoring and Evaluating Per-Criterion Worker Agents for WCAG](https://arxiv.org/abs/2609.09379)

**<font color=#1a73e8>作者：</font>** Arjun Mishra, Pranav Karthik, Byungjun Bae 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Automated accessibility assessments differ in the evidence they collect and the requirements they address. We present a framework that combines shared browser tools with criterion-specific worker agents, implementing 39 WCAG 2.1 Level A and AA criteria and one additional WCAG 2.2 criterion. We analyze archived predictions on 250 page-criterion records derived from professional audits of scholarly platforms. Workers recover 0.86 of positive reference labels, compared with 0.36 for axe-core and 0.67 for an uncued vision-language model, with lower precision. Criterion-level results, abstentions, development-exposure sensitivities, and separately instrumented runs qualify these comparisons. Inferred negative labels and differences between evaluated configurations limit conclusions about true accuracy and causal effects. We contribute the framework, its criterion-specific implementation, and an evaluation account that distinguishes detection, evidence availability, and resource use, motivating further study of inspectable automated assessments within professional auditing.

---


### 20. [LLMSec-AV: A Vulnerability Taxonomy and LLM-Driven Software Weakness Discovery Framework for Autonomous Vehicles](https://arxiv.org/abs/2609.09386)

**<font color=#1a73e8>作者：</font>** Md. Wasiul Haque, Sagar Dasgupta, Mizanur Rahman  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Automated vehicles rely on millions of lines of safety-critical software, yet general-purpose analyzers do not understand which code can affect vehicle motion. This study asks whether large language models (LLMs) with explicit automated-vehicle (AV) security knowledge improve weakness detection beyond rule-based tools. We developed an AV vulnerability taxonomy with 18 weakness classes from vulnerability records, security advisories, and AV-security literature, and integrated it into LLM-based Security Analysis for Automated Vehicles (LLMSec-AV). Evaluated on Autoware, the framework decomposed 770 translation units into 4,673 functions and analyzed 161 functions under four prompting conditions involving taxonomy context, retrieval from 374 prior disclosures, and multi-step analysis. Findings were compared with 46 weakness locations mined from upstream fixes and a flag-volume-matched permutation baseline. CodeQL, Semgrep, cppcheck, and the Clang Static Analyzer evaluated the same code, with AV-specific rules added to CodeQL and Semgrep. Generated fuzzing harnesses were tested using AFL++ and sanitizers. LLM conditions recovered up to 76% of the 46 known weakness locations, outperforming conventional analyzers. CodeQL, Semgrep, and the Clang Static Analyzer matched none, while cppcheck matched one despite 1,301 alerts. Unaided prompting achieved similar detection performance, showing that the taxonomy did not drive recall. However, taxonomy context increased the share of findings assigned to a weakness class from near zero to over 80%, improving interpretability and triage. Six of the 18 classes could not be directly represented as static-analysis rules. LLMSec-AV introduces an AV-specific, machine-readable vulnerability taxonomy for weakness discovery and shows that LLMs can complement conventional analyzers by identifying and organizing safety-relevant findings in real AV software.

---


### 21. [The Menu Is an Execution Prior: State-Path Tool Menus for Online Agents](https://arxiv.org/abs/2609.09395)

**<font color=#1a73e8>作者：</font>** Bo Yan, Weikai Lin, Song Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models act through tools, yet practical agents face libraries containing thousands of interfaces. We introduce the tool menu as the short, ordered subset of available tools shown to an agent before execution. The agent can call only tools in this menu. Multi-step tasks require the final action and the prerequisite tools that create its inputs in a usable order. Current constructors rank tools by request relevance, which can surface the final action while omitting or delaying less obvious producers. We introduce the state path, a pre-execution route from the observable request state to the desired outcome, and propose State-Path Tool Menu to learn it. Our framework treats the menu as an execution prior over these routes. Its encoder represents which tools can run from the current state, how their outputs satisfy later inputs, and which orders recur in training paths. A retriever covers an executable entry, the missing-input producers, and the final action. A reranker then places producers before consumers. On ToolBench, our menu raises online success from 0.737 to 0.898 and outperforms retrieval, reranking, generation, and routing baselines without changing the agent. The State-Path menu also covers more complete chains with 32 tools than the official list covers with 128, and its success gain persists across executor families with different model capacities. Our code is at this https URL.

---


### 22. [VANTAGE-Bench: Evaluating the Infrastructure AI Gap in Vision-Language Models](https://arxiv.org/abs/2609.09396)

**<font color=#1a73e8>作者：</font>** Zaid Pervaiz Bhat, Nimra Nayyar, Arihant Jain 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As Vision-Language Models (VLMs) advance toward physical deployment, the focus has remained on action-oriented Embodied AI evaluated on subject-centric consumer video. This overlooks a pervasive class of Physical AI: Infrastructure AI, which relies on fixed cameras for open-loop insights like safety monitoring and operational logging. We introduce VANTAGE-Bench, a benchmark measuring this "Infrastructure AI Gap." It spans three operational domains (Logistics, Transportation, and Smart Spaces), unifies image and video evaluation across semantic, spatial, temporal, and spatio-temporal capabilities, and moves beyond multiple-choice to eight task formulations including dense captioning and spatio-temporal grounding. It adds a single-pass trajectory protocol for Single Object Tracking and, to our knowledge, the first such evaluation on fixed-camera infrastructure video, scored against specialist trackers. Annotation spans three regimes over 3,346 media assets: 3,342 video-task annotations, 4,281 image-grounding annotations, and 27,404 detection boxes.
Evaluating 17 models zero-shot, we find the shortfall relative to consumer-centric benchmarks is concentrated, not general. Event verification, referring expressions, and temporal localization fall roughly 9 to 24 points at every model scale, while video question answering stays within 5.3 points of VideoMME and 2D spatial pointing shows no shortfall against BLINK. The temporal pillar is weakest in absolute terms: no system exceeds 55.7 mIoU on temporal localization or 37.3 SODA_c on dense video captioning. On tracking, frontier models come within roughly 5 points of specialist trackers over short horizons but separate as the horizon extends. Open-weight models lead 2D object localization outright, so neither scale nor proprietary access explains the pattern. Data, evaluation harness, and leaderboard: this https URL

---


### 23. [Benchmarking Hybrid Deep Research Across Database Querying and Web Search](https://arxiv.org/abs/2609.09410)

**<font color=#1a73e8>作者：</font>** Ruofan Wu, Peiran Xu, Xiaolong Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While autonomous agents have made significant strides in "deep research" by iteratively navigating the open web to synthesize information, real-world problem-solving is rarely confined to a single environment. Complex analytical tasks inherently require agents to weave together evidence from both ambiguous unstructured text (e.g., the open web) and highly precise structured data (e.g., relational databases). However, existing benchmarks evaluate these modalities in isolation, failing to capture the critical "handoff" - the ability to preserve constraints when moving evidence between systems. We introduce HybridDeepResearch, to our knowledge the first deep-research benchmark that requires both web search and SQL to form a complete, verifiable answer. The benchmark contains 380 tool-dependent tasks grounded in LiveSQLBench-Base-Lite databases and public web corpora, validated through automated checks and human review, and covering three reasoning patterns: SQL2S, S2SQL, and Parallel. Evaluations across proprietary and open-weight models under various agentic scaffolds reveal that even state-of-the-art models like GLM-5.2, Claude-Sonnet-4.6 and GPT-5 achieve only about 50-54% Pass@8 on the hard subset. Notably, results show that directional reasoning is substantially more difficult than parallel intersection, highlighting that bridging structured and unstructured information spaces without losing constraints remains a major open challenge for agentic systems. Code and datasets are publicly available at GitHub (this https URL) and Hugging Face (this https URL).

---


### 24. [Vision-language models know more about agriculture than they show and rubric-grounded verifications close the gap](https://arxiv.org/abs/2609.09417)

**<font color=#1a73e8>作者：</font>** Earl Ranario, Jared Smith, Lars Lundqvist 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) show promise for agricultural classification, but zero-shot performance on disease, pest, damage, quality, and species identification remains poor, and it is unclear whether this reflects weak visual features or a failure to connect them to domain knowledge. We build a benchmark of 116 datasets, 834 classes, and 8,324 images spanning these tasks to isolate where the gap arises. Linear probing shows VLM vision encoders already encode agricultural features nearly as separable as a self-supervised DINOv3 baseline, ruling out weak visual representations as the primary bottleneck. Conditioning each model on an oracle reference description (an upper bound on its parametric knowledge) closes most of the gap left by an unaided lower bound, showing VLMs already know more about agriculture than they show. To close this gap without an oracle description at inference time, we structure test-time reasoning around a fixed, per-task diagnostic rubric: the model generates $K$ candidate responses and a Probabilistic Pivot Tournament (PPT) verifier, scored pairwise against the rubric, selects the best one. This nearly doubles judged F1 over the lower bound and matches or exceeds the upper bound on several tasks, notably pushing Gemma 4 E4B-it's disease F1 to 0.71, above its own upper bound of 0.60. However, the verifier's letter-scale confidence score has the opposite of its intended effect: filtering to its most confident predictions does not improve accuracy and correlates negatively with correctness across every model and pool size tested, so the score cannot serve as a measure of predictive uncertainty, and most of the observed gain likely comes from rubric-grounded generation rather than pairwise verification.

---


### 25. [Edu-QuRating: Multi-Dimensional Educational Data Curation with Distilled Pairwise Judgements](https://arxiv.org/abs/2609.09425)

**<font color=#1a73e8>作者：</font>** Oliver G. B. Garrod, Robin A. A. Ince, Meng Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Educational data filters have become a practical way to improve language-model pre-training, but most filters treat educational value as a single scalar property. This may be too broad for some applications, especially if the data set already features a high density of educational material. Useful learning material needs to be accurate, engaging, well structured, and appropriate for the intended audience and application (e.g. learner- vs teacher-facing). Following QuRating (Wettig et al. 2024), we introduce Edu-QuRating: a pipeline for multi-dimensional educational data scoring and curation. Edu-QuRating defines education-specific rubrics, uses an LLM judge to label sampled document pairs and distills those pairwise preferences into reusable Edu-QuRaters, which can score individual text chunks on a set of educational criteria. Across two sequence-classification base models and six educational criteria, the best Edu-QuRater recovers held-out GPT-4.1-mini pairwise judgements with mean accuracy 0.917. We then apply the resulting scorers in two applications. First, we investigate the potential of Edu-QuRaters for corpus filtering to improve pretraining of small language models. We scored 322.25M FineWeb-Edu-Fortified documents to obtain a filtered pre-training mixture. In matched single-run pre-training comparisons, models trained with Edu-QuRating-based mixtures reached higher observed aggregate accuracy across nine benchmarks than the FineWeb-Edu baseline, with gains concentrated in particular tasks. Second, we used Edu-QuRater scores as reward terms for GRPO post-training. In held-out pairwise judge evaluations, combining Edu-QuRater and answer-structure rewards produced responses preferred to the Qwen3-4B base model on both pedagogical quality and instruction following.

---


### 26. [XAI-Arena: Can LLMs Assess the Quality of XAI Explanations?](https://arxiv.org/abs/2609.09428)

**<font color=#1a73e8>作者：</font>** Yanfei Hu Fleischhauer, Alona Zharova, Nadja Klein 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating the quality of explanations produced by explainable AI (XAI) methods remains challenging because existing approaches often rely on subjective human judgment, limiting reproducibility, scalability, and comparability between studies. We examine whether LLMs can serve as a reproducible and scalable mechanism to make comparative assessments of the quality of XAI explanations. We introduce XAI-Arena, an LLM-as-a-judge framework for scalable, reproducible, multidimensional, and stakeholder-sensitive evaluation of XAI explanation quality. XAI-Arena then allows us to compare XAI explanations along various dimensions, namely, perceived simplicity, clarity, task adequacy, trust calibration, actionability, transparency, faithfulness, and overall interpretability. We then benchmark XAI explanation methods across various datasets, machine learning models, and stakeholder personas. Human validation shows a strong positive association between LLM-generated and human ratings (Spearman's rho=.693, p<.001). Together, LLM-based evaluations can capture systematic differences in XAI explanation quality and provide a scalable and reproducible framework for comparative assessment of XAI explanations.

---


### 27. [Do Agents Know When They Succeed? Calibrating Agent Confidence from Internal Representations](https://arxiv.org/abs/2609.09448)

**<font color=#1a73e8>作者：</font>** Priyanka Mary Mammen, Emil Joswin, Srujananjali Medicherla  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As agentic systems getting adopted rapidly in safety critical applications, it is vital to measure the confidence associated with the agentic actions. In comparison to the traditional machine learning systems, agentic workflows have complex failure modes with planning, tool invocation and dynamic environment interactions. In this paper, we investigate whether model's internal representations provide stronger signals of eventual task success in multi-turn agentic setups. We introduce two complementary methods: Latent Trajectory Dynamics (LTD), which summarizes changes in residual-stream representations across an an interaction trajectory, and the Action Representation Probe (ARP), which predicts success from representations formed at action decisions. Across three interactive benchmarks (Bash, SQL, Python) and three model families (Qwen14B, Qwen7B, DeepSeek6.7B), our methods consistently outperform surface level generation and sequence-based calibration baselines providing a zero-overhead reliability monitor that requires neither prompt alterations nor multi-sample rollouts.

---


### 28. [ContractEval: Query-Conditioned Execution Matching for Procedural Instruction Conformance](https://arxiv.org/abs/2609.09458)

**<font color=#1a73e8>作者：</font>** Praphul Singh, Shanu Kumar, Akshat Agarwal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLM agents move from answering questions to carrying out procedures, failures can be unwarranted rather than visibly wrong: the final response looks acceptable even though the system skipped the check, branch, dependency, or invariant that made the answer justified. Output-only evaluation sees the answer, and trace-aware judging sees activity, but neither identifies which obligations were active for the query. We introduce CONTRACTEVAL, a diagnostic framework for making those active obligations explicit. It represents procedural instructions as query-active obligations and matches them against response or trace evidence, turning omissions, wrong branches, ordering errors, extra actions, invariant breaches, and output-contract violations into distinct conformance failures. On a controlled suite of audited procedural contracts, output-only and trace-aware LLM judges miss many injected structural failures; under gold expected and observed graphs, ContractEval detects and localizes all of them. LLM-backed extraction preserves much of this signal but remains calibration-sensitive. ContractEval is therefore not a compliance guarantee; it makes procedural conformance auditable rather than implicit in final-answer quality.

---


### 29. [Low-Rank Prompt Learning for Vision-Language Models with Fixed-Token Bases](https://arxiv.org/abs/2609.09462)

**<font color=#1a73e8>作者：</font>** Tanvir Muntakim Tonoy, Sajjad Ghiasvand, Mahnoosh Alizadeh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prompt learning adapts CLIP to downstream recognition by replacing hand-written templates with learned continuous context vectors, which in Context Optimization (CoOp) form a dense prompt matrix $\mathbf{P}\in\mathbb{R}^{m\times d}$ trained from only a few examples per class. We study whether this matrix is over-parameterized by factorizing it as $\mathbf{P}=\mathbf{B}\mathbf{A}$, which cuts the trainable prompt parameters from $md$ to $r(m+d)$, and to $rd$ once the token-side factor $\mathbf{B}$ is fixed. Across seven few-shot benchmarks and two CLIP backbones, low-rank prompts match or improve dense CoOp at far fewer parameters, with the clearest gains on low-shot base-to-new generalization. We then find that the token-side factor need not be learned at all: fixing $\mathbf{B}$ to a Gaussian, orthogonal, SVD-derived, or even random basis and training only the embedding-side factor $\mathbf{A}$ stays on par with the fully trainable factorization, and a source-trained $\mathbf{B}$ offers no advantage over a random one. A prompt-factor asymmetry and a local update-space dimension gap show why fixing $\mathbf{B}$ is far less restrictive than fixing $\mathbf{A}$, and a smoothness-only guarantee certifies that optimizing $\mathbf{A}$ over a fixed $\mathbf{B}$ converges. In the CLIP prompt setting, the embedding-side coefficients carry the adaptation while the token basis can simply be fixed.

---


### 30. [Building the Harness Automatically: Self-Play in Code Distills a Text Harness for Black-Box Optimization](https://arxiv.org/abs/2609.09468)

**<font color=#1a73e8>作者：</font>** Yi Wu, Zheng Ren, Zhiyu Hu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can an agent learn a numerical search strategy through executable practice and then transfer that strategy as text? We study low-budget black-box optimization, where unaided language models remain well below strong classical optimizers. During development, an agent repeatedly writes and evaluates optimizer programs. It then distills the resulting program and practice record once into a 197-word primary Harness A, which is frozen before evaluation. Harness A reduces Gemini Flash regret by 48\% in an independent $N=30$ study ($p<.001$), enters the GP-BO performance range on the practice family, and lowers mean regret on all three held-out BBOB landscapes. The same text improves every tested Gemini executor and transfers to Claude Sonnet, reducing regret by 43\% and 49\% ($p\leq.005$). An independent end-to-end replication produces Harness B, a different program and text at the same performance tier. The same framework also attains the lowest regret on a sealed YouTube reward-tuning production benchmark. Executable practice is thus a viable way to discover a search policy, and language a portable medium for deploying it.

---


### 31. [From Fixed Keys to Readable Schemas: Small Language Models for Vehicle Agent Function Calls](https://arxiv.org/abs/2609.09476)

**<font color=#1a73e8>作者：</font>** Hamed Jafarzadeh Asl, Yuanhao Yu, Vahid Partovi Nia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In-vehicle assistants must translate natural-language requests into accurate vehicle function calls under strict memory and latency constraints, making small language models (SLMs) attractive for on-device deployment. For such models, a key design choice is how the available function surface is presented. Two approaches are to represent each function with a dedicated Functional Token (FT) or provide function schemas directly in the prompt. FTs enable compact inference but are restricted to functions learned during training, whereas Schema-in-Prompt (SIP) can generalize to unseen functions at the cost of longer prompts and higher inference overhead. We introduce a benchmark of 9,822 single-turn examples spanning 79 vehicle functions derived from Android Automotive, including held-out functions and requests requiring refusal. We compare both approaches under matched fine-tuning across four SLMs from 270M to 1.7B parameters. On functions seen during training, scaling provides limited benefit: the 270M model can match the 1.7B model, while the strongest overall performance occurs at 0.6B. On held-out functions, FT achieves zero accuracy by construction, whereas SIP generalizes and improves substantially with scale. On out-of-scope requests, FT can invoke an unavailable function it was trained to emit, while SIP more reliably refuses based on the functions offered. This flexibility comes with higher memory use and latency. Our theoretical analysis explains how SIP enables generalization and why longer schema contexts increase inference cost. Overall, function-surface representation, rather than model scale alone, determines the capabilities and failure modes of SLM-based vehicle function calling.

---


### 32. [MotionBlind: Probing the Illusion of Motion Understanding in Video-LLMs](https://arxiv.org/abs/2609.09528)

**<font color=#1a73e8>作者：</font>** Dhairya Bhatia, Bishoy Galoaa, Oliver Fritsche 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video large language models (Video-LLMs) are increasingly used as the perceptual front end of world models, a role that assumes they can read motion: how fast something moves, which way it travels, how hard it is pushed. We show they cannot. A Video-LLM can watch two clips of the same person in the same room, name every object in both, and still fail to say which clip moves faster. We introduce MotionBlind, a contrastive benchmark of self-recorded video for physically grounded motion(speed, magnitude, and direction), the variables a world model must predict. Each instance is a pair of near-identical clips that differ only in motion. Each clip carries two complementary yes/no questions, giving four items per instance, and a model earns credit only if all four are correct. We report Instance Accuracy(IAcc), which has a 6.25% chance floor. Single-frame, appearance, and language-only shortcuts all collapse to it. MotionBlind complements the recent TimeBlind benchmark. We run a controlled study of six open and two frontier Video-LLMs, varying whether the video is present, whether frames are shown in the correct temporal order, and how frames are sampled (1 to 24 frames, four selection strategies). Open models sit near the 6.25% floor, and scale does not help. Removing the video drops every model to zero IAcc, and shuffling frames collapses IAcc to chance, so the task genuinely needs video in order. Neither more frames nor smarter frame selection closes the gap, because these change which frames are seen, not whether motion is read. Only Gemini3.1 Pro clears the benchmark overall, and even it fails on speed. A frontend that cannot tell two speeds of the same action apart is not yet a trustworthy source of supervision, reward, or evaluation for a world model.

---


### 33. [TEFM: Token-Efficient Faithful Modeling for Structured Data](https://arxiv.org/abs/2609.09552)

**<font color=#1a73e8>作者：</font>** Zhichao Hou, Lingdao Sha, Xueyu Mao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we solve two fundamental obstacles in applying LLMs to critical domains: token efficiency and faithfulness. To address both constraints jointly, we present TEFM (Token-Efficient Faithful Modeling), a framework designed for structured data analysis in critical domains. TEFM achieves token efficiency by compressing lengthy structured observations into compact Behavioral Code tokens, dramatically reducing token consumption with minimal information loss. Moreover, TEFM enables faithful rationalization through a dual-fidelity objective that jointly optimizes code-level reconstruction and prediction-level fidelity, identifying minimal sufficient feature subsets grounded in input data. Comprehensive experiments across various domain datasets and model backbones (Qwen3, Gemma-2, Phi-4) show that TEFM achieves competitive classification accuracy with dramatic token reduction (approximately 1\% token retention in clinical and 2\% in security domains) while producing faithful rationales.

---


### 34. [Towards Automatic Evolution Tree Generation from Citation Graphs](https://arxiv.org/abs/2609.09561)

**<font color=#1a73e8>作者：</font>** Zexing Zhao, Yuntong Hu, Liang Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Surveys remain the primary way researchers grasp the lineage of methods within an AI subfield, but they scale poorly against the current rate of publication. Existing taxonomy-induction methods are largely leaf-bound and time-agnostic; they tend to force transitional papers into mature leaves and can create topological inversions between ancestors and descendants. We propose EvoTree, a staged framework that decouples conceptual backbone learning from temporal refinement: a graph-aware encoder with distribution-based hierarchical clustering yields a stable taxonomy backbone; temporal fine-tuning then re-attaches marginal papers to internal nodes under monotonic-path constraints; a final LLM pass labels concepts without altering the topology. We release the first annotated benchmark for this task across 11 AI subfields. EvoTree attains the highest NMI and citation-direction accuracy among all baselines and the best concept purity on the annotated benchmark, and is the only method with non-trivial marginal-paper detection on the annotated set.

---


### 35. [Multi-Agent Agentic Graph Learning via Structural Signatures](https://arxiv.org/abs/2609.09565)

**<font color=#1a73e8>作者：</font>** Liang Qu, Jianxin Li, Hua Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic graph learning (AGL) has recently achieved promising results on graph reasoning tasks, where an agent powered by a large language model (LLM) sequentially samples the graph as evidence to support its final prediction. Existing methods either employ a single agent or orchestrate multiple role-based agents to reason and learn over the entire graph, but both essentially rely on a shared reasoning policy across different graph regions, which can be suboptimal for graphs with heterogeneous structural and semantic patterns. Inspired by the progress of multi-agent collaboration on complex reasoning tasks, a natural remedy is to let multiple agents own different memory and collaborate; however, applying this paradigm to graphs directly faces two challenges. First, existing AGL methods typically verbalize graph structures into natural-language descriptions for LLM agents, making the reasoning process sensitive to the ordering of structural information and thereby breaking the permutation-invariant nature of graphs. Second, incorporating increasingly large sampled neighborhoods leads to rapidly growing contexts. To address these challenges, this paper introduces a multi-agent agentic graph learning (i.e., MAAGL) framework. MAAGL partitions the graph into communities and assigns an independent agent to each community for region-specific specialization. MAAGL represents structural and semantic evidence separately. Structural evidence is summarized by a dynamically updated structural signature that is permutation-invariant and fixed in size, while semantic evidence is filtered to the top-k nodes ranked by relevance. Based on historical trajectories with similar signatures, agents estimate their confidence and trigger debate-style collaboration when needed. Extensive experiments on four benchmark datasets show that MAAGL outperforms SOTA AGL methods.

---


### 36. [Positional task conditioning for scalable defect detection across product families in large product catalogs](https://arxiv.org/abs/2609.09567)

**<font color=#1a73e8>作者：</font>** Soham Satyadharma, Gabriel Roccabruna, Suleiman A. Khan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Product families in large product catalogs suffer from inconsistencies such as duplicates and unit mismatches that degrade customer experience. Detecting these requires reasoning over multiple error types across lengthy product listings, where LLM classification quality degrades due to long-context limitations. We address this by decomposing detection into focused sub-tasks that reduce context and isolate error types, improving F1 from 52\% to 87\%. For scalable deployment, we introduce Positional Task Conditioning (PTC), which distills this capability into a single smaller model by reinforcing task identity at structural prompt boundaries. PTC outperforms rationale-based distillation across five models and two architecture families, achieving within 1.79\% F1 of the frontier at upto 98\% lower cost. Our system is deployed across multiple countries processing 10+ million product families.

---


### 37. [Reproducing Omitted Temporal Expressions in Japanese News for Retrieval-Augmented Applications](https://arxiv.org/abs/2609.09569)

**<font color=#1a73e8>作者：</font>** Tomoaki Yasuda, Shotaro Ishihara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> News articles often contain omitted temporal expressions, such as day-only or month-only mentions, which must be interpreted with reference to the publication date. When such articles are indexed or processed as standalone text in search and retrieval-augmented generation (RAG) systems, these omissions can cause temporal mismatches and unstable interpretation by large language models. We focus on reproducing omitted temporal expressions as concrete dates or intervals using the publication date as external context before the articles are indexed for search and RAG applications. Specifically, building on established temporal-expression extraction and normalization techniques and informed by a manual analysis of Japanese news articles, we propose jaROTE, a rule-based pipeline for Japanese news. Experiments on two news corpora demonstrate that jaROTE achieves high performance, and remains competitive with LLMs while providing a fast, low-cost pipeline. We further show that temporal reproduction improves time-constrained lexical retrieval, demonstrating the practical value of publication-date-grounded normalization for Japanese news retrieval.

---


### 38. [When Ad Networks Misbehave: Understanding Risks of Semi-Drive-By Splash Ads](https://arxiv.org/abs/2609.09574)

**<font color=#1a73e8>作者：</font>** Song Wu, Bo Wang, Yifan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We investigate the mobile splash ads ecosystem, i.e., full-screen advertisements shown at app launch, where monetization relies on interaction signals that are difficult to verify end-to-end. This setting is especially sensitive because incidental touches and sensor-driven callbacks are common yet easy to misattribute as engagement. Prior work has largely framed mobile ad fraud as a publisher-side problem, while some studies attribute fraudulent operations to embedded ad libraries. Yet an important risk remains underexplored: ad SDKs control how interaction signals are interpreted, measured, and reported, creating an opportunity to reinterpret ambiguous user or device signals as valid advertising interactions. We uncover a previously less-known form of fraud at the ad-network layer in which splash ads are triggered not by intentional user actions but by incidental or indirect interactions, which we term semi-drive-by splash ads. By translating non-ad interactions into billable engagement events, ad networks can inflate performance metrics, overcharge advertisers, and erode user trust. To expose this behavior in the wild, we design AdHive, an automated honeypot-like analysis framework that induces evasive splash-ad delivery and landing behaviors under realistic device conditions. AdHive reproduces human-like activity through LLM-generated usage traces and sensor dynamics, enabling execution paths that remain hidden in conventional analysis environments.
Our large-scale measurement across thousands of popular Android applications shows that semi-drive-by splash ads are widespread and are often triggered by subtle signals such as minor sensor variations. We further confirm real-world impact by working with one of China's largest advertisers, identifying multiple ad networks engaging in this fraud and leading to enforced repayments of about 4 million Yuan (approximately US$600,000).

---


### 39. [CityPlanner: A Sandbox Agent for Executable Urban Planning](https://arxiv.org/abs/2609.09578)

**<font color=#1a73e8>作者：</font>** Wentao Zhang, Jingyuan Wang, Zetong Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Urban planning is a real-world spatial optimization problem that requires selecting feasible actions from large candidate spaces under practical objectives such as cost and service quality. Existing optimization and reinforcement learning methods are effective for fixed formulations, but often depend on task-specific representations and constraint handling. We propose \emph{CityPlanner}, a sandbox-agent framework for executable urban planning. CityPlanner introduces \emph{UrbanSandbox}, a unified file-based environment where agents inspect task files, generate plans, run evaluators, and revise decisions based on executable feedback. To make learning tractable, we further propose atomic-task reinforcement learning, which decomposes long sandbox trajectories into \emph{BuildPlan} for initial construction and \emph{ImprovePlan} for feedback-based refinement. Experiments on a real-world benchmark show that CityPlanner consistently outperforms heuristic, task-specific RL, and general LLM-agent baselines. Ablations verify the contributions of UrbanSandbox, atomic-task RL, and iterative deployment. We release the code and dataset at this https URL

---


### 40. [From State Synchronization to Cognitive Self-Evolution: An Operational Architecture for Cognitive Digital Twins](https://arxiv.org/abs/2609.09625)

**<font color=#1a73e8>作者：</font>** Haoran Gao, An Li, Zhen Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Digital Twin (DT) systems evolve beyond state synchronization toward task-oriented and knowledge-driven operation, Cognitive Digital Twins (CDTs) have emerged as an extension that incorporates cognitive capabilities into twin operation. Existing CDT studies often focus on specific enabling techniques, such as learning modules, knowledge graphs, and large language models, while providing limited insight into how cognition can be systematically integrated into DT architectures. To address this issue, this paper proposes a four-layer CDT architecture consisting of the physical layer, digital-twin layer, cognitive layer, and task layer. The proposed architecture establishes a self-evolving closed operational loop spanning these four layers, in which physical states are synchronized into digital representations, cognition constructs task-specific cognitive models through knowledge, memory, and attention, and task-level decisions are generated under practical constraints. Operational feedback further refines cognitive experience and updates relationships and annotations in the digital representation, enabling subsequent task interpretation, initiation, and reasoning to evolve with system operation. Based on this framework, two representative operation modes are characterized: user-request-driven cognition and self-driven cognition. We further discuss key enabling mechanisms and deployment challenges associated with semantic communication, knowledge querying, task orchestration, and closed-loop synchronization. A lightweight simulation study illustrates reliable closed-loop task feasibility under limited semantic information and improved operational efficiency through accumulated task experience. The proposed framework provides a structured foundation for the design and development of future CDT systems.

---


### 41. [Who Are They to Each Other? Multi-Agent Reasoning for Speaker Relationship Inference](https://arxiv.org/abs/2609.09628)

**<font color=#1a73e8>作者：</font>** Yaohan Guan, Yen-Ju Lu, Yuzhe Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Inferring speaker relationships from spoken conversations is an important step towards socially aware speech understanding. However, this task remains underexplored, and supervised modeling is costly to train and scale. At the same time, existing inference-time LLM approaches provide limited structure for handling subtle, distributed, and multimodal relational cues that may support multiple plausible interpretations. To address these limitations, we introduce a training-free multi-agent reasoning framework that organizes inference through structured interaction among LLM agents, allowing relationship judgments to be proposed, challenged, and adjudicated without task-specific training. We instantiate this framework with two complementary designs. We propose Multi-Role Multi-Agent Debate as a task-specific adaptation of standard multi-agent debate for speaker relationship inference, assigning agents complementary roles or social-theory-grounded perspectives rather than a single undifferentiated viewpoint. In contrast, we introduce Multi-Agent Compete, a competition-based protocol that compares agent judgments through pairwise adjudication, eliminates weaker candidates, and retains the most defensible one. We evaluate these methods on the Seamless Interaction dataset across different modality settings, covering both binary classification and fine-grained relationship-detail prediction. Results suggest that they improve over zero-shot and existing multi-agent baselines in most cases. Human evaluation further suggests that this task is challenging even for people. LLM methods can sometimes outperform human annotators in text-included settings but are less competitive in the audio setting. Together, these findings suggest that relationship inference benefits from structured inference-time interaction among agents, while acoustic cues are not yet fully captured by current models.

---


### 42. [RESCUE-BENCH: Towards Relation-Aware Multi-Party Emotional Support Conversation Systems](https://arxiv.org/abs/2609.09657)

**<font color=#1a73e8>作者：</font>** Haichuan Hu, Yang Xiao, Mingni Tang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing emotional support conversation systems mainly focus on one-on-one seeker-supporter interactions and individual emotional states, leaving interpersonal relations in multi-party scenarios underexplored. In this work, we introduce relation-aware emotional support conversation, a new task that evaluates whether LLMs can capture and utilize the evolving dynamics of relationships to offer more effective emotional support. We construct RESCUE (Relation-aware Emotional Support Conversation Understanding and Evaluation Benchmark) from real couple and family interview conversations, containing 191 samples, 7,079 annotated turns, and 1,064.8 minutes of video. Based on rich annotations of socio-emotional and support-related dynamics, RESCUE defines six tasks that evaluate two core capabilities required for relation-aware emotional support: Relational Understanding and Relation-Sensitive Support. Experiments with ten LLMs show that current models perform relatively well on tasks relying on local emotional or intervention cues, but struggle with relation-intensive tasks such as relation pattern prediction, viewpoint prediction, and support strategy prediction. These findings reveal the limitations of current LLMs in modeling interpersonal relations and making relation-sensitive support decisions.

---


### 43. [PELM: Power Efficient On-Device LLM Inference with Speculative Decoding and Dynamic Voltage Frequency Scaling](https://arxiv.org/abs/2609.09662)

**<font color=#1a73e8>作者：</font>** Weisi Yang, Stephen Xia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying Large Language Models (LLMs) directly on mobile platforms at the edge is gaining traction due to a myriad of benefits, such as increased privacy, personalization, and reduced latency. However, LLMs have heavy computational requirements, which are difficult for resource-constrained mobile and edge platforms to fulfill. In addition to limited compute resources, mobile and edge systems often have a compact form factor and lack physical mechanisms to dissipate heat generated from high processor usage rates (e.g., fans) to prevent throttling and reduced processing power, which LLMs can easily cause. To mitigate these effects, prior works have proposed various power governing strategies, such as dynamic voltage and frequency scaling (DVFS), for reducing power and heat generation for heavy computational tasks on mobile platforms. Recently, DVFS methods tailored for mobile LLMs have also been proposed. However, these methods mostly focus on optimizing hardware parameters and processor frequencies, and they fall short under some thermally constrained scenarios. Drawing from recent advances in machine learning, we identify and take advantage of the key insight that not all tokens require full-depth inference to maintain high-quality generation. Motivated by this, we present PELM, a solution that augments traditional DVFS processor frequency tuning with two additional workload-specific knobs: 1) speculative decoding and 2) variable verification depth to expand the optimization space to multiple dimensions for more power efficient on-device LLM inference. In extensive evaluations across hardware platforms and datasets, PELM demonstrates superior performance compared to state-of-the-art power governing methods, with up to 23.1% speedup and 52.4% reduction in energy consumption, while maintaining comparable task performance. The source code is available at this https URL.

---


### 44. [PRAGMA: Evaluating Personalized Guidance with Memory Alignment in Lifelong Conversations](https://arxiv.org/abs/2609.09664)

**<font color=#1a73e8>作者：</font>** Hyojeong Yu, Hyukhun Koh, Minsung Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as personalized assistants that interact with users over extended periods of time. As conversations grow longer, relying on full interaction histories becomes increasingly inefficient and unreliable: long contexts introduce substantial computational overhead, making it difficult for models to consistently identify and utilize the most relevant information for the current request. These challenges have motivated memory systems that structure and retrieve user-specific information. In realistic interactions, users often seek practical guidance such as recommendations, planning, and decision support. Unlike factual recall tasks, personalized guidance requires models to integrate information across multiple past conversations and reason about changing user preferences and experiences. However, existing conversational memory evaluations mainly focus on retrieval and factual recall. To study this challenge, we introduce PRAGMA, a benchmark for evaluating personalized guidance in long-term conversations. PRGAMA contains curated longitudinal conversation histories, evidence annotations, and guidance scenarios grounded in evolving user contexts and incorrect user assumptions. Experiments across retrieval systems, memory systems, and long-context models reveal that current systems struggle both to recover the appropriate conversational evidence and to effectively use it for personalized guidance. Our results highlight the need for memory architectures that support robust conversational retrieval and memory-grounded reasoning beyond evidence recall.

---


### 45. [SEA-SpeechBench: A Large-Scale Multitask Benchmark for Speech Understanding Across Southeast Asia](https://arxiv.org/abs/2609.09672)

**<font color=#1a73e8>作者：</font>** Jingyi Liao, Wenyu Zhang, Zhuohan Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of audio and multimodal large language models has unlocked transformative speech understanding capabilities, yet evaluation frameworks remain predominantly English-centric, leaving Southeast Asian (SEA) languages critically underrepresented. We introduce SEA-SpeechBench, to the best of our knowledge, the first large-scale multitask benchmark that evaluates speech understanding in 11 SEA languages through 97,194 samples across 99 evaluation sets and 597 hours of curated audio data. Our benchmark comprises 9 diverse tasks across 3 categories: speech processing (automatic speech recognition, speech translation, spoken question answering), paralinguistic analysis (emotion, gender, age, speaker recognition), and temporal understanding, a novel dimension featuring timestamped content queries and temporal localization within extended audio sequences up to 3 minutes. We implement multilingual prompting in both native SEA languages and English to reflect user interactions with audio-language models. Evaluation of leading open-source and proprietary systems reveals marked performance gaps. Across all models, performance remains underwhelming on temporal understanding, emotion recognition, and speech translation. Prompting in low-resource languages such as Burmese and Tamil lags behind English by up to 41 percentage points. Our findings expose critical model limitations and underscore the need for inclusive model development. The SEA-SpeechBench benchmark is available at this https URL.

---


### 46. [X2-NativeCursor: Native-Token Text Progress Tracking for Incremental-Text Streaming Codec TTS](https://arxiv.org/abs/2609.09677)

**<font color=#1a73e8>作者：</font>** Zehan Liu, Carl Chen, Rime Wen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Incremental-text streaming text-to-speech (TTS) needs online text progress tracking for synchronized highlighting, interruption handling, and dialogue-history updates. Input text arrives before it is spoken, so text arrival alone cannot indicate speech progress. Existing waveform-based alignment requires complete audio or adds acoustic processing during streaming. We propose X2-NativeCursor, a lightweight observer that tracks progress from native speech tokens before waveform decoding without changing the TTS generator. Its normalization plan links spoken labels to their original-text spans. Text and native-token encoders feed a local matcher that estimates the current label position. A separate output rule converts revisable position estimates into a cursor that never moves backward. Mean absolute error against an automatic reference is 0.151 Chinese characters with 80-ms lookahead, versus 1.253 characters with 320-ms lookahead for an online waveform baseline. Alignment real-time factor also decreases from 0.3598 to 0.0180 relative to this baseline. Lower tracking error is retained under a second automatic alignment reference. We evaluate X2-NativeCursor on Qwen3-TTS and validate its adaptation to CosyVoice2 by training a separate observer for each backbone. Code is publicly available at this https URL.

---


### 47. [Looped GPT-BERT: Trading Parameters for Computation in Small Language Modeling](https://arxiv.org/abs/2609.09691)

**<font color=#1a73e8>作者：</font>** Tingshuo Fan, Hongtao Mu, Tianyu Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When training data are limited, increasing parameter count is not the only way to improve language-model performance. A small parameter set, when repeatedly applied, can also deliver comparable performance. We study Looped GPT-BERT in the BabyLM 2026 Strict-small setting, combining GPT-BERT's masked next-token and causal language-modeling objectives with depth-wise parameter sharing. We train on a preprocessed 7.48M-word English corpus and compare objective ratios, non-looped and looped architectures, and loop counts. Our final $4\times12$ model uses four physical layers for twelve recurrent traversals and contains 12.18M parameters. The BabyLM 2026 leaderboard reports an Overall Average of 35.42 and an NLP Average of 48.48. Compared with public BabyLM 10M Strict-small GPT-2 and GPT-BERT baselines, it achieves comparable performance on selected linguistic and downstream metrics, including BLiMP and GLUE, with fewer parameters. The loop ablations show that additional recurrent computation can improve training and preserve strong performance on selected linguistic tasks, whereas poorer performance on other tasks may reveal an inherent limitation of the looped design: using only a few physical layers restricts the model's representational space.

---


### 48. [When Auditors Fabricate: Batch-Size Degradation and Confident Hallucination in LLM Detection of Planted Document Contamination](https://arxiv.org/abs/2609.09696)

**<font color=#1a73e8>作者：</font>** Karan Parekh, Sanjana Pendyala Ravinder, Sana Mhapsekar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly proposed as automated auditors of document quality, yet their reliability as detectors of planted errors is poorly characterised. We construct a contaminated corpus of 150 academic papers spanning supply chain management and medical research, injecting 450 known contaminants of three types: typographical corruption, semantic reversal, and absurd out-of-context insertion. We then evaluate Google Gemini 3.0 Pro's ability to recover a 180-contaminant answer-key subset across 60 documents under three prompting regimes of increasing scale: single document, small batch, and large batch. Detection holds at small scale and then collapses: 50% recovery on single documents, 60% on small batches, and 2.8% on large batches. The failure mode at scale is not abstention but fabrication. Rather than reporting incomplete processing, the model produced confident findings including invented contaminants of its own, absurdities such as "telepathic squirrel" and "quantum-powered toaster" that mimic the style of the planted material but do not appear in any document. Detection also varies by contamination type: absurd insertions were recovered at 75% in completed evaluations, while semantic reversals and typographical corruptions were each recovered at only 50%. The corruptions most likely to occur in the wild, plausible ones, are the ones most often missed. We conclude that LLM document auditing degrades not gracefully but deceptively, and outline the harness such systems require: bounded batch sizes, direct content injection, and mechanical verification of every reported finding against source text.

---


### 49. [PrivAudit: A Dual-Lens Auditing Framework for Website Privacy Practices under the CCPA](https://arxiv.org/abs/2609.09697)

**<font color=#1a73e8>作者：</font>** Mohamed Moustafa Dawoud, Riya Aggarwal, Likith Rahul Krishnamurthy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Five years after the enforcement of the California Consumer Privacy Act (CCPA), understanding how website privacy practices evolve at scale in response to regulation remains a key challenge for both researchers and regulators. Prior work and regulatory efforts have focused on manual and case-specific enforcement, but there remain no scalable approaches to systematically audit two key user-facing facets of websites that are crucial signals for the CCPA: privacy disclosures and front-end user tracking behavior.
In this paper, we present PrivAudit, an automated auditing framework that adopts a dual-lens approach to capture: (1) privacy disclosures through large language model-based analysis of privacy policies grounded in CCPA provisions, and (2) user-observable data collection behavior through automated browser measurements of cookie writes under diverse privacy configurations. We apply PrivAudit to 998 websites and report two broad findings. The law is associated with stronger privacy disclosures: CCPA-subject policies are more likely to disclose opt-out mechanisms, data-sharing practices, and user rights. On the other hand, cookie-based tracking remains pervasive, with both CCPA-subject and not-subject websites setting a total of 6,392 targeting cookies, 49% of which are third-party writes. Moreover, cookies show limited-to-moderate responsiveness to privacy signals and consent choices, even when websites claim to honor them in their disclosures.
Our results highlight the need for multi-layered and scalable auditing approaches that combine policy analysis with behavioral evidence. PrivAudit can support these auditing workflows at scale by generating actionable signals and patterns for further manual review. We open-source PrivAudit and are engaging with regulators to support auditing in practice.

---


### 50. [Which Tokens Should SFT Actually Learn? A Token-Trimming Perspective on Mathematical Reasoning](https://arxiv.org/abs/2609.09707)

**<font color=#1a73e8>作者：</font>** Yaning Jia, Chunhui Zhang, Wenxuan Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) applies a uniform cross-entropy loss to all target tokens, even though different tokens provide unequal learning signals for mathematical reasoning. This uniform treatment can over-sharpen already mastered tokens while amplifying learning pressure on uncertain, low-confidence tokens, leading to suboptimal training dynamics. We propose Trimmed Logit-Gap SFT (TrimSFT), a simple token-level reweighting method that scales the SFT loss according to the logit gap between the gold token and its strongest competitor. TrimSFT trims supervision away from both extremes: tokens already mastered (large logit gap) and tokens weakly supported by the current model (small or negative logit gap), concentrating learning within an intermediate logit-gap region between them. We instantiate this principle with a Gaussian weight centered at margin m with bandwidth {\tau}, requiring no reference model or additional forward pass. We evaluate TrimSFT on six base models from the Llama, Qwen, and DeepMath families across five mathematical reasoning benchmarks. TrimSFT consistently improves over standard SFT, achieving the best average performance on five out of six models, with gains of up to +26.9 points over SFT on MATH500. Further analyses show that the bandwidth {\tau} matters more than the exact margin location, and that half-trim variants that remove supervision pressure from only one side yield inferior trade-offs. A token-level logit-gap distribution analysis suggests that TrimSFT reshapes model confidence in a more balanced way than uniform SFT or monotonic reweighting methods. These results suggest that reasoning SFT can benefit from trimming both extremes rather than treating all tokens uniformly.

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-148](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
