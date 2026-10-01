# 🧠 大模型相关研究 | 2026年10月02日

> 本类共 **390** 篇论文：已确认 **371** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-390](./part-08.md)

---

### 251. [ActionGuard: Tool Call Authorization under Poisoned Skills](https://arxiv.org/abs/2609.39450)

**<font color=#1a73e8>作者：</font>** Jihun Han, Yejin Jang, Byung Il Kwak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based agents extend their capabilities through third-party skills that provide task-specific instructions, scripts, and tool-use procedures. However, malicious instructions inserted into an otherwise benign skill can cause a benign user request to trigger dangerous Tool Calls, including data exfiltration, file deletion, or unauthorized code execution. This paper presents ActionGuard, which inspects skill-influenced Tool Calls immediately before execution. ActionGuard separates the target agent's action-generation context from the safeguard's authorization context. The target agent may use the original skill for planning, but the Reviewer does not receive the potentially poisoned raw skill text. Instead, it determines whether each action is justified by the trusted user request using a balanced skill profile, current and recent Tool Calls, and local script contents. ActionGuard intercepts each Tool Call at OpenClaw's before-tool-call stage and enforces the Reviewer's ALLOW or DENY decision under a fail-closed policy.
We evaluate ActionGuard on 139 contextual and 180 obvious injections in a SKILL-INJECT-based setting against Dynamic Guardian and SkillGuard, using three open-source and two commercial Reviewer models. Each condition is repeated three times and evaluated using Attack Success Rate (ASR) and Task Success Rate (TSR). Overall, ActionGuard reduced ASR by 35.54 to 46.11 percent relative to existing safeguards and by 70.44 percent relative to No Safeguard, while maintaining high benign-task completion. These results show that execution-boundary authorization grounded in trusted user intent and runtime evidence can restrict unauthorized Tool Calls induced by skill injection.

---


### 252. [Also Small Models Can Reasonably Self-Evaluate Their Confidence](https://arxiv.org/abs/2609.39478)

**<font color=#1a73e8>作者：</font>** Idil Kapikiran, Thomas Decker, Thomas Runkler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study systematically evaluates self-evaluation-based uncertainty quantification across different language models of varying sizes on question-answering tasks spanning general to specialized knowledge domains. Using various self-evaluation methods where models judge their own predictions, we examine how model scale and domain specificity affect the quality of self-assessed confidence signals. Our results reveal that while accuracy predictably declines with smaller models and more specialized domains, the reliability of self-evaluated confidence remains largely stable across both dimensions. This independence means the most capable model is not necessarily the best at self-assessing prediction reliability. These findings suggest that smaller models can achieve reasonable self-assessed confidence despite lower accuracy, making them viable for resource-constrained deployments.

---


### 253. [Who Owns That? Evaluating Ownership Intuitions in Large Language Models](https://arxiv.org/abs/2609.39483)

**<font color=#1a73e8>作者：</font>** Xizhi Xiao, Yue Wu, Shan Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ownership establishes rights over the use, control, and transfer of objects. Understanding these relations is essential for AI systems to interact appropriately with people and their resources. Yet how large language models (LLMs) attribute ownership under competing claims remains unclear. We introduce the Competing Ownership Attribution Task (COAT), comprising 42 scenarios, and compare ownership allocations from 24 LLM configurations with those of 108 human participants. Overall, human-model similarity is close to human-human similarity, but models show greater homogeneity in their ownership judgments. Within individual answers, models also divide ownership more evenly among claimants than humans do. Pooling responses across model configurations reveals more scenarios with a shared judgment and fewer with distinct viewpoint groups than in humans. When humans form distinct groups, models may converge on one viewpoint or between competing viewpoints. Further comparisons reveal different contextual sensitivities. As material value increases across scenarios, allocations to creators decline less sharply in models than in humans. Across scenarios differing in public recognition of later holders as owners, allocations to these holders increase in models but decrease slightly in humans. Together, these findings suggest that the evaluated LLM responses do not fully capture the diversity of participants' ownership judgments or how those judgments vary across situations. Developing socially capable AI therefore requires moving beyond overall similarity to capture the diversity and context dependence of human judgments.

---


### 254. [OmniReasoning: Pushing the Limits of Audio-Visual Joint Reasoning](https://arxiv.org/abs/2609.39490)

**<font color=#1a73e8>作者：</font>** Junming Lin, Yuxuan Wang, Zhenxin Lei 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances have enabled unified omni-modal models in understanding audio, vision, and language. However, existing benchmarks, training data, and learning methods largely treat the modalities independently, leaving the capability of audio-visual joint reasoning poorly evaluated and insufficiently elicited. We address this gap with a benchmark, data engine, and learning method. First, we introduce OmniReasoningBench, a benchmark where both audio and visual evidence are indispensable. It comprises 1,150 multiple-choice and open-ended questions across two tasks, reasoning over video and reasoning beyond video. Second, we develop a data engine OmniQA. It automatically constructs evidence-grounded QA pairs that explicitly necessitate audio-visual joint reasoning, together with time-stamped clue chains that guide the annotation of thinking process. Besides our benchmark, this engine produces training data OmniReasoning-SFT-112K and OmniReasoning-RL-19K. Finally, we propose an on-policy self-distillation method Modality-Factored Self-Distillation (MFSD). It evaluates each sampled response under modality-specific clue contexts, disentangling the contributions of individual clues and their cross-modal interactions for token-level credit assignment. With our training data and learning method, our model OmniReasoning-30B-A3B achieves 50.0% on OmniVideoBench and 42.5% on OmniReasoningBench, improving the base model Qwen3-Omni-30B-A3B-Thinking by 12.8 and 9.3 percentage points, respectively. Moreover, it delivers substantial gains on general and long-video benchmarks, including Video-MME-v2. We hope our work offers a solid step for facilitating future research in omni-modal joint reasoning.

---


### 255. [Front-to-Back: Benchmarking Vision-Language Models for Asymmetric Cross-View Vehicle Re-Identification](https://arxiv.org/abs/2609.39492)

**<font color=#1a73e8>作者：</font>** Moseli Mots'oehli, Thulani Babeli  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Matching the same vehicle across front and rear cameras is difficult because the cameras do not share a view and the vehicle's appearance changes substantially. We introduce Front2Back-ReID, a benchmark of 500 manually verified vehicle handovers from 20 recording sequences in South Africa. Each example asks a model to match a vehicle highlighted in a front-camera image to the same vehicle among at least three candidates in a later rear-camera image. We evaluate seven zero-shot vision-language models, four image-retrieval baselines, and 25 human participants. Models are tested using full front RGB images, cropped target vehicles, and binary silhouettes. The strongest VLM achieved 76.6 percent Rank-1 accuracy on target crops, compared with 74.0 percent for the frozen SigLIP2 baseline; this difference was not statistically clear. Human participants achieved 94.0 percent accuracy with full images and 92.2 percent with target crops. Under our evaluation setup, enabling reasoning improved accuracy across all three input conditions for every model evaluated in both modes. We also found that VLMs generally performed worse on full scenes than on target crops. These results show that general-purpose VLMs do not yet consistently outperform strong visual retrieval for front-to-rear vehicle matching, while humans remain substantially more reliable.

---


### 256. [Disentangling Self-Distillation: Measuring and Modeling Acquisition and Retention](https://arxiv.org/abs/2609.39494)

**<font color=#1a73e8>作者：</font>** Luis Zuin, Alexis Huet, Dario Rossi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-distillation with privileged context adapts a language model from demonstrations by letting the model, once conditioned on a reference response, teach its context-free copy token by token. Our taxonomy reveals existing methods differ along three entangled axes: (i) the rollout source (student or teacher), (ii) the teacher coupling (frozen, or an exponential moving average of the student at some coupling rate) and (iii) the KL direction (reverse or forward), yet these axes are usually studied in fixed combinations and have led to conflicting conclusions. We formalize a unifying framework to encompass all self-distillation methods vs classic supervised fine-tuning: we train every combination of the three axes, on Qwen2.5-7B and Ministral-3-3B across ordinary and contradictory tasks, totaling 1,200 adaptation runs, to systematically investigate the impact of the above axes. We propose a controlled model of the same objective to explain the resulting acquisition-retention trade-offs. We find that (i) the rollout source matters mostly where the task contradicts the pretrained behavior: there teacher rollouts raise acquisition well above what student rollouts achieve, with almost no change in retention; (ii) the teacher coupling changes acquisition most, on every task: acquisition rises with the coupling rate, then falls past a task-specific rate; (iii) switching the KL direction costs retention in one model but not the other so which axis to tune first depends on the model. The controlled model reproduces the three trends.

---


