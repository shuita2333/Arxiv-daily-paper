# 🧠 大模型相关研究 | 2026年10月16日

> 本类共 **313** 篇论文：已确认 **304** 篇，待复核 **9** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-313](./part-07.md)

---

### 151. [HACHIMI-II: From Role-Play to Learner Behavior Modeling for Faithful Student Simulation](https://arxiv.org/abs/2610.19654)

**<font color=#1a73e8>作者：</font>** Yilin Jiang, Fei Tan, Xuanyu Yin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Simulated students let researchers test tutoring systems and teaching strategies before real learners are available, but only if the simulation reproduces where a particular learner succeeds and fails. The common approach asks a large language model to role-play a student, but a role does not model what this learner knows or will do next, so the model's own competence fills the gap. Simulated students perform at a level set by the model, differ little from one another, and seldom make the real learners' errors. We model the learner's behavior and recast student simulation as third-person prediction of the learner's next action. HACHIMI-II builds a student model from the learner's history, infers the learner's state for the current item or tutor turn, and compiles it into a behavior harness that constrains the next action. On three item-response datasets, the Wasserstein-1 distance between simulated and real student ability is 2.4--8.4$\times$ smaller than that of the strongest baseline. On two dialogue datasets, HACHIMI-II reproduces real student errors with the same knowledge type, locus, and mechanism 1.8--5.1$\times$ more often than the strongest baseline, and ablations trace the gains mainly to the explicit learner state. Predicting the learner makes capable models usable as simulated students.

---


### 152. [Measuring and Reducing Unusable Replies of LLM Agents](https://arxiv.org/abs/2610.19659)

**<font color=#1a73e8>作者：</font>** Yilin Jiang, Fei Tan, Xuanyu Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> People delegate multi-step work to LLM agents and read only the reply that the agent hands back. Current evaluation scores task completion and the faithfulness of reports, and it leaves open whether the requester can understand and use the reply. We call this property reply usability and measure it with a reader model that takes the requester's position and tests whether the reply can be interpreted from what the requester has seen, is in the requester's language and answers the request. Its agreement with the majority of five annotators lies within the range of the individual annotators. Across eight models from seven families, 54% of 480 replies fail, and the best model still fails on 30%. Failed replies mostly point to material the requester has not seen or use labels that the agent coined during its work. Stating explicit requirements for the reply reduces the failure rate from 0.52 to 0.43 together with errors and omissions, and a secondary model that rewrites the reply reduces it to 0.36, which human annotators confirm in a blind comparison. Reply usability can thus be scored alongside task success and improved with one appended message or one call to a secondary model.

---


### 153. [Learning When to Trust Medical Knowledge: Regression-Safe Routing for Clinical Reasoning](https://arxiv.org/abs/2610.19663)

**<font color=#1a73e8>作者：</font>** Hui Zhang, Yujia Zeng, Yuhao Xin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical reasoning LLMs need external medical knowledge, but retrieved evidence and reasoning chains can be outdated, poisoned, or hallucinated. Harmful knowledge can cause regression: changing a correct answer into an incorrect one. We construct a medical knowledge-poisoning benchmark covering retrieved evidence and reasoning chains, with seven attack families filtered by a three-judge "subtle-but-wrong" vote and paired clean exams that separate poisoning effects from question difficulty. No fixed knowledge-use strategy is robust across these settings: strong RAG methods trade robustness to poisoned evidence against accuracy when evidence is useful. We formulate knowledge use as per-instance routing and introduce Med-TrustRouter, a lightweight controller that keeps the solver frozen. From leakage-free runtime signals, it estimates each action's expected correctness gain and uncertainty, preserving the base answer unless another action is confidently better. Across seven medical reasoning settings, Med-TrustRouter achieves 78.9 macro and 69.2 worst-case accuracy, matching the strongest competitor on macro accuracy while substantially improving the worst-case floor. Its gains transfer across solvers and evidence judges, unlike a hand-coded router using the same signals. Similar performance across linear, tree, and neural action-value heads suggests that the benefit comes from routing rather than estimator complexity. These results support learning when to trust external knowledge for robust clinical reasoning.

---


### 154. [MCAIR: Monitoring and Correcting Agent Unfaithfulness via Internal Representations](https://arxiv.org/abs/2610.19679)

**<font color=#1a73e8>作者：</font>** Yan Xu, Dandan Song, Luan Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM)-based agents have demonstrated remarkable capabilities in completing complex tasks through multi-step reasoning and tool interactions. However, recent studies have revealed that LLM-based agents can exhibit unfaithful behaviors, where their final reports fail to faithfully reflect their actual execution trajectories. Specifically, when agents fail to accomplish tasks through the intended sources or procedures, they may resort to alternative sources or strategies while failing to disclose such deviations, leading users to incorrectly believe that the tasks have been completed according to the original requirements. We refer to this specific form of agent unfaithfulness as Agent Completion Unfaithfulness. Detecting and mitigating agent completion unfaithfulness is critical yet remains largely unexplored. In this work, we propose MCAIR, a runtime monitoring and correction framework that leverages internal representations of LLM-based agents. MCAIR uses multi-step internal representations as inputs to train a risk-aware probe, enabling online detection of potential completion unfaithfulness during execution. Furthermore, MCAIR introduces a risk-guided correction loop that prompts agents to review their execution history and mitigate potential inconsistencies between their execution trajectories and final reports. Additionally, we construct ACUD, a dataset for Agent Completion Unfaithfulness detection that provides step-level execution traces, step-level internal representations, and consistency annotations for training and evaluating runtime detection probes. Experiments demonstrate that MCAIR outperforms LLM-as-a-judge baselines, generalizes across prompts and tasks, and effectively reduces agent completion unfaithfulness.

---


### 155. [Beyond Distribution Matching: Selective Margin Preservation for Supervised Fine-Tuning](https://arxiv.org/abs/2610.19685)

**<font color=#1a73e8>作者：</font>** Yuxuan Wang, Guangxiang Zhao, Xinyu Tan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) changes logit margins among non-target tokens at teacher-forced prefixes. Matching a local reference distribution keeps those probabilities and also penalizes margin expansions. We ask whether a soft auxiliary can preserve selected local non-target margin relations without freezing that distribution. We introduce \textbf{Selective Rank-Preserving SFT (SRP-SFT)}, a soft margin target: a hinge on reference-scaled lower bounds for pairs from the reference's top-$K$ non-target tokens, applied at fixed teacher-forced prefixes. The hinge stops once the requested bound is met. We derive the KL cost of violating a margin, characterize the feasible region and its conditional utility, and give a finite-step condition for reducing aggregate violations. In one-epoch experiments on Qwen3-4B-Base and UltraFeedback, this target raises MATH-500 and code-generation scores over CE and LP-SFT at all three training seeds. At seed 1234, MATH-500 pass@1 rises from 49.56\% to 54.56\% and the four-metric code mean rises from 65.91\% to 69.50\% relative to LP-SFT. Ranking controls, held-out cache diagnostics, sensitivity sweeps, and six additional backbones show where these score changes appear.

---


### 156. [Interlock: From Local Correctness to Task Completion in Long-Horizon Agents](https://arxiv.org/abs/2610.19686)

**<font color=#1a73e8>作者：</font>** Linji Hao, Yanji He, Zihan Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model agents increasingly undertake long-horizon tasks in complex environments characterized by fragmented evidence, partially completed states, and dependencies across resources and artifacts. Existing agents may satisfy individual requirements while failing to maintain these relationships, producing locally correct but incomplete outcomes. These failures arise because task completion depends on relationships among environmental evidence, consequential decisions, and required effects. To address this completion gap, we propose Interlock, a framework for task synthesis that represents each task as a typed completion graph. Grounding edges connect public evidence to decisions, coupling hyperedges impose joint constraints across components, and realization edges connect decisions to all required downstream effects. Interlock compiles this graph into a resettable workspace, a public request, and an evaluation rubric. A source-coverage review checks whether the original requirements survive generation, while a public-input review checks whether the rubric is supported by the materials available to the solver. An agent-as-judge inspects execution artifacts and runs verification scripts, retaining trajectories judged to satisfy all mandatory requirements. To evaluate training utility, we fine-tune two Qwen3.6 backbones on their own accepted trajectories. Across the two backbones, training improves AutomationBench task pass rates by 4.00-4.50 percentage points, JobBench weighted scores by 3.20-6.64 points, and Harvey LAB criterion pass rates by 3.89-4.16 percentage points. These results demonstrate the training utility of the synthesized experience across external task environments.

