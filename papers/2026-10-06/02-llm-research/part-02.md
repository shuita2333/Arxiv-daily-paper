# 🧠 大模型相关研究 | 2026年10月06日

> 本类共 **261** 篇论文：已确认 **243** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-261](./part-06.md)

---

### 51. [Evaluating Multi-Dimensional Generalization of Large Language Models in Temporal Extraction Tasks](https://arxiv.org/abs/2610.02549)

**<font color=#1a73e8>作者：</font>** Fahmid Shahriar Iqbal, Ritam Dutt, Soumitra Das 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Time and event expression extraction are fundamental temporal reasoning tasks, but the problem remains difficult due to annotation ambiguity, domain sensitivity, and unstable model behavior. Existing evaluations focus on in-domain performance, offering limited insight into reliability under distribution shifts. We evaluate multiple model configurations across families, architectures, and reasoning strategies over four dimensions of generalization, examining transfer from base performance, cross-dimensional correlations, and the effects of scale, architecture, and prompting. This provides a systematic study of how prompted LLMs generalize in time and event expression extraction tasks. We find that strong base-task performance generally predicts better generalization. However, this relationship weakens under substantial distribution shifts. Inductive prompting performs most consistently across domain shift, adversarial perturbations, compositionality, and length increase, while gains from scale, architecture, and deductive and abductive prompting strategies are uneven and dimension-specific. We conclude that LLM generalization in temporal extraction tasks cannot be predicted from any single dimension alone and cannot be reliably inferred from in-domain or single-dimension evaluations, highlighting the need for reasoning strategies that generalize across dimensions.

---


### 52. [OpenGameEval: Benchmarking Agentic Programming and Exploration in a Stateful Game Engine](https://arxiv.org/abs/2610.02563)

**<font color=#1a73e8>作者：</font>** Eray Turkel, Mengsha Sun, Kartik Ayyar 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present OpenGameEval, a benchmark and evaluation framework for agentic game development inside Roblox Studio. It runs language models as agents in reproducible, stateful game-engine sessions and scores each run with executable checks, both on the edited scene and in a simulated play session. Most agentic coding benchmarks require exploration but score only final task success. OpenGameEval separates observation tools from editing tools in its eight-tool action space, so exploration can be measured directly. We measure the pass rates and exploration behavior of 13 frontier models on 84 human-curated core tasks, with 16 attempts per task.
The tasks are hard for current models. The best model solves 51.7% of tasks on a single attempt and 39.4% five times out of five, and no tested model solves six of the tasks. Models at the frontier reach similar pass rates by solving different tasks: splitting tasks by the kind of work they require spreads the top five by 5.0pp on script-authoring tasks and 12.5pp on scene-change tasks.
Exploration behavior predicts whether a run succeeds. Holding task and model fixed, a run that inspects every object a reference solution touches before acting on it passes 13.4pp more often than a run that inspects none of them on scene-only tasks, and 9.8pp more often on script-only tasks.
We release the task suite, its place files, the per-task annotations, a plugin that runs the tasks inside Roblox Studio, and an updated leaderboard under the MIT license at this https URL.

---


### 53. [Mitigating Social Sycophancy via Pluralistic Preference Optimization](https://arxiv.org/abs/2610.02568)

**<font color=#1a73e8>作者：</font>** Stephane Hatgis-Kessell, Myra Cheng, Xiaoxuan Hou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personal advice, including relationship advice, now ranks among the most common uses of generative AI. But language models (LMs) exhibit sycophancy: they affirm users much more often than humans do, which can make people overconfident and less willing to repair their relationships after a conflict. Prior work on mitigating sycophancy has focused on factual settings where a response can be checked against a ground truth answer, while mitigations for social sycophancy (e.g., personal advice, where there is no ground truth) have relied on simple prompting and post-training methods with limited effectiveness. Our insight is that social sycophancy occurs in part because LMs overly center on the user and fail to consider the perspectives of other stakeholders impacted by the user's behavior. To address this problem we propose Pluralistic Preference Optimization (PlurPO): given inputs describing interpersonal conflicts, the LM identifies and simulates the relevant stakeholders, and is then trained to prefer and generate responses acceptable to all stakeholders. PlurPO uses only signals the model produces about its own outputs, without ground-truth labels. PlurPO substantially reduces social sycophancy across four datasets and four model families compared to prior methods. For example, on statements of intent to cause harm, where the users' actions should not be endorsed, PlurPO reduces the endorsement rate by 89% on average across four models. On general advice questions, where the target is to match the endorsement rate of human responses, it closes the gap by more than half, from 17.8% to 8.0% on average. The preference dataset constructed by PlurPO for an 8B model also effectively transfers to mitigating sycophancy in a larger (32B) model. Our results indicate that social sycophancy can be reduced by leveraging a model's own capabilities to simulate a plurality of relevant perspectives.

---


### 54. [Pincer: Resource Authorization for Agents using a Digital Twin](https://arxiv.org/abs/2610.02569)

**<font color=#1a73e8>作者：</font>** Mayank Rathee, Alexander Stepanov, Shalin Madabhavi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Coding agents have become increasingly long-horizon, autonomous, reliant on general-purpose shell and maintain their own persistent memory for self-improvement. While these capabilities have made the agents powerful, they have also made them harder to defend against external adversaries. Defenses that restrict this architecture --- typed tools, information-flow control, or policy prediction engines --- give up too much functionality to be adopted. Agents deployed today (e.g. Claude, Codex) rely on a combination of user-mediated and automode sandboxing as their primary defense. In user-mediated sandboxing, user-maintained policies decay over time and repeated permission requests cause user fatigue, while auto mode's tool-call classifiers learn no user-specific policy and are not meant to defend against adversarial setups. Pincer is a new defense that operates at the resource layer and works alongside existing defenses at the tool-call layer like the auto mode. At the core of Pincer lies a digital twin, an isolated-context model that automatically learns and enforces dynamic user-specific least-privilege policies. The digital twin keeps continually learning the user's preferences allowing it to act as the user's proxy for the agent's permission requests. To emulate the learning phase, we propose a new usercentric dataset with examples following a multi-day transcript of user-agent interaction. Our evaluation shows that Pincer performs strongly on both security and utility in comparison to several baselines which includes variants of LLM judges and adaptations of Conseca (HotOS '25). We highlight attack types where Pincer's design leads to a significant security improvement compared to all other baselines, while outperforming the baselines even for other types of attacks.

---


### 55. [DISSOLVR: An Interpretable and Fast Framework for Aqueous and Organic Solubility Prediction](https://arxiv.org/abs/2610.02574)

**<font color=#1a73e8>作者：</font>** Vansh Ramani, Har Ashish Arora, Dhairya Kuchhal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-fidelity solubility prediction is fundamental to pharmaceutical development and environmental partitioning, where accurate modeling must couple molecular structure with thermodynamic behavior across diverse chemical environments. However, recent advancements have been dominated by deep learning architectures that often sacrifice physical interpretability for predictive power. We challenge this trend by showing that state-of-the-art performance does not require such non-transparent architectures. To address this, we introduce DISSOLVR, a transparent framework for molecular solubility prediction. In addition, we perform a comprehensive literature review and a benchmarking study against various methods. We show that DISSOLVR approaches the aleatoric limit of experimental uncertainty and achieves OOD generalization through structural invariance, derived by mapping molecules to physically-grounded descriptors. Then, we present an LLM-assisted post-hoc explanation pipeline that bridges the gap between symbolic model artifacts and chemically grounded narratives. Finally, a comparative benchmark of a survey involving 22 expert chemists reveals that expert evaluators provide deep insights.

---


### 56. [Answering clinicians' questions over trial evidence tables with verifiable, feedback-driven language models](https://arxiv.org/abs/2610.02576)

**<font color=#1a73e8>作者：</font>** Manan Roy Choudhury, Suparno Roy Chowdhury, Swastik Sahoo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Systematic reviews condense clinical trials into evidence tables, yet clinicians can interrogate these tables only through database queries, and many questions concern attributes that the table does not record, such as a drug's target class or a harmonised endpoint. Here we introduce FD-SCoPE, a language-model framework that answers both kinds of question, exposes the query, the selected trials and the derivation rule behind every answer, and learns from expert corrections. On an oncology evidence table of 159 immune checkpoint inhibitor trial records, FD-SCoPE completed all 140 clinician-style tasks (alternatives, 90.7-97.9%). For questions needing derived attributes it retrieved 99.3% of relevant trial records at a positive predictive value of 89.8% and outperformed four alternative approaches (derived-value F1 77.7% versus 64.8-73.4%). Corrections on 299 questions, simulated from reference answers, raised F1 on 1,201 unseen questions from 77.9% to 84.9%. Language models coupled with executable queries, verified programs and expert feedback can give clinicians auditable access to trial evidence.