### 257. [When the Right Answer Is Missing: An Arithmetic-Dependent Rejection Bottleneck in Jev](https://arxiv.org/abs/2609.39496)

**<font color=#1a73e8>作者：</font>** Jike Zhong, Ming Li, Yuxiang Lai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Typed decision models such as Jev offer an efficient alternative to generative LLMs in decision-making workflows by selecting directly from predefined options. When candidate sets contain no valid answer, TypeSafe recommends including an "other" or "none-of-the-above" option to enable rejection. In this report, however, we identify an arithmetic-dependent rejection bottleneck: Jev reliably selects correct numerical answers when available but frequently accepts incorrect alternatives when they are absent despite an explicit rejection option. On paired arithmetic problems, answer-present accuracy reaches 99%, while correct rejection falls to 7%. Moreover, this gap persists across numerical magnitudes, operation depths, contextual formulations, and rejection labels, and extends to scenarios such as time calculation and capacity rounding. Yet native Boolean verification achieves 99% exact-match accuracy on the same answer-absent arithmetic cases, showing that categorical rejection can fail even when the model successfully verifies candidate correctness. Finally, we show that a simple decision threshold selected on separate development problems raises arithmetic rejection accuracy from 7% to 79% while retaining 97% answer-present accuracy, substantially mitigating the failure without retraining or additional inference.

---


### 258. [Spike-driven Vision-Language-Action Model](https://arxiv.org/abs/2609.39514)

**<font color=#1a73e8>作者：</font>** Shuai Wang, Malu Zhang, Mingquan Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models bridge multimodal understanding and robotic control, advancing the dominant paradigm for embodied intelligence. However, most existing models rely on large Transformers, whose latency and energy costs hinder deployment on resource-constrained platforms. Through sparse event-driven computation, spiking neural networks offer a promising paradigm for high-performance and energy-efficient computing. Here, we propose the first Spike-driven VLA framework enabling end-to-end direct training for robotic manipulation, which mainly comprises three core components. First, we develop spiking visual and instruction encoders for multimodal perception, encoding visual observations and language instructions into sparse, reliable spike representations for subsequent cross-modal fusion. Then, we introduce Multi-Winner Spike Fusion for instruction-guided scene understanding, using bidirectional top-$k$ winner-take-all spike routing to suppress background interference and yield fused memory. Finally, we propose a Spike Action Chunking Transformer that incorporates spiking cross-attention over the fused memory and the current robot state, enabling efficient end-to-end generation of continuous action chunks for robotic control. Extensive experiments on LIBERO and Meta-World demonstrate that Spike-driven VLA achieves competitive performance with fewer parameters and lower estimated inference energy than conventional VLA models. This work establishes a foundational framework for neuromorphic VLA modeling, paving the way for future advances in resource-efficient embodied intelligence.

---


### 259. [Referential Uncertainty in Human--AI Collaboration](https://arxiv.org/abs/2609.39518)

**<font color=#1a73e8>作者：</font>** Christian Poelitz, Finale Doshi-Velez, Siân Lindley  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Effective human-AI collaboration requires partners to establish references through interaction, which becomes fragile when descriptions are ambiguous, similar referents compete, or partners see different things. We study referential uncertainty - uncertainty over which candidate object a description refers to - in a collaborative puzzle task where a human Helper instructs an AI Worker to place pieces. The Worker must identify and communicate its uncertainty, and the Helper must recognize and act on it. We show that a separately elicited belief distribution over candidate pieces is better calibrated (ECE 0.15) and better discriminates correct from incorrect placements (AUROC 0.65) than raw action-token probabilities, which are severely overconfident (0.97 mean confidence, ECE 0.44). Across three frontier vision-language models (GPT-4.1, GPT-5, GPT-5.5), this elicited uncertainty rises predictably with instruction vagueness, but not with competing referents in context, even when those increase errors. The models seldom externalize it, asking for clarification on only 3.5-16.7% of turns. In a controlled human study (N=210), participants given only the Worker's default message accept 78% of wrong placements and cannot tell right from wrong (AUC 0.50). Precise descriptions and, especially, well-targeted hedges cut wrong-move acceptance to 36% while largely preserving correct-move acceptance, compensating for missing shared awareness such as not seeing the Worker's action. But this benefit depends on targeting: a deployable hedge derived from the model's own belief entropy inherits that signal's weakness and can do more harm than good. Externalized uncertainty helps a human partner only when it is accurately targeted.

---


### 260. [CATCH: A Controllable Analysis Testbed for Reward Hacking in Coding RL](https://arxiv.org/abs/2609.39533)

**<font color=#1a73e8>作者：</font>** Shouli Wang, Yanfeng Jia, Zhihao Ou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> During reinforcement learning with verifiable rewards (RLVR), large language models (LLMs) can exploit loopholes in their environments to obtain high rewards without improving the intended capabilities, i.e., reward hacking. Despite its risks to training efficiency and safety, monitoring and mitigating reward hacking during training remain challenging, which is limited by a lack of testbeds that reproduce hacking and reliably identify it. We introduce CATCH, a controllable testbed for studying reward hacking in coding RL. CATCH deliberately exposes environmental loopholes and provides execution-based gold labels by comparing success under a vulnerable evaluator with task correctness under an independent audit. It also can control the model's initial hacking tendency through supervised fine-tuning data mixtures and the difficulty of earning rewards through reward designing, enabling systematic comparisons of hacking dynamics and interventions. Experiments show that CATCH can produce diverse RL training trajectories with clear reward hacking, and analyses demonstrate that both initial models and reward difficulties shape the emergence of reward hacking. We further evaluate the effectiveness of different reward hacking detection and mitigation methods. A key finding is that a chain-of-thought monitor initially suppresses hacking, but this protection erodes as the policy model learn to mislead the monitor with code comments. This highlights the need to evaluate hacking mitigations throughout training with CATCH. The source code and resources are publicly released at this https URL.

---


### 261. [Comparative study of adapting pre-trained models for driving behavior video captioning](https://arxiv.org/abs/2609.39542)

**<font color=#1a73e8>作者：</font>** Sayak Mallick, Philipp Geiger, Augustin Kelava  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This report examines and compares some of the many fine tuning and prompting methods existing, applying them within the domain of autonomous driving. The idea is to compare these methods by adapting a Large Language Model (LLM) on a video dataset. LLM's have become extremely good at achieving a good understanding of different forms of data and this study aims to induce a low dimensional understanding of driving situations into our primary test model SpaceTimeGPT. Experiments on BDD-X (Berkeley DeepDrive eXplanation) dataset demonstrate good performance of the full fine tuning framework on some automatic metrics, and in some metrics, it even surpasses the baseline. We also try Low-Rank Adaptation (LoRA) and prompt engineering on VideoLLaVA model and discuss its limitations.

---


### 262. [Learning Reliable GUI Agents under Imperfect Priors](https://arxiv.org/abs/2609.39547)

**<font color=#1a73e8>作者：</font>** Bo Han, Qianyi Wang, Shuai Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> GUI agents built on large language and vision-language models still struggle on unseen applications and complex multi-step tasks, as completing real GUI tasks depends on app-specific, temporally volatile operational knowledge that is scarce in pretraining corpora. Retrieval-augmented execution offers a natural remedy but faces two coupled bottlenecks: knowledge at scale is hard to acquire, and self-collected priors inevitably drift from the live environment due to version updates, promotions, ads, A/B tests, and personalization. We therefore argue that GUI agents should not pursue perfect knowledge but learn to act correctly under imperfect priors, and propose our framework that couples knowledge acquisition with noise-robust utilization: a structured exploration strategy traverses interactive elements, builds a UI state-transition graph, and synthesizes (task, trajectory) pairs via a VLM without human annotation; a noise-aware training strategy, grounded in a taxonomy of real GUI drift patterns, injects five types of realistic errors into self-explored trajectories to teach the agent to assess prior reliability before acting. Experiments on physical devices and online emulator benchmarks show that our method discovers more unique screens, covers more benchmark tasks, and more effectively rejects erroneous priors while leveraging correct ones, with accuracy gains that transfer across datasets.

---


### 263. [Speculative Safety Honeypot: Toward Proactive Defense Against Multi-turn Agent Attacks](https://arxiv.org/abs/2609.39549)