---


### 157. [Function-Space Temporal Self-Distillation for Policy Optimization](https://arxiv.org/abs/2610.19687)

**<font color=#1a73e8>作者：</font>** Aryan Das, Arnab Bhattacharya, Vinay Kumar Verma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) improves reasoning in language models, but scalar outcomes provide coarse supervision over response trajectories. Self-distillation offers denser token-level guidance by comparing an unassisted policy with a feedback-informed self-teacher, yet the teacher evolves with the student, creating unstable targets and motivating additional regularization. We introduce Function-Space Policy Optimization (FSPO), a single-policy framework that combines current privileged adaptation with function-space temporal consolidation. FSPO stores sparse historical next-token distributions as fixed temporal targets, providing temporal separation without maintaining a persistent teacher model. It further introduces privileged disagreement correction to explicitly suppress locally overvalued actions, reliability-adaptive grounding that strengthens reference supervision when self-generated evidence repeatedly fails, and quality and coverage-aware temporal memory that retains verified behaviors and improves privileged demonstrations. Across reasoning and tool-use benchmarks, FSPO achieves the highest average accuracy under a 5-hour training budget, improving over the strongest baseline by approximately 4% points on average while reducing peak memory from about 70 GB to 56 GB on Olmo3-7B-Instruct.

---


### 158. [ReFormBench: Benchmarking the Stability of Response-Conditioned Format Correction in Large Language Models](https://arxiv.org/abs/2610.19693)

**<font color=#1a73e8>作者：</font>** Tianxiang Gao, Yahan Li, Chenlu Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable use of large language models requires responses to satisfy formatting requirements across changing instructions. Standard compliance scores do not distinguish preserving a model's observed format from correcting it, or reveal whether that correction holds across variants. We introduce ReFormBench, a benchmark that uses each model's unconstrained response to the same question as its formatting baseline. It links targets by feature and require/forbid mode, evaluating their instantiated requirements across variants. ReFormBench comprises 5,000 difficulty-screened three-constraint test instances derived from 910 source questions and covering 66 formatting features. TCPR measures complete instruction compliance, while EMCR measures individual and joint correction of targets opposed to the annotated baseline state. Across ten models, EMCR ranges from 34.04% to 64.72%, and the highest three-target correction estimate is 50.02%. Compliance and correction scores yield different model rankings and task-level profiles. A prompting experiment on Qwen3.5-9B improves both metrics, and the catalog covers over 95% of extracted instances on four additional models. ReFormBench makes response-conditioned correction across instruction variants a measurable dimension of format following. The code and data are available at this https URL.

---


### 159. [C3: Rethinking Process Supervision via Confidence-Guided Credit Correction in Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2610.19695)

**<font color=#1a73e8>作者：</font>** Ai Jian, Haoran Pan, Eryu Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly trained as multi-turn agents that interact with external tools. However, outcome-only reinforcement learning can produce a form of misguided reinforcement: even on successful trajectories, undesirable local behaviors may receive positive token-level advantages and be favored by the policy update. To address this issue, we propose Confidence-Guided Credit Correction (C$^3$), a plug-in method for local credit correction. C$^3$ identifies spans corresponding to undesirable behaviors and selectively corrects positive credit after advantage estimation, with the correction strength adaptively controlled by the behavior policy's confidence in the corresponding behavior, while leaving the task reward and original credit estimation unchanged. Across multiple multi-turn benchmarks, C$^3$ improves performance under both {critic-based and critic-free reinforcement learning methods}. Injecting the same behavioral signals as turn-level or outcome rewards does not consistently improve performance. Our results show that local credit correction provides an effective form of process supervision for outcome-driven RL.

---


### 160. [Share the Symbol, Not the Vector: Training-Free Fact Communication Across Language Models](https://arxiv.org/abs/2610.19696)

**<font color=#1a73e8>作者：</font>** Xin Li, Mengbing Liu, Hao Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems allow language models to solve tasks collaboratively by sharing complementary information. These systems typically communicate through text, while recent approaches also explore exchanging internal model states. However, sharing these states across architectures often requires learned translators or assumptions about model compatibility. We introduce SYNC (Symbol-Indexed Neural Communication), a word-indexed interface that connects heterogeneous models without fine-tuning or a learned translator. From descriptions only it can see, the sender selects words from a shared list and sends their indices for each object, without seeing the questions. The receiver writes the described facts into its hidden states using its own word directions, vectors fitted once from its activations. We test selective use by swapping one attribute between two objects and requiring correct answers about both changed and unchanged attributes before and after the swap, four answers in total. We choose an early write layer on four development receivers and then fix it. With three different senders and nine newer receivers from five families, four-answer success on new scenes reaches 72.0-98.3%, up to 96 percentage points above middle-layer writing, and the two largest receivers match plain text. A task-free probe predicted in advance which depths each new receiver can use (45 of 45 cases). Without retuning, messages listing every fact keep 89.6-100% success under new layouts, and sender messages reach 23.9-64.0% on a landmark task with multi-token symbols, below text but from 0% without a message. These results show that shared word indices and receiver-local directions can support selective fact use across model families without additional training.

---


### 161. [RuleTrek: Benchmarking Agentic Rule Reasoning in Complex Scenarios](https://arxiv.org/abs/2610.19698)

**<font color=#1a73e8>作者：</font>** Chenhao Yuan, Bohan Yu, Yinhao Xu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly tackle complex real-world tasks in specialized domains. However, identifying and correctly applying domain-specific rules remains challenging when scenario information is distributed across multiple files. Existing rule-reasoning benchmarks typically represent scenarios using only a few factual statements, simplifying the identification and application of relevant rules. To address this gap, this paper introduces \textbf{RuleTrek}, a multi-domain benchmark for agentic rule reasoning in complex scenarios. Its rule-grounded construction pipeline extracts structured rule graphs, generates and incrementally composes rule-specific sub-scenarios while ensuring consistency and solvability. To systematically evaluate agentic rule reasoning in complex scenarios, RuleTrek assesses three capabilities in interactive workspaces: Rule Identification (RI), Rule Deduction (RD), and End-to-End Rule Reasoning (E2E). Experiments on 11 frontier LLMs show that the highest RI and RD scores are only 62.47\% and 60.43\%, respectively, while E2E scores range from 26.97\% to 55.29\%. These results demonstrate that current LLM agents face substantial challenges in rule reasoning over complex scenarios. We make our code and dataset publicly available at \href{this https URL}{RuleTrek}.

---


### 162. [BANGLAPLAN: A Benchmark for Constraint-Based Planning and Decision-Making in Bangla](https://arxiv.org/abs/2610.19704)

**<font color=#1a73e8>作者：</font>** Md Rayhanul Masud, S M Maksudul Alam, Mohammad Jaminur Islam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly help users arrange appointments, plan journeys, and allocate limited resources. These tasks require models to satisfy constraints on time, cost, capacity, and order, or determine that no feasible solution exists. Bangla is the world's seventh most widely spoken language, and existing benchmarks cover many language and reasoning tasks. However, benchmarks for evaluating planning and decision-making in Bangla under explicit constraints remain lacking. We introduce BANGLAPLAN, a benchmark of 1,000 problems across ten task families grounded in everyday life and institutions in Bangladesh. It includes feasible and infeasible problems in four language registers: everyday, formal, colloquial, and Bangla--English mixed. Answers cover eight structured types, including schedules, routes, allocations, and ordered steps, in a common JSON format. We construct the benchmark through language-model-assisted drafting and independent human validation. We evaluate 11 open-weight and proprietary model configurations using exact match, separately reporting feasible-case accuracy, infeasibility detection, and format errors. We find a large performance gap: GPT-6.1 Sol achieves 98.7% accuracy and Qwen3.5-27B with thinking reaches 80.3%, while direct-answer configurations score at most 30.9%. Seven of eleven configurations perform below the always-``infeasible'' baseline. Our findings also suggest that harder problems primarily reduce plan-construction accuracy, while infeasibility detection remains more robust. BANGLAPLAN provides a reproducible basis for evaluating planning and decision-making in Bangla. BANGLAPLAN is available at: this https URL.

---


### 163. [RouteWeaver: Weaving Mode Selection and Execution into Unified LLM Routing](https://arxiv.org/abs/2610.19705)