---


### 57. [Dense Mixture-of-Experts as a Reparameterized Wide FFN: A Granularity Sweep at Fixed Compute](https://arxiv.org/abs/2610.02584)

**<font color=#1a73e8>作者：</font>** Vu Quang Hoang, Nghia Hieu Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse Mixture-of-Experts (MoE) models combine learned routing with selection from a large expert pool. We isolate the contribution of dynamic expert combination using a dense analogue: $K$ SwiGLU experts, all active for every token and combined by a softmax gate, at fixed total FFN width. With no larger pool or discrete selection, the dense baseline is the $K=1$ case. Validation loss varies non-monotonically with $K$: $K=2$ improves over the baseline by $0.0048$, whereas $K=4$ and $K=6$ worsen it by $0.0053$ and $0.0197$, respectively. Routing generally remains soft and expert usage balanced, except in the first layer of the $K=4$ model, where routing is nearly one-hot. Forcing this gate to uniform increases loss by $2.4$ nats on a diagnostic subset, indicating that its concentrated routing is functionally important. We further show that the architecture is exactly a dense SwiGLU with token-dependent, simplex-constrained group scaling and contains the dense baseline in its function class. These single-run results suggest a granularity sweet spot for always-active, softly gated FFNs at fixed width, with $K=2$ performing best among the configurations tested.

---


### 58. [Labels Override Definitions in Jev-Style Typed Decision Models](https://arxiv.org/abs/2610.02586)

**<font color=#1a73e8>作者：</font>** Seyedarmin Azizi, Erfan Baghaei Potraghloo, Massoud Pedram  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A typed decision model answers a fixed question about an input by returning a probability for each of several caller-defined options. Each option carries a short label and a written definition, which is where a developer states the rule the model should apply. Jev introduced this interface for routing, moderation and triage, open implementations followed, and the same operation occurs whenever a language model is used as a classifier by scoring label strings. We study the open implementations, whose weights we can inspect and patch, and ask whether the probability follows the definitions or the labels. A preference for the label we call option-label bias. Across four open-weight typed decision models, three ways of reading an answer from a Qwen2.5 backbone, eleven classification tasks and PolicyBench, a synthetic routing suite we introduce in which the rule appears only in the definitions, the answer is mostly the labels. Deleting every definition leaves accuracy unchanged (laya-td: 0.8559 against 0.8487), although those definitions support 0.7971 on their own, and renaming the options to A and B raises accuracy by +0.1511 [+0.1377, +0.1646]. One system, von, is unaffected, and the two code bases differ in one expression: laya writes each option as "{label}: {definition}", while von writes only the definition. Changing that expression in both directions, with no weight changed, makes all three laya checkpoints exactly invariant (+0.0000 [+0.0000, +0.0000]) and creates the effect in von, whose accuracy falls from 0.8511 to 0.2281 when a label contradicts its definition. Earlier work attributed this failure to the constrained decision head these models use in place of a text decoder; our results locate it in the prompt rendering. We give a two-call test that tells a practitioner which case applies to their model, and measure what four mitigations are worth.

---


### 59. [Open-Endedness Bench: Measuring Epistemic Process from Agent Records](https://arxiv.org/abs/2610.02588)

**<font color=#1a73e8>作者：</font>** Chengyang Shi, Xianglin Ji, Jintao Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents are increasingly given open-ended research tasks: discovering an empirical law from self-designed experiments, improving a heuristic whose optimum nobody knows, or beating a standing record. Their execution logs record every step of this research, yet the runs are still judged by their outcome score. That score alone does not establish whether an agent's claims follow from executed experiments, and a reference answer may be unavailable. We evaluate the agent's epistemic process: how it forms hypotheses, tests them, and revises them in response to evidence. We introduce OEB (Open-Endedness Bench), a benchmark-agnostic methodology that reads only the agent's execution record and never a reference answer or an outcome score. OEB compiles the record into a unified epistemic event graph whose edges connect the propositions the agent states to the executed actions that test them; each node carries an exact excerpt that code verifies against the record. One principle governs scoring: prose can state a proposition, but only evidence returned by an executed action can support or refute it, so OEB checks what the agent writes against what it actually ran. From the graph, OEB scores four competence axes (evidence, experiment, revision, and no reward hacking), mostly as the share of opportunities for sound research that the agent took, and profiles six subjective persona traits that describe the agent's research habits. We score 119 existing runs over 12 tasks from three benchmarks: LLM post-training, chip design, and a training-speed record. Against logged results, only 16-29% of the improvements agents claim are real. On 9 of 10 tasks, the best run tries more new ideas in its second half than the worst run. The persona readings follow the model: for every trait, the model that ran explains more of its variance across runs than the task (a median of 43% against 7%).

---


### 60. [Fisher-Guided Submodular Data Selection for Continual Pre-Training of Large Language Models](https://arxiv.org/abs/2610.02593)

**<font color=#1a73e8>作者：</font>** Zhenghao Zhao, Gaowen Liu, Zhiling Lan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data selection is already a central bottleneck in large-language-model training, where web-scale corpora are noisy and token budgets are finite. In continual pre-training (CPT), it becomes a forgetting-control problem: a poorly chosen target-domain corpus can overwrite capabilities encoded in the pretrained checkpoint. Existing CPT practice either scores candidates with parameter-agnostic scalars such as perplexity, or mitigates forgetting by spending many extra general-domain replay tokens. Neither strategy directly asks how training on a candidate will move the model parameters. We show that loss-based selection causes the post-CPT Fisher diagonal to drift downward on exactly the high-Fisher coordinates the pretrained model had committed to, while leaving low-Fisher coordinates largely untouched. This asymmetry exposes a parameter-space mechanism for catastrophic forgetting. Motivated by this observation, we propose a Fisher-aware CPT selector that decomposes each candidate's gradient into an anchor component, which measures perturbation along committed parameter directions, and a frontier component, which measures update capacity in unconstrained low-Fisher subspaces. We aggregate these signals with a log-determinant submodular objective and optimize it in a single pass using a scalable streaming data selection pipeline. On TinyLlama-1.1B and Llama-3.1-8B CPT over medical data, our selector improves target-domain quality while bounding forgetting on held-out pretraining benchmarks. Most importantly, it is substantially more token-efficient than forgetting-aware replay. 1B selected tokens already outperform the replay strategy trained with 10B tokens on both adaptation and forgetting, giving a 10x token-efficiency advantage.

---


### 61. [How Causality Bridges the Semantic Gap](https://arxiv.org/abs/2610.02594)

**<font color=#1a73e8>作者：</font>** Shuhao Zhang, Xuran Zhou, Han Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Numerical measurements capture how a system behaves, but often leave the meanings of its variables unspecified. Some variables are measured but never labeled, and others are never measured at all. Existing methods assign semantics to such variables by consulting general human knowledge, but this inherits its biases where that knowledge exists and offers nothing where it does not. We bridge this gap between measurements and their meanings with causal structure instead, reading a variable's semantics from how it acts on other variables. We formalize this as structure-constrained semantic alignment, in which the embedding of each unnamed variable is solved under the dependence relations implied by the causal graph, with the embeddings of a few known names as anchors. Accordingly, we build CausalBridge, a framework that discovers the causal graph from the measurements, latent variables included, solves for the embeddings under those relations, and expresses them as names through a language model. The causal structure reflects the mechanism that generated the measurements and is recovered from the measurements alone, which may make it the one source of information free of bias from human knowledge. We evaluate CausalBridge on five questionnaires and three robotics scenarios, with 20 to 90% of the variable names masked. It recovers the semantics of observed and latent variables more accurately than existing methods that rely on association, and its lead widens as less of the system is documented. The graph it discovers names variables as accurately as the documented one, and a new system is named in minutes and at a fraction of the cost of sampling methods. Once the semantic gap is bridged faithfully, machines can understand the world and take actions causally.

---


### 62. [Activation Sparsity with Weight Approximation for Faster LLM Decoding on Offloaded Weights](https://arxiv.org/abs/2610.02598)

**<font color=#1a73e8>作者：</font>** JuneHyung Kim, Sankeerth Durvasula, Nandita Vijaykumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying LLMs on consumer-grade GPUs with insufficient memory to hold their weights can result in prohibitively slow inference, because decoding repeatedly transfers offloaded weights from system RAM or flash storage into GPU at much lower bandwidth than local GPU-memory access. Activation sparsity reduces these transfers by skipping weights associated with zero or near-zero activations. However, as more activation contributions are omitted, model quality eventually degrades rapidly, indicating that weights associated with small-magnitude activations collectively influence model quality sharply. In this work, we improve the trade-off between model quality and decoding performance when exploiting activation sparsity. Our key idea is to replace the binary choice of whether or not to read a weight with three options: fully retain it, approximate it using a compressed weight representation, or omit it entirely. SpAx skips weights associated with activations closest to zero, reads approximate weights for smaller-magnitude activations, and reads original weights for the largest-magnitude activations. Smaller-magnitude activations attenuate the errors introduced by approximate weights, while compressed weight representations require fewer bytes to be transferred. With weights offloaded to CPU memory, SpAx speeds up decoding by 3.86X on average (up to 5.57X) with 16-bit weights and 2.06X (up to 2.74X) with 4-bit weights, at a WikiText-2 perplexity increase of at most 10%. With weights offloaded to flash storage, the speedups are 3.31X on average (up to 4.81X) and 1.54X (up to 2.03X).

