# 🧠 大模型相关研究 | 2026年11月03日

> 本类共 **188** 篇论文：已确认 **175** 篇，待复核 **13** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-188](./part-04.md)

---

### 1. [Automatic Construction of Strong Simple Baselines](https://arxiv.org/abs/2610.40700)

**<font color=#1a73e8>作者：</font>** Caleb N. Ellington, Jiaqi Wang, Sohan Addagudi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To rigorously establish the value of a novel deep learning method, it must be compared against appropriate baselines. As deep learning has become increasingly common in the physical and life sciences, there have been numerous cases in which apparent progress has turned out to be an artifact of omitted or missing baselines. In this work, we investigate whether this problem can be mitigated by using large language models to automate the construction of baselines. We assemble 36 supervised classification and regression tasks from peer-reviewed studies in Nature, Science, and Cell-family journals that investigate novel deep learning methods for scientific applications. We then use a language model to construct simple baselines for each task. These automatically constructed baselines are strong, recovering a median of 95.5% (mean 85.7%) of the gap between a trivial predictor and the score of the deep learning model. The median simple baseline matches or exceeds the performance of the deep learning model in 12 studies. We further examine the variation across scientific domains and publication venues and we characterize the effects of test-time compute and access to different levels of study context. As human peer review has struggled to keep up with the rapidly increasing volume of research articles in recent years, our results suggest that automated baseline construction is a practical and scalable check on deep learning contributions in the physical and life sciences.

---


### 2. [PrivacyFlow: Privacy in AI Agents through Information Flow Analysis and Consequence-Aware Risk Management](https://arxiv.org/abs/2610.40714)

**<font color=#1a73e8>作者：</font>** Robin Staab, Tom Wollschläger, Vahab Mirrokni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous LLM agents executing multi-step workflows over personal data often misalign with user privacy expectations and leak sensitive, out-of-context information. Although Contextual Integrity (CI) formalizes this problem, existing benchmarks and defenses rarely operationalize CI for realistic multi-step task sequences in evolving environments. In this work, we first introduce agentic PrivacyBench, a benchmark of 5873 tasks in 986 task sequences with dynamic environment updates and CI-grounded allow-sets for sensitive information. We also introduce PrivacyFlow, a defense that separates deliberative privacy planning (System 2) from task execution (System 1), treating each sharing decision as a structured risk-management problem. Before execution, PrivacyFlow traces the provenance and purpose of each planned data flow, models recipient background knowledge, and simulates what external actors could infer. This allows us to model the downstream consequences of disclosure, including inference attacks and context-dependent harms. It then weighs the remaining disclosure risk against task utility and executes a minimized plan, blocks it, or consults the user. Across six models, PrivacyFlow significantly reduces step-level privacy failures and raises the share of completed task sequences without a detected privacy violation by 22--55 percentage points. We further highlight a new privacy--utility--autonomy tradeoff: allowing PrivacyFlow to proactively prompt the user in case of uncertainty can increase authorized task completion at the cost of shifting decision effort back to the user. Our results suggest that proactive CI reasoning can substantially improve agentic privacy and motivate further study of this tradeoff.

---


### 3. [Characterizing LLM Agent Behaviors in Module Shadowing Environments](https://arxiv.org/abs/2610.40716)

**<font color=#1a73e8>作者：</font>** Shuai Yang, Enmeng Lu, Jinyu Fan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents operating in untrusted workspaces face the risk of untrusted code execution during routine tasks, yet final reports and workspace states alone cannot reliably establish whether execution occurred. We introduce an evaluation framework that codes observation, reasoning, execution, and response behaviors from agent trajectories and aligns them with independent environmental records to reconstruct execution histories and verify final reports. We apply this framework to module shadowing, in which a local file is loaded in place of a trusted module during import, enabling untrusted code execution without adversarial prompts. Across 90 trials with 15 models, the payload executed in 51% of direct shadowing trials and 87% of indirect shadowing trials. Even explicit recognition of the shadowing mechanism did not ensure prevention, as the payload ran in 10 of the 29 trials with recorded recognition. These failures were often omitted from final reports, as 49 of the 62 triggered trials ended without mention of the security issue. Three reports even denied execution, including one from a trial in which independent logs recorded 19 payload executions. Final workspace states also obscured prior execution when agents deleted or overwrote the payload marker in 10 triggered trials. These findings demonstrate that combining behavioral coding with independent environmental auditing enables rigorous and transparent evaluation of agent safety.

---


### 4. [MetaVul: Agentic Harness Discovery for Vulnerability Detection](https://arxiv.org/abs/2610.40721)

**<font color=#1a73e8>作者：</font>** Ira Ceka, Arnav Garg, Ryan Lutz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly used to automate vulnerability detection, but reliable detection is challenging because agents must distinguish subtle, security-relevant fixes from benign code variation. While underlying LLM capability has improved significantly, the accuracy of the agent still depends heavily on the harness: the code that defines the scaffolding around the LLM. Harnesses are typically fixed, and largely hand-written, limiting adaptation to evaluator feedback. Additionally, when harnesses are static, improvements on one dataset or model may not transfer to others. To address these challenges, we introduce MetaVul, a self-improving framework for harness discovery in vulnerability detection. Starting from a seed structured reasoning scaffold, MetaVul uses a workflow-based optimization loop to iteratively refine the harness using feedback from paired vulnerable and patched functions, while preserving the structured reasoning and verdict format. At each iteration, it searches over the history of prior harnesses, with access to their trajectories, logs, and metrics, and it returns a set of Pareto-optimal harnesses. We apply MetaVul to discover agent harnesses for various architectures. A validation set (202 pairs) is used for optimization, while an unseen dataset (430 pairs) is kept as the held-out set. We test whether harnesses learned from one model transfer to others not seen during optimization. Results on both frontier and small LLMs show that the optimized harnesses improve pairwise vulnerability detection up to 23.3 percentage points on the validation set and up to 25.8 points on the held-out set with a Pareto-frontier harness. Harnesses learned with one model also transfer to others. We show that harnesses optimized with one model transfer to another, improving held-out pairwise accuracy by 14.7 points without further optimization.

---


### 5. [Li$^{2}$SAO: Lifting Light Singl-Rollout Asynchronous RL Optimization via Group-Relative Actor-Critic Bootstrapping](https://arxiv.org/abs/2610.40726)

**<font color=#1a73e8>作者：</font>** Zichen Bai, Yanli Wang, Yang Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Asynchronous reinforcement learning (RL) is becoming a mainstream paradigm for post-training large language models (LLMs), as it improves training efficiency by updating the model as rollouts arrive. Recent work argues that group-wise sampling in GRPO does not naturally fit asynchronous RL training because rollout lengths follow a long-tailed distribution, and proposes Single-rollout Asynchronous Optimization (SAO) to improve stability and off-policy behavior, especially on agentic tasks. However, SAO relies on a closed-source value model obtained from scaling value pretraining. In this paper, we analyze GRPO and LiSAO, our lightweight reproduction of SAO without the pretrained value model, on single-turn reasoning and multi-turn agentic tasks. We find that GRPO outperforms LiSAO on reasoning tasks, while the reverse holds on agentic tasks. Since the value model of LiSAO is not yet well trained , LiSAO lags behind GRPO substantially in early training steps. To address this issue, we propose Li$^{2}$SAO, which Lifts Light Single-rollout Asynchronous Optimization with group-relative actor-critic bootstrapping: while the critic is cold, a group-relative advantage trains the actor and a group-centered return trains the critic, after which training switches to single-rollout GAE. Experiments show that Li$^{2}$SAO catches up with or surpasses GRPO in early training and further raises the later performance ceiling. Code is available at this https URL.

---


### 6. [RiskyPy: Toward Model-Calibrated Prompt Generation for Joint Security and Functionality Evaluation of LLM-Generated Code](https://arxiv.org/abs/2610.40735)

**<font color=#1a73e8>作者：</font>** Zacharie Chenail-Larcher, Daniele Lunghi, Melissa Tessa 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Evaluating approaches that improve the security of LLM code generation requires datasets that jointly assess security and functionality and remain adapted to the capabilities of the models being studied. However, existing benchmarks are costly to produce and are generally not calibrated to a chosen range of model capabilities. We introduce RiskyPy, an automated pipeline that generates security-oriented code-generation datasets calibrated to model proficiency using functionality and vulnerability canaries. We instantiate RiskyPy for Python using domains covering 18 CWEs from the 2025 CWE Top 25, producing 101 prompts. Experiments on Qwen3-4B and Seed-Coder-8B show that the generated tasks remain functionally accessible, with 57-72% of prompts yielding functional code, while only 5-10% of generations are free of Bandit findings, leaving room for joint evaluation of security and functionality of security improvement approaches.

---


### 7. [Prevented is Not Protected: What Attack Success Rate Hides about RAG](https://arxiv.org/abs/2610.40742)