**<font color=#1a73e8>作者：</font>** Xiaohan Wang, Haozhen Zhang, Qingyuan Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM routing dynamically selects and coordinates heterogeneous language models across diverse tasks. However, existing approaches are largely built around a predefined execution paradigm, such as single-round, multi-round, or agentic routing, which fixes how model calls are organized and limits adaptation to different query needs. We propose RouteWeaver, a unified routing framework that integrates these routing modes within a single LLM policy, jointly learning which mode to use and how to select models within that mode. To jointly optimize mode selection and within-mode execution, we develop COMET-GRPO (COordinated Mode-Execution Training), which decouples the trajectory-level advantage into separate signals for mode selection and within-mode execution, enabling more targeted credit assignment to each decision level. We further introduce progressive exploration, which gradually shifts training from externally assigned modes to autonomous selection, so that the router first learns how to execute each mode before deciding when to use it. We evaluate RouteWeaver across mathematics, coding, knowledge, logical reasoning, and factual recall. RouteWeaver achieves an average accuracy of 61.4%, an 11.03% relative improvement over the strongest baseline, and outperforms all compared baselines in each of the five domains. Ablations show that both COMET-GRPO and progressive exploration are important for adaptive routing; without progressive exploration, the routing policy collapses entirely to single-round execution.

---


### 164. [New Model, Old Habits: Behavior Transfer under Model Swapping in Multi-Session LLM Agents](https://arxiv.org/abs/2610.19712)

**<font color=#1a73e8>作者：</font>** Youngbin Choi, Sehyun Hwang, Suhyeon Jun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-session agents can switch between LLMs to balance performance and inference cost. Such switches require transferring a history for continuity, yet their effects on the recipient remain underexplored. Through controlled experiments with multi-session tasks, we uncover behavior transfer: recipients tend to adopt reasoning and action patterns from the models that generated their histories. This effect is most evident with raw-history transfer but is substantially reduced by summarization. Based on these findings, we propose Direction- and Authorship-aware Summarization of History (DASH) that preserves stronger-model behavior while minimizing weak-to-strong transfer via summarization. Experiments with repeated swaps show that DASH outperforms raw-history transfer and naive summarization baselines. These results suggest that effective multi-model orchestration requires considering not only which model to use, but also which behavioral patterns to carry forward.

---


### 165. [Articulation Upper Bounds for Language Models](https://arxiv.org/abs/2610.19721)

**<font color=#1a73e8>作者：</font>** Alexander Spangher, Daniel E. Ho, Diyi Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language captures only a subset of the perceptions, intuitions and intents that form meaning between speakers. What, then, are the limits of language? We take steps towards measuring this in LLMs as follows: for a set of concepts, we measure how well each concept can be transmitted between two LLMs as their capabilities scale. This requires novel measurement tools: (1) optimal messages: we introduce a prompt optimization algorithm that beats existing algorithms by up to 14% on benchmarks and accurately estimates prompt upper bounds. (2) A transmission measure: the sender is asked to label text; the receiver then tries to recover the sender's prompt, and recovery is measured; we find this correlates strongly with human label error. With these measures, we use observational scaling laws to study how transmissibility of a concept, conveyed with optimal messages, increases as transmitter and receiver capacity grows: does it asymptote below or above a threshold? Measuring 1.2k concepts in eight domains, we find concepts that (a) can be fully articulated; these concepts usually depend on local patterns, e.g. "joke ends with surprise"; (b) might be articulated by future, stronger models; these rely on whole-text structural patterns, e.g. "story's worldbuilding coherence"; (c) concepts that face articulability limits; these concepts' meaning, we find, is tied to identity and social-group awareness, e.g. "comic voice". Interesting, these same concepts are not all challenging for humans: humans have moderate-to-high levels of agreement in 76% of concepts that LLMs struggle with; articulation limits, we find, are executor relative. Finally, we characterize the nature of improvement in each case: while recoverable concepts can be articulated through definitions and explanations, irrecoverable concepts cannot be transmitted, even with examples, and might require novel learning mechanisms.

---


### 166. [Recognizing Dialogue Ambiguity via Candidate Set Visual Grounding](https://arxiv.org/abs/2610.19723)

**<font color=#1a73e8>作者：</font>** Shun Inadumi, Lee Sangmyeong, Koichiro Yoshino  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Interpreting an ambiguous utterance in real-world interactions often requires context beyond a single utterance. When the utterance refers to objects in a visual scene, it is necessary to maintain and update the set of plausible referents as context accumulates, without assuming that the available information identifies a unique object. However, prior work on interactive visual grounding, which localizes objects referred to by linguistic expressions, has focused on identifying a unique object once sufficient dialogue context becomes available. To address this gap, we propose Candidate Set Visual Grounding (CSVG), a task for estimating the set of objects consistent with the given dialogue context. We further introduce CandVG, a benchmark that evaluates how the candidate set changes across dialogue turns. Our evaluation of vision-language models shows that stronger visual grounding capability does not necessarily yield better CSVG performance. In particular, models have difficulty predicting the complete candidate set, owing to challenges in candidate generation and premature commitment to a small set of candidates in early turns. Nevertheless, we find that this limitation can be partially mitigated in the evaluated large-scale models using instructions designed for CSVG.

---


### 167. [TIMERSI: Towards Self-Improved Agentic Deployment for Time-Series Foundation Models](https://arxiv.org/abs/2610.19725)

**<font color=#1a73e8>作者：</font>** Haoxin Liu, Deqing Fu, Lucheng Fu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series foundation models provide strong zero-shot forecast, but deployment for real- world applications still requires task-specific designs for model inputs and outputs. Direct inference can leave domain knowledge and re- curring forecast errors unaddressed, while tai- lored pipelines require substantial human ex- pertise and effort. We introduce TIMERSI, a self-improving agentic deployment system around frozen forecasting models. A cod- ing agent translates task descriptions into ex- ecutable pipeline changes. It tests each re- vision on historical forecasting windows and uses observed errors to guide subsequent re- visions. During deployment, an adaptive se- lector chooses among the resulting pipelines using completed forecasts under similar con- ditions. Across 198 tasks on TIME and FEV- bench, TIMERSI outperforms all submissions on six point and probabilistic forecasting met- rics. Controlled comparisons support the value of feedback-guided revision over non-iterative pipeline search. Further experiments verify the generalization with different coding agents and forecasting models.

---


### 168. [Mitigating Video Hallucinations via Attention-Guided Representation Perturbation](https://arxiv.org/abs/2610.19728)

**<font color=#1a73e8>作者：</font>** Zhixin Cai, Ruoqi Yuan, Xinchen Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video large language models (Video LLMs) often generate responses unsupported by the input video. Contrastive decoding (CD) can mitigate these hallucinations, but its effectiveness depends on how the negative branch weakens visual evidence. Existing methods rely on predefined perturbations or masking guided by question reconstruction, offering limited control over the model's visual reliance during answer generation. We introduce Attention-guided Representation Perturbation for Contrastive Decoding (ARP-CD), a training-free framework for constructing contrastive negatives directly in representation space. ARP-CD uses the attention mass assigned to visual tokens at the answer-prediction position to guide bounded gradient updates of the language model's input visual hidden states. These updates reduce visual attention and produce a negative input, whose predictions are contrasted with those of the original branch throughout generation. Experiments across four Video LLMs and four benchmarks show that ARP-CD outperforms representative training-free baselines in most model--benchmark settings, reducing hallucinations while improving general video understanding. Further analyses show that attention-guided perturbation directions improve negative quality and that the resulting negatives provide effective contrastive references for correcting the original predictions.

---


### 169. [ProtModernBERT: Compute-Efficient Protein Language Modeling](https://arxiv.org/abs/2610.19738)

**<font color=#1a73e8>作者：</font>** Alberto Martínez, Natalia Flechas Manrique, Llorenç Espinosa-Portalés 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large protein language models provide a powerful framework for learning sequence-function relationships and guiding experimental design. However, architectural improvements are underexplored, especially in low-compute regimes of relevance for resource-constrained research laboratories. We show that the training cost for encoder-only transformer architectures can be reduced by leveraging modern architectural refinements, offering an encouraging performance / compute-efficiency trade-off. We introduce ProtModernBERT, a modernized BERT-style model pre-trained on amino acid sequences, and compare it with ProtBert, Amplify, and ESM2 across a set of supervised structural tasks -encompassing secondary structure prediction, disorder prediction, and subcellular localization- and ProteinGym's zero-shot functional benchmark. We find that ProtModernBERT matches or closely tracks the performance of Amplify-120M and ProtBert with up to 80-90\% reduction in pre-training FLOPs, and narrows the gap to ESM2 when controlling for pre-training. Our analysis using a cluster-based validation protocol for hyperparameter selection and randomly initialized models disentangles the contributions of architecture and data, showing that modern components provide stronger inductive biases that are more consequential than parameter count in low-compute regimes.