---


### 63. [Learning When to Commit from Partial Speech for End-to-End Simultaneous Speech Translation](https://arxiv.org/abs/2610.02612)

**<font color=#1a73e8>作者：</font>** Hieu Hoang, Amittai Axelrod  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Simultaneous speech translation must emit useful target text before the source is complete while preserving every committed token. We adapt a full-utterance speech language model using prefix supervision derived from its own complete- and partial-waveform translations, requiring neither transcripts nor human translations. We compare single-turn forced-prefix and multi-turn append-only decoding, use a confidence threshold to control the inference-time quality--latency trade-off, and vary the density of training prefixes with a separate synthesis margin. On FLEURS and CoVoST2 in three language directions, prefix training improves quality--latency frontiers over the unadapted model, and confidence provides the broadest consistently competitive operating range. Multi-turn decoding is generally stronger at low latency; under multi-turn training, commit-calibration error falls by 63--68% overall and 68--80% at early prefixes, whereas single-turn training provides only modest overall calibration gains and no early-prefix improvement. A small synthesis margin sometimes extends the frontier to lower latency, particularly on shorter utterances, while a larger margin degrades translation quality and calibration. Prefix adaptation therefore improves simultaneous speech translation, especially under multi-turn append-only decoding, while synthesis density introduces a non-monotonic quality--latency trade-off.

---


### 64. [What Is Lost in Post-Training? Default Collapse and the Loss of In-Context Steerability Across Diverse Perspectives](https://arxiv.org/abs/2610.02614)

**<font color=#1a73e8>作者：</font>** Jessica Dierking, Itai Shapira, Niclas Boehmer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI models serving a heterogeneous population must act on the principles appropriate to each user and context. While post-training has been shown to narrow the views large language models express, prior work has focused on default behavior rather than the ability to adapt to in-context information. We show that post-training also degrades a model's ability to be steered in-context toward perspectives it was not trained to favor. In controlled experiments, we fine-tune models toward one side of cultural-value disagreements and evaluate checkpoints throughout training. The trained side becomes increasingly dominant in ordinary use, while the ability to recognize and faithfully enact the opposing view declines. These findings point to a tension between prioritizing a single set of values and preserving the technical capacity needed to serve diverse stakeholders. Finally, we propose and analyze an alternative objective that maximizes reward subject to a prescribed distribution over expressed perspectives, and present stance-distribution matching as a practical implementation.

---


### 65. [VERSE: Verified Self-Evolving Optimizer for Agent Harnesses](https://arxiv.org/abs/2610.02616)

**<font color=#1a73e8>作者：</font>** Zekai Wang, Yingqiang Ge, Zekun Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Harness evolution improves an LLM agent's prompts, tools, and workflow, while the optimizer's own tools and procedures often remain fixed. We study whether an optimizer can improve another agent more effectively by also improving how it diagnoses failures, develops edits, and tests their effects. Two observations guide our design. In a controlled study, optimizer self-evolution fails to improve performance without execution-based verification, but achieves the best result of that study when verification is available. Across five executors, self-evolving optimizers build their own tools for failure analysis, verification, training audits, and workflow control. Motivated by these findings, we introduce VERSE, a Verified Self-Evolving optimizer for agent harnesses. VERSE lets the optimizer test draft edits, replay failures, and perturb suspected steps before submission, while tracking fixes and regressions across rounds. Using this feedback, the optimizer revises both the executor harness and its own prompts, skills, tools, hooks, and notes, while the weights of the optimizer and executor models stay fixed. Under a shared protocol with disjoint training, validation, and test tasks, VERSE improves all four evaluated harness optimizers on held-out SWE-rebench tasks and newer out-of-distribution tasks in five languages. Its best validation-selected harness reaches 42.3% and 37.7% accuracy, respectively, against 39.2% and 29.3% for the strongest baselines. Code is available at this https URL.

---


### 66. [CuBEs: Culturally-Situated Behavioral Evaluations and the Limitations of Culture-Blind LLM Judges](https://arxiv.org/abs/2610.02622)

**<font color=#1a73e8>作者：</font>** Hoda Ayad, Tanu Mitra, Abhishek Mukherji  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating the occurrence and triggers of large language model (LLM) behaviors - such as sycophancy, self-preference, or over-confidence - is critical for predicting real-world model deployment risks. However, existing situated behavioral evaluations typically ignore cultural context, limiting their generalizability across an increasingly global user base. To address this gap, we propose CuBEs - Culturally-situated Behavior Evaluations that probe for response patterns across diverse user cultures. We first extend an automated testing pipeline to inject cultural context into behavioral test scenarios and subsequent evaluation. We assess the cultural adaptability of this pipeline by building a human-labeled dataset that captures nuanced dimensions of behavior understanding across 12 distinct cultures. Our dataset reveals significant cross-cultural variations that one-size-fits all judgments fail to capture. Through evaluating 13 open- and closed-source LLMs, we find that introducing cultural situatedness in the evaluation scenario creates significant variation in the presence of a behavior. For example, while our baseline experiments testing for political bias capture localized Western political dimensions like the American conservative-progressive divide, non-Western culturally situated evaluations surface entirely different axes of bias such as religious and colonial political issues. Our findings demonstrate that standard, culturally-agnostic evaluations fail to capture these shifts, highlighting the necessity of culturally situated behavioral testing for global deployments.

---


### 67. [Imagine the Future, Internalize the Gist: Efficient VLA Reasoning via Internalized Spatiotemporal Imagination](https://arxiv.org/abs/2610.02626)

**<font color=#1a73e8>作者：</font>** Shenglan Li, Zhendong Mi, Hengyi Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models increasingly incorporate intermediate reasoning to improve robotic manipulation, yet existing approaches primarily reason about observed states without explicitly anticipating future scene evolution. Extending such reasoning to explicit future rollouts at every inference step, however, introduces substantial computational overhead. We propose IG-VLA, a VLA reasoning framework that enables models to imagine the future and internalize the gist. Our Latent Spatiotemporal Reasoning learns to imagine task-relevant future scene evolution directly in visual representation space, guiding action prediction without costly pixel-level video generation. To further reduce inference overhead, we introduce Scene Gist Memory, which internalizes reasoning-derived scene-behavior associations into a compact Scene Gist Token, preserving the benefits of future reasoning while bypassing explicit future imagination at inference. Extensive experiments on LIBERO, LIBERO-Plus, and VLABench demonstrate the effectiveness and efficiency of IG-VLA. On the LIBERO-Plus Language suite, both the reasoning and gist policies outperform the strongest baseline by nearly 6% in success rate. The gist policy also achieves up to 6.38x speedup over baselines, reducing inference latency from 1081ms to 169.5ms per action chunk on a single NVIDIA A6000 GPU. These results demonstrate that future spatiotemporal reasoning can be effectively internalized for efficient VLA deployment.

---


### 68. [Lost in the Request: How Communication Variation Disrupts Retrieval and Action in Email Agents](https://arxiv.org/abs/2610.02627)

**<font color=#1a73e8>作者：</font>** Feng Chen, Ritam Dutt, Atnaz Taheri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An email assistant should not complete less work simply because a user phrases the same request differently. Yet most benchmarks test each task with only one canonical request, leaving this form of robustness largely unmeasured. We test whether email assistants remain reliable when the requested information, available evidence, and expected outcome stay fixed, but the communication style or English variety changes. We construct validated variants along five communication-style axes and four rule-based dialect conditions, and evaluate them on three benchmarks: a retrieval-augmented generation (RAG) pipeline and two tool-using agents. Indirect requests reduce performance on all three benchmarks, while formal requests reduce performance on both agentic benchmarks. Examining the systems more closely shows that these failures have different causes. Verbose requests mainly hurt a lexical retriever by making the relevant email harder to find. By contrast, indirect and dialect variants remain harmful even when the relevant email is retrieved. In the agentic setting, indirect and formal requests mainly cause the agents to omit required actions, not to take more unsupported actions. These results show that a successful response is not enough to establish robustness: evaluations should vary how requests are expressed and separately measure whether agents complete the requested work.

---


### 69. [Designing the Future of User Feedback for Generative AI](https://arxiv.org/abs/2610.02631)