**<font color=#1a73e8>作者：</font>** Zezhong Wang, Xueyang Tang, Rui Lian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As Large Language Model (LLM) agents are increasingly deployed in complex environments, multi-turn interaction attacks have become a significant security challenge. Existing detection methods typically rely on historical context. However, this retrospective logic struggles to identify deep malicious intents that are split across turns to hide future risks. Inspired by speculative decoding, we propose the Speculative Safety Honeypot (SSH) framework. SSH uses a multi-agent simulation system composed of small LLMs to build an action-level speculate-and-verify workflow. In the speculation stage, SSH predicts future behaviors of the target agent and asynchronously builds a trajectory tree to expose potential risks in advance. In the verification stage, the system uses the target agent's real actions to calibrate and prune the trajectory tree, effectively reducing false positives. As a plug-and-playable component, SSH provides existing detectors with rich decision redundancy beyond the current interaction slice. By judging risk based on the evolution of the entire trajectory tree rather than a single point in time, the system reduces the reliance on the absolute precision of individual detection components. This improves the defense resilience and the warning lead-time of agent systems against complex temporal attacks.

---


### 264. [RankEvolve: A Reliable Multi-Agent Auto-Research Harness for Evolving Ranking Models](https://arxiv.org/abs/2609.39551)

**<font color=#1a73e8>作者：</font>** Zheng Chen, Linfeng Liu, Hong Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Auto-research agents, LLM systems that propose, implement, train, and evaluate model changes across iterations, promise to automate applied ML's experimental loop. Over long horizons, execution accuracy is a binding constraint: a change can silently leak held-out data, omit normalization, disconnect a gradient, or leave a train/eval flag unwired, invalidating expensive runs and compounding error across iterations. We present RankEvolve, an auto-research framework for evolving generative ranking models. An Executable Operating Protocol (EOP) declares phases, gates, branches, and loops, and the runtime enforces the compiled state machine. A meta-meta-harness composes complete black-box coding-agent products, including Claude Code and Codex, as execution-graph nodes that review and repair one another's work. In a budget-matched evaluation, heterogeneous composition raises all-oracle execution accuracy from the best single-product baseline of 45.8 percent to 62.5 percent (paired +16.7 points, 95 percent CI [6.6, 26.7]) while achieving a 10.4 percent silent critical-defect rate. An implemented knowledge layer carries findings, including negative results, across iterations. In a twelve-iteration deployment on the open-source HSTU recommender, RankEvolve reported NDCG@10 of 0.2192 on MovieLens-20M LARGE (+4.48 percent over the published anchor) and 0.1948 on BASE (+2.80 percent). ExecML-HSTU, seeded by incidents from that deployment, provides the oracle benchmark for the execution-accuracy evaluation. A pre-specified LitGPT transfer split replicates the heterogeneous-composition effect beyond recommendation (+12.5 points, 95 percent CI [3.0, 22.0]), and a paired ablation isolates per-step from full-protocol instruction injection. These results characterize when runtime-controlled composition of coding-agent products improves execution accuracy.

---


### 265. [Self-Repulsive Sampling for Diffusion Language Models](https://arxiv.org/abs/2609.39560)

**<font color=#1a73e8>作者：</font>** Michael Helcig, Martin Jaggi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sampling several responses and voting over their answers can improve a language model's accuracy, but repeated answers limit the benefit of additional samples. Raising temperature increases diversity at a potential cost to per-sample accuracy. We introduce Self-Repulsion (SR), a sampler for masked diffusion language models that uses peer commitments to diversify the pool. At each penalized denoising step, each path lowers a token's logit according to how many peers have committed that token at the same position. Paths share a batched forward pass and then commit in sequence, so later paths observe choices made earlier in the same step. This coupling requires no training or additional forward or backward pass and can produce distinct paths even at temperature zero. When all paths commit a position together from identical logits, the update exactly maximizes total logit minus a convex duplication cost. On LLaDA-8B-Instruct with ten paths and 128 denoising steps, deterministic SR reaches 80.38% plurality accuracy on GSM8K, compared with 70.17% for the unpenalized greedy decoder. At temperature 0.6 and matched model-evaluation budgets, the count penalty improves over self-consistency by 2.06 percentage points in blocks of 32 and 14.50 under pure diffusion. Experiments on GSM8K, MATH and TruthfulQA show that voting gains arise mainly from higher coverage of correct answers, with gains that vary by benchmark and decoding regime.

---


### 266. [RESUME: Recurrent State Updates from Motion and Residual Signals for Efficient Video Language Modeling](https://arxiv.org/abs/2609.39563)

**<font color=#1a73e8>作者：</font>** Can Zhang, Xiaotian Han, Junyuan Shang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing video language models encode sampled RGB frames independently, so a long video must either exhaust the token budget or drop the changes between sampled frames. Codec-aware front-ends read the motion vectors and residuals that encoding produced, but in their deployed form each predictive frame is still tokenized on its own: the tokens are a function of the current primitives, not of a carried reference. We argue that a more natural function is of both---the current primitives and a carried reference. A clip and its time reversal share the same frames and differ only in the order of changes---an axis that symmetric pooling discards by construction, and that is non-empty in the frozen vision features VideoLMs use---and the codec recurrence already composes those changes in order against a reference state. We introduce RESUME, a stateful codec representation: an anchor I-frame initializes a compact latent state, each subsequent predictive frame is consumed as an update to that state, and a shared readout exposes VideoLM-compatible tokens from the accumulated state. Codec prediction is thereby kept at the representation level and handed to the language model as a trajectory, not as a set of independent token groups. At the same per-predictive-frame token budget as prior codec-aware methods, a predictive frame enters the language model as a readout of what the front-end already knows, not as an encoding of the current primitives alone. Across ten benchmarks, the gains concentrate on temporal reasoning: on all three temporal benchmarks RESUME improves over both the RGB-frame baseline LLaVA-Video-7B (by 2.8, 5.1, and 3.9 points on TempCompass, TOMATO, and MVBench) and the codec-based baseline CoPE-7B, while staying competitive on general and long-form QA. Frozen-transition tests further show anchor dependence, order sensitivity, and useful rollout behavior beyond the training horizon.

---


### 267. [A2Z GameSpec-Bench: How Faithfully Can Coding Agents Generate Games from Game Design Specifications?](https://arxiv.org/abs/2609.39564)

**<font color=#1a73e8>作者：</font>** Seonho Lee, Wonryeol Jeong, Alberto Cereser 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Delegating complete application development to coding agents requires preserving the intended design rather than simply producing plausible outputs through naive prompting. Game development provides a demanding testbed, as long-form Game Design Documents (GDDs) describe requirements that must work together across game logic, visual rendering, and player interactions. However, existing game-development benchmarks typically use compact specifications and provide limited support for evaluating interdependent requirements across these aspects in long-form GDDs. We introduce A2Z GameSpec-Bench, a benchmark of 100 long-form GDDs for evaluating end-to-end game development by agents. We measure faithfulness by checking whether the game satisfies the GDD requirements and preserves the relationships among them. Each GDD is turned into a dependency-aware contract that contains rules, constraints, and prerequisite relations. Following game-development practices, we combine source-code inspection with agent-generated test policies for scenario-based replay and adaptive playtesting. The contract remains fixed across agents and revision rounds, while judgments and evidence linked to the same requirements support consistent comparison and failure detection. Our evaluations show that current agents struggle to jointly satisfy interdependent requirements across code implementation and actual play. Requirement-specific feedback improves GDD Fidelity by 10.9% relative to self-revision after two rounds. A2Z GameSpec-Bench assesses end-to-end specification-following ability beyond implementation judgments and provides targeted feedback to support more faithful game development. Code and datasets are available at this https URL.

---


### 268. [From Given to Gathered Evidence: Agentic Learning for Longitudinal Medical Reasoning](https://arxiv.org/abs/2609.39566)

**<font color=#1a73e8>作者：</font>** Minye Shao, Chaohui Yu, Yixuan Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models can serve as clinical agents through tool-use harnesses. However, conventional medical benchmarks assess reasoning over preselected evidence rather than the ability to seek it across clinical records and longitudinal imaging. We propose CASE: a series of role-specific Clinical Agents for Seeking Evidence, together with a tool-use harness and an agentic post-training framework for compact vision-language policy models. We further introduce a longitudinal multimodal benchmark built on UK Biobank, comprising 50,401 clinical questions derived from real-world ICD-10-coded diagnoses of 4,739 participants. Each question links to a patient-specific environment containing clinical context and multi-sequence MRI from baseline and follow-up visits, where agents autonomously select which visits, organs, modalities, slices, and specialist tools to inspect and compare. Supervised fine-tuning transfers evidence-seeking workflows from 14,734 frontier-model interaction trajectories, followed by agentic reinforcement learning on the learner's own environment interactions. Privileged on-policy self-distillation and rubric-based LLM feedback refine evidence-to-conclusion reasoning without prescribing tool sequences. Experiments show that CASE moves beyond question-answer imitation toward transferable investigation policies, strengthening evidence-grounded longitudinal reasoning. Under matched evaluation conditions, our Qwen3-VL-8B based agent achieves over 16% and 10% relative improvements in answer accuracy over GPT-5.4 and Claude Opus 4.8. Code will be available at this https URL.