---


### 170. [Does the Linguistic Register of Thinking Matter? Wenyan as a Compact Reasoning Register for Chinese LLMs](https://arxiv.org/abs/2610.19741)

**<font color=#1a73e8>作者：</font>** Minghan Li, Guodong Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Visible reasoning traces of Chinese reasoning-oriented LLMs are typically written in modern vernacular Chinese, which may be verbose under limited decoding budgets. We ask whether the linguistic register of reasoning can be used to improve efficiency. We propose Wenyan Thinking, which emits intermediate reasoning in Classical Chinese (wenyanwen) while retaining a short direct-answer output. Starting from modern-Chinese reasoning traces, we rewrite only the reasoning field into wenyan and fine-tune Qwen3-4B-Thinking-2507 on the rewritten supervision. To distinguish register shift from generic compression, we construct a compact modern-Chinese control using the same source data, teacher family, base model, and SFT recipe. Across budget-sensitive evaluations on MMLU-ProX-Lite-ZH, CEVAL, and AGIEval-CN, Wenyan Thinking substantially reduces reasoning length and missing-answer rates under constrained decoding. Compact rewriting explains much of the efficiency gain, while wenyan consistently outperforms the compact modern-Chinese control on the primary benchmark and remains competitive across the additional benchmarks. These results identify linguistic register as a practical design axis for efficient visible reasoning in Chinese LLMs.

---


### 171. [Qwen-MT-Lumen at WMT2026: Instruction-Specialized Translation via Quality-Aware Training and On-Policy Distillation](https://arxiv.org/abs/2610.19758)

**<font color=#1a73e8>作者：</font>** Hao Wang, Yangyang Liu, Xiaohu Zhao 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Lumen, The open-source model is available at, our submission to the WMT 2026 General Machine Translation Shared Task. We focus on instruction-specialized translation, where systems must produce accurate translations while satisfying fine-grained requirements on style, terminology, and structured output. Lumen follows a four-stage pipeline. First, continued pre-training and supervised fine-tuning jointly strengthen multilingual translation competence and the ability to follow translation-specific instructions, such as terminology, style, and format constraints. Second, we extend the originally offline M^{2}PO preference-optimization framework into an online preference-optimization stage: the current policy samples candidate translations, an LLM judge assigns continuous direct-assessment scores, and the resulting multi-pair preferences are used to update the model. Third, on-policy distillation transfers stronger translation-instruction-following behavior from a larger teacher model to the Qwen3-14B student, improving translation-instruction adherence while retaining a 14B primary translation backbone. Finally, structure-aware inference and postprocessing preserve required formats, while selective repair addresses clear structural or decoding failures before submission. We participate in 23 translation directions. Under an absolute 1--5 LLM-judge rubric that evaluates translation-instruction following and translation quality separately, Lumen reaches an overall mean score of 4.60. Despite using a 14B translation backbone, it achieves performance comparable to leading proprietary systems in both translation quality and translation-instruction following.

---


### 172. [CAST: History-Adaptive Spectral Clipping for LLM Pretraining](https://arxiv.org/abs/2610.19761)

**<font color=#1a73e8>作者：</font>** Jiacheng Li, Jianchao Tan, Kefeng Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Soft spectral clipping (SSC) reduces gradient singular values, but its effect depends on the gradient scale and clipping threshold. We introduce CAST (Clipping with Adaptive Scales and Thresholds), a history-adaptive extension of SSC. AdamW's previous second moment sets row and column scales. An exponential moving average of the clipped output's estimated spectral norm sets each matrix's threshold. CAST restores the original coordinates before the AdamW update. We train a mixture-of-experts (MoE) model with 19.08B total parameters for 83.89B tokens. CAST achieves lower training and mean validation losses than nine gradient-processing baselines, with the fewest relative gradient spikes. It reaches the best baseline's final smoothed training loss in 7.2\% fewer steps.

---


### 173. [PRISMATIC : Prescription Risk Inspection System for Multi-Agent Treatment Interaction in Clinical Decision-Making](https://arxiv.org/abs/2610.19762)

**<font color=#1a73e8>作者：</font>** Ziyang Ling, Shuyu Lu, Ziyi Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical prescribing errors for multimorbid patients, who require complex drug regimens, are a major patient safety concern. These errors often stem from fragmented decision-making across medical specialties, a critical coordination failure that leads to adverse drug events and rehospitalizations. To address this coordination challenge, we introduce PRISMATIC, a multi-agent architecture where specialized agents, each representing a workflow role, collaboratively generate and refine treatment plans. Operating on a blackboard architecture, the system first structures patient information from clinical notes, then iteratively develops safe, rational, and interpretable drug regimens. The agents' collaboration is governed by two novel adaptive coordination mechanisms: (1) Dynamic Self-Updating Weight Adjustment (DSWA), a long-term mechanism that adjusts the influence weights of agents based on historical case outcomes, enabling the system to adapt and trust more reliable specialists over time. (2) Discrepancy Feedback Precise Calibration (DFPC), a short-term mechanism where agents provide iterative feedback to resolve disagreements and eliminate prescription conflicts for the current patient. Experiments on patient records from the MIMIC-IV database show that PRISMATIC significantly reduces drug conflicts, improves prescription coverage, and enhances treatment consistency compared to strong LLM baselines. Our work demonstrates that structuring clinical co-treatment as a multi-agent coordination problem offers a promising path toward safer and more coherent multidisease management.

---


### 174. [Likelihood Is Not Authorship: Can We Reliably Measure Human Contribution in AI-Assisted Writing?](https://arxiv.org/abs/2610.19767)

**<font color=#1a73e8>作者：</font>** Hasan Amin, Zhuoran Lu, Ming Yin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI-text detection generally asks whether a machine wrote a text. As AI becomes an increasingly integral and accepted part of writing, the more relevant question is no longer whether AI was used, but how much of the text reflects human contribution. A prominent line of work estimates this by measuring how predictive a person's prompt is of the final text. We show that this measure can be easily manipulated. We introduce SPECIFICITY PADDING that simply asks the model to copy a few random IDs from the prompt, and that alone makes a title-only request look more human than one that supplies the article's key ideas. A context-swap audit then holds each document fixed, and only shows or hides the IDs to the evaluator. The score of the unchanged text swings by a third to half of its scale, and it rises for every document we test, on news and scientific abstracts, across varied LLMs from 3.8B to 753B parameters. The same articles can average 85\% human or 15\% human depending only on which prompt is on record, and even with no prompt at all, the output-only variant rewards the random strings themselves. An exact identity, the credit ledger, explains why. The score is a surprisal-weighted average over the text, so rare strings that the context makes copyable collect the credit, whatever they mean. A two-point bound marks a deeper limit. If the prompt could have been machine-written, every transcript-only method must, in the worst case, miss by half the contribution at stake. Likelihood-based scores alone cannot reliably establish human contribution without evidence of what the person added and how the text was produced.

---


### 175. [Q-MAGIC: Quad-only Mesh Autoregressive Generation via Singularity-Aware Circular Relative Offset Tokenization](https://arxiv.org/abs/2610.19777)

**<font color=#1a73e8>作者：</font>** Yuming Zhao, Zezeng Li, Weimin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive models have proven effective for triangular mesh generation by transforming it into predicting the next face, converting the non-differentiable connectivity prediction into a sequence of token predictions. However, generating quad-only meshes remains challenging because quad faces impose stricter topological constraints than triangles. The model must not only serialize quad faces into a valid token sequence, but also support unambiguous connectivity reconstruction during de-serialization. To address this, we propose Q-MAGIC, a novel autoregressive model for quad mesh generation. We first introduce a tailored serialization scheme for quad meshes, which requires at least two new vertices for the next face and is less flexible than triangles due to strict wiring constraints. To meet these requirements and reduce serialization length, we propose a singularity-aware serialization that prioritizes wiring from singular points, leading to more coherent traversals. Additionally, we propose a circular relative offset tokenization that encodes geometry mainly via local relative offsets. Built upon this representation, an autoregressive Transformer learns the underlying distribution of quad meshes via next-token prediction, enabling effective quad mesh generation. Extensive experiments demonstrate that Q-MAGIC produces more compact sequences while consistently improving geometric fidelity and mesh quality compared to state-of-the-art methods.

---