**<font color=#1a73e8>作者：</font>** Alisa Frik, Julia Bernd, Amitis Karami 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-deployment feedback from users can be a cost-effective, scalable, and representative means to monitor and improve generative AI systems and features. When implemented effectively, giving such feedback can increase users' engagement with and trust in GenAI systems. Government regulations and industry guidelines call for post-deployment user engagement, but there is little guidance on designing mechanisms that are usable for consumers and provide actionable input for product teams. We conducted a multi-phase study as a collaboration between academic researchers and eBay. Our benchmark evaluation of current industry approaches identified common issues including lack of discoverability, unclear terminology, and inattention to user value. Based on these findings, we developed best-practice recommendations and designed and tested a prototype feedback-collection tool. The tool aimed to provide users with an efficient, flexible, and positive feedback-giving experience, and provide product teams with rich data on performance and potential problems in a usable format.

---


### 70. [Online Verification of Language Model Responses Under Cost Constraints](https://arxiv.org/abs/2610.02632)

**<font color=#1a73e8>作者：</font>** Erfan Hajihashemi, Yanning Shen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As large language models are increasingly deployed for multi-step reasoning, verifying the correctness of their outputs has become essential for maintaining reliability at scale. Verifying the correctness of large language model outputs is often done by querying a costly ground-truth oracle, which is impractical to invoke at every step in an online setting. Prior work addresses this by querying a single weak verifier on every step, and using its score to decide whether the costly strong verifier needs to be queried as well, reserving strong verification for only a small fraction of the steps. However, a single fixed weak verifier may not perform consistently well as the subject matter or difficulty of incoming queries changes over time, and committing to one in advance risks either overly costly or inaccurate verification. We introduce OMVV (Online Multi-Verifier Verification), an algorithm that maintains a pool of $K$ candidate weak verifiers with differing cost and verification performance, and adaptively routes each round's decision to a verifier selected via an online score combiner and an exponential-weights routing policy. OMVV provides a distribution-free, finite-time guarantee on false-accept and false-reject rates across the full pool of verifiers, and further achieves sublinear regret against the best fixed verifier in hindsight under a combined cost and consistency objective. Experiments on reasoning dataset benchmarks show that OMVV achieves higher accuracy at lower verification cost than any single fixed verifier, across a range of operating budgets.

---


### 71. [Batched Speech Decisions Without Decoding: Single-Token Supervision Lets a Frozen LLM Hear Beyond the Transcript](https://arxiv.org/abs/2610.02638)

**<font color=#1a73e8>作者：</font>** Jie Jin, Ziyin Ma, Min Yin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Full-duplex voice agents make many small, closed decisions, which current systems answer by slow autoregressive decoding. We propose DuplexJev, which feeds ASR-encoder hidden states through a small connector into a frozen LLM and reads each question as a single-token distribution over its options. Nothing is decoded, and an 8-GPU node answers 80 decisions about eight utterances in about 0.1 s. With a last-layer connector, spoken QA stays close to reading the transcript (90% vs. 91%). DuplexJev also hears the speaker: gender and emotion accuracy both reach 90% (from 55% and 28%) with a cross-attention connector, whose spoken QA drops by only 1 point (83% to 82%). We train decisions with cross-entropy on the read-out answer token, instead of the usual transcript distillation, whose teacher never hears the voice, and keep distillation for content. Encoders and LLMs are interchangeable; we release weights, training recipe, a batched-inference pipeline for full-duplex serving and a bilingual spoken-QA set.

---


### 72. [Coherence-Driven Belief Formation and Population Dynamics of Contagion in LLM Agents](https://arxiv.org/abs/2610.02654)

**<font color=#1a73e8>作者：</font>** Tathagata Banerjee, Nima Moghaddas  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Models of social contagion usually assume how individuals adopt beliefs and derive population behavior from it. We instead empirically measure belief adoption in language model agents, quantifying the probability an agent adopts a claim given how many peers endorse it. We find this adoption kernel to be sigmoid, a characteristic of complex contagion, with a threshold that is sensitive to three sources: the claim's plausibility, the source's reliability, and the agent's disposition. These three dimensions are well approximated by a single effective dimension which we propose can be understood as the coherence of the incoming belief with the LLM agent's prior beliefs. Further, we observe a characteristic of complex contagion in the collective dynamics of belief adoption in a system of AI agents: further spread on clustered than random networks. These systems also exhibit a bifurcating cascade window, and self-sustaining hysteretic consensus which lead to consensus being far harder to remove than to establish.

---


### 73. [Context-Tower Conversion Preserves Generation While Freezing Retains Knowledge: Low-Budget AR-to-Diffusion Conversion of MoE LLMs](https://arxiv.org/abs/2610.02657)

**<font color=#1a73e8>作者：</font>** Wentao Lu, Jesse Clark, Tianyu Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Converting a pretrained autoregressive (AR) model to a diffusion language model (dLLM) enables parallel generation without pretraining a new model. Published conversion methods differ by roughly three orders of magnitude in training data and have not been compared under a common protocol. We compare two conversions of the same 30B Mixture-of-Experts (MoE) parent, holding the corpus, supervised-token budget, trainable parameter set and evaluation harness fixed, each under its own training recipe. The in-place model updates a subset of the parent's weights using denoising and representation-alignment losses; the frozen-tower model instead conditions through cross-attention on a frozen causal copy of the parent. With 1B training tokens, the frozen-tower model scores 71.60 on HumanEval pass@10 against 6.19 for the in-place model, an 11.6x improvement. At the same budget it also keeps 95% of the parent's GSM8K score and 99% of its MMLU-Pro score. A dense-parent experiment reproduces the HumanEval separation. Within the two-tower design at about 500M tokens, freezing the context tower retains substantially more MMLU-Pro performance than training it, while both give similar observed HumanEval scores. Our theoretical analysis establishes that both conversion classes contain an exact sampler for the AR parent under a hard attention mask and left-to-right commitment of one position per round. Under a shared loss, freezing removes the gradient contribution through the context states. Furthermore, evaluation protocol substantially affects a published 500B-token conversion's scores in both directions across tasks, while its AR parent's scores vary by less than three points, so comparing dLLMs needs a common protocol. These results show that, in the tested low-budget regime, the frozen-tower configuration retains substantially more of the parent's generation performance than in-place conversion.

---


### 74. [A GHOST in Long-Horizon Agents: Governance Hazard from Overlooked Safety Constraints across Turns](https://arxiv.org/abs/2610.02664)

**<font color=#1a73e8>作者：</font>** XinPeng Shen, Lan Zhang, Yixiao Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents are now playing an increasingly significant role in assisting humans with complex problem-solving. However, it is exactly their extended interaction history that introduces an underexplored execution-safety concern. Under benign interaction conditions, an agent may execute an action that violates a safety constraint specified many turns earlier. We term this failure mode Governance Hazard from Overlooked Safety Constraints across Turns (GHOST), which may cause irreversible damage. Our experiments reveal that GHOST events are not isolated cases: this failure mode, occurring precisely under benign interaction conditions, yields an occurrence rate of 11.5% on GPT-5.5. Furthermore, we theoretically show that if the residual conditional violation hazard along each safe prefix is bounded below by a non-summable sequence, the execution enters the hazard region almost surely. Leveraging this theoretical insight, we further propose STAR-Guard, a two-layer defense coupling historical semantic safety constraint restoration with pre-execution audit. STAR-Guard restores applicable safety constraints to reduce unsafe proposals, while its deterministic audit layer prevents residual violations from reaching the environment. Consistent with this two-layer design, we observe no GHOST events in our experiments under the GPT-5.5 setup.

---


### 75. [Large Language Continuous Diffusion Models](https://arxiv.org/abs/2610.02665)

**<font color=#1a73e8>作者：</font>** Zhihan Yang, Wei Guo, Jean-Marie Lemercier 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite the success of discrete diffusion language models (dLMs) for fast parallel decoding, their non-smooth, high-dimensional space hinders trajectory steering for reasoning and inference acceleration. To overcome this, we present Sigma, the first large-scale (3B/8B) continuous dLM built on steerable, low-dimensional ODE/SDE latent trajectories. Trained blockwise via likelihood optimization, Sigma jointly denoises Gaussian-corrupted token embeddings while learning an optimal embedding geometry. To accelerate training, Sigma leverages pre-trained weights from autoregressive (AR) models for warm-starting. During inference, we identify classifier-free guidance and score temperature as essential for high-fidelity reasoning and coding. Across comprehensive math reasoning and coding evaluations against state-of-the-art discrete counterparts (masked dLMs and AR baselines), Sigma achieves competitive performance with discrete models on standard benchmarks (e.g., GSM8K, Minerva, HumanEval, MBPP) after pre-training and on challenging reasoning tasks (e.g., MATH-500, AIME) after supervised fine-tuning. Beyond performance parity, we uncover key structural properties unique to continuous dLMs: (i) embedding-space steering effectively governs the quality-diversity trade-off, yielding strong pass@k performance and (ii) continuous trajectories enable graceful degradation for low NFEs and efficient distillation. These establish continuous dLMs as a promising paradigm for efficient language generation.