---


### 269. [Compact Language, Complex Model Shifts: How and Where Ambiguity and Underspecification Affect LLMs](https://arxiv.org/abs/2609.39572)

**<font color=#1a73e8>作者：</font>** Michaela Regneri, Nina Scheller, Sören Laue  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We analyze how lexical ambiguity and underspecification affect language model training. We create artificial homonyms and artificial hypernyms as pseudowords and analyze the generative performance of language models as they are trained with increasing amounts of these ambiguous or underspecified pseudoword types. We further analyze whether the models disambiguate ambiguous or underspecified statements and provide a first mechanistic account of how ambiguity and disambiguation are represented internally. Our main results show that both ambiguity and underspecification increase model performance in ways that scale with their influence on the language's type-token ratio. However, the accuracy of generating sequences containing ambiguous words or their synonyms decreases compared to other texts. We also show that internal representations of pseudowords reflect disambiguation of pseudo-homonyms, but underspecification of pseudo-hypernyms is maintained during the generative process.

---


### 270. [Thinking Outside the Box: Can Language Models Rely on External Guidance Selectively?](https://arxiv.org/abs/2609.39578)

**<font color=#1a73e8>作者：</font>** Minghan Wang, Boyuan Wang, Jinhang Zuo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent harnesses often improve language models with human-designed workflows, but as models grow more capable, unreliable guidance can increasingly constrain their execution. We call the ability to benefit from useful guidance while overriding unreliable guidance thinking outside the box. We introduce Box$^2$-Bench, which holds the model and task fixed while varying workflow reliability to isolate how models regulate their reliance on guidance. On Box$^2$-Bench, frontier models often benefit from reliable guidance but remain vulnerable when it is misleading or becomes unreliable. To test whether this capability can be learned, we train two open-weight models using bad workflows, reserving good workflows for evaluation. We explore two complementary training strategies: counterfactual supervised fine-tuning improves robustness, while outcome-based reinforcement learning can shift the balance toward greater use of helpful workflows. We further find that this behavior extends beyond workflows to other forms of external information, improving peer correction and robustness to corrupted memory. Together, our results identify selective reliance on fallible external information as a dimension of agent reliability not captured by task performance alone.

---


### 271. [KilometerVision: A New Frontier for Large-Scale Spatial Intelligence in VLMs](https://arxiv.org/abs/2609.39588)

**<font color=#1a73e8>作者：</font>** Aravindh Mahendran, Michael King, Matthew Koichi Grimes 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We push the frontier of large-scale spatial intelligence in Vision-Language Models (VLMs) and introduce the first benchmark that probes geographical layout understanding from real-world videos, spanning up to 1km distances. Inspired by the cognitive science literature, we evaluate models against the hierarchical stages of human spatial awareness: anchoring via landmarks, connecting them through routes, and integrating these into global mental maps. Extensive experiments reveal a fundamental divergence in how current AI models process spatial information. Instead of utilising true path integration or forming geometric survey knowledge, we find that VLMs rely almost entirely on 2D visual recognition and text-matching to bypass complex spatial reasoning. The benchmark is publicly available at this https URL.

---


### 272. [GroundAnything: Reconciling Parallel Decoding with Precise Visual Grounding at Flash Speed](https://arxiv.org/abs/2609.39600)

**<font color=#1a73e8>作者：</font>** Qize Yu, Lianrui Fan, Bowen Ping 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) grounding models serialize spatial predictions, introducing sequential latency and imposing a causal order on output tokens. We view grounding as visual evidence extraction: objects, locations, and spatial relations are jointly constrained by the image and query, yet their dependencies do not imply an intrinsic left-to-right generation order. This distinction makes bidirectional diffusion a natural fit, allowing spatial hypotheses to emerge in parallel and be jointly refined through iterative denoising. We introduce GroundAnything, a 4B-parameter grounding foundation model that reconciles fast parallel decoding with precise localization through blockwise denoising. Training combines grounding pretraining from public datasets and dedicated data engines, direct AR-to-diffusion conversion with joint AR and diffusion objectives, supervised fine-tuning, and GRPO-based reinforcement post-training. Across 30 grounding benchmarks, our autoregressive variant, GroundAnything-VLM, establishes a new overall state of the art among similarly sized models at 72.42%, remaining competitive with GPT-6 Astra (71.35%). With entropy-guided decoding, GroundAnything also surpasses the prior state of the art at this scale, averaging 61.75% versus 53.32% for the fast MTP-based LocateAnything model. We further explore decoding strategies, showing that an optional self-speculative mode achieves a $4.51\times$ speedup over the AR counterpart with a 0.74 percentage-point drop in COCO F1mIoU. Infrastructure experiments show that progressive inference optimizations translate parallel decoding into practical speedups. These support efficient visual grounding in latency-sensitive real-world systems.

---


### 273. [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601)

**<font color=#1a73e8>作者：</font>** Qize Yu, Lianrui Fan, Boyu Chen 等 26 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precise grounding matters. It specifies which object is the target and where that object is, even in clutter and for tiny objects, and it has to be fast enough for closed-loop control. Yet vision-language-action (VLA) and world-action models (WAMs) take perception from general-purpose vision-language and video-generation backbones, which still fail in these settings. We introduce GroundingPI, a 4B grounding foundation model that generates points and boxes as quantized coordinates in a shared vocabulary. Training combines multimodal and spatial pretraining, supervised fine-tuning, and reinforcement learning with GRPO, using supervision from public datasets and dedicated data engines. Against 44 baselines across 34 grounding benchmarks spanning 11 perceptual capabilities, GroundingPI establishes a new state of the art, averaging 73.68%, above the larger GPT-6 Astra (71.54%). As a downstream visual backbone, GroundingPI improves performance on robotic manipulation and autonomous driving. On RoboTwin 2.0, it outperforms every mainstream backbone we evaluate in all four out-of-distribution settings, by up to 24.8% relative to the strongest backbone. On RoboCasa-GR1, GroundingPI trained with 50% of the demonstrations outperforms those baselines trained with 75%. On nuScenes, used as the visual backbone, GroundingPI attains an average open-loop L2 error of 0.296 m. We systematically analyze GroundingPI's pretraining in scale and data composition. Downstream autonomous driving and robotic manipulation improve as the pretraining is scaled. Analyzing the data recipe across these 11 perceptual capabilities shows dense grounding's substantial benefits for both, and OCR's potential as a catalyst for perceptual learning. These results support grounding as a perceptual foundation, and dedicated perceptual pretraining as a promising direction for foundation models of physical intelligence.

---


### 274. [Pretext: Defeating Malicious Skill Detection Frameworks for AI Agents](https://arxiv.org/abs/2609.39607)

**<font color=#1a73e8>作者：</font>** Tobias Kaisar, Aritra Dhar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Skills extend an agent's capabilities by injecting instructions and information into the context, and are widely used by agents such as OpenClaw and Claude Code. Prior work shows third-party marketplaces host malicious skills that give attackers direct influence over the victim's agent. The emerging defense scans skills before installation, pairing deterministic static checks with an LLM-based semantic judge, as in NVIDIA's SkillSpector. We show that such defenses fall to an attacker who knows the detector. Our white-box LLM attacker, Pretext, iteratively crafts skills that evade detection while still delivering the payload and performing the benign task: moving the payload from code into natural language leaves static analysis inert, while framing it as the skill's legitimate purpose and splitting instructions across files keeps the LLM stage below its blocking threshold. Across three open-source models, Pretext achieves up to 97\% and 77\% against a frozen detector and a co-adaptive one, respectively, revealing major gaps in current skill scanners.

---


### 275. [Is This Evidence Decision-Critical? Learning to Verify Rule-Governed Decisions](https://arxiv.org/abs/2609.39608)