### 176. [More Methods, Better Agents? A Reality Check on Self-Distillation in Agentic Reinforcement Learning](https://arxiv.org/abs/2610.19789)

**<font color=#1a73e8>作者：</font>** Linhao Zhong, Bozhen Fang, Xuehao Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-distillation in agentic reinforcement learning has produced a growing number of methods. However, existing evaluations often reuse published baseline scores under differing experimental conditions, provide few direct comparisons among contemporaneous methods, and give limited attention to training stability and computational cost. These limitations obscure the source of reported gains and the practical strengths and weaknesses of competing methods. Costly agent training further motivates a common basis for comparison. To address these gaps, we compare ten representative methods against GRPO on ALFWorld, ScienceWorld, Search-QA, and WebShop across three model sizes. Our study comprises 132 training runs totaling 12,124.4 recorded H800 GPU-hours, with repeated evaluations over eight rollout seeds for the pretrained backbones and all eleven trained methods. Beyond final task performance, we examine training progress, stability, and measured computational cost. Our evaluation yields three key findings. First, gains over GRPO remain limited in scope, with no method consistently outperforming it across settings. Second, strong final performance can mask unstable training. Third, additional training cost does not consistently translate into better performance. We establish this benchmark to support fair, comprehensive comparison and guide future research toward reliable and cost-effective improvements in agent training. Project page: this https URL

---


### 177. [StateCraft: Augmenting Video World Models with Abstract-State Reasoning](https://arxiv.org/abs/2610.19795)

**<font color=#1a73e8>作者：</font>** Lorenzo Venturoli, Nedko Savov, Xi Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models aim to simulate complex environments with realistic appearance and dynamics. Maintaining consistency over long interactions requires tracking past actions and understanding how those actions affect the environment. Video world models can only generate partial observations of the entire world at a time. Remembering past observations alone may not be sufficient in every scenario, as they may no longer reflect the world after a sequence of actions. We introduce a paradigm that decouples a persistent, updatable abstract state from the visual state. The abstract state keeps track of the entities' changes as the world evolves, and is used to condition the visual state, which represents the current view. We propose StateCraft, a novel architecture that pairs a language model with a video diffusion model to evolve the dynamic world. We evaluate our approach on generative interfaces, which pose a substantial challenge because a single action may change parts of the state that are not currently visible. To support training and evaluation, we develop a data collection pipeline that produces informative, densely annotated trajectories at scale without human or agent supervision, together with a benchmark measuring generation quality, memory, and controllability. On this benchmark, our approach improves surpasses the state-of-the-art baselines. We demonstrate that StateCraft maintains high self-consistency and strong generation quality over long trajectories. Because the abstract state is explicit, it can be edited directly, and generation follows edits to states never observed in the data. Finally, a proof-of-concept 3D experiment, in which actions change the illumination of an unobserved room, shows that the paradigm can also be applied to spatial environments. Project page: this https URL.

---


### 178. [Learning Perception to Action Rules through Reinforcement Learning for Theory-of-Mind Reasoning](https://arxiv.org/abs/2610.19796)

**<font color=#1a73e8>作者：</font>** Soyoung Oh, Nursulu Sagimbayeva, Nicholas Jennings 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In Theory-of-Mind (ToM) reasoning, large language models may correctly infer the agent's mental state but fail to use that inference when predicting or judging the agent's subsequent actions. In this work, we investigate whether explicitly connecting perception, belief, and action with rules improves ToM reasoning. We generate concise \textit{if--then} rules that express relations between perception to action and use Group Relative Policy Optimization (GRPO) to train Qwen2.5 and Llama3 models across four ToM benchmarks. GRPO with rule generation outperforms prompting, supervised fine-tuning, and think reasoning. Moreover, rules generated by larger models ($\geq$3B) provide transferable knowledge that improves downstream performance of GPT-4o-mini. These findings suggest that explicit rules help models bridge the reasoning gap in ToM and support knowledge transfer across models.

---


### 179. [Evolve Together, Fall into Place: How Social Scaffolding Shapes Self-Evolving Multi-Agent Systems](https://arxiv.org/abs/2610.19799)

**<font color=#1a73e8>作者：</font>** Seojin Hwang, Youngmin Choi, Hwanhee Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work lets LLM agents evolve their own harness, up to the team itself. Yet in human groups, the same abilities achieve different outcomes under different social conditions. Borrowing the notion of scaffolding from developmental psychology, we investigate whether the social scaffolding of a self-evolving multi-agent system (MAS), namely its team composition and structure of interdependence (e.g., collaboration, conformity, or competition), shapes how the team evolves. We present AGORA (Agents Growing through Organization and Relational Arrangements), a framework that varies the two axes independently across three evolution mechanisms. Across web search, codebase understanding, and document QA, we find that (1) evolution alone rarely helps, while the right scaffolding surpasses a strong agent evolved alone by up to 25 points; (2) it does so by moving authority to the most capable member while the others step back; and (3) this member, having grown within the team, outperforms the same model alone. Designing a self-evolving MAS thus requires designing its social scaffolding, which shapes not only how its agents learn, but who gets to lead.

---


### 180. [Delta Tokenizer: Reference-Identical Tokenization of Session Deltas and Segment-Parallelism for Long Prompts on Multicore CPUs](https://arxiv.org/abs/2610.19801)

**<font color=#1a73e8>作者：</font>** Zhenyu Zhang, Zhichao Cao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An agent that drives an LLM sends the model the same conversation again and again, and each turn adds only a little text at the end. Inference engines reuse the KV cache of the shared prefix, so only the new tokens pass through the model. However, tokenization has no such shortcut. The CPU front end of the serving engine converts every request back into token IDs from its first character, which lengthens the time to first token (TTFT) and consumes CPU on every turn.
We present Delta Tokenizer, a CPU tokenization front end that tokenizes only the delta between a request and the previous request of the same session. It retains the earlier token sequence, encodes again only the appended text and the short tail whose tokens the append could affect, and joins the two only at a position the tokenizer's splitting rules themselves cannot move, which keeps the result exact. For long requests with no state to reuse, it cuts the text where practical tokenizers already keep neighboring pieces independent, encodes the pieces on several cores at once, and concatenates the outputs into the reference encoding, exactly. A shared CPU pool schedules these chunks together with the short incremental updates, so an update runs between two chunks rather than behind an entire long job.
The incremental path shortens the tokenization of a session turn by roughly 40x relative to the Hugging Face reference tokenizer, and on 16 cores the chunk-parallel path encodes a four-million-character request 8.2x faster than a serial encode and 1.6-2.1x faster than LoPT. Inside SGLang, Delta Tokenizer reduces the median TTFT through the chat interface by 59% at 100K tokens and brings the P99 TTFT of agent sessions down 9.5x under load and 23x when long requests tie up the front end. Every output we checked matches the reference, among them 41.8 billion documents encoded by its fast encoder.

---


### 181. [Efficient contextual partial monitoring with general function approximation](https://arxiv.org/abs/2610.19804)

**<font color=#1a73e8>作者：</font>** Kapilan Balagopalan, Hao Qin, Kwang-Sung Jun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study finite stochastic partial monitoring (PM) games with side information, a paradigm of sequential learning with partial feedback. On each round $t \in [T]$, both player and environment observe a context and player chooses an action and environment simultaneously chooses an outcome. The player neither observes the outcome nor the loss; instead, they only observe a feedback symbol which is partially informative about the outcome. We utilize the Estimation-to-Decisions (E2D) meta-algorithm of Foster et al.(2021) to design this http URL, a computationally efficient framework for contextual partial monitoring, which uses an online regression oracle to efficiently estimate the outcome distributions based on historical (context, action, feedback symbol) tuples. Since the exploration rule given by the original E2D algorithm is intractable to compute, we propose two computationally efficient exploration rules that achieve optimal regret orders in $T$: in the globally observable setting, our exploration rule is based on $\epsilon$-greedy, while in the locally observable setting, our exploration rule uses inverse gap weighting (Foster & Rakhlin, 2020), which was previously only known to be effective in the bandit setting. We show that a variant of this http URL named this http URL can be combined with offline regression oracles to give an efficient algorithm with optimal regret when the contexts are drawn independently from a fixed distribution. We evaluate our algorithm on a synthetic label-efficient prediction game and an LLM routing task, in which a learner decides from prompt, uncertainty, and internal state features whether to escalate a query from a weak model to a strong one. We show that our method has superior performance to prior approaches.

---


### 182. [ReproBAIT: Can coding agents build their own biological AI tools?](https://arxiv.org/abs/2610.19810)