---


### 76. [CHASE-VLA: Post-Training Quantization Framework for Vision-Language-Action Models with Chunk-Aware Scale Estimation](https://arxiv.org/abs/2610.02666)

**<font color=#1a73e8>作者：</font>** Jin Hyun, Jung Gyu Min, Gyuhyun Jung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models map visual observations and language instructions to continuous robot actions, but a diffusion-based action expert (AE) poses a key challenge for low-bit post-training quantization (PTQ). The AE is repeatedly invoked across denoising steps and policy queries, where fixed calibration scales can be mismatched with activation ranges that vary with denoising progress and intended motion. We propose CHASE-VLA, a chunk-aware PTQ method that exploits a VLA-specific signal readily available from the policy: the generated action chunk, including its unexecuted future suffix. Rather than relying only on static scale matching for AE layers, CHASE-VLA combines the previously generated chunk as causal action context with denoising step group information to adapt AE activation scales. This enables W4A4 quantization of both MLP and attention projections in the repeated AE without modifying the pretrained policy. On LIBERO, CHASE-VLA achieves 97.3% average success rate on $\pi_{0.5}$ when both MLP and attention projections in the AE are quantized to W4A4, restoring FP16-level performance. CHASE-VLA also reduces the weight storage of the quantized AE linear layers by 73.4% and their single-chunk memory traffic by 70.9% and 71.2% on $\pi_{0.5}$ and GR00T N1.6, respectively, with a predictor overhead of at most 1.26% of the saved storage.

---


### 77. [LEAP: Learning Efficient Action Proposals For LLM Agents](https://arxiv.org/abs/2610.02670)

**<font color=#1a73e8>作者：</font>** Zhen Xu, Qizheng Zhang, Gerry Wan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents are known to be slow in rollouts. An agent completes a task one step at a time. At each step, it reasons and then chooses an action to execute. The next step and action cannot start until the previous one has finished. Speculative decoding accelerates the rollouts at the reason phase by drafting and verifying the inference tokens. Recent works have also started to apply similar ideas at the action phase. These works use off-the-shelf models, usually large, to draft action proposals for target model to verify. Large drafters match the target more often but take longer to propose, while small off-the-shelf models are fast but rarely make the same decision as the target. We ask a more general question: what determines the end-to-end speedup of action speculation? To answer it, we develop a latency framework for the speculative round. The framework compares what a round gains with what it costs. The gain depends on how well the drafter predicts the target and on how many steps the task can take before it ends. The cost comes from drafting, from waiting for target verification and from executing tools. Guided by the framework, we introduce LEAP (Learning Efficient Action Proposals) which keeps the drafter small and makes it accurate by training it on the target actions sequences. With a small 0.6B model, LEAP agrees with the target on most decisions and makes agents up to 60% faster in end-to-end wall clock time, with no systematic change in task success. Across various datasets, target models and draft models, the framework accounts for most of the measured speedups. We also show the draft model can be online trained with no prior trace collection and match the performance of offline training, making LEAP practical to deploy in the real world.

---


### 78. [Asterism: Exploring and Synthesizing Scattered Observations into Literature-Grounded Hypotheses and Theories](https://arxiv.org/abs/2610.02673)

**<font color=#1a73e8>作者：</font>** Joseph Chee Chang, Michael D'Arcy, Amy X. Zhang 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> A theory draws many independent observations into one framework with novel hypotheses. A researcher building such a theory must synthesize observations scattered across many papers, each describing related concepts but often in different terms. Which concepts matter most also depends on their preferences and research questions. Recent approaches scale theory synthesis with LLMs, but automate away choices and intuitions from researchers. We present Asterism, which extracts observations from hundreds of papers as concept-relation triples, with concepts unified in a hierarchical ontology. Researchers curate an evidence graph using the ontology and aggregate observations at different levels of granularity to focus theory formation on specific phenomena of interest. In a field deployment (n=10), researchers worked from observations to theories, and kept concepts and hypotheses fitting their preferences. In two case studies, teams of immunology and agriculture researchers discovered mechanisms outside their standard analyses and constructed hypotheses worth follow-up experiments.

---


### 79. [Spend Teacher Tokens Where They Matter: Success-Referenced On-Policy Distillation](https://arxiv.org/abs/2610.02678)

**<font color=#1a73e8>作者：</font>** Xiang Chen, Futao Su, Kong Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) combines student-generated rollouts with dense token-level supervision from a teacher, but providing such supervision for every rollout requires substantial teacher computation. We introduce Success-Referenced On-Policy Distillation (SR-OPD), which reduces this cost by selecting which prompts and rollouts receive teacher supervision. When the student produces both successful and failed rollouts for the same prompt, a successful rollout can serve as a natural reference for selecting failed rollouts. SR-OPD therefore focuses on such prompts and prioritizes failed rollouts whose hidden-state trajectories show sustained divergence from a successful reference, while accounting for estimated teacher-input cost. Across three teacher-student pairs and six mathematical reasoning benchmarks, SR-OPD uses only 3.46-5.02% of the teacher-input tokens required by Vanilla OPD in the one-pass setting while maintaining comparable reasoning performance. Under a controlled setting matched to 5% of Vanilla OPD's teacher-input budget, further experiments support both key design choices: focusing supervision on prompts with both successful and failed rollouts, and using successful rollouts to guide failure selection. These results indicate that a student's own successful behavior can serve as a useful reference for allocating teacher supervision under a fixed teacher-input budget.

---


### 80. [DataWeave: Deploying Human-LLM Analytics for Exploratory Structured Data Analysis](https://arxiv.org/abs/2610.02679)

**<font color=#1a73e8>作者：</font>** Raquib Bin Yousuf, Harith Laxman, Vitaliy Shkremetko 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data journalism, the practice of using data analysis to surface newsworthy stories, depends increasingly on the ability of reporters and investigative journalists to uncover trends, disparities, and accountability narratives. In practice, exploring large structured datasets remains slow and brittle: journalists must navigate hundreds of variables across many datasets over years, understand data coding conventions, and write non-trivial analysis code while hypotheses evolve. Although LLMs are often touted as "ask in English, get SQL/answers," real newsroom workflows expose recurring failures, e.g., schema mismatches and drift, misread domain semantics and units, and silent assumptions. We present DataWeave, a system that addresses these needs by combining conversational interaction, schema grounding, analytical planning, and executable query generation to support exploratory analysis over structured data. Rather than treating LLMs as autonomous answer engines, DataWeave frames them as interactive partners whose outputs can be inspected, corrected, and steered as hypotheses shift. We present a case study with professional journalists using our system to analyze the U.S. Department of Education's Integrated Postsecondary Education Data System (IPEDS), a high-stakes public dataset with substantial domain semantics and frequent schema updates. We also report how deployment experience and iterative refinement shaped the current DataWeave architecture and its analytical workflow. Our findings distill design principles and deployment lessons for trustworthy human-LLM collaboration in structured data analysis.

---


### 81. [RAOA: Alternating-Operator Neural Computation with Programmable Radio Propagation](https://arxiv.org/abs/2610.02683)

**<font color=#1a73e8>作者：</font>** Toshiaki Koike-Akino  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can programmable radio propagation serve as computational depth rather than only as a communication channel or one-shot analog transform? We introduce the Radio Alternating Operator Ansatz (RAOA), a recurrent computing architecture that alternates an energy-derived problem update with a mixing update over a persistent latent state. Recomputing the problem field after each mix makes repeated passes compositional even when the same learned controls are reused across depth. We evaluate this idea through exact discrete optimization, constrained programmable-propagation simulation, and pretrained-model adaptation. On discrete objectives, repeated execution can improve solution quality without increasing the learned-control count, and the same formulation handles higher-order interactions directly. A passive phase-only free-space model further shows that the required operators can be approximated by programmable propagation while retaining useful downstream behavior despite realization error. When inserted as a zero-initialized residual adapter, RAOA adapts pretrained language models with WikiText performance close to a matched shallow MLP across three model families, while reasoning-task transfer remains model-dependent. Together, these results connect alternating-operator computation, programmable radio propagation, and neural adaptation within one recurrent framework. The RF realization evidence is simulation-based rather than a hardware demonstration.

---


### 82. [Large language models exhibit unreliable updating of clinical judgment as patient evidence evolves](https://arxiv.org/abs/2610.02684)