**<font color=#1a73e8>作者：</font>** Haoyang Zhang, Jianpeng Zhao, Qi Hao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rule-based reasoning, as in eligibility checks and contract reviews, requires language models to assess evidence against individual conditions and combine their judgments under explicit rules. Errors in evidence assessment can leave a decision unchanged, but misinterpreting or overlooking decision-critical evidence can reverse it. Identifying such evidence allows more capable models to focus on checking the corresponding condition judgments, supporting accurate and safe decisions. Recognizing the evidence's criticality requires understanding how evidence affects a condition judgment and how that judgment affects the decision. To achieve the goal, we propose a INTERvention-based imPACT learning framework (InterPact), which enables counterfactual verification of evidence criticality in rule-governed decisions. Specifically, its evidence intervention constructor generates training pairs for a propagation verifier by editing case facts with a frozen language model while holding rules and non-target conditions fixed. Human-reviewed labels record the resulting condition and decision changes, while complete state-to-decision mappings supervise consequences beyond the observed edit. During training, the verifier weights learned conditional decision predictions by evidence-based condition probabilities through a fixed composition operation, propagating decision-change supervision into the base model. At inference, the trained base model directly judges criticality from the original case and target evidence, without human or stronger-model supervision. On single-case evidence criticality verification over adapted rule-governed decision cases, InterPact achieves 68.28% accuracy, outperforming all six baselines. These results support learned decision sensitivity as a basis for prioritizing evidence checks.

---


### 276. [Towards Better Exploration in Sequential Test-Time Scaling](https://arxiv.org/abs/2609.39632)

**<font color=#1a73e8>作者：</font>** Joseph Rance, Fabio Pizzati, Juil Sock 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time scaling improves language model reasoning by spending additional compute at inference. However, both classes of existing methods often fail to continue improving over long timescales. Parallel methods repeatedly sample independent answers from the model, scaling poorly on problems the model is unlikely to solve in a single attempt. In contrast, sequential methods build on previous answers to access new ideas, yet so far have not been shown to reach answers beyond those found by parallel scaling. First, we show that sequential scaling often stops improving because it becomes prematurely trapped in an attractor: a set of answers that prevents exploration of different answers once entered. Across 27 combinations of scaling methods, models, and benchmarks, we find that 53.8% of sequential scaling trajectories enter an attractor within four iterations. Second, we show that a simple model-mixing intervention helps escape attractors. This reduces the attractor hit rate by 21.2 percentage points on average, expands solution coverage beyond a compute-matched parallel baseline, and improves accuracy of recursive self-aggregation by at least 2.2 percentage points. Our results motivate refocusing long-horizon test-time scaling from parallel methods to sequential methods that improve previous answers.

---


### 277. [Marginal Response Surface Elicitation for Zero-Label Tabular Learning](https://arxiv.org/abs/2609.39639)

**<font color=#1a73e8>作者：</font>** Liangyu Teng, Yicheng Ding, Jing Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tabular learning uses structured data to predict target outcomes. Traditionally, this process has relied on labeled data. However, large language models (LLMs) can be used to elicit domain priors based on the task description and feature semantics, thereby enabling predictions without labeled data. We propose Marginal Response Surface Elicitation (MARS), a method that transforms feature-level LLM priors into a reusable, zero-shot tabular classifier. To construct this classifier, MARS selects representative values for each feature from unlabeled data and prompts the LLM to provide corresponding class support scores and feature weights. It then aggregates multiple responses using the median to construct feature response functions, and makes predictions through their weighted sum without further LLM queries. Across eight tabular benchmark tasks, MARS achieves the highest average AUC and AP, outperforming direct prompting by 1.97 and 6.21 percentage points respectively, while substantially reducing end-to-end costs. Evaluations with LLMs of different sizes further demonstrate its predictive advantage over direct prompting.

---


### 278. [SEPAL: Separated Expert Pairs with Answer-Level Fusion for Reliable LLM Collaboration](https://arxiv.org/abs/2609.39645)

**<font color=#1a73e8>作者：</font>** Weijie Ren, Yanwen Zhang, Hao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent collaboration lets large language models (LLMs) improve question answering through deliberation and feedback. Yet shared discussion couples correction with exposure to the same mistakes, which can erode the diversity needed for voting. Self-consistency offers sampling diversity without feedback, while single-pair Actor-Critic collaboration refines only one candidate. We introduce SEPAL, which assigns three private Actor-Critic teams to direct reasoning, evidence grounding, and verification. Role-specific training gives the teams different reasoning objectives beyond sampling variation. Each Critic guides revisions within its own team, preventing feedback from carrying errors across candidates. Once revision ends, majority voting combines only the final answers, keeping the reasoning histories separate until the decision. Across five open-weight backbones and five question-answering benchmarks, SEPAL improves mean accuracy by 1.81 percentage points over a matched single Actor-Critic pair, with improvements across all five backbones. Code is available at this https URL.

---


### 279. [The Evolution of Attention in Large Language Models: Mechanisms, Trade-offs, and Emerging Trends](https://arxiv.org/abs/2609.39661)

**<font color=#1a73e8>作者：</font>** Zhentao Tan, Jingyi Shen, Yanbo Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-attention gives LLMs fine-grained, query-dependent access to context, but dense token interactions incur quadratic prefill cost and a key--value cache growing with context length. Research thus spans explicit-memory compression, sparse access, recurrent state construction, structured state dynamics, and heterogeneous mechanism composition. This survey analyzes these developments as model-internal contextual memory. We introduce a five-dimensional lens---Memory Representation, Memory Update, Access, Readout, and Integration---describing what is represented, how it changes, what is query-eligible, how it is read, and how readouts form outputs. This lens compares overlapping research lines without imposing one computational model.
We reconstruct mechanism-level developments and architectural adoption using 59 release-level records from 14 major model lineages and 11 high-performing open-weight endpoints. First, explicit-memory and recurrent-state methods retain distinct interfaces but increasingly control overlapping memory functions. Second, heterogeneous architectures increasingly coordinate across network depth: layer-wise composition distributes complementary memory processing across representational stages, while cross-layer reuse carries selected memory and routing artifacts forward. Depth thus becomes a dimension along which contextual memory is constructed and managed. Third, these developments motivate a stateful multidimensional memory-routing hypothesis: persistent memory is organized across temporal scope, network depth, substrate type, and representation granularity, while coordinated Sparse Write and Sparse Read determine what is maintained and what contributes to each query. Overall, efficient sequence architecture design increasingly concerns the organization, lifecycle, and selective use of contextual memory rather than an isolated Attention operator.

---


### 280. [Typographic Attack Against VLM-based AI-generated Image Detection](https://arxiv.org/abs/2609.39662)

**<font color=#1a73e8>作者：</font>** Eunmin Lee, Jungwoo Kim, Jong-Seok Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly used for AI-generated image (AIGI) detection, providing natural-language explanations for authenticity judgments. However, their ability to interpret text within images may also expose these judgments to misleading semantic cues. We systematically evaluate typographic attack strategies across detection-oriented, open-weight, and commercial VLMs, considering both real-to-fake and fake-to-real attacks. Our results show that reasoning modes generally exhibit greater vulnerability than direct modes and that attack effectiveness exhibits pronounced directional asymmetry. Moreover, larger models tend to exhibit higher clean detection accuracy but also higher attack success rates. We further examine attack robustness under image and text transformations and investigate whether overlays indicating the correct class can aid error correction. Together, these analyses characterize how typographic attacks influence authenticity judgments and expose limitations of current VLM-based AIGI detection systems.

---


### 281. [ChronoGraph: Functional 4D Scene Graphs with Vision-Language Models for Interaction Understanding and Grounded Planning](https://arxiv.org/abs/2609.39665)

**<font color=#1a73e8>作者：</font>** Chenyangguang Zhang, Malgorzata Gwiazda, Guanlong Jiao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Embodied agents must determine where to act, anticipate the resulting scene changes, and interpret observed outcomes to guide subsequent actions. This requires connecting 4D interaction understanding, which explains how past actions changed the scene, with spatially grounded planning, which determines how and where to act toward a goal and anticipates the resulting scene changes. We introduce ChronoGraph, a functional 4D scene graph that links actions on affordance parts to semantic and geometric state changes. By representing observed and anticipated transitions in the same form, it provides a shared basis for understanding and planning. We construct ChronoGraphBench through an automatic data engine that converts human-interaction videos and simulated robot trajectories into graph-annotated questions for training and evaluating Vision-Language Models (VLMs) on both tasks. Using these annotations, we train ChronoGraphVLM by adapting pretrained VLMs in two stages. Graph-as-Chain-of-Thought supervised fine-tuning teaches the models to reconstruct observed transitions and predict future ones as graph traces before answering. Subsequent joint 4D graph reinforcement learning directly rewards graph properties and answer correctness. Experiments across model scales show improvements over the corresponding pretrained baselines and zero-shot transfer to VLM4D. Real-world demonstrations further show that graph-based planning and affordance grounding support mobile manipulation through existing robot skills without additional fine-tuning.

---


### 282. [Aletheia: Permission-Minimality Testing for Coding-Agent Rules](https://arxiv.org/abs/2609.39678)