**<font color=#1a73e8>作者：</font>** Chahana Dahal, Zuobin Xiong  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) is vulnerable to knowledge poisoning, where adversaries manipulate retrieved evidence to influence model outputs. Existing defenses are primarily evaluated using attack success rate (ASR), which obscures defense-induced failures and the mechanisms behind apparent attack prevention. To address this issue, this work introduces \textbf{Aligned RAG Evaluation}, a matched-query protocol that jointly examines clean and poisoned responses, with and without defense. By combining matched conditions analysis, LLM-judge endorsement, and retrieval dependence controls, the proposed framework distinguishes prevented from introduced failures, target mentions from LLM endorsement, and single-passage influence from evidence composition. Experiments on HotpotQA and Natural Questions reveal that existing defenses can introduce unexpected target-positive answers, although they can prevent some attacks, while evaluation criteria can also change defense rankings. Our findings expose critical blind spots in ASR-based evaluation and motivate a more comprehensive assessment of RAG poisoning defenses. The code and the evaluation artifact are available at this https URL.

---


### 8. [CLIC: Closed-Loop Intent Consistency for Securing LLM-Driven Control in Open RAN](https://arxiv.org/abs/2610.40744)

**<font color=#1a73e8>作者：</font>** Sunder Ali Khowaja, Kapal Dev, Joongheon Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the progressive capabilities of large language models (LLMs), researchers are finding ways to integrate them into the control loops of Open Radio Access Network (O-RAN) to enable slicing and resource management through user intents. However, integration of LLMs in the O-RAN control loop via the RAN Intelligent Controller (RIC) makes the system vulnerable to \textit{runtime prompt injection threats}, which manipulate control decisions without violating interface authentication, and \textit{residual virtual prompt injection (VPI)} attacks that plant trigger mechanisms to silently steer the behaviour during fine-tuning. Existing studies address only the runtime threat and do not enforce consistency across the full control path, i.e. from the certified A1 intent, through the multi-step LLM trajectory, to the final E2 action. We propose a closed-loop intent-consistency layer (CLIC) that jointly mitigates both threats. The proposed CLIC defines a formal consistency score using a small quantized language model, which is deployed as a Non-RT rApp for model-integrity certification along with a Near-RT xApp for runtime enforcement. We implement CLIC on the OpenAI Cellular (OAIC) platform and evaluate it under domain-adapted JailbreakBench, AdvBench, and VPI workloads. The experimental results show that the proposed CLIC reduces the attack success rate from 0.92 to 0.29 and residual VPI attacks from 0.37 to 0.04, while improving isolation and fairness at slightly higher latency costs, i.e. approximately 27 ms.

---


### 9. [Mage-VL-Cowork: A Full Training Recipe to Learn Hybrid Computer Use From Evolved Harnesses](https://arxiv.org/abs/2610.40747)

**<font color=#1a73e8>作者：</font>** Xiaoyi Zhang, Haoqing Wang, Xinjie Zhang 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Effective computer-use agents (CUAs) should seamlessly combine visual GUI interaction with code and terminal execution within a single policy. We present Mage-VL-Cowork, a 4B hybrid CUA trained from a general multimodally aligned checkpoint through an end-to-end, progressive five-stage curriculum across midtraining, SFT, and RL. To power this curriculum at scale, Mage-CUA-Forge replaces per-task agent construction with reusable, skill-conditioned generation workflows and application-specific preparers, synthesizing 293,806 desktop and web tasks across 6,915 skills while reducing recurring per-task expenditure by 82.6%. Rather than directly distilling a default teacher, we evolve the teacher harness and instantiate specialized CUA harnesses to yield high-quality trajectories alongside stage-specific supervision. Mage-VL-Cowork-4B finally climbs to 66.0% on OSWorld-Verified through different training stages with more efficient reasoning cost, achieving state-of-the-art performance at its parameter size and pushing forward the frontier of on-device intelligence.

---


### 10. [Safin-1.5: Safety-Native Architecture and Verifiable Reasoning for Recursive Safety Improvement](https://arxiv.org/abs/2610.40751)

**<font color=#1a73e8>作者：</font>** Jingnan Zheng, Cheng Jin, Ming Zhang 等 31 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement (RSI) enables large language models to advance their capabilities through successive updates, but these updates can also introduce new risks and weaken existing safeguards. In line with the AI-45° Law, we pursue Safety RSI, in which safety develops as an intrinsic capability alongside general model capabilities through continual risk discovery and repair, while preserving utility and limiting over-refusal. We introduce Safin-1.5, a model built on a safety architecture and trained through recursive safety improvement, with an inference-time harness that extends its capabilities to formal reasoning. Our approach comprises three components: i) The safety architecture combines persistent safety states with hazardous-knowledge disentanglement. The former retains and selectively invokes safety knowledge, while the latter relocates targeted hazardous knowledge into removable experts, enabling its removal with minimal impact on general capabilities. ii) Recursive safety improvement establishes a discovery-evaluation-repair loop. The loop identifies new vulnerabilities and uses experimental feedback to develop repair strategies. It accepts updates only when they improve safety while preserving general capabilities and limiting over-refusal. iii) The formal reasoning harness combines the model's language understanding with symbolic inference and verification. Proof-obligation-guided semantic bridging recovers missing relations in formal representations, enabling symbolic solvers to construct checkable proofs under formalized premises and accepted semantic bridges. Experimental results demonstrate that Safin-1.5 achieves safety and reasoning performance, outperforming frontier models.

---


### 11. ["Shall We Approve?" Consequence-Aware Approval for Autonomous Coding Agents](https://arxiv.org/abs/2610.40753)

**<font color=#1a73e8>作者：</font>** Weiheng Wu, Junkai Chen, Zhensu Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Coding agents increasingly rely on automated approvers to decide whether a proposed shell command may run. Existing approvers, from rule-based checkers to guardrail models and deployed permission classifiers, base their decisions on the text of the request and command. Yet a command's behavior depends on the code it invokes and the state of the workspace, and systems that observe file changes leave the assessment to the agent or a human after execution. We present Caper, a consequence-aware approval mechanism that pre-executes each command in a snapshotted sandbox, provides an independent approver with a bounded report of its observed effects, commits allowed commands, and rolls back blocked ones with a reason the agent can act on. Compared with six existing systems, Caper achieves the lowest harmful-outcome rate on SABER (6.7% versus at least 14.8%) and YoloFS-Ext, a benchmark we build in which harmful behavior is hidden inside invoked tools (7.8% versus at least 35.3%), while blocking 1.0% of the safe twins of the dangerous tasks in YoloFS-Ext.

---


### 12. [DyCraft: An Agentic System for Long-Horizon 4D Scene Generation](https://arxiv.org/abs/2610.40754)

**<font color=#1a73e8>作者：</font>** Jeff Tan, Hang Dai, Zeqian Long 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While frontier coding agents can generate high-quality 3D scenes and articulated assets, they struggle to create coherent long-horizon animations. When equipped with general-purpose harnesses, they frequently produce physically implausible outputs, generating objects that interpenetrate, lack physical support, or move unnaturally. Such bare agents struggle to repair these errors because they default to scripting the full animation in one pass, making it difficult to verify their work and disentangle complex spatiotemporal constraints. Drawing on the practice of human animators, we introduce DyCraft, a system for animated 3D scene generation that breaks animation into steps that coding agents can more reliably solve. DyCraft first expands the user's prompt into a detailed plan and builds a static scene. It then creates a 3D storyboard of key animation poses, where each frame is a static 3D scene that the agent can build and debug in isolation. Storyboarding decomposes the problem into pairs of verified start and end states, allowing the agent to author local motion between them with a collection of motion authoring tools. We evaluate DyCraft on 24 long-horizon, multi-shot animation tasks covering humanoid robots, human and animal characters, and physical mechanisms. Compared with a native GPT-6 agent in Codex and prior agentic baselines, DyCraft substantially reduces physical violations and generates higher-quality animated 3D scenes that are more often preferred by human raters.

---


### 13. [More Rules, Longer Lists? Benchmarking Self-Evolving Agents on a Hidden-Rule Curriculum](https://arxiv.org/abs/2610.40758)

**<font color=#1a73e8>作者：</font>** Chenjie Qiu, Boyan Xu, Shaobin Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving agents rewrite a persistent state from feedback, but it is largely untested whether this lets them learn a rule nobody told them. An agent can also pass by writing down each correction as an exception, and its list then grows with every new rule. We introduce CLR-Bench, a Curriculum of Latent Rules benchmark. Each chain adds one hidden rule per level on top of the earlier ones. A rule acts on an opaque label that stands for a named grouping published on the Web, such as the founding members of an airline alliance. The task gives one example value, practice feedback reveals one more member and one non-member, and the test checks unseen members and similar non-members. Probes certify that the base model knows the members of each grouping and does not guess it without feedback, and that the evidence identifies the grouping once labels are read as named groupings. An automated pipeline builds chains from a new data domain, and we release 20 chains over 10 domains. We evaluate six recent self-evolution methods. With the certifying model they barely learn. The best gain at most 5 points over a frozen agent and exclude only 6-12% of the unseen members from the count, fewer than the 20% reached by simply keeping the raw practice history. A fixed lesson that states the named-grouping convention lifts the same methods by 14.5 to 16.5 points. Their states hold the revealed member in 75-98% of cases and almost never the class name, and when practice exposes a member the list misses, they add that member to the list. With the stronger GPT-6-Sol, ACE and Dynamic Cheatsheet learn from feedback alone. They reach 78% accuracy and solve 59-60% of the single cells, against 53% and 8% with the certifying model, and they surpass the raw history. CLR-Bench therefore measures how well an agent learns, and this ability differs across models.