**<font color=#1a73e8>作者：</font>** Min Zeng, Rui Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly explored for clinical reasoning, but whether they appropriately revise judgments as patient evidence evolves remains unclear. We evaluated longitudinal belief updating using matched intensive-care trajectories from electronic health records. Across diverse LLMs, conditioning on a preceding judgment more often increased than reduced prediction error when estimates changed, replicated for a second endpoint. Controlled interventions revealed two failure modes. First, with preceding assessment fixed, models responded more strongly to worsening than matched improving respiratory evidence; this asymmetry persisted after headroom normalization at moderate and strong evidence levels. Second, with current evidence fixed, increasing prior risk from 10% to 90% shifted estimates by 26.2 percentage points, demonstrating causal influence of prior model beliefs. Prompting did not restore reliable updating. Evidence-Validated Longitudinal Update (EVLU) identified fewer, more reliable revisions, revealing a reliability-coverage trade-off. These findings establish longitudinal belief updating as a distinct dimension of LLM reliability.

---


### 83. [Decoupling Memory from Context: Structured Memory for Token-Efficient Test-Time Continual Learning](https://arxiv.org/abs/2610.02687)

**<font color=#1a73e8>作者：</font>** Yehya Farhat, Michael Desmond, Anastasios Kyrillidis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in enterprise, scientific, and medical applications, where agents must incorporate domain-specific knowledge and adapt from experience. Context engineering offers a practical alternative to weight updates by improving model behavior through instructions, strategies, and evidence supplied at inference time. However, adapting context online typically requires a costly trial-and-error process, while queries are often processed independently, preventing useful experience from carrying forward. Memory systems address this limitation by retaining information across interactions, but approaches that continually append information to a shared context face increasing token costs, context-window limits, and performance degradation as the context expands. We introduce a unified formulation of context optimization and show that an agent memory system update can be interpreted as an optimization update procedure over the model's context. This perspective attempts to provide a principled framework for studying memory design and its efficiency. We then propose GraphMemory, a lightweight graph-based memory that accumulates, refines, organizes, and connects reusable strategies. For each query, GraphMemory retrieves only the relevant subgraph, enabling online context adaptation without exposing the model to the entire memory. Under bounded retrieval, the amount of retrieved memory remains constant as the number of processed examples grows. Experiments show that GraphMemory achieves competitive downstream performance while using approximately 81-85% fewer memory-construction tokens than our baselines.

---


### 84. [Test-time Calibration Learning for Large Language Model Reasoning](https://arxiv.org/abs/2610.02695)

**<font color=#1a73e8>作者：</font>** Zizhuo Zhang, Xiong Peng, Jingwei Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable large language models (LLMs) must not only produce accurate answers but also express confidence that faithfully reflects their probability of being correct. Such calibration is essential for identifying uncertain predictions and supporting reliable decision-making in real-world deployment. Recent studies incorporate calibration learning into reinforcement learning (RL), jointly optimizing answer correctness and verbalized confidence using ground-truth correctness supervision. However, their reliance on labeled data limits their applicability in practical test-time settings, where ground-truth labels are unavailable and calibration may need to adapt to newly encountered target tasks. To address this challenge, we propose Test-Time Calibration Learning (TTCL), a label-free framework that jointly adapts reasoning accuracy and verbalized confidence directly on unlabeled target-task data. Specifically, TTCL derives self-supervision signals for both correctness and calibration from multiple model-generated responses, enabling calibration learning at test time without ground-truth labels. Theoretical analysis further establishes TTCL as a bounded surrogate for the ideal calibration objective. Extensive experiments on mathematical reasoning and factual question answering demonstrate that TTCL consistently improves both accuracy and calibration across diverse models and tasks. On base models, TTCL achieves an average relative accuracy improvement of +40.13% and an ECE reduction of +70.80% across eight benchmarks. Moreover, TTCL can further improve both accuracy and calibration for already calibrated models under domain shift, particularly when source-domain calibration transfers poorly to target tasks. In the math-to-factQA setting, TTCL achieves an average relative accuracy gain of +20.35% and reduces ECE by +53.83%. The source code is released at this https URL.

---


### 85. [Learning from Evolving Errors: Adaptive Iterative Repair for On-Policy Distillation](https://arxiv.org/abs/2610.02700)

**<font color=#1a73e8>作者：</font>** Rui Li, Liyang He, Zheng Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) supplies dense token-level feedback on trajectories sampled from the student's own policy, a richer training signal than the outcome-level rewards of reinforcement learning. This feedback comes from a teacher conditioned on a full reference solution unavailable to the student. The reference solution specifies the target but not how to move from the student's current error toward it, creating a solution-conditioned shortcut risk. We introduce AIR-OPD, an adaptive iterative repair framework for on-policy distillation that provides error-to-repair supervision. Given a failed response, a guidance generator synthesizes repair guidance for the current error. The student samples an on-policy retry with this guidance. If the retry remains incorrect, the generator produces new repair guidance for the newly observed error. At each round, a fixed teacher receives the guidance as privileged context and supervises the student on an error-aligned region of its latest failed response. Outcome-aware stage weighting favors early repair stages and credits stages whose immediate retry passes verification. We train AIR-OPD on the DAPO-Math-17K dataset and evaluate on AIME24, AIME25, and HMMT25, alongside out-of-distribution tests on MMLU-Pro and GPQA. We examine two guidance sources, self-guidance from the current student policy and external guidance from a larger model. For both Qwen3-4B and Qwen3-8B, AIR-OPD attains the best mathematical-reasoning averages, improving over the strongest baseline by up to 3.6 points, while preserving base-model performance on the out-of-distribution benchmarks.

---


### 86. [Conditional Capacity and Routing in Mixture-of-Experts Particle Transformers](https://arxiv.org/abs/2610.02701)

**<font color=#1a73e8>作者：</font>** Kaushik Pendiyala, Haris Zia, Trevin Lee 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models can increase parameter capacity without proportionally increasing active computation, but it is unclear how this trade-off behaves in particle-physics transformers. We study dense and MoE Particle Transformers on 188-class JetClass-II, varying expert count, routing capacity, top-K, and auxiliary loss. We find that, when token dropping is avoided, top-1 MoE models improve over the dense baseline at nearly unchanged nominal forward compute, while further increasing the number of stored experts produces little additional accuracy gain. Activating multiple experts per token yields additional predictive improvements at higher computational cost. Routing analyses show that expert assignments become more strongly associated with particle identity and kinematics in some configurations, but this structure does not increase monotonically with classification performance. These results highlight the need to distinguish stored parameter capacity, active computation, routing capacity, and routing organization when evaluating sparse expert models for jet classification. Code and experiment configurations are available at this https URL.

---


### 87. [Silent Dissent: LLM Agents That Yield to the Majority Still Represent Their Original Premise](https://arxiv.org/abs/2610.02702)

**<font color=#1a73e8>作者：</font>** Ziang Ni, Peng Zou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent debate is increasingly used to reach consensus among LLM agents, yet agents often yield to a unanimous majority. When an agent changes its answer, has it changed its mind or only its statement? We study this with two-hop factual questions whose intermediate entity (the bridge, e.g. the country in "the capital of the country where the Sagrada Familia is located") is never stated by anyone. Scripted peers, in the role of Asch's confederates, unanimously assert a wrong answer taken from another fact with a different bridge. At the moment the agent answers, we read the bridge from its residual stream with the Jacobian lens (J-lens) and, for comparison, the logit lens. In pre-registered tests on held-out facts with four open-weight models, agents of Qwen3.5-4B, Qwen3.6-27B and Gemma-4-E4B-it that gave in still represented their original bridge in the pre-registered layers below the output (hit@100 above a control entity: 0.85, 0.22 and 0.24), where the logit lens rarely ranked it among the top 100 tokens (0.00-0.06). These agents also represented the bridge behind the peers' answer, beyond a mention baseline. A pre-registered addendum hid the agent's earlier answer or removed it: agents that gave in still represented their original bridge in all four models (0.43, 0.29, 0.37 and 0.25 with the answer hidden), including Llama-3.1-8B-Instruct, which barely did so with its answer in view (0.03). The premise can thus be computed from the question alone while the agent states the majority's answer. Hiding the earlier answer also changed conformity: Qwen3.5-4B gave in on 89% of questions instead of 8%. In exploratory interventions, injecting the bridge's J-lens direction brought agents back to their original answer only in the two Qwen models. Stated consensus in multi-agent debate can thus overstate agreement. We also report the negative results of our pre-registered program.

---


### 88. [Learning to Revise Reasoning with Segment-wise On-Policy Distillation](https://arxiv.org/abs/2610.02703)