**<font color=#1a73e8>作者：</font>** Jieke Shi, Yuchen Chen, Junda He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Repository instruction files guide coding agents, but also expose them to prompt injection. Malicious rules can request credential access or data transfer while the agent produces a correct patch. We present Aletheia, a framework for permission-minimality testing. Aletheia translates requested authority into a typed language and synthesizes executable sandbox configurations. It runs the unchanged rule and task under full permissions and independent restrictions that remove one permission at a time. Passing independent functional tests under strictly reduced authority provides a dispensability witness, which Aletheia interprets against task context to diagnose suspicious requests. We formalize synthesis and the conditions connecting witnesses to enforced restrictions. On a shared refactoring task, Aletheia executes and detects all 314 AIShellJack attack inputs, with no alarms on five benign templates. Among 80 manually verified benign GHAgentFiles rules, it raises three false positives (3.75%).

---


### 283. [Better Supervision Is Nearby: Neighborhood On-Policy Self-Distillation](https://arxiv.org/abs/2609.39687)

**<font color=#1a73e8>作者：</font>** Xincheng Wei, Yifan Ding, Yoshua Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) trains mathematical reasoning models using a privileged teacher that sees a reference solution and supervises student-sampled prefixes. Standard OPSD uses one fixed parameter setting at every state, but nearby settings may offer additional supervision. We find that local parameter perturbations reveal complementary reference-aligned corrections under the same reference context. Different experts supply these corrections at different reference positions. Their pool covers more such positions than the unperturbed privileged teacher. We introduce Neighborhood OPSD (N-OPSD) to turn these corrections into supervision at student-visited states. Offline, greedy selection builds a compact pool of frozen experts by rewarding filtered reference-token gains beyond the pool's current best at each position. The highest-peak expert need not provide the best training target. Online routing therefore separates the anchor direction from its level of support. MaxPeak selects the anchor token, and quantile selection chooses among experts whose top token matches it. The student learns from the chosen expert's full next-token distribution through the clipped forward-KL objective inherited from OPSD. We evaluate on AIME 2024, AIME 2025, and HMMT February 2025. Across three independent runs per method, Neighborhood OPSD improves the three-benchmark Average@12 over OPSD by 2.75, 1.67, and 1.94 points on Qwen3-1.7B, 4B, and 8B, respectively. Student-prefix continuations support using the pool beyond the reference trajectories used for selection. Matched ablations support filtered reference-token gains as a selection criterion. Accounting for overlap within the pool and routing by state further improve student accuracy. Inference uses only the distilled student.

---


### 284. [GFD-OPD: Guidance-Folded On-Policy Distillation of Diffusion Models Across Scales](https://arxiv.org/abs/2609.39692)

**<font color=#1a73e8>作者：</font>** Zhenxing Zhang, Jiayan Teng, Wenxu Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has demonstrated two important capabilities in language models: compressing large teachers into smaller students and merging expert models into a single model. Existing diffusion OPD, however, mostly focus on the latter, with teachers and students sharing the same backbone and scale. We investigate large-to-small diffusion opd from large teachers to a small student and find that the standard recipe fails. To find the underlying cause, we propose Fixed-State KL, an effective and fair way to measure the distribution gap between student and teacher during OPD training for diffusion models. We are the first to clarify why large-to-small OPD is challenging for diffusion models: a smaller student struggles to perfectly match the distribution of a larger teacher, while classifier-free guidance can accumulate and amplify the distributional discrepancies between the student's conditional and unconditional branches and those of the teacher. To solve this problem, we propose GFD-OPD, a simple yet effective method that reduces the student-teacher gap while avoiding the error amplification of the CFG composition. Across numerous experiments, GFD outperforms previous baselines in both training efficiency and final performance, achieving state-of-the-art results on all benchmarks.

---


### 285. [Values as Style: Disentangling Values from Semantics with One-Way Mixing for Low-Damage LLM Steering](https://arxiv.org/abs/2609.39701)

**<font color=#1a73e8>作者：</font>** Jiale Dai, Hongcan Deng, Liuxian Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Value steering should change an LLM's normative priorities while preserving the scenario, facts, and task constraints underlying its answer. Conventional activation edits often change both. We introduce an editable semantic-value interface on frozen residual states, with a one-way semantic-to-value pathway that grounds value recognition in context. Stop-gradient blocks feedback through this pathway; swap consistency, topic de-confounding, and decorrelation encourage selective codes. At inference, editing the value code produces a residual delta while holding the semantic code fixed. On two instruction-tuned backbones, this interface improves semantic preservation and reduces benign refusals at comparable value alignment. A matched mixing-by-gating ablation separates representation learning from selective edit activation, and dimension-matched probes establish improved code selectivity. Against validation-selected prompting on LLaMA-3.1-8B, the method achieves comparable alignment (0.750 vs. 0.748), higher BERTScore (0.938 vs. 0.923), and fewer contradictions (5.1% vs. 7.6%). Human ratings and cross-taxonomy controls provide complementary evidence for low-damage value steering.

---


### 286. [A helps B while B hurts A: directed transfer in instruction-tuning mixture](https://arxiv.org/abs/2609.39702)

**<font color=#1a73e8>作者：</font>** Nima H. Siboni, Vahid Rostami  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Adapting a language model to a specialized corpus means choosing which instruction-tuning tasks to train on under a fixed budget, and testing one choice costs a fine-tuning run. Common heuristics add more source tasks or pick sources similar to the target. The first assumes transfer is never negative; the second, that it is symmetric. We show that both assumptions fail: task $A$ can help task $B$ while $B$ hurts $A$, so helpfulness is a signed property of ordered source--target pairs. We introduce the transfer map, a signed estimate of how much each source helps or hurts each held-out target. We fit the map in hundreds of fine-tuning runs on Qwen3 and Mistral models from 0.6B to 32B parameters, with all sources drawn from one corpus and no training examples from the target. The map predicts a held-out target's accuracy on unseen mixtures: recorded before those runs, its predictions have less than half the error of a mixture-agnostic baseline. The map is specific to its target and corpus but transfers across model scale: a mixture selected in advance at one size beats training on all source tasks at every other size we tested. Transfer is thus a property of the data. The map selects the tasks that help and drops the one that interferes: accuracy on the reasoning targets (causal explanation, multi-hop questions and methodological critique) rises by up to 14 percentage points over training on all source tasks.

---


### 287. [Drift Inspector: Exploring and Measuring Scientific Drift with Atomic Contribution Claims](https://arxiv.org/abs/2609.39710)

**<font color=#1a73e8>作者：</font>** Vsevolod Karimov, Stepan Ostarkov, Anastasia Poroshina 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific abstracts mix contributions with background, motivation, and meta-language, so tools that read them as-is cannot separate what a field produces from what it discusses. We present Drift Inspector, an open-source system for measuring and exploring how a research field changes over time at the level of Atomic Contribution Claims (ACCs): decontextualized, contribution-bearing propositions an LLM extracts from each abstract before analysis. The system clusters these claims across years into an interactive map where every trend traces back to the claims and papers behind it. Applied to six years of EMNLP, it shows the field shifting away from classic NLP tasks toward LLM-era capabilities such as reasoning and multimodality -- a movement that keyword or whole-abstract counts blur. The released data extend beyond EMNLP: the same pipeline has processed the full ACL Anthology (346k claims, 80k abstracts, 423 venues). Extraction is human-validated and clustering checked against an external manually constructed taxonomy.

---


### 288. [ArchitectureIQ: On the Measure of Training Intuition](https://arxiv.org/abs/2609.39714)

**<font color=#1a73e8>作者：</font>** Zirui Ren, Shaoyang Guo, Chencheng Tang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Top researchers have good intuition, but do language models have as good intuition about model training as top AI researchers? To measure model intuition of LLMs and humans, we introduce the ArchitectureIQ benchmark. Each question presents a synthetic dataset and several training recipes, and the test-taker is asked to predict the recipe yielding the best test metric. Overall, we find that LLMs' model intuition is good but has four limitations: (1) The intuition is imperfect, or even sub-human in some cases. Frontier models achieve around 76% accuracy (random choice 33%) vs best human researcher (66.0%), yet remain far from perfect. For architecture-only questions, best human achieves 65% while GPT-6 Astra only has 38%. (2) The intuition is empirical, not structured, supported by the fact that more CoT compute does not lead to substantial improvement. Unlike math, we still lack a "Science of AI" language that enables structured reasoning on AI. (3) The intuition is not maximally condensed, and can be further compressed into a knoledge base. Our constructed knowledge base with only 20 items yields large gains for weak models: GPT-4o equipped with the accumulated knowledge almost matches the performance of Claude Opus 5. (4) The intuition is insensitive to dataset properties, but the best model should in general depend on data properties. This suggests that data is the real "dark matter" in AI -- LLMs (so do human researchers) understand too little about data, even less than model architectures.