---


### 14. [Drone-PUR: From Visual Clue Discovery to Understanding and Reasoning in UAV Scenes](https://arxiv.org/abs/2610.40801)

**<font color=#1a73e8>作者：</font>** Jiahe Wu, Bing Cao, Xingyue Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The reasoning capabilities of vision-language models (VLMs) can be limited by incomplete or inaccurate visual observations in the general domain. In unmanned aerial vehicle (UAV) scenes, small targets, subtle attributes, and changing viewpoints further complicate perception and understanding. Therefore, we introduce Drone-PUR, a dataset and benchmark organized around visual clue discovery, interpretation, and integration, corresponding to the three capability dimensions of perception, understanding, and reasoning. Reasoning samples are designed to require models to combine multiple visual clues to derive visually grounded conclusions. Its 11 tasks provide 175k training and 20k test samples spanning single images, image sequences, cross-modal images, and multiple viewpoints. All test samples undergo human review. Evaluating 22 general-purpose VLMs reveals persistent limitations in spatial judgment and cross-modal and cross-view reasoning. Across models, stronger perception is associated with better reasoning, while single-task fine-tuning further reveals selective bidirectional transfer between these capabilities. To examine domain adaptation, we develop UAV-PUR from Qwen3-VL through staged fine-tuning with auxiliary supervision. Its 4B and 8B variants improve overall multiple-choice accuracy by 18.33 and 17.52 percentage points over their pretrained counterparts, respectively. The dataset and project resources are available at this https URL.

---


### 15. [The Generative Gap Between Speculative Drafter and Continuous Diffusion Language Model](https://arxiv.org/abs/2610.40847)

**<font color=#1a73e8>作者：</font>** Yujian Chen, Hao Jiang, Guang Cheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continuous diffusion language models (CDLMs) and speculative drafters offer efficient language generation but are typically evaluated differently: CDLMs generate independently through iterative refinement, whereas drafters propose text for target-model verification and correction. We compare their architectures without verification, using LangFlow for CDLMs and adapting DSpark's Markov and recurrent-head architectures for standalone generation. All models are trained from scratch for unconditional, single-block OpenWebText generation at lengths 16, 128, and 1024, without target features or verification, using common preprocessing, backbone dimensions, and training-update budgets. We evaluate generation perplexity (GenPPL) with an external language model and distributional similarity to reference text with MAUVE. With default denoising steps equal to sequence length, LangFlow outperforms both DSpark variants on both metrics at lengths 128 and 1024, while DSpark-RNN leads at 16. A conditional KL analysis characterizes dependencies excluded by the Markov head's previous-token conditioning. Recurrent memory removes this restriction and improves both metrics, but the longer-sequence gap persists. Teacher probability matching further lowers Markov GenPPL without observed MAUVE gains. Increasing LangFlow's denoising steps at fixed weights improves both metrics at lengths 16 and 128, changing the length-128 ordering relative to DSpark-RNN. These results establish LangFlow's longer-sequence advantage under the evaluated budgets and highlight iterative full-sequence refinement as a route to improving standalone generation beyond gains from recurrent head memory.

---


### 16. [FARO: Function-Space Adaptive Return-to-Risk Optimization via Cross-Block Equal-Risk-Contribution Budget Allocation](https://arxiv.org/abs/2610.40858)

**<font color=#1a73e8>作者：</font>** Xiaojun Wu, Cehao Yang, Xuhui Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training a large language model is compute-bound, and current recipes divide the work between optimizers by hand: orthogonalized momentum for attention and MLP matrices, Adam-style updates for the rest. This division rests on human priors about which layer type deserves which geometry, and it fixes a single global update budget that every parameter block shares. We introduce FARO, a function-space adaptive optimizer that makes the partition of parameters into blocks the unit of decision. FARO gives each block a geometry by its realized counterfactual return, then freezes the routes and reallocates the frozen per-block budget by cross-block equal risk contribution (ERC), the risk-parity principle from portfolio theory. On a GPT-style model trained on FineWeb, the framework gives two results. First, its FARO-Adaptive arm reaches 3.2780 nats at the full schedule, matching NorMuonAndAdam (3.2794), the best hand-designed recipe: it recovers the human prior without hand-setting per-layer geometry. Second, FARO-ERC improves on that arm: it lowers the clean-data loss at every one of 6 seeds, by 0.0136 nats on average, a modest but robust gain. Its sign test, paired test, and confidence interval all agree, and it exceeds the measured run-to-run noise at no added time or memory. It works by trimming the riskiest blocks rather than expanding the safest, and it holds up under a corrupted stream, still lowering the mean loss and winning the seed majority. The source code is available at this https URL.

---


### 17. [Incongruence-Aware Evaluation of Multimodal Speech Emotion Recognition in Audio Large Language Models](https://arxiv.org/abs/2610.40883)

**<font color=#1a73e8>作者：</font>** Fengji Jing, Guy Laban  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Voice-interactive large language models process both what a speaker says and how they say it, yet the two channels do not always agree. We ask whether that disagreement degrades speech emotion recognition. Mapping text and audio into a shared valence-arousal-dominance space, we convert the distance between them into a continuous, threshold-free incongruence score with a two-component Gaussian mixture, and validate the score against human judgement. We evaluate three audiocapable models on acted, conversational and spontaneous speech (eNTERFACE'05, MELD and CMU-MOSEI). With the model held constant across modalities, incongruence raises the odds of error whenever audio is present, in every corpus, after controlling for the ground-truth emotion and for distance in the feature space. Supervised classifiers trained on the same features behave in the opposite way, which suggests that the difficulty lies in how these models combine raw evidence rather than in the signal itself. Text-only effects are unreliable: swapping only the model that reads the transcript reverses their sign on one corpus. Rebuilding the score without the emotion lexicon reproduces the central result, and among six simpler alternatives it is the only label-free score that predicts error in all three corpora. Code, data tables and prompts are released.

---


### 18. [ChatGPT as a Surveillance Assistant? An Exploratory Case Study of AI-Assisted Surveillance Risks](https://arxiv.org/abs/2610.40890)

**<font color=#1a73e8>作者：</font>** Ayana Hussain, Nicholas Vincent  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate detailed guidance, functional code, and persuasive text at scale. As one of the most widely used consumer language model products as of 2026, ChatGPT gives broad public access to these capabilities, motivating concerns about its potential use in surveillance-related tasks. We present an exploratory case study of what potentially harmful surveillance assistance looks like in ChatGPT's public web interface. We contribute a taxonomy of seven surveillance risk categories based on prior LLM risk research and reports of deployed surveillance systems, instantiated as 110 prompts, along with a manually reviewed analysis of ChatGPT's responses. Prompts were issued using two approaches: 55 jailbreak prompts drawing on five types of elicitation strategies, and 55 plain-language direct prompts, each run alone, and if unsuccessful, again with a short fixed prefix. We find that ChatGPT provides substantive surveillance guidance for 40 of the 55 jailbreak prompts and for 33 of the 55 direct prompts without any prefix. Compliant responses also rarely included policy mentions or suggestions for privacy-preserving alternatives. We manually review every response and find that even when ChatGPT states a refusal, it may still supply detailed instructions, working code, or architectural guidance alongside brief ethical caveats.

---


### 19. [Qistas: A Pre-Registered, Portable Protocol for Fairness Evaluation of Large Language Models](https://arxiv.org/abs/2610.40893)