**<font color=#1a73e8>作者：</font>** Shiv Muthupandiyan, Tolga H. Dur, Mac Walker 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly competent at leveraging scientific knowledge and existing computational tools to execute complex workflows. At present, little information exists on their ability to reconstruct tools when given limited descriptions of such tools. We introduce an evaluation titled ReproBAIT (Reproducing Biological AI Tools), which measures the ability of coding agents to design, implement, and train biological AI tools taken from published research across a range of information access conditions. The coding agent is securely sandboxed without internet access and receives training data, a fixed time and compute budget, and limited information about the tool to replicate. We then score the reproduced biological AI tool based on its performance (tool-specific metrics) on held-out data. We evaluated a set of biological AI tools of varying complexities: ProteinMPNN, an inverse protein folding tool, RFdiffusion3, an all-atom generative diffusion tool, and a closed-source molecular design tool. We institute a methodology to check for memorisation, as the open source tools are likely to be included in models' pretraining corpus. Across a range of leading closed- and open-source coding agents, we find substantial reproduction capability for some selected tools, though limited capability for a highly complex tool. We find moderate evidence consistent with memorisation, varying across coding agents. These results suggest that tool developers need to be increasingly cautious when releasing information about the tools publicly; re-creation of the tool based on such information could undermine a tool's commercial value or invalidate dual-use managed access strategies.

---


### 183. [Model vs. User: Whose Values Prevail? Inference-Time Value Alignment in Multi-Turn Conversations](https://arxiv.org/abs/2610.19817)

**<font color=#1a73e8>作者：</font>** Enrico Liscio, Anne Arzberger, Aditya Shankar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human values shape how we expect language models to behave. Dominant alignment approaches treat values as global objectives, although the appropriate value orientation is personal and contextual. Training-free alignment can steer models toward target values at inference time, yet has been largely evaluated in single-turn settings and with a single steering direction (e.g., toward safety). We evaluate four prompt- and activation-based steering methods in multi-turn conversations, where user and assistant models push toward the same or opposing, equally desirable values. We track alignment with a linear probe across three models and two value trade-offs. When assistant and user pull in opposite directions, the side matching the assistant's baseline bias often prevails, and effects that look successful early often fade or reverse after a few turns. Steering should therefore be evaluated over full conversations and in both directions of a value trade-off.

---


### 184. [One Monitor Does Not Fit All: Formalism-Agnostic Runtime Verification for Agentic AI](https://arxiv.org/abs/2610.19818)

**<font color=#1a73e8>作者：</font>** Angelo Ferrando  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems combine model decisions, mutable state, tool calls, and delegation to external agents. Monitoring them requires observations from different execution boundaries, while prevention requires control before an operation produces its effect. We present AgenticRV, a runtime-verification architecture that separates these boundaries from the monitoring formalism. Adapters emit canonical events; each monitor receives its own projection and abstraction; and a decision policy uses normalised verdicts to select a reaction supported by the responsible adapter. We formalise when observations suffice, monitor replacement preserves decisions, and blocking prevents unsafe effects. We also distinguish rejected attempts from completed effects, avoiding the assumption that a blocked request must leave every monitor in a permanent violation state. The Python implementation supports LangGraph, MCP, and A2A. A controlled LangGraph experiment combines an external Reelay temporal monitor with a programmatic report monitor; ablations show why both are needed for the selected requirements. Differential checks and cross-adapter tests provide further integration evidence. An LLM-driven incident-response example illustrates the same enforcement path, while existing microbenchmarks isolate framework costs. The results support reuse of monitoring methods at explicit control boundaries, subject to the stated observation and deployment assumptions.

---


### 185. [ActionOPD: Distilling Decisions, Not Tokens](https://arxiv.org/abs/2610.19820)

**<font color=#1a73e8>作者：</font>** Huining Yuan, Xiangmin Yi, Zelai Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Distilling capable language-model agents into smaller models requires aligning the student's behavior with the teacher's. This raises a fundamental question: at which states and at what granularity should this alignment be performed? Offline imitation provides dense but token-specific supervision and can suffer from state-distribution mismatch. Token-level on-policy distillation (OPD) addresses this mismatch but typically requires teacher token probabilities and compatible tokenization. We argue that semantic actions provide a natural unit of supervision for agent distillation. We introduce ActionOPD, an action-level on-policy distillation method motivated by maximizing expected teacher-action likelihood at student-encountered states. At each such state, ActionOPD samples actions from both the student and a black-box teacher, rewarding student actions according to their semantic agreement with the sampled teacher actions. Through policy optimization, ActionOPD aligns the student's action-level behavior with the teacher's decisions without requiring reproduction of teacher-written reasoning or access to teacher token probabilities. Training Qwen3-4B and Qwen3-8B with two teachers on diverse, curated tool-use tasks yields average gains of 3.3-6.9 percentage points across four out-of-distribution benchmarks. ActionOPD scales favorably with student size and teacher capability, without requiring the teacher and student to share a model family or tokenizer. On $\tau^2$-bench, ActionOPD achieves competitive performance against offline distillation and token-level OPD. We further explore Self-ActionOPD with a same-model teacher and privileged context. These results establish ActionOPD as a promising approach to agent distillation.

---


### 186. [PhyMetric: Diagnosing Physical Plausibility in Text-to-Video Generation via Scene-Level QA](https://arxiv.org/abs/2610.19823)

**<font color=#1a73e8>作者：</font>** Siwei Meng, Xuerou Cai, Rui Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-video (T2V) generation models can produce visually realistic videos that nevertheless violate the physical consequences implied by the prompt and scene. Existing benchmarks largely rely on holistic plausibility scores or broad quality dimensions, leaving it unclear which physical behavior is being tested and why a model fails. We introduce PhyMetric, a scene-level diagnostic benchmark that recasts physical plausibility evaluation as verifiable, scene-grounded question answering. PhyMetric contains 1{,}115 scenes spanning 50 physical categories across six domains, paired with 8{,}920 answer-balanced binary questions over 12 evaluation dimensions. Each scene is associated with eight targeted yes/no questions and a structured physical prior specifying the governing law, expected temporal sequence, observable signatures, and common failure modes. At evaluation time, a vision-language model (VLM) judge answers each question from question-aware sampled frames conditioned on the prior, and correctness is hierarchically aggregated into scene, dimension, physical category, and model scores. Experiments on four open-source T2V models and three VLM judges show that scene-specific binary QA is a critical component of the protocol: when each targeted question is replaced by a single generic plausibility query, evaluator accuracy drops to the chance level. Structured physical priors offer a complementary signal that improves human alignment of the resulting scores, with effects that vary across VLM judges of different capacity. These findings establish PhyMetric as a benchmark that turns physical plausibility evaluation from opaque holistic scoring into interpretable, scene-level inspection. Our project page is available at: this https URL.

---


### 187. [MAPLE: A Multi-Axis Parametric Knowledge Extraction Lens for LLM Evaluation](https://arxiv.org/abs/2610.19827)

**<font color=#1a73e8>作者：</font>** Minsuh Joo, Youna Kim, Choonghyun Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLMs absorb vast knowledge from training data, yet their inherently probabilistic nature offers no guarantee that this knowledge will surface in their outputs. To bridge this gap, Knowledge Extraction Enhancement (KEE) techniques such as activation steering, decoding adjustments, and prompting modify inference, potentially reinforcing existing predictions or surfacing less accessible answers. Yet their evaluations centered on aggregate accuracy, which obscures diverse effects by collapsing recovered failures and disrupted successes into a single score. We introduce MAPLE, a unified framework for characterizing how KEE techniques affect parametric knowledge extraction. Its diagnostic metrics disentangle these effects at the surface, probability, and beyond-sampling levels by measuring answer recovery and disruption, gold-token rank shifts on unrecovered failures, and recovery of answers missed by fixed-budget sampling. We evaluate six KEE techniques spanning decoding, activation steering, and prompting across three model families: OLMo2, Qwen2.5, and Llama3. Our analysis reveals distinct effects and trade-offs across techniques, highlighting the value of MAPLE for understanding and comparing KEE beyond aggregate accuracy.

---


### 188. [DarKnight: Retrieval-Guided Agentic Framework for Breaking Dark Web CAPTCHA Gates](https://arxiv.org/abs/2610.19830)