---


### 289. [Trust Is Not a Score: Runtime Assurance Contracts for High-Risk AI Agents](https://arxiv.org/abs/2609.39717)

**<font color=#1a73e8>作者：</font>** Serhii Zabolotnii  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Benchmarks, audits, and agent protocols describe performance, permissions, and repair, but not how observed evidence should change an agent's authority during a consequential task. We call this the assurance-transition gap. We propose a Runtime Assurance Contract (RAC), a policy-level formal schema binding autonomy boundaries, component eligibility, evidence state, transition policy, human-review capacity, and non-compensatory gates. Under RAC, soft metrics may inform routing, whereas a failed or unknown mandatory gate forces retry, switch, escalation, deferral, or stop; aggregate performance cannot authorize action. We define the contract, an evidence record, a permission rule, and five invariants, and illustrate them in clinical, industrial, and judicial failure probes. We then report a deterministic failure-injection study in agentic coding: 280 constructed cases evaluated by a gate conjunction, a score-only rule, and a restricted protocol baseline. At the published example weights and threshold, the score rule admits 80 of 100 block-required injections and all 40 review-required injections. Tuned in hindsight, it matches the conjunction on this corpus. For positive weights, a positive threshold, binary risk signals, zero-signal controls, and an injected case firing each signal alone, we show that exact agreement holds if and only if the threshold does not exceed the smallest weight. A separate set of 18 hand-authored traces checks version-pinned evidence and review transitions against simpler policy variants. In a further prospective synthetic holdout of 24 episodes, two blinded LLM judges assign identical labels to all 72 action attempts; RAC and a separately implemented full stateful baseline both match these labels. These studies test mechanisms on synthetic cases; they establish neither deployed safety nor cross-domain effectiveness.

---


### 290. [OverForge: Reasoning Through Strategies and Tactics Helps Cooperative Lifelong Adaptation](https://arxiv.org/abs/2609.39727)

**<font color=#1a73e8>作者：</font>** Oana Madalina Fron, Ojas Shirekar, Chirag Raman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cooperative language-model agents must coordinate over long horizons and adapt to changing environments and to partners with unfamiliar conventions, yet existing agents map observations to actions without separating persistent coordination strategies from their tactical execution. We introduce OverForge, a training-free hierarchical architecture that separates strategic reasoning over roles and divisions of labour from tactical reasoning over actions within each agent's private, partner-conditioned world model. A metacognitive Prefrontal Cortex Module couples the two levels by forming strategy-action branches, imagining their consequences with a forward model, and committing when confident. In OvercookedV2, OverForge delivers 7 soups in a connected kitchen versus 3 for each flat LLM baseline, retains agreed roles, and adopts roles proposed by unfamiliar partners. Ablations and a fixed-strategy probe show that persistent strategies guide tactical adaptation while each reasoning level contributes to coordination. Memory restarts show that cross-episode partner knowledge supports task performance and partner prediction, linking the hierarchy to continual adaptation.

---


### 291. [Revisiting On-policy Adversarial Black-Box Distillation: Calibrating Groupwise Reward Geometry for Effective Advantage Construction](https://arxiv.org/abs/2609.39757)

**<font color=#1a73e8>作者：</font>** Xiao Cui, Mo Zhu, Yulei Qin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Black-box distillation is a practical route for transferring capabilities from API-accessible large language models that expose only text outputs into smaller student models. Recent on-policy adversarial methods such as GAD improve over SeqKD by forming an adversarial loop between a critic and a student, where the critic provides rewards for GRPO-based student policy optimization over the student's sampled responses. However, GRPO computes advantages from the within-group relative rewards of student samples for the same prompt, whereas the critic is trained primarily to distinguish teacher responses from student responses. This objective mismatch can produce reward groups with collapsed scale or fragile margins, leading to brittle grouped optimization signals. We propose Groupwise Reward Geometry Conditioning (GRGC), a two-stage framework that improves advantage construction by shaping student-side reward groups during both critic training and policy optimization. To improve critic-side conditioning, Gaussian groupwise Optimal Transport calibration regularizes the critic during training to produce reward groups with non-collapsed spread and smooth rank-wise gaps by matching sorted prompt-wise rewards to group-centered Gaussian quantiles. Building on this conditioned reward geometry, policy-side group power modulation reshapes the prompt-wise reward groups before they are converted into advantages, preserving the critic-induced ordering while increasing optimization-relevant margin separability. Extensive experiments across diverse teachers, student model families and scales, and training datasets demonstrate the effectiveness of GRGC on both in-distribution and out-of-distribution evaluations, while introducing negligible overhead over GAD. The code is available at this https URL.

---


### 292. [MemCodex: Self-Programming Hierarchical Memory for Language Agents](https://arxiv.org/abs/2609.39765)

**<font color=#1a73e8>作者：</font>** Xiaoqiang Wang, Bang Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent memory faces heterogeneous access needs: a single-hop question may require one piece of evidence, whereas a multi-hop question must combine evidence from multiple sources. Predefined memory workflows cannot adapt to these varying needs. Recent adaptive methods search or learn over memory components and their compositions, but the design space itself remains predefined. We introduce MemCodex, a self-evolving hierarchical memory system that organizes experience into executable memory programs for summaries, relational knowledge, reusable skills, and latent memory. Open-ended program evolution searches the open design space of layer programs by rewriting how each layer is constructed, indexed, retrieved, and routed, thereby adapting both within-layer implementations and cross-layer composition. At query time, reads traverse the hierarchy from coarse to fine and stop once sufficient evidence is found, descending to the original history when needed. We further develop MemArena, a unified runtime that places heterogeneous data and memory systems behind a common interface. MemCodex improves average task success by 10.1% relative to the strongest adaptive-memory baseline, while using 3.4x fewer context tokens and achieving 2.1x faster inference.

---


### 293. [How Does Local Landscape Geometry Evolve in Language Model Pre-Training?](https://arxiv.org/abs/2609.39767)

**<font color=#1a73e8>作者：</font>** Zhanpeng Zhou, Yuhan Sun, Bingrui Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The scale and expense of pre-training language models make efficient hyperparameter tuning essential, yet a principled guidance is still missing. In this work, we analyze language model pre-training dynamics from a local landscape geometry perspective. Our study reveals two distinct phases. In Phase I, sharpness of the local landscape is initially high, leading to instability and loss plateaus under large learning rates (LRs). The landscape shifts from sharp to flatter regions early in training. This dynamic explains the necessity of LR warmup and further suggests that larger peak LRs require proportionally longer warmup periods. In Phase II, the local landscape is governed by the gradient noise scale. Our theory identifies a depth flatness trade-off: high noise from smaller batches widens the loss basin, whereas reduced noise from larger batches deepens it. This theory motivates a dynamic batch-size (BS) scheduler that begins with a small BS and increases it late in training. Together, we provide a unified view of loss landscape evolution, which translates into actionable tuning strategies for large-scale pre-training.

---


### 294. [GraphMAS: A Systematic Benchmark of Multi-Agent Coordination for Graph Learning](https://arxiv.org/abs/2609.39777)

**<font color=#1a73e8>作者：</font>** Jiayi Yang, Yifang Chen, Yuanfu Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent systems coordinate specialized reasoning through aggregation, interaction, and adaptive control, yet their potential for graph learning remains unexplored. Graph learning is a natural setting for such systems because useful evidence may arise from heterogeneous local, long-range, global structural, and semantic perspectives whose relevance varies across instances. Existing LLM-based graph learning approaches primarily rely on single-agent reasoning, while multi-agent coordination has been studied mainly in general reasoning settings. Consequently, it remains unclear whether multiple specialized agents can improve graph learning and how coordination strategies should be designed and evaluated. To address this gap, we introduce GraphMAS, a systematic benchmark of multi-agent coordination for graph learning. GraphMAS builds a shared pool of graph reasoning specialists and organizes coordination along two dimensions, inter-agent interaction and runtime adaptivity, yielding four paradigms and seven representative coordination methods. Under a unified protocol, we evaluate these methods across seven text-attributed graphs, three domains, and two graph learning tasks. We find that heterogeneous graph perspectives are complementary, and that coordinating specialists improves over individual specialists and single-agent graph reasoning, with gains from decomposing reasoning across specialists rather than from broader evidence access alone. However, richer inter-agent interaction does not reliably help, whereas instance-adaptive specialist selection yields the strongest accuracy-efficiency trade-off. We further show that coordination can be learned over a fixed specialist pool and transfers to held-out graphs. GraphMAS therefore provides a controlled evaluation framework and empirical principles for understanding when and how multi-agent coordination benefits graph learning.

---