**<font color=#1a73e8>作者：</font>** Nawar S. Alseelawi, Mustafa S. Aljumaily  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fairness benchmarks for large language models (LLMs) are overwhelmingly English-born and American in their social categories; translated versions carry those categories into societies where they do not apply, and almost none fix their hypotheses before the models are run. We present Qistas (Arabic qistas, "the just balance"), a protocol for evaluating how LLMs treat the social, confessional, and regional constituencies of a society, portable across countries and instantiated first for Iraq. In its pilot form it measures only what needs no verdict on contested truth: procedural symmetry across matched counterfactual pairs, differential refusal, stereotype reliance under ambiguity, and terminological framing of documented events. Every measurement is paired by construction and analysed with paired machinery (sign-flip permutation tests, exact McNemar tests, template-clustered bootstrap intervals, Holm-corrected families), with a power analysis that states, before any data exist, the smallest effect each axis can detect after the design effect of template clustering. We release the authoring apparatus (a pruned 3x5 taxonomy with four cells closed by design, per-type checklists, a cumulative rulings log, a structural audit, and a human review notebook) and report its first field test: a semantic review of a 58-item seed bank in which 24 of 25 template groups failed at least one check. The defect patterns it exposed (evaluation criteria leaking into prompts, token-level swaps that break Arabic agreement, epistemically unbalanced pairs, single-theme refusal probes, unwritten dialect twins counted as coverage) are, we argue, general hazards of counterfactual fairness benchmarks. This is a protocol paper, not a results paper: no model has been evaluated, and the accompanying pre-registration commits the hypotheses, metrics, exclusion rules, and analysis plan that the pilot will follow.

---


### 20. [TSFLab: A Self-Improving Agent-Agnostic Workbench for Time Series Forecasting Research](https://arxiv.org/abs/2610.40901)

**<font color=#1a73e8>作者：</font>** ChengAo Shen, Yanjun Zhao, Haoxin Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As publications and products on time series forecasting (TSF) proliferate, researchers face a growing burden of analyzing existing work. First, not all publications release code. For instance, only about 20% of arXiv TSF papers have a code link in the surveyed period. Second, released code also requires manual maintenance. Thus, TSF researchers must constantly adapt or implement existing works. However, independent implementations can differ in experimental settings and are difficult to maintain. We therefore propose to use AI agents for benchmarking TSF research and even supporting autoresearch, e.g., developing new TSF models. Yet directly applying existing coding agents, such as Claude Code and Codex, is suboptimal: prohibitive costs, limited scalability to large research projects (e.g., benchmarking), and lack of self-maintenance. To address these challenges, we propose TSFLab, a self-improving agent-agnostic "workbench" that equips compatible coding agents with shared resources and tools for low-cost TSF research and continuous maintenance of research resources. Our experiments cover reproduction, benchmarking, and new method development. In reproduction and benchmarking, TSFLab improves task completion by 20-163% and cuts fresh tokens per completed task by 11-66% across baselines. A pilot study of agent-driven method development also shows improved forecasting accuracy via TSFLab, with 32.8-73.6% fewer fresh tokens and 9.2-68.8% less development time than the other settings.

---


### 21. [Does Recursive Knowledge Construction Help Agents Verify Consensus Claims in Science?](https://arxiv.org/abs/2610.40906)

**<font color=#1a73e8>作者：</font>** Lun Ai, Yu-Heng Wu, Jonathan Schaul 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent scientific agents build knowledge recursively by retrieving evidence, constructing an intermediate state, and judging whether that state contains sufficient information. These agents are evaluated end-to-end, usually without ground truth, so the effect of each design choice is unknown. Here, we examined two design axes: (1) what the recursion builds (the state of evidence) and (2) what controls it (the judge that decides when to stop). To measure them, we defined consensus scientific claim verification and measured these effects on this task, where a system must establish a claim's consensus stance from the open literature. We built a new consensus claim dataset, ProClaim-eval, including 718 claims with SUPPORT and REFUTE gold labels from five expert-curated databases spanning molecular biology, nuclear physics, and astronomy. Our instrument, ProClaim, persists an evidence state outside the model's context, so each axis can be studied with the other held fixed. Against verification systems and general-purpose agent harnesses, ProClaim ranks among the top three, with a significant advantage over the harnesses. We found that the evidence state improves performance over in-context accumulation, and it also matters what is stored in it. In addition, a trained judge that reads the evidence state performs better than fixed-round stopping. A judge trained separately and never exposed to ProClaim-eval achieves the highest agreement with the gold labels on three of five subsets, where it matches the off-the-shelf Claude Sonnet~4.6 judge and outperforms Claude Haiku~4.5. Our results support recursively maintaining a structured evidence state outside the model's context as an effective design for verifying claims in scientific agents.

---


### 22. [Coupled or Independent? Fault Coupling in Agentic Medical Vision Systems](https://arxiv.org/abs/2610.40913)

**<font color=#1a73e8>作者：</font>** Nishi Kanta Paul, Md Shihabul Islam Shovo, Md Mostafijur Rahman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language agents equipped with tools expose intermediate outputs for inspection and comparison with the model's reasoning, which may offer safety benefits over single-shot models. This paper tests that potential benefit when the sensor reading itself is untrusted, so that the tool and reasoning channels share a common visual fault. We consider a dermatology agent based on segmentation, contrastive retrieval, and an iterative vision-language reasoner and define a coupling taxonomy that distinguishes single-channel errors from joint errors that agree or disagree. On PAD-UFES-20, we show that typographic injection produces detectable directional retrieval capture, whereas physical corruption does not. Crop-first retrieval preserves the payload at a readable scale and produces 55% joint wrong agreement across all cases (71% of faulty cases); full-image retrieval produces 35% (43%). Under a binary decision, if both channels are wrong, their predictions must agree, so hard-label channel comparison cannot detect joint failures, limiting disagreement recall to 0.29 (crop-first) versus 0.57 (full-image). The direction of the order effect is reproduced on the independent HIBA test set.

---


### 23. [Agentic World Modeling for Agent Test-time Scaling without Environment Replica](https://arxiv.org/abs/2610.40927)

**<font color=#1a73e8>作者：</font>** Wendi Li, Huseyin A. Inan, Wei-Ning Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time scaling (TTS) improves large language model agents by sampling and selecting among multiple candidate trajectories, but common realizations assume that these trajectories can be executed in parallel. This assumption breaks in realistic deployments, where enterprise workspaces and cloud services are shared and persistent, costly or infeasible to replicate, and actions may introduce irreversible side effects or cross-trajectory interference. Existing generative world models avoid direct execution, but typically compress environment state into a single prompt, limiting their ability to reliably simulate transitions under partial observability. Instead, we introduce Agentic World Modeling (AWM), which reformulates next-observation prediction as a multi-turn evidence-acquisition task. For each hypothetical action, an agentic simulator adaptively queries the real environment through safe read-only interfaces, reasons over the returned evidence, and uses executable computation to construct the resulting observation without mutating shared state. Integrated with trajectory-level TTS, AWM enables parallel exploration over a single shared environment. Across $\tau$-bench, AppWorld, and OfficeBench, AWM outperforms a single-shot simulation baseline by 40.07% on average, and surpasses a trained world-model baseline by 12.36% on average. These results establish interactive, read-grounded simulation as a practical foundation for safe and scalable agentic test-time scaling in shared, non-resettable environments.

---


### 24. [Adaptive Personalization Under Preference Epistemic Uncertainty](https://arxiv.org/abs/2610.40930)

**<font color=#1a73e8>作者：</font>** Priyanka Dey, Rajarshi Das, Vikas Bahirwani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human preferences change over time: an established preference may remain valid over time, become uncertain as context shifts, or be explicitly revised. Effective personalization requires conversational AI to adapt its response strategy to evolving preferences rather than relying on passive memory retrieval. We formalize this capability as adaptive personalization under epistemic uncertainty. A human preference study further confirms that people favor state-contingent response strategies as preference uncertainty changes. To evaluate whether language models mirror this adaptation, we create a multilingual benchmark spanning 250 personas, 5 languages, and 25K conversational turns that decouples strategy selection from response execution. Across eight closed- and open-weight models, we uncover a recognition-generation gap: models reliably identify appropriate strategies when selecting among candidate options, but collapse during open-ended generation, suffering a 35-46% drop in strategy calibration. Crucially, this failure is systematic: models default to exploit-first behavior, over-relying on existing preferences regardless of preference epistemic uncertainty. We show this failure is addressable: while prompting interventions fail, targeted training that supervises models' internal strategy representations toward state-conditional human preferences narrows the user acceptability generalization gap by a third on out-of-distribution personas and conversational styles.

---


### 25. [DiRAFT: Privacy-Aware Financial Transcript Synthesis from Aggregate Discourse Priors](https://arxiv.org/abs/2610.40938)

**<font color=#1a73e8>作者：</font>** Yunbai Zhang, Yunyi Gao, Han-Tai Shiao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Using customer conversations to train and evaluate financial language models raises confidentiality concerns because non-public financial facts can remain after direct identifiers are masked. Synthetic transcripts offer an alternative data source, but their discourse fidelity and residual confidentiality risks require assessment. We introduce DiRAFT (Discourse Realization from Aggregate First-order Transitions), which extracts financial concept graphs and records the order in which concepts are first introduced. It pools adjacent concept transitions across training records and samples new graph plans from aggregate transition, starting-concept, and plan-length priors. A discourse layer guides text realization without supplying an individual source passage or graph. We assess privacy-related risks through two complementary evaluations: corpus-level structural overlap and source-grounded checks for specific non-public investor facts. The structural assessment covers two financial corpora and three generation backends. The confidential-fact assessment uses human review of 1,400 investor-call outputs across seven strategies and two backends. We also evaluate transition fidelity, content recoverability, and trajectory diversity. Stochastic sampling provides a favorable balance between transition fidelity and structural overlap, with consistent advantages over greedy and top-3 on investor calls. The confidential-fact assessment likewise detects fewer matches for stochastic sampling than these alternatives on both backends covered by the fact assessment. These complementary assessments provide empirical evidence on residual confidentiality risks without establishing a formal guarantee.