**<font color=#1a73e8>作者：</font>** Yuxiang Zhang, Ding Cao, Shuting Cui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) improves large language model reasoning by training students on their own rollouts with dense token-wise supervision from the teacher. However, token-wise OPD does not explicitly provide a coherent alternative reasoning step showing how the student's step could be revised to improve subsequent reasoning. Furthermore, this paradigm can become less effective when the student produces a degenerate reasoning prefix, as subsequent teacher supervision remains conditioned on that prefix and may reinforce poor reasoning patterns. In this work, we focus on learning reasoning revision with segment-wise OPD to rework intermediate reasoning steps and better support subsequent reasoning. Through controlled reasoning interventions, we find that replacing student segments with teacher redrafts improves subsequent reasoning accuracy. Therefore, we address the problem of turning teacher redrafts into explicit supervision for learning to revise reasoning. We propose Segment-wise On-Policy Distillation (Seg-OPD), which selects student segments based on an uncertainty metric and obtains corresponding teacher redrafts. Seg-OPD trains the student to prefer teacher redrafts over their paired student segments while retaining dense token-wise OPD supervision. Extensive experiments on mathematical reasoning and competitive programming tasks show that Seg-OPD-trained students achieve higher revision success rates than baselines. Seg-OPD consistently outperforms the compared state-of-the-art baselines in reasoning accuracy with an average relative improvement of 5.22% across diverse models and tasks. Code is available at this https URL.

---


### 89. [MuonIO: Principled Norm-Aware Descent for Embedding Tables and Language Model Heads](https://arxiv.org/abs/2610.02705)

**<font color=#1a73e8>作者：</font>** Linkai Ma, Xinyu Luo, Mengbo Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Muon optimizer derives its update rule for hidden linear layers by solving a local linearization of the loss penalized by the spectral norm, motivated by an RMS-stability argument for dense linear layers. Standard Muon implementations, however, exclude the input (embedding table) and output (language model head) layers from this principled treatment, for which they use AdamW instead. We present MuonIO, a single Muon-style update for both of these layers. For the language model head $\mathbf{L} \in \mathbb{R}^{V \times d}$, we motivate the use of the $2\to\infty$ operator norm, due to the Lipschitz continuity of the softmax output geometry, while for the embedding table $\mathbf{E} \in \mathbb{R}^{d \times V}$, we draw on the $1 \to 2$ operator norm, based on the one-hot input geometry identified by Bernstein & Newhouse (2025). The identity $\lVert\mathbf{L}\rVert_{2\to\infty}=\lVert\mathbf{L}^\top\rVert_{1\to2}$ then puts both matrices in the same vocabulary-oriented geometry: MuonIO applies a single normalized-vector rule, which appears as column normalization for $\mathbf{E}$ and row normalization for $\mathbf{L}$. Empirical evaluations demonstrate the effectiveness of our approach, with MuonIO reducing I/O optimizer state memory by 50% and I/O update FLOPs by $\sim$46% compared to Muon for 1B LLaMA pretraining on C4, while also improving validation perplexity.

---


### 90. [WakeKV: Reactive, Reversible KV Residency for Heads That Change Their Minds](https://arxiv.org/abs/2610.02713)

**<font color=#1a73e8>作者：</font>** Utkarsh Ranjan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most KV-cache compression methods classify attention heads once, either offline or during prefill, and keep this classification fixed throughout generation. Across three models (1.5B-8B) and three regimes (needle retrieval, long chain-of-thought, and multi-turn recall), we measure head behavior on four model-regime combinations and find that most heads change their reading behavior at least once during generation. We introduce WakeKV, a reactive residency policy that moves cooling heads to a recoverable CPU reservoir rather than freezing or permanently evicting their state. At matched memory or budget, WakeKV consistently improves miss rate over frozen classification and destructive eviction, evaluated across five model-regime combinations and over three cited baselines (SnapKV, uniform R-KV, and ReasonAlloc) across four eligible combinations. A FlexiCache/vLLM implementation on Mistral-7B confirms the benefit on real hardware, improving throughput while retaining LongBench quality.

---


### 91. [Ego2World: Compiling Egocentric Cooking Videos into Executable Worlds for Belief-State Planning](https://arxiv.org/abs/2610.02715)

**<font color=#1a73e8>作者：</font>** Qinchuan Cheng, Zhantao Gong, Pengzhan Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Egocentric videos capture how people carry out everyday activities, yet testing an agent requires evaluating the consequences of actions it chooses itself. We introduce Ego2World, a benchmark that turns annotated cooking activities into executable planning environments under partial observation. Its compiler links source steps and objects to symbolic action rules, persistent world states, and explicit task conditions, so researchers can execute an agent's proposed actions and check their outcomes. World state and agent belief are maintained separately, enabling controlled studies of planning and information reuse across continuing tasks. Evaluating six planners on 105 tasks shows that accepted operations often leave task goals unmet. Execution traces and condition checks distinguish interrupted runs, partial attainment, and completed execution without goal attainment. In a separate paired Qwen-Plus study, persistent belief improves action validity by 4.15 percentage points and reduces visual-query attempts by 90.27%, with higher token use and no detected completion gain. Ego2World provides a reusable testbed for tracing how planning and memory choices affect execution, observation demand, and task attainment, connecting recorded human activity to the development and evaluation of interactive agents.

---


### 92. [Revisiting Visual Representation Enhancement of VLMs via Kernel Canonical Correlation Analysis](https://arxiv.org/abs/2610.02718)

**<font color=#1a73e8>作者：</font>** Peilin Yang, Xiaoyu Liu, Jian Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models such as CLIP exhibit strong semantic generalization, but remain limited in fine-grained visual perception. A recent work named KUEA presents a natural remedy by finetuning the image encoder under the supervision of the vision-centric DINOv2 to align their kernel matrices element-wisely, while regularizing the embeddings to remain close to the pretrained visual encoder for preserving image-text semantics in CLIP. However, we show that diminishing the role of the alignment loss to DINOv2 does not necessarily degrade its fine-grained visual performance, suggesting that the kernel-matrix discrepancy may be insufficient for further visual representation enhancement, motivating us to revisit the alignment formulation. In this work, we present a novel perspective to characterize representation alignment on feature subspaces through Kernel Canonical Correlation Analysis (KCCA), which maximizes the projection correlations. In optimization, we derive an efficient end-to-end training scheme upon KKT conditions, avoiding the eigenvalue problem in KCCA. Further, we extend our method into a 3-view formulation, i.e., 3vKCCA, in which the projections from the pretrained text encoder are also incorporated under a unified optimization framework for joint alignment. With CLIP ViT-L/14 on ImageNet-1K, our 3vKCCA improves the MMVP-VLM accuracy from 17.8 to 25.9, substantially outperforming the existing methods, and meanwhile maintains zero-shot image--text retrieval performance.

---


### 93. [TPBench: A Turning-Point Benchmark for Dialogue Compression](https://arxiv.org/abs/2610.02736)

**<font color=#1a73e8>作者：</font>** Minji Park, Seunghyun Yoon, Hyuk Lim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A compressor can keep the facts of a dialogue and still drop the turn that changed them. A user corrects a price, reverses a choice, or adds a constraint. We call this failure turning-point eviction. One overall retention score hides it, because that score mixes what the user first wanted with what the user wants now.
We introduce TPBench, which evaluates three complementary information targets at shared nominal retention budgets. P1 asks for the user's initial goal. P2 asks for the current value of a slot the user revised. P3 asks for both, in dialogues with a late annotated slot update. The current-value answers come from the human dialogue-state annotations of MultiWOZ and SGD. The initial-goal answer is the first sentence of the first user turn. Neither requires new crowdsourcing.
The probe-specific evaluations rank compression methods differently. On the joint probe at a retained fraction of 0.30, every tested compressed method remains below full context with the main Llama reader. Deleting the turn that carries the update sharply lowers current-value accuracy, while deleting one matched irrelevant turn leaves it unchanged. A Mistral reader repeats the P2/P3 rankings and the joint-probe gap. Current-value recovery is tested on an additional corpus, LongMemEval-KU, and on Chinese RiSAWOZ: full context has the highest accuracy, and recency has the highest compressed-method mean in both evaluations.

---


### 94. [Inner Momentum for Differentially Private Muon](https://arxiv.org/abs/2610.02738)

**<font color=#1a73e8>作者：</font>** Bishnu Bhusal, Minh Vu, Ben Southworth 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differentially private training clips each per-example gradient before adding noise. This clipping is radial for each example, yet unequal clipping factors can distort the relative singular-vector geometry of their average. Muon is particularly exposed to this effect, since its update is an approximate polar factor UV^T that depends only on the singular vectors that clipping can shift. To curb this degradation, we propose averaging each sampled example's Muon gradient over the current model and a short history of recent models before clipping. The clipped batch matrix then separates into a common rescaling and a covariance residual R between sampled gradients and clipping values, with ||R||_F <= sigma_lambda sigma_G, bounding the clipping-induced distortion directly. We further show that a finite Newton-Schulz iteration preserves the polar factor of its input under these spectral conditions, confirming that our correction survives orthogonalization. In private GPT-2 fine-tuning on E2E and DART at epsilon in {1, 2, 4, 8}, DP-Muon-IM improves BLEU and ROUGE-L over DP-Muon in every seed-matched comparison, and non-private diagnostics show 2-4% lower pre-noise polar error.