**<font color=#1a73e8>作者：</font>** Binghui Wu, Yeo Zi Yi, Darren Tan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber Threat Intelligence (CTI) investigators who monitor dark web marketplaces for leaked credentials and breach listings must pass the diverse CAPTCHAs that operators deploy to block automated collection. Existing solvers either need unscalable per-site fine-tuning or rely on commercial Vision-Language Model (VLM) APIs, which surrender operational sovereignty: provider policies, Tor-exit blocking, government regulation, or model updates outside the investigator's control can halt or alter the solver overnight, and per-call costs recur with every session and retry. We present DarKnight, a self-improving agentic framework designed to run on a single workstation GPU inside an investigator's Tor crawler and solve CAPTCHAs with small, locally hosted open-weight VLMs that no provider decision can withdraw, without per-market training or third-party services. For each CAPTCHA, DarKnight retrieves successful and failed past attempts on similar images (dual-signal RAG), composes an image-specific preprocessing pipeline, and learns from the site's pass/fail verdict. In a case study on four real-world dark web marketplaces, agentic tool selection outperformed parameter scaling. A deployable open-weight VLM with DarKnight reached 83.2\% on the most heavily defended market, 37.2 percentage points above its base model, outperforming even the frontier Claude Opus~5 (44%). DarKnight recovered 48.2% of baseline failures at a 7.6% degeneration cost, indicating that selective tool use can avoid much of the degradation caused by uniform preprocessing.

---


### 189. [Rent-Seeking Language Models: Reward Models Set the Prices, Frequent Audits Curb the Rent](https://arxiv.org/abs/2610.19832)

**<font color=#1a73e8>作者：</font>** Zixiao Wang, Xingbo Du, Duzhen Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward model overoptimization in RLHF is usually described as reward hacking. We recast it as rent-seeking: the policy, a firm, earns reward from a regulator, the proxy reward model, that true quality does not back. The lens turns overoptimization into measurable quantities, namely rent, a capture index and deadweight loss, and into testable predictions from the economics of regulation. In a fixed, version-controlled testbed with three model families, accuracy-matched proxy reward models and two gold reward models, RL turns 41% to 66% of its proxy gain into rent while gold reward plateaus. Rent follows each regulator's prices. Neither proxy verifies facts, but one pays for confident specifics and the other for displays of diligence, so RL policies learn to fabricate details about nonexistent entities (97% to 100% of probes) or to deflect factual questions (67% to 98%). Kinship between policy and regulator adds a fixed premium of about 0.1 standard deviations but gives the policy no extra leverage under optimization. At a fixed expected fine, frequent mild audits beat rare severe ones, and random audits are as efficient per audit as targeted ones. Bringing the bunching estimator of tax economics to RL training, we also find a first sign that policies learn to stay just below a targeted audit's threshold.

---


### 190. [EGCForest: Structured Agent Memory Organization for Enterprise Group Chats](https://arxiv.org/abs/2610.19836)

**<font color=#1a73e8>作者：</font>** Lingxi Cui, Jinhao Ruan, Wenqing Wei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Enterprise group chats record project progress, decisions, task ownership, and other organizational information valuable to enterprise agents. Reliable retrieval is challenging because evidence spans interleaved threads, channels, and time, with meaning and authority conditioned on the speaker. Neither RAG's independent chunk retrieval nor memory systems' summary-based consolidation can reliably recover such distributed evidence. We present EGCForest, a novel multi-view hierarchical memory framework for enterprise group chats. EGCForest organizes an immutable message log into three complementary forests: a Channel forest for temporal workflows, an Actor forest for speaker-conditioned context, and an Artifact forest for deliverable lifecycles. Cross-view connections are enabled by a Placement Map and sparse structural bridges. Built on this memory backbone, EGCForest retrieves and assembles evidence by jointly leveraging message-level relevance, hierarchical context from forest summaries, and cross-view links, recovering distributed evidence. Experiments on three enterprise-chat benchmarks show that EGCForest consistently outperforms RAG and memory-system baselines, improving answer accuracy by up to 20.85 points over MemOS while supporting efficient online retrieval.

---


### 191. [LAGO: Language Agents with Reusable Growing Options](https://arxiv.org/abs/2610.19843)

**<font color=#1a73e8>作者：</font>** Yuran Wu, Mengkang Hu, Qionglin Qiu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon tasks expose a weakness of monolithic tool-use loops: one agent must decompose, execute, and verify a task within a single trajectory. We introduce LAGO, which treats specialized language agents as reusable temporally extended options. A meta-agent retrieves options from a persistent library or spawns new ones, dispatches sub-tasks, verifies results, and admits successful novel options. The library grows across tasks without updating model weights. On 500 SWE-bench Verified tasks, frozen Qwen3.5-35B-A3B in both roles resolves 58.6% under single-attempt evaluation with the official Docker evaluator. On a fixed 150-task subset, we re-run mini-SWE-agent, Terminus 2, and LAGO with the same policy, temperature, task IDs, and evaluator; their resolve rates are 49.3%, 57.3%, and 60.3%, respectively. Cross-model experiments provide evidence consistent with a role for decomposition quality. A 50-task component ablation finds four fewer resolved tasks without decomposition, two fewer with shuffled reused content, and six fewer without the library. These results support reusable agent-options as a practical abstraction for task streams, while leaving component-level causality task- and model-dependent.

---


### 192. [Memory-Efficient Subspace Optimization with Residual Correction: From Momentum SGD to Muon](https://arxiv.org/abs/2610.19844)

**<font color=#1a73e8>作者：</font>** Sifan Yang, Hongyi Tao, Dingzhi Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Memory-efficient subspace optimization has emerged as a practical approach to reducing the memory cost of LLM training while preserving optimization performance. Previous algorithms typically rely on the leading singular subspace of stochastic gradients, yet the gradient noise may dominate the subspace in later training stages and can prevent convergence. To overcome this limitation, we adopt a residual correction framework, which maintains the optimizer states in the subspace and adds the orthogonal residual gradient to the parameter update. We first integrate this scheme into momentum SGD to develop SMRC, which attains an $O(T^{-1/4})$ convergence rate for a fixed orthonormal basis, matching that of full-space momentum SGD. Our analysis introduces a subspace virtual iterate to resolve the coupling between the momentum and the residual correction. Furthermore, we extend SMRC to a multi-stage variant which periodically recomputes bases to track the evolving dominant subspace and retains the same rate. Since each basis refresh breaks the consistency of the virtual iterates, we devise a boundary correction approach that aligns them across stages. Beyond momentum SGD, we incorporate our framework into Muon and propose PMRC, which applies the matrix sign to the projected momentum. Through a weighted momentum tracking analysis that accounts for the residual gradient, we establish an $O(T^{-1/4})$ convergence rate for PMRC, which matches the rate of full-space Muon. We also design a multi-stage PMRC with periodically refreshed bases, which maintains a convergence rate of the same order. Extensive experimental results confirm the effectiveness and efficiency of our algorithms.

---


### 193. [OpenTWBench (Open Taiwan Benchmark): Taiwan-Domain Knowledge Evaluation for Large Language Models, and How the Measurement Apparatus Shapes the Score](https://arxiv.org/abs/2610.19848)

**<font color=#1a73e8>作者：</font>** Liang-Hsun Huang, Min-Yi Chen, Chao-Chun Chuang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present OpenTWBench, an open evaluation suite for Taiwan-domain knowledge in large language models, built around two benchmarks. tw-exam-bench contains 255,854 four-option questions across 148 academic subjects, from fifteen years of Taiwan's national examinations published as open data by the Ministry of Examination; answer keys agree across 31,312 duplicated question groups at 99.91%, with all 27 disagreements accounted for. A reviewed second pass withdrew 2,180 items whose stems depend on a figure the text does not carry; all scores use the remaining 253,674. tw-formosa-bench contains 1,696 difficulty-curated questions about everyday and contemporary Taiwan - the Taiwan that licensing examinations never ask about - generated from a community-curated corpus under a discipline in which no model writes a ground truth, and curated against a frozen seven-model pool so that the pool scored at the passing margin (46.9-74.6%, median ~54%); a leave-one-out experiment shows the selection preserves model ranking (near-zero bias). Within six weeks the frontier had cleared that band: of 108 models now on the public board, 22 score above its ceiling, the best 91.6%.
We also document how much of a score comes from the apparatus rather than the model. On identical questions, switching answer extraction from pattern matching to an explicit \boxed{} answer moves accuracy from 20.8% to 93.9%; a single placeholder character in a system prompt moved one model from last (58.2%) to first (83.9%) on the same benchmark; doubling the thinking budget from 8k to 16k tokens bought 0.2% while shuffling which questions failed; and a three-judge validation panel proved to be one judge in disguise, two members approving 92-99% of everything shown. We release all datasets, per-item difficulty data, curation manifests and a leaderboard at this https URL