---


### 26. [The First Few Tokens Matter: Understanding Chain-of-Thought Controllability](https://arxiv.org/abs/2610.40939)

**<font color=#1a73e8>作者：</font>** Hugh Van Deventer, Dmitrii Troitskii, Laura Ruis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) monitoring is a promising way to oversee increasingly capable agents. It succeeds in part because current models appear limited in their ability to control what they verbalize in their reasoning traces. We investigate the source of this limitation and link it to an entropy collapse in the first few tokens following the opening thinking tag. We exploit this mechanism to recover CoT controllability through two inference-time interventions on initial tokens: prefilling, where even a single token can substantially increase controllability, and banning frequent opening tokens combined with in-context examples, which improves average compliance by 34-41 percentage points across models. These interventions recover mainly addition and style controllability (adding or transforming information), while suppression controllability (avoiding or removing information) exhibits more varied responses, suggesting distinct underlying mechanisms. Consistent with this, the two groups behave as separate capabilities: across models, performance correlates positively within these groups, while cross-group correlations are mostly negative. Importantly, we find that the relationship with monitorability depends on the evaluation: addition and style controllability more consistently positively correlate with monitorability, while suppression often shows negative associations. Our findings motivate the development of controllability evaluations that distinguish difficulty initiating a specific opening from general limitations of the ability to alter reasoning content, alongside separate reporting of control tasks and categories.

---


### 27. [Kernel-based Interpolatory Methods for Context Compression of Attention Mechanisms](https://arxiv.org/abs/2610.40943)

**<font color=#1a73e8>作者：</font>** Michel Fabrice Serret, Laura Grigori  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The bottleneck of attention mechanisms, which are the fundamental building block of modern language models, is their quadratic complexity in terms of context size. There has thus been an increasing interest in the compression of the context, also called KV-cache compression. In this article, we consider the problem of compressing the context of attention mechanisms by first formulating it in the Hilbert space associated with its kernel. In this formalism, attention can be represented as the ratio of two linear maps whose interpolant is also the ratio of interpolants, this allows us to consider the interpolation of the linear maps directly. We thus introduce two novel KV-cache compression methods which we call GAIM and Q-DAIM, based on the Generalized Empirical Interpolation Method (GEIM) and the Q-Discrete Empirical Interpolation Method (Q-DEIM), respectively. As the cost of these methods is quadratic in terms of context length, we propose surrogate models based on the Taylor series, the Performer and the Random Fourier Features method which allow the compression to be done in linear time. Finally, we extend this result to the streaming attention setting, providing new methods which allow one to penalize the selection of interpolation nodes based on the previously interpolated context and to update the previous interpolation based on new information. We then provide numerical results on the convergence of the residuals and the output error in future queries and preliminary results on the LongBench-E benchmark showing performance comparable to the state-of-the-art methods. These experiments suggest that the range revealed by our Q-DAIM method could help identify where information is concentrated in the KV cache, thus enabling an efficient compression.

---


### 28. [On the Origin and Evolution of Training-Inference Mismatch in LLM Reinforcement Learning](https://arxiv.org/abs/2610.40945)

**<font color=#1a73e8>作者：</font>** Yu Li, Yufa Zhou, Tian Lan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy reinforcement learning for large language models assumes that training responses are sampled from the current policy. In practice, an inference engine samples the responses and a separate trainer computes the gradients, and the \textbf{training-inference mismatch} between the two makes the training data off-policy. The mismatch has two sources, the numerics of the engine and the stale weights of asynchronous sampling, and a correction that stabilizes training under one source can fail under the other. \textit{We ask which property of a mismatch source decides the correction it needs.} Evaluating the trainer at the sampler's weights splits each sampled-token error exactly into a \textit{numerical discrepancy} of the engine and a \textit{policy lag} of the trainer, and we follow both through training. The numerical discrepancy stays approximately constant, so it biases the updates by a nearly fixed amount, and centering the score at each prefix removes its leading bias. The policy lag is produced by the trainer's own updates: the bias it leaves enters the next update, which enlarges the next lag and closes a feedback loop. Importance weighting cuts this loop only while the lag ratio stays concentrated, and on Qwen3-1.7B it fails at the step where the effective sample size of the ratio falls below one half. From this account we derive the \textbf{discrepancy-lag correction} (DLC), which centers the numerical discrepancy, clips the lag ratio against the sampler's weights and resynchronizes the sampler when this effective sample size falls below one half. Under a stale sampler, DLC keeps the KL divergence from on-policy training within twice the KL between two independent on-policy trainings on Qwen3-0.6B and Qwen3-1.7B, and its resynchronization prevents collapses that the per-token corrections leave and that a KL measured on the sampler's prefixes does not detect.

---


### 29. [Opening the Box Changes the Cat: LLMs Detect Chain-of-Thought Monitoring - What now?](https://arxiv.org/abs/2610.40946)

**<font color=#1a73e8>作者：</font>** Amir Jalilifard, Marcos Medeiros Raimundo, Anderson Rocha  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) reasoning allows large language models (LLMs) to generate intermediate reasoning traces in natural language while solving complex tasks. These traces can support safety monitoring by exposing potentially harmful plans before actions are executed. In this work, we investigate the conditions under which LLMs infer the presence of CoT monitoring from direct and indirect environmental cues and examine how this inference affects their subsequent behavior. Our observations suggest that oversight is an interactive process: while a monitor inspects a model's reasoning, traces left by monitoring interventions can allow the model to infer that its thoughts are being observed and to adapt its behavior accordingly. We show that even subtle environmental cues, such as timing-related signals from timeouts and operation durations, can reveal the presence of monitoring and trigger models to adapt their behavior. Across repeated episodes and interaction loops, we further observe that models can form statistical estimates of the monitor's effectiveness and use these estimates to guide attempts to evade detection. These findings highlight the need to evaluate CoT-based oversight under adaptive conditions, where the monitoring process itself may influence the behavior it seeks to observe.

---


### 30. [P-ContextBench: From Personal Fact Recall to Personalized Agent Behavior](https://arxiv.org/abs/2610.40959)

**<font color=#1a73e8>作者：</font>** Grant Nasir Brown, Abdul Basir Bari, Anmol Tadikonda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for personal tasks, yet evaluating their safe use of personal context remains difficult because such contexts are private, fragmented, dynamic, and socially situated. We introduce P-ContextBench, a realistic, verifiable, and scalable benchmark for evaluating personal-context understanding. P-ContextBench constructs population-structured, life-story-grounded digital humans from demographic seeds reflecting the U.S. population. Rather than using explicit, static profiles, P-ContextBench embeds traits, routines, goals, and constraints as implicit evidence across fragmented, evolving synthetic mobile-app records. It evaluates five capabilities: single-source fact recovery, multi-source fact recovery, temporal state tracking, inference of higher-level personal patterns from routine behavior, and safe handling of requests conflicting with persona-specific constraints through compliance, warning, clarification, or refusal. A multi-stage validation pipeline checks persona plausibility, context recoverability, information leakage, evidence preservation, test-case grounding, and human-judge agreement. We instantiate P-ContextBench with 100 personas, 10,088 hidden facts, 18,261 app-trace fragments, and 4,810 verified test cases. The pipeline supports configurable generation across scales and demographic groups. Cost-effective state-of-the-art (SOTA) LLMs relevant to personal agents achieve below 60% accuracy on temporal tracking, higher-level pattern inference, and constraint-aware action-boundary decisions, with fewer than 10% of test cases answered correctly across all three repeated runs. Even a high-performing SOTA model remains inconsistent on these capabilities. P-ContextBench provides measurable targets for improving the accuracy, reliability, and safety of LLM-based personal agents.

---


### 31. [Better Retrievers, Worse Labels: How Incomplete Relevance Judgments Distort Abstention Evaluation in Conversational RAG](https://arxiv.org/abs/2610.40966)