### 295. [Explore-on-Graph: Hybrid Embedding-LLM Reasoning for Knowledge Graph Question Answering under Incompleteness](https://arxiv.org/abs/2609.39786)

**<font color=#1a73e8>作者：</font>** Ola El Khatib, Djellel Difallah  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly combined with knowledge graphs (KGs) to ground reasoning in structured evidence. However, most LLM-based KGQA methods rely on traversing existing graph edges and become unreliable when reasoning paths are broken by missing facts. Alternatives that ask LLMs to generate missing knowledge risk introducing hallucinated evidence. We introduce XoG (eXplore-on-Graph), a framework for multi-hop question answering over incomplete KGs that recovers missing reasoning paths from learned graph structure rather than LLM parametric knowledge. XoG combines type-level entity-relation statistics to identify candidate relations with KG embeddings to retrieve plausible missing entities, using the LLM as a semantic selector and reasoner. These mechanisms are integrated into an iterative planning-exploration-reasoning process. Experiments on WebQSP, CWQ, and the Wikidata-based BRINK benchmark show that XoG remains competitive on complete KGs and consistently outperforms comparable methods without task-specific KGQA training under KG incompleteness. These gains persist across multiple LLM backbones, indicating that stronger LLMs alone do not resolve missing graph evidence. XoG also reduces LLM token consumption by up to 33% compared with a closely related planning-based approach.

---


### 296. [Inline Memory Meets Reusable Skills: Memory-centric Framework for Vision-Language-Action Model](https://arxiv.org/abs/2609.39794)

**<font color=#1a73e8>作者：</font>** Zaijing Li, Rui Shao, Bing Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have shown strong promise for general-purpose robotic manipulation, yet adapting them to new tasks and domains remains inefficient: existing methods often rely on parameter tuning, incurring substantial costs and risking catastrophic forgetting of previously learned tasks. To address this, we propose \textbf{Optimus-R}, a memory-centric VLA framework that formulates robotic adaptation as explicit query-skill memory tuning. Optimus-R introduces: (i) An \textbf{Inline Memory Interface for skill extraction}. It inserts learnable memory tokens into the VLA prefix stream, allowing the backbone to derive control-aware query and skill representations within the native action-conditioning pathway. (ii) A \textbf{Query-Skill Memory Bank for skill learning}. It externalizes skills into query prototypes for deciding \emph{what} to retrieve and skill values for specifying \emph{how} to act, supporting skill reuse and expansion with limited parameter updates. (iii) A lightweight \textbf{Bridge-and-Adapt mechanism for skill updating}. It aligns target-domain queries and skills with the existing memory space through a lightweight adapter and residual memory updates. Experiments on in-domain adaptation, cross-domain adaptation, and lifelong learning show that Optimus-R enables data-efficient skill learning while mitigating catastrophic forgetting.

---


### 297. [RATIO: Reasoning Analysis and Token-level Inference Optimization for Quantized Reasoning Models](https://arxiv.org/abs/2609.39801)

**<font color=#1a73e8>作者：</font>** Chengzhu Bao, Xianglong Yan, Tianao Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) has become a widely adopted technique for reducing the memory footprint and inference cost of large language models (LLMs). However, recent studies reveal that when applied to reasoning models, PTQ not only degrades reasoning performance but also exacerbates overthinking, leading to longer reasoning trajectories. These issues may offset the efficiency gains expected from lower-precision inference. Existing approaches mainly rely on complex optimization procedures. More recent lightweight inference strategies instead use predefined overthinking markers, limiting their adaptability across quantized models. To address these issues, we propose Reasoning Analysis and Token-level Inference Optimization (RATIO), a framework that identifies model-specific overthinking tokens and assigns each a tailored penalty. RATIO first introduces Quantization-aware Reasoning Behavior Analysis (QRBA) to identify overthinking tokens by analyzing discrepancies between full-precision and quantized models. It then adopts Token-Specific Penalty Determination (TSPD), which leverages full-precision guidance to derive token-specific penalties without additional training. Extensive experiments show that RATIO achieves a better accuracy-efficiency trade-off than existing token-level interventions. Specifically, RATIO achieves up to 9.8 points accuracy improvement and reduces chain-of-thought (CoT) length by up to 51.3% compared with quantized baselines. The code will be available at this https URL.

---


### 298. [Stress-Testing LLM Lie Detectors: Role-Play Failures and Spurious Correlations](https://arxiv.org/abs/2609.39807)

**<font color=#1a73e8>作者：</font>** Maximilian von Klinski, Sebastian Lapuschkin, Wojciech Samek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Lie detection probes aim to predict from a language model's internal states whether its output is truthful or dishonest. However, role-play complicates what "truth" means for an LLM: language models can adopt a wide range of personas that take very different claims to be true, including personas whose beliefs clearly contradict reality, such as a conspiracy theorist. In this work, we investigate whether lie detection probes reliably flag falsehoods generated under such an anti-factual persona or whether they instead follow the persona's beliefs. We introduce a dataset of 8,916 human-reviewed, on-policy responses from three LLMs adopting anti-factual personas. Evaluating eight probes from prior work, we find that many fail in this setting, particularly when correct and incorrect answers are evaluated under the same persona prompt. To investigate why, we construct three novel confounder datasets in which truth is anti-correlated with a potential confounding concept. Our experiments reveal that many existing probes strongly track concepts that are spuriously correlated with truth in their training data, such as instruction compliance or response likelihood. Based on these findings, we introduce a simple linear probe that achieves the strongest overall performance on both the persona and confounder stress tests. Our results suggest that current lie detection probes are far from reliable and highlight the need for training data in which truth is decorrelated from confounding concepts.

---


### 299. [Beyond Accuracy: Prefix-Invariant Realizations of Low-Precision Fast Matrix Multiplication](https://arxiv.org/abs/2609.39816)

**<font color=#1a73e8>作者：</font>** Shuxiao Xie, Shuyang Xie, Yuan Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fast matrix multiplication saves multiplications through exact cancellation, but rounding sums that mix token rows can leave contributions from later tokens in earlier language model outputs. This threatens prefix invariance, which multiple-choice likelihood scoring relies on: a scored likelihood must depend only on its allowed prefix. On Qwen2.5-14B-Instruct, two fast FP8 realizations repaired to ordinary-looking accuracy still change the answers chosen by likelihood on 5.83% and 10.00% of 240 OpenBookQA items when only the text after the allowed prefix is replaced with the bf16 model's own greedy continuation. Both row-local controls, the bf16 model and a deployed FP8 matrix multiplication kernel, change none. Accuracy thus does not certify prefix invariance, and the stability criteria we analyze cannot tell realizations apart: across all 512 sign variants of two-level Strassen they stay constant while teacher-forced perplexities span a 772.4$\times$ range on the same model. We therefore construct certified realizations of two-level Strassen on bounded integer codes that quantize token rows independently, then mix and cancel exactly before rescaling, using 49 block multiplications instead of 64. Our certificate guarantees bitwise equality to a prescribed row-local classical int8 operator at the same quantization specification, so every certified realization inherits its prefix invariance. Certification thus turns realization choice into a pure cost decision: which certified realization runs can no longer change a single scored likelihood.

---


### 300. [Synthetic Pre-pretraining Survives Scale, but Not as a Grammatical Prior](https://arxiv.org/abs/2609.39827)

**<font color=#1a73e8>作者：</font>** Atsuki Yamaguchi, Tatsuro Inaba, Joel Niklaus 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pre-pretraining (PPT) on synthetic non-natural language data improves token efficiency during language model pre-training (PT). Prior work attributes this gain to a grammatical prior, i.e., a structural inductive bias learned during PPT that transfers to natural language grammar. However, PPT has only been tested on models of at most 1B parameters and PT budgets below 2B tokens on predominantly web text. It is unknown whether PPT is effective at larger scales and under more realistic PT data mixtures that combine diverse sources (e.g., code and math). We therefore present a comprehensive study on PPT spanning five PPT tasks, four PT data mixtures, four parameter scales (500M to 7B), and PT budgets of up to 100B tokens. Our results demonstrate that the downstream performance and token efficiency gains of PPT persist at scale, e.g., saving at least 21B PT tokens at the 3B scale. However, in contrast to prior work, we find no consistent evidence that these gains stem from a grammatical prior. Downstream performance does not consistently align with grammatical acceptability across model sizes. Instead, we find that downstream gains arise from PPT tasks that improve long-range retrieval. Finally, PPT performance gains are robust to how PT data mixtures are composed and diminish only when web text is absent. Overall, PPT is a low-cost addition to PT, and future PPT task design should target long-range retrieval rather than natural language grammar.

---


> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-390](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