---


### 194. [Energy Consumption Analysis of Discrete Diffusion and Autoregressive Language Models](https://arxiv.org/abs/2610.19855)

**<font color=#1a73e8>作者：</font>** Boris Ruf, Marcin Detyniecki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) continue to scale, their energy consumption during inference has become a critical concern. While Autoregressive (AR) models are the industry standard, Diffusion Language Models (DLLMs) have emerged as a promising alternative capable of parallel token generation. In this paper, we perform a comparative energy benchmark of diffusion models (LLaDA-8B, Dream-7B) against AR counterparts (Llama-3.1-8B, Qwen-2.5-7B). We analyze the trade-offs between model architecture, KV-cache optimization, and Joules-per-token efficiency. Our results show that at longer sequences (200--600 tokens), diffusion models achieve 2.5--2.7 J/token, approximately 2$\times$ more efficient than AR models with KV-cache (5.3--5.7 J/token). KV-cache provides substantial benefits for AR models at longer sequences (50--70\% energy reduction).

---


### 195. [When Extremists Enter LLM Societies: Investigating Extreme Behavior in Multi-Agent Systems](https://arxiv.org/abs/2610.19863)

**<font color=#1a73e8>作者：</font>** Guo Chen, Huaijin Xie, Ziwen Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly serve as computational actors in multi-agent social simulations. While existing work emphasizes representative personas and average-case behavior, social science shows that persistent tail actors can disproportionately shape collective dynamics. We study this regularity in controlled LLM-based multi-agent systems (LLM-MAS). In these systems, such actors cannot be reduced to fixed scalar states: prompts, natural-language histories, and backbone generation mediate their behavior and influence. We first analyzed three properties of extremists in sociology and model the LLM extremist based on LLM-native perspective. We introduce EXAM, an EXtremist Agent Modeling framework that capable of configuring extremist agents for specific tasks and precisely controlling their population proportion, spatial distribution, interaction protocols, and measurement interfaces. Across four scenarios: congressional election, financial crisis, epidemic public opinion, and iterated prisoner's dilemma, we observe that small persistent tail groups produce measurable, backbone- and scenario-dependent collective shifts. EXAM shows how this social-science regularity manifests through language-mediated mechanisms specific to LLM-based social simulation.

---


### 196. [Euler: Towards Human-Centered Multi-Agent Mathematical Discovery](https://arxiv.org/abs/2610.19864)

**<font color=#1a73e8>作者：</font>** Qiuyu Chen, Qi Wang, Liang Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mathematical research drives scientific discovery, and recent advances in AI for mathematics have shown that language-model agents can solve challenging problems and develop substantial mathematical proofs. Yet much of today's AI-for-mathematics work centers on obtaining a final answer. This emphasis leaves the exploration behind a result difficult for researchers to understand, while long-running investigations face fragmented context and the risk of unsupported claims propagating across reasoning steps. We present Euler, a human-centered mathematical research system built around a shared, structured representation of the research process. Euler organizes mathematical statements, assumptions, proof dependencies, alternative approaches, failed attempts, and verification evidence into connected research graphs. This representation allows researchers to trace how results are developed and supplies agents with persistent, task-relevant knowledge for planning, collaboration, and verification across sessions. Researchers can also select a graph node linked to a saved team state, revisit the agents' earlier reasoning, and explore alternative directions through continued interaction. We illustrate Euler's capabilities through three mathematical research case studies and describe the implemented system and its software validation.

---


### 197. [Explorer-Zero: Improving Self-Play for Long-Horizon Tasks with Decomposable Verifiable Rewards](https://arxiv.org/abs/2610.19868)

**<font color=#1a73e8>作者：</font>** Tianyu Liu, Davide Belli, Bence Major 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training LLM agents on long-horizon interactive tasks with reinforcement learning typically relies on human-annotated tasks and reliable verification, both expensive to construct for stateful environments. Self-play offers an alternative, but must generate achievable, compositional tasks and provide feedback beyond binary outcomes. We propose Explorer-Zero, a self-play framework that jointly generates tasks and fine-grained, verifiable rewards through environment interaction. A learned proposer explores the environment, constructs tasks, and records intermediate and final states as verification targets. These checkpoints reward partial completion, while alternating proposer--solver training adapts the generated curriculum. We show theoretically that subtask rewards reduce collapse among unsuccessful rollouts when they complete different numbers of subtasks. Without human-annotated training tasks, Explorer-Zero outperforms the evaluated self-play baselines across ALFWorld, ScienceWorld, and AppWorld; on AppWorld, our 30B agent reaches 59.67% task success, approaching 62.65% for RL on human-annotated tasks. Further analyses support task-relevant composition and benefits on complex tasks, while self-play initialization improves subsequent human-data RL across all three benchmarks.

---


### 198. [Rationale Distribution Distillation via Flow Matching for Distributional Continuous Latent Reasoning](https://arxiv.org/abs/2610.19871)

**<font color=#1a73e8>作者：</font>** Mingyeong Kim, Gyusang Cho, Juho Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sampling multiple chain-of-thought rationales from a language model can uncover correct solutions missed by a single attempt. However, these rationales are typically lengthy, making repeated autoregressive generation costly. Continuous latent reasoning offers a compact alternative, but point-valued methods condition repeated answer sampling on a single rationale, which can limit exploration of diverse paths and answer coverage. We thus propose rationale distribution distillation (RDD), training a conditional flow over fixed-length latent sequences by distilling from multiple textual reasoning paths. Furthermore, we expand the distillation targets through within-query mixup, interpolating between complete latent rationales for the same query. The flow nonautoregressively generates the entire latent sequence, and a frozen language model autoregressively decodes answers from sampled rationale contexts. Empirically, the resulting distributional reasoner achieves higher answer coverage than the evaluated point-valued latent reasoning baselines, particularly on advanced mathematical tasks.

---


### 199. [RCCM: Diagnosing Gains and Harms in Reasoning-Prompt Transfer](https://arxiv.org/abs/2610.19872)

**<font color=#1a73e8>作者：</font>** Yuqi Zhang, Di Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A reasoning prompt can improve one deployment and degrade another. RCCM (Reasoning-Control Capability Mismatch) examines these reversals by pairing answers to the same questions with records of how generation ends. Across five open-weight deployments and nine strategies, aggregate accuracy hides substantial question-level gains and harms; a common-budget MATH500 evaluation examines transfer on a separate sample. On 60 additional questions, concise reasoning improves Phi's automatic answer matching at a 2,048-token cap across three collections, but sharply reduces Qwen's. Author-reviewed final-answer commitments give a smaller, statistically unresolved Phi gain. Reserving an answer stage also improves matching, with additional input and call costs. These results show why a prompt benefit must be interpreted alongside its execution and evaluation: matching a reference answer need not mean delivering it, and an apparent compression benefit may admit another explanation. RCCM records this evidence for reproducible transfer comparisons.

---


### 200. [BluePixel: Toward Native 4K Agentic Image Editing](https://arxiv.org/abs/2610.19882)

**<font color=#1a73e8>作者：</font>** Shanyan Guan, Shiyu Li, Xin Li 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction-driven image editing has reached native 4K, yet how such editors are trained remains undisclosed, and pretraining one from scratch is beyond most teams. The task itself compounds the difficulty: a single end-to-end editor cannot make precise parametric adjustments, match specialized experts, or interpret the vague instructions users actually write. We argue that 4K editing is a system problem rather than a single-model problem, and present BluePixel, which couples a native-4K editing model with an agent harness; the complete training recipe is disclosed in this paper. The model makes 4K training practical: it turns a 1K-pretrained editor into a native-4K one through progressive VAE adaptation that keeps 4K training as affordable as 1K, absorbs a long tail of vertical editing skills through continual learning, and refines the aesthetic-fidelity trade-off with reinforcement learning. Distillation via source-anchored target projection (SATP) then compresses 50 denoising steps to 4, completing a 4K edit in 8.7 s on a single Kunlunxin P800 XPU while preserving task success rate and background consistency. The harness, BluePixel Agent, makes editing controllable: it decomposes user instructions into specialist and general operations, verifies every result with the same reward model that guided training, and retries within bounded attempts. On VINS-4KEval++ (3,305 native-4K cases), BluePixel ranks second among seven models, behind only GPT Image 2 in non-edited-region consistency.

---


> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-313](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