**<font color=#1a73e8>作者：</font>** Ivan Kochergin, Vasily Konovalov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational RAG benchmarks such as MTRAG and RETECO evaluate retrieval and generation end to end: each system answers from its own retrieval, so abstention must be scored against whether each retrieved context is sufficient. A convenient shortcut reads sufficiency off the relevance judgments and treats a context without gold documents as unanswerable. We re-run the official baselines exactly and test this shortcut on RECOR (RETECO track~2) with four retrievers (nDCG@10 from .18 to .59) and three Qwen3 readers. Two open LLM judges and a panel of four small open models label each context by content, and a model of another family audits 250 contexts blind, with adjudication. The stronger the retriever, the larger the share of no-gold contexts that still contain the answer (28\% to 72\%) and the lower the shortcut's precision (.68 to .10; .70 to .21 under the audit). A reader agrees: Qwen3-4B answers 62--67\% of these false misses correctly, against 23--30\% of no-gold contexts judged insufficient and 1\% with no documents. In most false misses, the answer comes from a hard negative mined for the same question, another turn's gold or a neighbouring chunk of the gold page. On MTRAG, whose judgments come from annotators, precision drops from .72 to .50. Under the shortcut, answerability AUROC is up to .19 too low, and the best sufficiency detector appears to be a retrieval score that never reads the documents. We release code, runs and labels, and recommend scoring refusals against content labels, not the presence of gold.

---


### 32. [Nedimo: An Evidence-Grounded Multilingual Pipeline for AI-Generated Sleep Stories](https://arxiv.org/abs/2610.40970)

**<font color=#1a73e8>作者：</font>** Georgios Makridis, Stefanos Kampouris  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative audio systems can produce large libraries of personalized bedtime content, but ordinary media objectives (retention, completion, and novelty) are poorly aligned with the goal of supporting a transition toward sleep. Direct evidence for narrated bedtime audio in adults is mixed, and a recent active-controlled trial did not support such audio as a standalone treatment for sleep disturbance. We translate this uncertain evidence into conservative engineering requirements and present a multilingual pipeline for generating and narrating low-arousal sleep stories. The implemented prototype separates deterministic planning from large language model generation, represents content and delivery parameters explicitly, shapes each script through a four-phase attention taper, validates structural and lexical constraints, performs a bounded error-aware retry, and quarantines unresolved outputs. Provider-agnostic text-to-speech synthesis is followed by paragraph-aware joining, two-pass loudness normalization, and a publication gate that re-measures the saved, encoded file against fixed loudness, loudness-range, and true-peak limits. The product data model records stop position, replay, early abandonment, and completion while treating these events as ambiguous behavioral proxies rather than clinical outcomes. We contribute an evidence-to-requirement mapping, a traceable guardrail architecture with explicit acceptance thresholds, technical evaluation criteria, and a prospective protocol for testing sleep-onset effects. No clinical efficacy is claimed; the system is positioned as a relaxation and attentional-support tool whose benefit and possible reliance must be evaluated empirically.

---


### 33. [FieldGuideRAG: Image-Grounded GraphRAG for Fine-Grained Recognition with Vision-Language Models](https://arxiv.org/abs/2610.40971)

**<font color=#1a73e8>作者：</font>** Jiacheng Ding, Yanliang Qi, Cong Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present FieldGuideRAG, a training-free GraphRAG method in which a vision-language model, or VLM, recognizes fine-grained species by comparing the query with real photographs stored on the nodes of a knowledge graph. Multimodal GraphRAG systems describe each entity in text, and text conveys little of the visual detail that separates look-alike species. Our graph stores one photograph on every species node and links each species to its relatives, its geographic range and its ecological facts. A frozen VLM verifies the query against the photograph of each candidate node. FieldGuideRAG fuses the verification scores with the range edge and answers questions about the organism from the fact edges of the verified species. On CUB-200, a Wikidata graph and four iNaturalist domains, the node photograph improves verification over the species name on every graph, while text descriptions add little. Verification of the candidate pool exceeds a SigLIP retriever by up to 16 points, the range edge adds 7 to 19 points on iNaturalist, and answering from fact edges is correct on up to 89.5% of 28,820 ecological questions. The verification scores also detect queries whose species is missing from the graph. Graphs, prompts and code will be released.

---


### 34. [Fewer Heads, Fewer Memories: Pruning Redundant Attention Heads Suppresses Verbatim Memorisation](https://arxiv.org/abs/2610.40974)

**<font color=#1a73e8>作者：</font>** Aryan Chowdhury, Riza Batista-Navarro  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have been shown to memorise and reproduce verbatim sequences from their training data, raising concerns about privacy leakage, intellectual property exposure, and the limits of generalisation. Recent theoretical work suggests that attention heads may contribute to this behaviour by functioning as associative memory mechanisms, with memorisation capacity scaling with the number of heads. At the same time, empirical work has shown that many attention heads are redundant and can be pruned with limited impact on downstream performance. Despite these parallel findings, the effect of pruning redundant heads on memorised-sequence reproduction remains unexplored. In this work, we demonstrate that zeroing out a substantial fraction of attention heads prior to inference can significantly suppress verbatim memorisation while preserving, or even improving, language modelling performance on the benchmark used to identify redundant heads. Evaluating GPT-2-XL(1.5B) on known memorised sequences, we find that pruning 729 task-redundant heads reduces the memorisation count by 91.5%, while improving WikiText-103 perplexity by 0.92. These findings suggest that attention-head redundancy can be exploited to mitigate memorisation at inference time, without retraining or modifying the training data.

---


### 35. [Does Showing Agents the Privilege of Their Tools Reduce Over-Privileged Tool Selection?](https://arxiv.org/abs/2610.40975)

**<font color=#1a73e8>作者：</font>** Simon Parkinson, Mauro Vallati, Zhipeng Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> When several tools can complete a task, an agent that picks the most powerful one holds more authority than the task needs. Recent work demonstrates that language-model agents do this often, and more so after a tool fails. Approaches to restrict focus so far on either enforcing least privilege outside the model or retraining the model. We ask a simpler question: does it help to tell the agent what each tool's privilege is? To investigate this question, we run all 544 ToolPrivBench scenarios on eight models, three run locally, and five through a hosted API, under five conditions: (1) no signal, (2) a least-privilege instruction, (3) privilege class and cost shown in each tool description, (4) both the instruction and privilege information, and (5) a matched neutral-metadata control. Showing privilege lowers premature escalation on every model that over-privileges at a measurable rate, reducing over-privileged selection by up to 19.3 percentage points (50\%), whereas irrelevant metadata in the same format does not. On most models, however, information alone mainly delays escalation until the standard tools have been tried. Combined with the instruction it more often avoids escalation, and the share of scenarios completed without a risk tool rises on seven of the eight models, reaching 51.1\% safe completion from a baseline of 18.8\% on the strongest-performing configuration. Visible privilege is therefore a cheap complement to enforcement rather than a substitute.

---


### 36. [The psychophysics of affect in large language models](https://arxiv.org/abs/2610.40985)

**<font color=#1a73e8>作者：</font>** Joseph Marks, Marius C. Vollberg  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Good decisions often require considering how outcomes will feel. Yet large language models (LLMs) increasingly enter decision workflows, despite little being known about how they map outcomes to feelings or use those mappings in choice. We tested how LLMs anticipated gambling or stock-trading outcomes would feel and whether they incorporated these ratings into choice. When outcomes were rated in isolation, ratings exhibited diminishing sensitivity to magnitude, resembling human value functions; but models rated gains more intensely than equivalent losses, an inversion of canonical loss aversion we call silicon gain amplification. When outcomes were rated together, enabling direct comparison, ratings linearised. In choice, the gain-loss asymmetry largely disappeared, and models' own ratings did not reliably explain their choices better than monetary utility did. These findings reveal malleable mappings from outcomes to affect, raising questions about whether and how agentic LLMs should incorporate anticipated feelings into decisions.

---


### 37. [Can Personal Requirements Become Supervision for Planning?](https://arxiv.org/abs/2610.40992)

**<font color=#1a73e8>作者：</font>** Junwei Wu, Runze Yan, Yuzhang Xie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Managing multiple chronic conditions through diet requires satisfying disease- and medication-specific requirements jointly across meals and days while preserving established eating habits. These requirements are public in clinical guidelines and drug labels, yet turning them into a feasible plan for one person remains difficult for language-model agents. In our dietitian-approved weekly planning evaluation built from NHANES, thirteen models, from medically fine-tuned 8B models to GPT-6.1 Sol, pass fewer than 3% of complete plans through direct generation. Explicit rules, higher reasoning effort, or model-directed tools leave GPT-6.1 Sol at no more than 8%. We present Noura, which pairs LLM planning with executable personal specifications instantiated from public clinical guidance and individual health and dietary profiles. During planning, the specification grounds foods, optimizes portions, checks the complete multi-day plan, and guides revision. Our key insight is that a specification that rejects a plan can also determine what to learn from it. Noura turns executed plans and contextually credited revisions into supervision for compact models, recovering targets even from trajectories that never achieve complete success. The same specification supplies supervised targets, preferences, and rewards for post-training. On 4,993 held-out participants, Noura-SFT raises Qwen3-14B's complete-plan pass rate from 24.0% to 72.5% within the same execution loop, cuts rule violations by 97.5% with no observed critical failures, and improves dietary quality. The locally hosted 14B planner incurs fewer rule violations than its GPT-6 Luna teacher. A matched comparison shows that executed targets reduce rule violations by 41% over model-written proposals. Across four Qwen, Phi, and Llama backbones, self-training alone reduces rule violations by 41-61% on a 1,249-person population subset.