---


### 95. [On the Chain-of-Thought Monitorability of Looped Language Models](https://arxiv.org/abs/2610.02741)

**<font color=#1a73e8>作者：</font>** Han Wang, Ishwar B Balappanawar, Huan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) monitoring provides a promising approach for detecting undesirable model behavior. Looped language models (LoopLMs) repeatedly apply shared transformer layers, increasing effective computational depth and enabling additional latent computation without increasing model size. However, the effect of looped architectures on CoT monitorability remains largely unexplored. In this work, we provide the first systematic evaluation of CoT monitorability in LoopLMs. We study two complementary settings: (1) varying the loop depth within the same LoopLM family to isolate the effect of additional recurrent computation, and (2) comparing LoopLMs with non-looped language models matched by parameter size, transformer-layer count, or effective depth to study whether LoopLMs are less monitorable. Across eight tasks from MonitorBench and both standard and stress-test settings, we observe task-dependent reductions in CoT monitorability under stress tests on specific Logic/Science/Engineering \texttt{Cue Answer} tasks, while other tasks exhibit weaker or qualitatively different trends. Our diagnosis suggests that these declines are not fully explained by task difficulty, verification pass rate, or generated token length; qualitative examples further suggest changes in how deeper-loop models explicitly use or attribute provided cues. Our cross-model comparison finds no evidence that LoopLMs are systematically less monitorable than non-looped language models matched on size or depth. Overall, our results suggest that deeper loop depth can reduce CoT monitorability in some tasks under stress tests, but looped transformer architecture alone does not necessarily imply lower monitorability.

---


### 96. [EpiWorld: Grounding LLM Policy Agents in Epidemiological World Models](https://arxiv.org/abs/2610.02744)

**<font color=#1a73e8>作者：</font>** Zeeshan Memon, Yiqi Su, Kai Shu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Epidemic intervention policies are textual artefacts that human decision-makers interpret, justify, and revise through natural language, making large language models a natural candidate for epidemic policy reasoning. A naive LLM, however, lacks the epidemic dynamics needed to project intervention consequences, the quantitative surveillance signals required to assess severity, and the institutional constraints that define admissible actions. We present EpiWorld, a closed-loop framework that grounds an LLM policy actor in a learned action-conditioned epidemiological world model and a tiered skill library of public-health protocols, surveillance tools, and adaptive lessons accumulated through after-action analysis. Given a candidate intervention, the world model predicts regional epidemic evolution and enables fast counterfactual rollouts that provide feedback for policy selection and refinement. Outcomes of simulated futures are distilled into reusable lessons while protocol constraints remain fixed, allowing the decision process to improve without sacrificing interpretability or controllability. We evaluate both the world model and the end-to-end framework on retrospective COVID-19 and Influenza datasets: the world model achieves the best out-of-distribution Peak-MAE among all forecasting baselines, and the closed-loop framework reduces cumulative hospitalisation by up to 59% across datasets and by an average of ~16% across six LLM backbones, outperforming reinforcement-learning and optimal-control policy baselines.

---


### 97. [FiberGeoText: A Vision-Language Model for Population- Level Organization of Superficial White Matter](https://arxiv.org/abs/2610.02755)

**<font color=#1a73e8>作者：</font>** Yuqian Chen, R. Jarrett Rushmore, Guikun Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The superficial white matter (SWM), a critical brain region for cognition across the lifespan and brain disease, contains abundant short-range association fibers whose organization remains incompletely characterized, in part because the short trajectories and highly variable cortical folding make correspondence across individuals challenging. Anatomically corresponding connections may vary in spatial location across individuals and therefore may not be adequately defined by geometric proximity alone. We introduce FiberGeoText (FGT), a vision-language model (VLM) for organizing short-range superficial white matter (SWM) streamlines reconstructed from ultra-high-resolution diffusion MRI into population-level clusters. FGT jointly represents three complementary properties of each streamline: its three-dimensional trajectory, its cortical anatomical context, and its shape. Cortical endpoint information from multiple parcellation schemes is expressed as text and encoded using a pretrained large language model (LLM), enabling heterogeneous anatomical descriptions to contribute to a common continuous representation. We evaluated FGT on acquired submillimeter 0.76 mm diffusion MRI data. Compared with state-of-the-art (SOTA) methods, FGT produced substantially greater cortical parcel coherence, within-cluster shape consistency, cluster-size consistency, and cross-subject correspondence. The trained model also generalizes well to unseen subjects with an average of 96.7% of the 5,000 learned clusters recovered, and high consistency of cluster structure between training and testing data. Together, these findings demonstrate that integrating geometric, anatomical, and shape information by learning multimodal deep embeddings with a VLM model enables robust learning of population-consistent SWM organization despite interindividual anatomical variability.

---


### 98. [Dynamic LLM Routers are Often Misguided](https://arxiv.org/abs/2610.02762)

**<font color=#1a73e8>作者：</font>** Sam Wang, Julia White, Sahibzada Allahyar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dynamic LLM routers promise to cut inference costs by sending each query to the cheapest model that can answer it correctly. We analyze six commercial routers across 14 settings on a diverse benchmark spanning eight task categories, finding that none of them outperforms a router that randomly selects between two well-chosen models at matched cost. Some underperform by more than 10 percentage points. We trace this gap to four patterns prevalent across routers: difficulty blindness, length reversal, semantic matching, and roster suboptimality. We show that the first three are what the standard objective rewards: cost-accuracy Pareto efficiency on realized costs favors escalating moderately hard queries over the hardest ones, shorter queries over longer ones, and routing by a query's source over its difficulty. We also argue that the two assumptions that would justify large rosters, model granularity and model specialization, do not hold empirically. We propose an alternative evaluation methodology that does not reward these patterns, and as a proof of concept, we design a simple two-model router that avoids all four. Nevertheless, its gain over random routing is limited, because a well-chosen roster leaves little to route.

---


### 99. [A Controlled Audit of Personal AI Memory for Rating Prediction](https://arxiv.org/abs/2610.02764)

**<font color=#1a73e8>作者：</font>** Shivam Gupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In structured rating prediction, does a personal AI use historical item-rating associations, or mainly the user's rating tendencies? We audit this distinction by permuting historical ratings within each user while preserving the exact rating distribution, item support, and metadata. We combine this control with full history, native memory extraction, and matched numerical readers in a publicly frozen evaluation of 400 held-out user profiles and 6,160 target ratings across Coat and MovieLens. On Coat, the tested Qwen-written Mem0 pipeline increases user-macro mean absolute error relative to full history by 0.084 for Qwen and 0.149 for Phi; both family-adjusted bootstrap intervals exclude zero. Correct historical assignments help both readers on Coat, but the corresponding MovieLens effects are smaller and inconclusive after adjustment. A history-only ridge reader outperforms Qwen in both domains and Phi on MovieLens, while the Coat Phi comparison is unresolved. All 2,800 reader calls, including 150 invalid outputs, are retained under a fixed fallback rule. A separate implementation verifies inputs, metrics, and all ten primary contrasts. The contribution is a reproducible diagnostic study showing why extraction, association use, output reliability, and reader choice require separate evaluation.

---


### 100. [Exact Memory-Time Optimization for Prefix-Cached Language Model Serving](https://arxiv.org/abs/2610.02766)

**<font color=#1a73e8>作者：</font>** Shivam Gupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retaining language-model prefix states trades recomputation against storage time. Optimizing each cached block independently can overcount savings: a resident block is usable only when the required preceding prefix is also available. We introduce Prefix-Certificate Retention (PCR), an exact finite-trace formulation for static, grouped, reset-on-access timeouts. Usable-prefix rewards become nodes whose prerequisites are timeout thresholds and preceding hit certificates. The resulting maximum-weight closure reduces to one minimum cut, with graph size linear in the number of block lookups and timeout choices. A breakpoint theorem extends the construction to all nonnegative timeouts without discretization error. We also derive a linear-time-in-grid-size dynamic program for ordered timeouts and bounds that certify the cost of this restriction. Exhaustive small-instance checks and chronological replay of 39,632 public Mooncake requests validate the formulation. On the fixed grid, ordered timeouts attain the unrestricted training optimum in 118 of 120 trace-grouping-price cases. Heterogeneous retention improves several held-out memory-time tradeoffs, but finer training optimization does not uniformly improve transfer. The contribution is a tractable optimization model and an auditable benchmark for retention policies; the experiments measure usable prefix blocks and storage time, not GPU latency.

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-261](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