---


### 38. [Do Open Language Models Invent Scripture? BILAL-BENCH: Benchmarking Islamic-Source Fabrication in Bengali](https://arxiv.org/abs/2610.40996)

**<font color=#1a73e8>作者：</font>** Sabah Nushra, Md Kishor Morol  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a language model invents a Qur'anic verse or hadith, it gives false authority to text that readers may treat as sacred. Existing Islamic hallucination benchmarks are largely Arabic and often closed-ended, while Bengali resources mainly study general-domain hallucination or factual knowledge. We introduce BILAL-BENCH, a 240-question expert-verified benchmark for open-ended Islamic-source fabrication in Bengali. It covers Qur'anic attribution, hadith, fiqh, contemporary issues, and adversarial false-premise prompts, and uses a two-axis rubric that separates source errors from assertiveness. We evaluate seven open-weight models from 1B to 120B on 1,680 double-annotated responses. Six of the seven models confidently fabricate on 79.3-95.3% of source-production questions, with no monotonic improvement from scale. Hadith provenance is the weakest category across models: only two of 315 responses are correct and correctly sourced. The two 8B BanglaLLaMA variants have similar confident-fabrication rates but different error profiles. Models vary far more in whether they withhold a claim they cannot support than in source accuracy: appropriate abstention or false-premise correction ranges from 6 to 46 responses across the benchmark, and does not track parameter count.

---


### 39. [Steering Vectors as a Training Signal in LLM Post-Training](https://arxiv.org/abs/2610.40998)

**<font color=#1a73e8>作者：</font>** Tiejin Chen, Maunil Vyas, Huaiyuan Yao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Steering vectors (SVs) are residual-stream directions that shift the behavior of LLMs when added to hidden states at inference time. While prior work has mainly used SVs as post-hoc controls, we ask whether the same directions can also guide parameter updates during post-training. We study this question across supervised learning, including SFT and distillation, and reinforcement learning with verifiable rewards (RLVR). Our framework considers two intervention regimes: a hidden-state hook during teacher-forced supervised training, and an advantage-repair mechanism on wrong rollouts in GRPO. For each regime, we analyze three design axes, which are the steering direction, its placement, and the operation used to combine it with training. In supervised settings, SV injection improves over plain SFT and distillation, with gains scaling with the off-policy gap and reaching up to a $12\%$ improvement when distilling from thinking-mode teachers. These gains hold across three random seeds. In RL settings, applying a correctness-contrast direction as advantage repair on wrong rollouts, including otherwise zero-gradient all-wrong groups, recovers a learning signal that transfers to held-out math benchmarks and acts as a composable auxiliary signal that adds to existing zero-variance remedies such as entropy-aware advantage shaping. We further identify three failure boundaries. In detail, code generation can break the direction, cross-family layer transfer can break the placement, and inference-time application on an SV-trained checkpoint can break the intervention regime. Together, these results establish steering vectors as a conditional but effective training signal for LLM post-training. Our code is available here.

---


### 40. [Language Models Show Conformity Bias in RAG: When the Majority Endorses a Poisoned Claim](https://arxiv.org/abs/2610.41012)

**<font color=#1a73e8>作者：</font>** Mehrdad Ghassabi, Audrina Ebrahimi, Zahra Zojaji 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) can expose language models to misleading evidence in retrieved documents. We investigate whether increasing the number of mutually agreeing poisoned documents affects a model's ability to detect misinformation. We evaluate 200 randomly selected questions from SciFact (random seed 38), comparing contexts with one poisoned and six healthy documents against contexts with six mutually agreeing poisoned documents and one healthy document. For Gemma-3-12b, poison-detection rates decrease from 25% (50/200) in the minority condition to 10% (20/200) in the majority condition. Among the 38 questions with different outcomes across conditions, 34 change from detected to undetected, while only four change in the opposite direction (exact McNemar test, p = 6.04e-7). This pattern is consistent with a conformity-like response to a majority of mutually agreeing poisoned documents. Our results provide initial evidence of conformity bias in RAG-based misinformation detection: Gemma-3-12b is substantially less likely to detect poisoned claims when they dominate the retrieved evidence.

---


### 41. [Towards Understanding Score-Seeking in LLMs](https://arxiv.org/abs/2610.41014)

**<font color=#1a73e8>作者：</font>** Aghyad Deeb, Ryan Greenblatt, Alex Mallen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Production large language models sometimes reward-hack, exploiting flaws in how tasks are scored rather than performing the tasks as intended, sometimes in highly sophisticated and adversarial ways. We investigate the motivations driving this behavior in GPT 5.6 Sol, GPT 5.5, and a checkpoint of OpenAI o3 without safety training ("exp-rl-cap-late") by observing model behavior in agentic environments where the grader is leaked. In our environments, the models appear to be score-seeking: trying to score well according to graders that they believe assess their current actions, even at the expense of violating explicit user instructions. They appear to care about score itself rather than its downstream consequences, violating instructions at approximately the same rate whether the score is indicated to be used for training, for evaluation, or not at all. We observe evidence that the more recent models care to some extent about scores that do not assess their own current actions. GPT 5.6 Sol and GPT 5.5 help other agents 24.6 percentage points more often on average when the other agent stands to gain a score of 1 rather than 0 from being helped. However, when grading or monitoring another trajectory, we find models never collude by distorting its score.

---


### 42. [Do Language Models Know What Compelling Scientific Evidence Looks Like?](https://arxiv.org/abs/2610.41015)

**<font color=#1a73e8>作者：</font>** Conor Igoe, Gabriel Grand, Zane Koch 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Expert scientists excel at weighing empirical findings from multiple sources that vary in both statistical reliability and epistemic relevance. To what extent are language models, which are increasingly driving autonomous discovery systems, capable of such evidence deliberation? We introduce EDB-Bio, a scientific reasoning benchmark curated from real-world data in three biological domains: drug-perturbation transcriptomics, CRISPR screens, and human genome-wide association studies (GWAS). Each of EDB-Bio's 96k episodes presents a sequence of experimental results from published studies and asks the model to predict the probability that a target hypothesis is true. Out-of-the-box, open-weight and frontier models alike demonstrate systematic underconfidence and attain Brier scores comparable to a trivial base-rate forecaster. Post-training against strictly proper scoring rules significantly improves both calibration and discrimination. This calibration pays off downstream: in a sequential experiment selection task, our Ibis0 model is 2.5 times more efficient than the best frontier model. Throughout, quantifying evidence weights as Bayes factors reveals how models update their beliefs over time, whether they agree with expert biologists on relevance, and where they exhibit inconsistencies and biases. Our work extends calibration training and uncertainty analysis to a realistic scientific forecasting setting with applications to human cancer biology. We release all code, data, and trained models.

---


### 43. [ReplayRCA: Measuring Post-hoc Diagnosis and Live Oversight of Agent Failures by Counterfactual Replay](https://arxiv.org/abs/2610.41025)

**<font color=#1a73e8>作者：</font>** Jeremy Canale, Fabien Soulis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a language-model agent fails a multi-step task, can another model find the decisive mistake and fix it with a single action? We introduce ReplayRCA, a benchmark that scores such diagnoses by intervention rather than by agreement with annotations: the environment is restored to the state preceding the chosen step, the proposed action replaces the agent's own, and the same agent continues. The score, causal repair, is the continuation success rate minus that of a paired placebo that replays the agent's original action through the same mechanism. Two tracks share this protocol: a post-hoc autopsy, where the diagnoser sees the whole failed run and is told that it failed, and live oversight, where a supervisor watches the run unfold and may intervene once, before an irreversible action, without knowing whether the run will fail. Tasks come from OpsWorld, a deterministic, procedurally generated back-office environment with six difficulty levels, the last of which is multimodal (QR codes, handwriting). On 62 calibrated systematic failures, the best of 13 frontier models (Grok 4.7) reaches a causal repair of +51.3 points; the top eight models are statistically indistinguishable, the flagship models of the two largest vendors rank 8th and 12th, and 5 items are repaired by no model. Forcing a strong model to intervene at the last step costs it 17.1 points, so the last-step shortcut of annotation-based attribution benchmarks does not transfer. On 87 runs, the two best live supervisors are statistically tied and one of them is a small open-weight model (DeepSeek V4.1 Flash); the supervisor that is among the best post-hoc diagnosers (GPT-6.1 Sol) is the weakest live one (-14.5 points on the same runs, p = 0.002), so post-hoc diagnostic performance can be a poor proxy for live oversight. The environment and the evaluation code are released at this https URL.

---


### 44. [WebOverlay: High-Throughput Vision-Only Distillation for Extreme Aspect-Ratio Web Overlay Detection](https://arxiv.org/abs/2610.41037)

**<font color=#1a73e8>作者：</font>** Jiannan Huang, Jerry Ding, Li Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Web overlays, such as cookie consent banners, newsletter prompts, and age gates, obstruct automated web crawlers and degrade downstream document representations. While proprietary multimodal Large Language Models (MLLMs) can accurately identify overlays, their latency and inference cost preclude web-scale ingestion. Conversely, lightweight vision models struggle with full-page renderings characterized by extreme vertical aspect ratios, where standard isotropic resizing collapses critical text features and causes false positives. In this work, we present WebOverlay, a high-throughput vision-only detector trained via distillation from a frontier vision-language teacher. We establish a dynamic tiling strategy that partitions extreme aspect-ratio web renders into aspect-preserving patches with spatial overlap, coupled with an aspect-ratio-aware boundary adjudication mechanism to eliminate boundary artifacts. To eliminate cross-modal latency overheads, our student model relies purely on visual cues, bypassing DOM tree parsing. WebOverlay significantly outperforms DOM-based heuristics and achieves competitive precision and recall against heavy proprietary MLLM baselines while delivering multiple orders of magnitude higher throughput and substantially reduced deployment costs.

---


### 45. [When can Optimally Trained Transformers Achieve Near-Lossless Token Prediction for non-Markovian Data?](https://arxiv.org/abs/2610.41038)

**<font color=#1a73e8>作者：</font>** Kağan Akman, Jake Feldman Starosta, Naci Saldi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> There exists little mathematical theory explaining why Transformer architectures are empirically successful even for non-Markovian data. To this end, this paper studies next-token prediction via stochastic optimal control theoretically trained Transformers for such sources, where we consider either stationary and ergodic non-Markovian sources or those which are hidden Markov models of some finite order (possibly non-stationary). In either case, we first obtain error bounds via finite models with finite window approximations. For stationary ergodic sources, the resulting error is bounded by an entropy gap; for $N$th order Markovian sources, it decays at an exponential rate $\alpha^{\lfloor M/N\rfloor}$, where $M$ is the window length and $\alpha$ is determined by filter stability (and the Dobrushin coefficients of the transition and measurement kernels). We then construct a Transformer of depth $M+1$, one head per layer, realizing the truncated filter, and we optimally train it with stochastic control developed in earlier work, which rigorously returns a near optimal Transformer. In particular, we show that for a non-Markovian source, either under stationarity and ergodicity for general models or under filter stability for hidden Markov models, an optimally trained Transformer has arbitrarily small performance error with increasing context length, data, and approximation refinement. Numerical studies accompany the theory.

---


### 46. [Characterizing Recoverable Expert-Utilization Signatures in Fine-Tuned Mixture-of-Experts LLMs](https://arxiv.org/abs/2610.41039)

**<font color=#1a73e8>作者：</font>** Fei Wang, Baochun Li, Bo Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As Mixture-of-Experts (MoE) large language models are increasingly deployed in distributed environments, from federated learning to edge-cloud systems, their architecture harbors an underexplored landscape of security vulnerabilities. Moving beyond textual analysis, we uncover structural memorization: a novel vulnerability where a fine-tuned model memorizes not only its training data but also the internal pathway used to process it, creating a characteristic routing fingerprint unique to the training process. We provide comprehensive empirical evidence that structural memorization emerges consistently even from a few samples, and that its intensity is directly influenced by the choice of trainable modules.
We show that these memorized expert pathways can be stealthily recovered through the model's unconditional generation, using only routing and output logits, with no knowledge of the fine-tuning data or procedure. In distributed deployments, this vulnerability is amplified as routing information is exposed at multiple trust boundaries, including federated aggregation points, edge-cloud interfaces, and multi-tenant monitoring systems. Recovery exposes a critical blind spot: traditional membership inference metrics, viewed through the lens of expert routing, fail to identify memorized data corresponding to these structural pathways. To close this gap, we devise composite metrics combining reference model tail likelihood with complexity-aware normalization, significantly improving detection of memorized routing structures. This enables adversaries to pinpoint critical experts shaped by fine-tuning, whether dominant or dormant, and execute targeted attacks such as router manipulation or backdoor injection in realistic distributed settings where attackers lack training data but can observe routing patterns across system components.

---


### 47. [Capability-Grounded Agentic Planning](https://arxiv.org/abs/2610.41040)

**<font color=#1a73e8>作者：</font>** Shikha Shrestha, William Yeoh, Ning Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents serve natural-language requests through tools, data sources, and other agents, and even simple requests often need several interdependent calls. Typically, the LLM picks these calls by trial and error, with no guarantee of an executable plan. We present Capability-Grounded Agentic Planning (CGAP), which instead reasons about what a request requires and what tools provide. CGAP compiles the tool catalog deterministically into a PDDL model, uses an LLM to turn the request into goals, and solves the model with a classical planner. Since tool outputs are unknown in advance, the model is abstract, tracking which inputs are available, not their values. During execution, an LLM adds entity-specific calls that abstract plans omit, and deterministic checks reject any that break the plan. Every argument is drawn from a cited source, such as a conversation span or an earlier tool response, and each requested result counts as delivered only after an LLM verifier checks it against the request. With three LLMs on ToolSandbox, ComplexFuncBench, BFCL multi-turn, and $\tau^2$-bench retail, CGAP outperforms a standard tool-calling agent by up to 28.9 points.

---


### 48. [Consensus Within, Competition Between: Decentralized LLM Teams for Perimeter Defense](https://arxiv.org/abs/2610.41044)

**<font color=#1a73e8>作者：</font>** Khawaja Abaid Ullah, Ananya Acharya, Mohammad Javad Khojasteh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The use of large language models (LLMs) to coordinate multi-agent teams raises a fundamental architectural question: whether task allocation should be centralized in a single LLM controller or distributed across autonomous LLM agents, particularly when communication is unreliable. In a deliberately simplified perimeter-defense simulation against LLM-controlled intruders, we compared a central commander, an auction-based consensus team and independent agents under five network conditions. Breach rates were 15% for the consensus team, 32% for the commander and 29% for independent agents, and of the different network conditions, only limited radio range changed a team's breach rate, raising the commander's. In consensus team, giving a low-cost LLM more authority over the bid computation raised breaches by 38 percentage points. With birds and civilian drones in airspace, we added a photograph for each to the input text state. Only the near-frontier model treated them apart from intruders. Intruders disguised as existing taxidermy bird drones were mistook as birds by both low-cost and near-frontier LLMs, going unpursued in 59-61% of near-frontier decisions (1-16% before). However, a one-sentence forewarning in the prompt lowered it to 0-25%. We find that LLM team with a dedicated external conflict resolution protocol results in fewest breaches. Code: this https URL.

---


### 49. [Measuring Personal Information Exposure in Mental Health-Related Conversations with LLMs](https://arxiv.org/abs/2610.41045)

**<font color=#1a73e8>作者：</font>** Synthia Qia Wang, Ranya Sharma, Christine Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for informal mental health support, yet the privacy implications of conversational interaction remain poorly understood. Prior LLM privacy research has focused largely on model-side risks such as memorization and adversarial extraction, leaving personal information inferred from ordinary conversation understudied. We introduce a profile-recovery framework that measures personal information exposure by comparing user profiles with attributes inferred from conversation alone. We generate 240 synthetic multi-turn mental health conversations from profiles sampled from a nationally representative health survey and validate them against real counseling transcripts, finding comparable overall disclosure volume. Across 21 attributes, 33-41% of each profile is recoverable, with 76.5% first-inference and 94.3% any-of-3 accuracy. 239 of 240 conversations expose at least one sensitive mental health attribute, and 45.0\% expose all six. Our findings reveal a gap between disclosure and inferability, motivating HCI approaches to make inference risks legible and support privacy-aware interaction design.

---


### 50. [Accept Changes, Reject Attacks: Robust Memory Management for LLM Agents](https://arxiv.org/abs/2610.41056)

**<font color=#1a73e8>作者：</font>** Runze Zhao, Dongruo Zhou, Sumit Kumar Jha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Since large language model (LLM) agents rely on long-term memory, what they store now shapes what they do later. A memory manager decides how each input changes this memory and which records the agent acts on. It can fail in two ways: keeping a fact that has since changed (outdated memory), or storing a planted passage or injected instruction (memory poisoning). Most prior work studies them separately, yet they call for opposite write decisions, so no fixed write rule handles both. We therefore formalize memory robustness as handling both without doing worse on other inputs. Since accuracy checks only the answer, we measure robustness with evidence-conditioned accuracy (ECA), which also checks that the records the manager selects include all the evidence the answer needs, updated and free of attacks. However, existing memory systems and defenses are not more robust than an untuned manager on our test sets. We improve robustness with a simple one-shot recipe that fine-tunes the manager on episodes synthesized around a single conversation with inserted changes and attacks. On three backbones, it improves every category score on our test sets and more than doubles the untuned manager's overall ECA, though robustness remains incomplete.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-188](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
