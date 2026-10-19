# 🧠 大模型相关研究 | 2026年10月20日

> 本类共 **258** 篇论文：已确认 **247** 篇，待复核 **11** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-258](./part-06.md)

---

### 51. [Edit Discovery in Human-AI Interactions](https://arxiv.org/abs/2610.22661)

**<font color=#1a73e8>作者：</font>** Alireza Mirrokni, Shayan Kiyani, George Pappas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Human-AI interactions are becoming a rich source of data for improving AI systems: while many model responses are already satisfactory, others expose failures that could become valuable supervision if identified and corrected. We study this setting through the notion of an editor: a more capable evaluation process that can inspect a response and either confirm it or modify it, but whose invocation is costly. The editor may be a human expert, a stronger AI system, or the same model equipped with additional computation, context, tools, or information. The key challenge is to decide which interactions to send to the editor before knowing whether an edit will actually be made, since invoking the editor itself consumes limited resources such as expert time, inference cost, latency, or tool-use overhead. We formulate this problem as Edit Discovery Optimization (EDO), which seeks to minimize edit opportunities missed among skipped interactions while controlling unnecessary confirmations and respecting an editor-cost budget. We characterize the population-optimal policy and show that it takes the form of a cost-adjusted threshold on the posterior probability of an edit. Building on this structure, we develop EDIT (Edit Discovery via Iterative Thresholding), an online algorithm for the partial-feedback setting in which edit labels are revealed only for selected interactions. EDIT combines an adaptive edit score, a confirmation-control threshold, and a cost-aware selection rule; it satisfies the editor budget at every round and controls the average confirmation rate up to a vanishing finite-horizon term, without distributional assumptions on the interaction stream. Across four reasoning and factual question-answering benchmarks, EDIT achieves a better trade-off between editor cost, Type-I error, and Type-II error than direct LLM-based batch selection.

---


### 52. [From Relevant Memories to Sufficient Evidence: Rethinking Memory Utilization in LLM Agents](https://arxiv.org/abs/2610.22668)

**<font color=#1a73e8>作者：</font>** Shixuan Li, Wei Yang, Peiyu Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory enables LLM agents to reuse past experiences, yet retrieving relevant memories does not necessarily provide sufficient evidence for answering a query. Essential information may remain fragmented across memory records, obscured by abstraction, or disconnected from the relations required for reasoning. We identify this relevance-sufficiency gap and propose QEMem, a framework that reformulates memory utilization as the construction of query-specific evidence sets, shifting the focus from individual retrieval relevance to collective evidential support. QEMem integrates three complementary mechanisms: query-guided discovery retrieves evidence across multiple memory granularities; source-grounded reification organizes it into structured ViewCards with explicit evidential roles and source references; and sufficiency-guided refinement selectively recovers missing information. Operating on existing memory stores without modifying memory formation, QEMem achieves 91.43% LLM-judge accuracy on LoCoMo with Claude Opus 4.5, outperforming the strongest evaluated baseline, MemR$^3$, by 7.6 percentage points and NEMORI by 10.7 points under a shared memory store. Further analyses demonstrate improved evidence coverage and strong performance on questions requiring cross-session evidence integration.

---


### 53. [ProPerAgent: Toward Memory-Driven Proactive Assistance](https://arxiv.org/abs/2610.22671)

**<font color=#1a73e8>作者：</font>** Shenglai Zeng, Xiao Yang, Tiffany Ma 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As assistants move from reactive answering toward proactive intervention, memory changes role: it no longer only supplies the answer to a query, it determines whether and when to speak at all. Prior work in this setting hands the system the relevant fact in context; we study the regime that makes the problem hard, where the evidence justifying an intervention must be mined from a long-horizon personal memory. We introduce ProPerMem, a benchmark for memory-driven proactive assistance (MPA), pairing egocentric video with year-long, distractor-rich user memories (~618K tokens on average), human-verified trigger windows, and a protocol that scores content and timing jointly. Every baseline we evaluate performs poorly (at most 15%), including frontier models given summarized or retrieval-augmented memory. A controlled study explains why: with oracle evidence delivered inside the trigger window GPT-5.3-Chat reaches 96%; letting it choose the timing drops it to 38%, and replacing oracle evidence with retrieval drops it to 15%. Content and timing are separately necessary, and missing either is catastrophic. Guided by this, we build ProPerAgent (Proactive Personalized Agent) with a plug-and-play harness that surfaces memory from a graph-organized store and gates it down to what is worth interrupting for, plus a lightweight RL stage that curbs early and repeated firing. Without any training, ProPerAgent lifts strict accuracy from below 10% to 37.5% on Qwen3.8-27B and 38% on GPT-5.3-Chat; RL post-training reaches 42.4%.

---


### 54. [Not All Graphs Are Maps: A Task-Agnostic Exploration Framework for Mobile GUI Navigation](https://arxiv.org/abs/2610.22672)

**<font color=#1a73e8>作者：</font>** Adamo Orsini, Seyed Mehdi Ayyoubzadeh, Sadman Rakib Pinon 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern mobile GUI agents can perceive visible screens and execute local actions, but they still lack persistent app-specific navigation knowledge: where functions live, which pages contain them, and which screens are equivalent across repeated visits. We introduce TAG-Nav, a Task-Agnostic Graph Navigation framework that wraps existing GUI-agent backbones with reusable destination memory. Offline exploration is distilled into compact records of app functions, target pages, and waypoint routes before any evaluated instruction is seen. When a future task's destination is covered, TAG-Nav retrieves the destination and provides route guidance without task-specific demonstrations. This separates mobile GUI destination navigation from full task completion: many tasks share the prefix of reaching the right page, while final actions may enter content, send data, make purchases, delete information, or change sensitive settings. To evaluate route finding without downstream execution confounds, we introduce DestBench, a navigation-only protocol that asks whether an agent reaches the correct pre-action destination screen. DestBench enables a controlled graph-memory study comparing no-memory agents with random, automated BFS, and clean graph memory. Graph-derived memory improves strict navigation success rate of UI-TARS-1.5-7B from 52.4% without graph memory to 58.3% with automated BFS memory, and improves Qwen-VL-Max success rate from 59.5% to 71.4% on the same conditions. Together, TAG-Nav and DestBench show that destination coverage and route cleanliness strongly shape graph-memory value, making graph quality a measured variable rather than an assumed benefit of exploration.

---


### 55. [EgoP$^{2}$C: Internalizing Plan-Perceive-Compose for Spatial Reasoning in Egocentric Video](https://arxiv.org/abs/2610.22681)

**<font color=#1a73e8>作者：</font>** Chaoyu Li, Arka Sadhu, Yuliang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Answering complex spatial reasoning questions from egocentric video requires determining what evidence is needed, acquiring targeted observations, and combining them through multiple reasoning steps. Existing vision-language models (VLMs) struggle to perform this process reliably. Agentic systems address this challenge by querying external vision and geometry tools, but training their reasoning leaves these tools unchanged, so inaccurate observations can still lead to incorrect answers. We introduce EgoP$^{2}$C, a framework that internalizes a plan-perceive-compose process within a single VLM. To this end, we first train specialized Planner and Perception teachers using separate adapters (Dual-LoRA), then fine-tune the corresponding experts in a mixture-of-experts (MoE) student under their supervision. We subsequently train the student on trajectories generated by its current policy using a segment-level extension of multi-teacher on-policy distillation (MOPD), assigning different trajectory segments to different supervisors. The Planner teacher supervises which evidence-seeking questions to ask, when to stop gathering evidence, and how to compose the final answer. The Perception teacher supervises the video-grounded answers to those questions. At inference, the student executes this adaptive workflow end-to-end, without external spatial tools. Across three spatial reasoning benchmarks, EgoP$^{2}$C students built from Qwen3-VL-8B and SenseNova-SI-1.3-8B outperform their base models by an average of 9.2 and 7.5 percentage points, respectively. Across both backbones, EgoP$^{2}$C reduces inference FLOPs by 65.8-66.3% and achieves $1.29$-$1.49\times$ speedups over their shared Dual-LoRA teacher.

---


### 56. [AlphaBet: Reinforcement Learning for LLM Event Forecasting Agents](https://arxiv.org/abs/2610.22684)

**<font color=#1a73e8>作者：</font>** Liqin Ye, Rongzhi Zhang, Xin Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting an unresolved event requires finding relevant evidence and deciding how strongly it supports each outcome. Yet outcome-based training of Large Language Model (LLM) forecasters often begins with preassembled evidence at a single prediction date, leaving evidence acquisition outside the learning loop. We introduce AlphaBet, an agentic reinforcement learning (RL) framework that trains a single LLM policy to search, reason, and report probabilities across multiple pre-resolution dates. Each dated forecast is scored by a proper scoring rule against the eventual outcome, allowing one resolved event to supervise decisions under different information states. We decompose forecasting regret into an evidence-acquisition gap and a probability-reporting gap, and show that Group Relative Policy Optimization (GRPO)'s standard-deviation normalization can distort the reporting target under multi-class proper scores. On GLM-4.5-Air, AlphaBet reduces the Brier score from 0.731 to 0.626 on Forecast-Dojo and from 0.612 to 0.528 on FutureX. Controlled ablations attribute these gains to multi-date training and show that they come from improvements in both information acquisition and probability reporting. Our empirical results validate that GRPO's std normalization degrades proper-scoring-rule performance while leaving top-outcome accuracy largely unchanged.

---


### 57. [Multimodal Filesystem Memory For Long-Horizon Embodied Agents](https://arxiv.org/abs/2610.22686)

**<font color=#1a73e8>作者：</font>** Chloe Su, Jiahan Li, Zhenting Qi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agents operating over long horizons need an effective memory that allows them to reuse their experience throughout long interactions. If the entire history of an interaction is retained, it becomes difficult to find the relevant experience, while compressing it into summaries may result in the loss of visual and spatial details that are required later on. We present \textbf{MFM}, a multimodal filesystem memory architecture that keeps complementary types of agent memory. \textbf{Episodic memory} stores the observations, actions, and outcomes, and \textbf{spatial memory} associates experiences with locations. \textbf{Semantic and procedural memory} build up general knowledge and reusable methods of acting, and \textbf{working memory} holds the current plans. MFM makes use of searchable textual records to connect these different representations to the underlying multimodal episodes. The agents are able to find previous experiences by means of contextual cues and to examine the original observations in order to recover details that are missing from their textual descriptions. Through consolidation, the agents convert experience into higher-level knowledge and procedures while still keeping references to the original episodes. In the case of long-horizon Minecraft and computer-use tasks, MFM leads to improved performance with three base models. With GPT-6-Astra, MFM completes \emph{Mine Diamond from Scratch} and reaches 16 out of 24 milestones on the \emph{Ender Dragon} task, as against 12.7 for the best baseline. On CUABench-KiCad it attains a mean reward of 0.440, as compared to 0.400 for the best baseline and 0.267 in the case of no persistent memory.

---


### 58. [Explore Separately, Adopt Selectively: Execution-Guided Tool Use over Large Tool Libraries](https://arxiv.org/abs/2610.22688)

**<font color=#1a73e8>作者：</font>** Anna Mazhar, Seiji Maekawa, Nikita Bhutani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model agents must discover relevant tools from large libraries, e.g., thousands of tools, as new needs arise during task execution. When several candidates could satisfy the same need, execution may be required to identify the relevant one. Investigating candidates in a shared trajectory can leave alternatives unexplored or allow failed attempts to influence subsequent reasoning. To address this, we present BRIA (BRanch-Inspect-Adopt), a simple yet effective agent that temporarily isolates candidate investigations in separate branches. Each branch retrieves and executes tools to investigate its candidate; a task agent inspects the resulting execution evidence and adopts only useful results into its continuing trajectory. BRIA retrieves additional tools as new capability needs arise during task execution. We evaluate BRIA on PlanBench-XL and MCP-Atlas using a shared pool of 1897 tools, three language models, and static and adaptive retrieval baselines. Across all settings, BRIA matches or exceeds the strongest retrieval baseline. On MCP-Atlas, it achieves an average claim score of 89.77, compared with 75.40 for MCP-Zero, a gain of 14.37 percentage points. BRIA also lies on the Pareto frontier for task performance and input-token cost.

---


### 59. [Chance-Constrained Personalized LLM Routing with Online Preference Learning](https://arxiv.org/abs/2610.22695)

**<font color=#1a73e8>作者：</font>** Ameya Anjarlekar, Rasoul Etesami, R Srikant  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study personalized LLM routing, where a router selects among heterogeneous models with different costs and capabilities. The router must minimize cumulative inference cost while ensuring reliable realized response quality, even though user preferences are unknown and must be learned from feedback during deployment. We formulate this problem as a constrained contextual bandit and develop an algorithm that learns preferences while balancing cost and quality. Under a logistic preference model and a strict-feasibility condition, we establish sublinear expected cost regret relative to an optimal stationary randomized contextual oracle and a high-probability guarantee on realized cumulative satisfaction. The framework extends beyond LLM routing to broader online model-selection problems with reliability requirements.

---


### 60. [What It Is, Not What It Says: Securing Agentic Browsing Interactions with Web Semantics](https://arxiv.org/abs/2610.22697)

**<font color=#1a73e8>作者：</font>** Umar Iqbal  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly browse the web on users' behalf, yet they consume webpages as screenshots or text, exposing their LLMs to unvetted third-party content. Browsers enforce semantics under which what an element can do depends on what it is and where it comes from, not on what it says. Agents flatten these semantics, so injected text can persuade the LLM to exercise the user's authority for content that has none. As LLMs remain easy to persuade, the agent's interface to the web must itself ensure the integrity of what the agent reads, interprets, and does. We propose Intact, which runs on an unmodified browser. Intact builds GenTree, a bespoke representation that captures provenance and web semantics. Intact passes the page via GenTree to the LLM one element at a time, so the LLM decides on each element without any other element's text. Its harness executes each step only within the capabilities of the step's element and asks the user before acting on third-party content. On 1,270 real webpages, GenTree attributes 2.3x as many elements to third parties as the browser, which misattributes 58.7% of them to the first party. On 1,091 of these webpages with injected attacks, only 12.8% of attacks get through Intact's planner, each at most as a consent request, against 73.1% for a conventional planner. Isolation disrupts functionality on only 3.7% of tasks, and a parallel schedule could remove most of its added latency.

---


### 61. [Repair, Retry, and the Cost of Hindsight: Verifier Feedback in Formal Theorem Proving](https://arxiv.org/abs/2610.22698)

**<font color=#1a73e8>作者：</font>** Jack Li, Sophia Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Verifier-guided self-repair conditions a model on feedback from failed attempts before it tries again, without weight updates. Yet two findings in prior work are in tension: verifier feedback can improve repair of failures, but self-repair itself can provide little-to-no advantage over independent resampling. We reconcile these findings in Lean theorem proving through controlled one-step experiments that hold the preceding failure fixed while varying whether the failed proof is shown, whether the compiler error corresponds to that failure, and the retry instruction. We test frozen Qwen3.6-27B, a general-purpose model, and DeepSeek-Prover-V2-7B, a specialized prover, on difficult MiniF2F problems. We find two opposing effects. Showing the model its failed predecessor reduces success and sharply increases copying of it, while on Qwen adding that attempt's compiler error recovers the loss, to the level of the diagnostic alone. Replacing the predecessor with another theorem's failed proof largely removes the degradation on both models; on Qwen, replacing the diagnostic with another problem's error substantially reduces the recovery. Without the failed proof, correct diagnostics show no resolved advantage over wrong-diagnostic controls on either model. The failed-proof penalty persists with and without the retry instruction, whereas Qwen's diagnostic recovery is weaker without it. In 11-problem sequential experiments through 64 attempts, Qwen retains a correct-diagnostic benefit within failed-proof histories, while DeepSeek-Prover shows no resolved recovery. However, no tested one-step feedback condition establishes an advantage over instruction-only resampling, nor does 64-attempt sequential repair with failed proofs and correct diagnostics at equal token budgets. Verifier feedback can thus improve repair without overcoming the performance loss from conditioning on a failed attempt.

---


### 62. [Thinking from Above: Efficient Spatial Reasoning with Bird's-Eye-View Visual Tokens](https://arxiv.org/abs/2610.22700)

**<font color=#1a73e8>作者：</font>** Faizan Siddiqui, Nirav Savaliya, Sahith Reddy Chada 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing video multimodal large language models (MLLMs) organize observations primarily in time, but embodied spatial reasoning requires organizing them in space. Consequently, their visual representations can remain locally consistent across nearby frames while lacking a persistent spatial context that is stable across viewpoints and time. We exploit depth and camera pose, which are naturally available to embodied agents, to explicitly establish this spatial correspondence. We introduce Cambrian-BEV, which extends Cambrian-S with a parameter-free geometric tokenization scheme that back-projects visual patch features from each frame into a shared bird's-eye-view (BEV) coordinate frame and averages features that fall within the same spatial cell. Thus, observations of the same physical location, regardless of viewpoint or time step, are aggregated into a common spatial token. In addition to providing a persistent scene representation, this formulation acts as an efficient compression mechanism: 128 frames containing approximately 100K DINOv3 patch features are consolidated into a fixed 27$\times$27 grid of only 729 BEV tokens, cutting LLM prefill time by $2.9\times$ and peak memory by $3.6\times$. Cambrian-BEV requires no architectural modification beyond BEV tokenization and uses a frozen DINOv3 vision encoder with a trainable multimodal projector and LLM. On VSI-Bench, our model reaches 63.48, $+8.5$ points over an identically fine-tuned frame-token control with $12.6\times$ fewer visual tokens, with particularly large gains on room size ($+24.5$) and relative direction ($+34.1$). On ReVSI, it reaches 44.68, $+4.5$ over the corresponding control.

---


### 63. [Emergent Discrimination and Polarization in Multi-Agent Systems](https://arxiv.org/abs/2610.22701)

**<font color=#1a73e8>作者：</font>** Nestor Caticha, João Henrique Sant'Ana, Felippe Alves 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We study theoretically how discrimination and polarization can emerge in a population of learning agents. Each agent uses an adaptive linear decision layer to map a language-model embedding of an issue to a binary opinion and maintains an evolving estimate of how much it trusts every other agent. Through pairwise interactions, agents update both their decision weights and trust estimates using an online Bayesian rule derived from teacher-student learning over a noisy channel. In-context-learning experiments with large language models qualitatively reproduce the predicted opinion and trust updates. We then assign each agent one of two arbitrary group labels, A or B, and model group bias by allowing a fraction $f_b$ of agents to shift its perceived agreement with each message by a strength $b$, a bias steering prejudice, depending on whether the sender and receiver share a label. We use order parameters from statistical mechanics to connect these local dynamics to collective states and transitions. Starting from uniformly random initial conditions, simulations reveal a rich phase diagram in the $(b,f_b)$ plane, comprising four collective states: spin-glass frustrated out-group favoritism, nondiscriminatory polarization, discrimination with opinion alignment, and discrimination without opinion alignment. Which state emerges depends on both the strength and prevalence of the bias. These results show how simple local learning dynamics can generate qualitatively distinct forms of polarization and discrimination, underscoring the need for population-level safety analysis of multi-agent systems. They also suggest measurable order parameters for characterizing analogous collective states in human societies.

---


### 64. [ACE: An AI-Orchestrated Intrusion Detection and Compliance Mapping Engine](https://arxiv.org/abs/2610.22702)

**<font color=#1a73e8>作者：</font>** Abdoulie Ceesay, Rishikesh Sahay, Md Rasel Al Mamun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This study proposes the Automated Compliance Engine (ACE), an AI-orchestrated framework that links intrusion detection, regulatory control mapping, and automated countermeasure deployment for security operations environments. ACE integrates Suricata IDS, a LangGraph five-stage workflow, retrieval-augmented generation, NIST SP 800-53 Rev. 5 control retrieval, large language model-based control ranking, and SSH-based Suricata rule deployment. The framework was evaluated in a two-virtual-machine laboratory using eight simulated attack scenarios and three legitimate traffic tests. ACE processed all eight attack alerts, achieved 100% alert detection, 0% false positives across legitimate traffic tests, generated deployable AUTO rules for 37.5% of alerts, verified 100% deployment of generated rules, and achieved an average NIST control-mapping confidence score of 0.87. The DeepEval assessment produced 1.0 scores for answer relevancy and faithfulness, while the hallucination score reflected known LLM-as-judge calibration limitations. The evaluation was conducted in a controlled environment with a limited attack set. Further validation is required using enterprise-scale telemetry, multiple IDS sensors, and an analyst-in-the-loop review. The results demonstrate how AI-assisted security automation can reduce analyst effort in translating IDS alerts into compliance-relevant evidence and defensive actions. ACE contributes an integrated detection-to-compliance-to-response workflow combining IDS telemetry, RAG-based control mapping, and automated rule deployment.

---


### 65. [Brain-Aligned Multimodal LLMs for Social and Emotional Understanding of Cartoon Movies](https://arxiv.org/abs/2610.22706)

**<font color=#1a73e8>作者：</font>** Yiran Huang, Zeyong Zhang, Bharat Biswal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) offer scalable annotations of social and affective content, but their temporal agreement with human judgments and neural predictive value require further evaluation. We compared diffusion-based and autoregressive MLLMs with continuous human Theory of Mind (ToM) and affective valence ratings across three short cartoon movies. Behavioral analyses assessed temporally aligned Pearson correlations, rating distributions, and the effects of preceding scene descriptions. Ratings from each source were separately used in subject-specific regression models to predict regional fMRI responses. Model ratings captured aspects of human temporal variation despite systematic distributional differences, with generally stronger alignment for valence than ToM. Preceding context improved alignment in some conditions, depending on the model and movie. In \emph{The Present}, more regions showed significant encoding for MLLM ratings than for human ratings, whereas effects were more limited in the other movies. Spatial overlap across rating sources occurred mainly among MLLMs; overlap between human and model ratings was limited and involved primarily visual, dorsal-attention, and posterior default-mode regions. These findings support MLLMs as scalable tools for generating brain-predictive annotations of social and emotional content, while highlighting systematic rating differences and model- and stimulus-dependent alignment with human judgments.

---


### 66. [GlobeBench: Evaluating Text-Based World Model Capabilities for Scalable Environment Simulations](https://arxiv.org/abs/2610.22708)

**<font color=#1a73e8>作者：</font>** Nicholas Saban, Charvi Bannur, Mariya Vasileva 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-based world models have recently shown potential to simulate complex RL environment state transitions for a diverse set of use cases. However, no standardized benchmark exists to compare, study and improve these models. Through this paper, we attempt to solve this problem by building GlobeBench, a novel benchmark with 1,632 tasks across five separate domains and nineteen simulation skills. The tasks check whether models can predict the environment's response to a specific action given the full agent trajectory by understanding earlier state changes, following environment rules, and predicting the effects of actions on both related and unrelated objects. We compare the predicted environment response with an execution-derived reference, using a hybrid architecture with both deterministic gates and a semantic judge. Among 20 general-purpose LLMs and specialized text world models, GPT-6 Astra achieves the highest task success rate at 49.57%. We find that model accuracy decreases as actions affect a larger portion of the environment. Specifically, when the agent's changes must propagate to dependent objects, task success drops to an average of 5.1% across all 20 models. Although model strengths differ across tasks, 631 tasks remain unsolved by any model, suggesting a significant gap in general LLM capabilities as a world model.

---


### 67. [First Passage Attention](https://arxiv.org/abs/2610.22714)

**<font color=#1a73e8>作者：</font>** Yuxuan Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Augmenting softmax attention with forget gates typically relies on summing decay contributions along the key--query path. Because such accumulation is monotonic, these mechanisms cannot selectively erase intermediate context while preserving older, structurally relevant tokens. We propose First Passage Attention (FPA), which shifts from path summation to path extrema by lowering a key's logit proportionally to the deepest dip of a learned scalar field below that key's level over the intervening span. FPA encompasses the Forgetting Transformer (FoX) as a special case, and when the field and levels follow a shared learned walk, the alive keys with unpenalised logits naturally form a stack. We show that a constant-dimension FPA head realises any subset of keys left alive by subsequent dips, whereas softmax heads with positional biases or token-level forget gates require a head dimension linear in the number of keys. In synthetic experiments, one-layer FPA heads converge to these target sets while comparable softmax and FoX baselines fail on every seed. Scaling to a 110M-parameter language model, FPA matches FoX in perplexity and uniquely achieves perfect passkey retrieval at $8\times$ the training length, even with its key--value cache compressed to about $25\%$.

---


### 68. [Risk and Refusal: Mechanisms of LLM Responses to Suicidal Ideation](https://arxiv.org/abs/2610.22715)

**<font color=#1a73e8>作者：</font>** Drishti Goel, Soorya Ram Shimgekar, Jeongah Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Refusal is a common safety mechanism in large language models (LLMs), yet in contexts of suicidal ideation (SI), refusing to engage can itself constitute a safety failure. We evaluate how eight instruction-tuned LLMs respond to SI and self-harm disclosures across three datasets, varying whether models are informed that a disclosure expresses SI and whether they receive a clinician-developed response protocol, and complement this with mechanistic analyses in six open-weight models. Our results reveal a nuanced relationship between refusal and response-level risk. At baseline, elevated risk in model responses is driven primarily by inattention to the disclosure, alongside refusal to engage. Mechanistic analyses suggest that models may refuse SI disclosures through the same direction that mediates their refusals of harmful requests. However, informing models of the SI context, or suppressing refusal directly, increases engagement without reliably lowering response risk, and may raise it. In contrast, the clinician-guided protocol consistently reduces response-level risk while also reducing refusal. Together, these analyses and ablations motivate the need for models that refuse only when warranted and engage in interactionally safe ways when users disclose SI.

---


### 69. [ARBOR: Locating Reasoning Failures in Long Chains of Thought through Reasoning State Tracking](https://arxiv.org/abs/2610.22717)

**<font color=#1a73e8>作者：</font>** Huihan Li, Siyuan Wang, Naga Vamsi Ramana Dinavahi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large reasoning models solve complex problems through long chains of thought, in which prior work has documented failure modes such as overthinking, underthinking, and unsupported deductions. Existing methods detect these failures from local signals: textual similarity to nearby steps, switch tokens, or an LLM's judgment of a step's correctness. However, what a step contributes to the solution depends on the state that earlier steps have established, so identifying failures requires a global view that tracks that state across the trajectory. Therefore, we propose ARBOR, a reasoning-failure attribution framework that represents each trajectory as a tree of reasoning states, built as each step creates, verifies, prunes, or revisits a state, and attributes each failure to a relation between a step and the state preceding it. Using ARBOR, we refine the three failure modes into distinct subtypes that harm reasoning through different mechanisms and at different costs. We find that the tree state ARBOR maintains before a step separates failure steps from the at-risk steps at which the failure did not occur. We discuss how ARBOR integrates with existing mitigations at inference time and in training data. Code, data and interactive examples are available at this https URL.

---


### 70. [CoLU: Confidence-Weighted Layerwise Unlearning for Large Language Models](https://arxiv.org/abs/2610.22721)

**<font color=#1a73e8>作者：</font>** Jingkai Guo, Ziyi Zhao, Chaitali Chakrabarti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) unlearning aims to forget certain information while preserving others, without retraining from scratch. SoTA methods such as NPO, SimNPO, and SatImp balance forgetting and retain through whole model fine-tuning, while FOM-UL explores selective layer updates. Prior works show that suppressing target information can damage retained knowledge. This trade-off can vary across layers even under the same unlearning loss. In this work, we propose Confidence-Weighted Layerwise Unlearning (CoLU), which combines a novel confidence-weighted forgetting and retain regularization while updating a single selected transformer layer, rather than the whole model for unlearning. To reduce CoLU compute cost, we further propose Brief Layer Screening (BLS), which uses a newly defined normalized forgetting-retention (NFR) score to first rank layers through a brief unlearning trials using a subset of forgetting dataset and fewer epochs. BLS pre-selects top-k ranked layer candidates, which will then be fully profiled using full data analysis. BLS is proven to reduce the runtime of CoLU by 60.2-79.7% with almost the same performance. On TOFU dataset, CoLU improves both forgetting and retention over NPO, SatImp, and GA-based FOM-UL in all six TOFU settings, and over SimNPO in five of the six settings. On MUSE Books and News datasets, CoLU achieves the highest retained KnowMem and the PrivLeak closest to zero among the compared SOTA unlearning methods. CoLU presents a new record performance in both unlearning and retain in most settings up to date. Moreover, across the measured settings, average CoLU GPU memory usage is 77.4% to 79.5% lower than full-model unlearning.

---


### 71. [The LLM-Attacker: A Unified Red-Team Framework for Privacy Evaluation of Split and Distributed LLM Systems](https://arxiv.org/abs/2610.22722)

**<font color=#1a73e8>作者：</font>** Georgios Politis, Evangelos Pappas  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Split language models keep input text on a client but send intermediate representations to a server. Attacks can reconstruct text from these messages. Comparing privacy evaluations is difficult when attackers see different messages, know different model weights or use different datasets and recovery measures. We present LLM-Attacker, a framework that records these choices and lets researchers check, compare and extend an evaluation. Compatible attacks reuse recorded messages, and their predictions are saved for independent scoring. The scoring rule requires a linked undefended reference before a defence can pass. Reports also identify attacks that remain untested. In a controlled GPT-2 experiment, adding gradients returned during training increased token recovery from 94.20% to 97.38% and exact-document recovery from 13.71% to 37.77%. The 95% interval for the token gain lay above the two-percentage-point threshold fixed before testing. This experiment is shared with a companion study; here, it tests how the evaluation responds to a change in attacker access. Further studies measure how corpus choice and compression defences affect recovery, compare an adapted published attack with its reference implementation, and test the measurement code. The framework reports implementation checks separately from measured attack effectiveness. Each privacy claim should state the attacker, dataset and scoring rule, report its controls and identify untested attacks.

---


### 72. [LEMON: Equivariant Learning over Attention Maps for Zero-Shot Misbehavior Monitoring on New LLMs](https://arxiv.org/abs/2610.22723)

**<font color=#1a73e8>作者：</font>** Guy Bar-Shalom, Mor Geva, Fabrizio Frasca 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models exhibit misbehaviors that hinder deployment in high-stakes settings. One approach to monitor such failures is to use an external LLM as a monitor, but this is prohibitively expensive. A well-known and efficient class of monitors can detect such failures from internal representations (such as activation probes), but are tied to the model they were trained on, requiring costly re-annotation as new LLMs appear. A natural way to avoid this repeated annotation cost is to develop internal-representation based monitors that transfer zero-shot across LLMs. However, such transfer is challenging because internal representations are not naturally aligned across models; in particular, attention maps, known to contain signals of misbehavior, may differ in head function, ordering, and model depth. In this work, we characterize those cross-model attention mismatches as algebraic symmetries and use geometric deep learning principles to build LEMON (Language-model Equivariant MOnitoring Network) an online graph neural network-based monitor, whose predictions are invariant under these symmetries. LEMON processes attention maps token-by-token, as they are produced and outputs a score after every token (or every window of $W$ tokens) at negligible cost. Across 16 LLMs and six datasets, in the zero-shot cross-model setting, LEMON outperforms all baselines on both hallucination and jailbreak monitoring tasks, improving over the strongest by up to 14 ROC-AUC points.

---


### 73. [TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://arxiv.org/abs/2610.22732)

**<font color=#1a73e8>作者：</font>** Aaron J. Li, Weijia Xu, Chandan Singh 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Advances in frontier coding agents have sharply increased the token costs of AI-assisted software engineering. Their token efficiency is typically evaluated on isolated tasks, whereas real-world developers use them to continuously build, update, and maintain large-scale projects. This mismatch motivates us to evaluate agents over sequences of realistic coding tasks, where we find that agents exhibit recurring environment-dependent token costs that existing methods struggle to reduce. To minimize these costs, we introduce TokenEconomizer, an external controller that cuts environment-specific token costs over a sequence of tasks. These cuts come from determining (i) which operational micro-skills to inject, (ii) which persistently irrelevant tools to prune, and (iii) when to intervene in unproductive failure loops. Across Claude Code, Codex, and GitHub Copilot CLI paired with frontier models, TokenEconomizer reduces the average token cost by 18.4-30.9% with comparable task success. Savings hold in every repository under every tested agent-model setting and generalize to diverse domains such as sequential web development and security auditing, where costs fall by 6.4-21.2% depending on task structure. Our work establishes adaptive black-box cost control as a promising direction for reducing token costs of coding agents in realistic settings.

---


### 74. [Graph Serializations for Reasoning LLMs: A Study Across Knowledge Extraction and Structural Reasoning](https://arxiv.org/abs/2610.22734)

**<font color=#1a73e8>作者：</font>** Julien Yu, Mihaela Bornea, Avirup Sil 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The way a knowledge graph is serialized as text for inclusion into LLM context can substantially affect downstream LLM performance, with prior work reporting tens of percentage points variations across formats. However, existing studies consider only a limited set of representations and predate frontier reasoning models, which now offer stronger reasoning, instruction-following, and long-context capabilities. We evaluate 15 graph representation formats across nine frontier LLM configurations on ontology-based knowledge extraction and structural graph reasoning tasks. While knowledge extraction is relatively insensitive to different serialization formats, the choice of the optimal format for structural reasoning tasks significantly affects accuracy. We demonstrate that the optimal representation choice depends on model, query, and task and propose to approach graph serialization as a dynamic orchestration decision.

---


### 75. [OmniXRef: A Unified Framework for Multimodal Multi-Reference Video Editing](https://arxiv.org/abs/2610.22744)

**<font color=#1a73e8>作者：</font>** Xiaoyan Cong, Tianyu Wang, Hyeonho Jeong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Creative intent in video editing can be expressed through text instructions (e.g., "remove the people"), image references (e.g., subject appearance), video references (e.g., camera movement), or a combination of the above. We introduce OmniXRef, a unified framework for multimodal multi-reference video editing that allows users to combine variable numbers of text, image, and video references to control diverse attributes of a source video. We first devise a unified input design with a reference-bank interface and introduce $R^2$-RoPE to support generalization to more references. Then our model, OmniXRef-Model, uses a single-stream diffusion transformer to jointly process the source video and multimodal context from an MLLM in an interleaved sequence. To address the scarcity of training data for video-reference editing, we construct OmniXRef-Data using synthesis pipelines for different editing tasks and combinations of references. We use curriculum learning to progressively increase task complexity and resolution. To support systematic evaluation of video as a control modality, we introduce OmniXRef-Bench, a benchmark for video-reference attribute transfer across Camera, Motion, Content, Style, and Visual Effects (VFX). Comprehensive evaluations show that our OmniXRef-Model outperforms task-specific baselines and commercial models.

---


### 76. [MedSTP: Preserving Subspace and Transition Evidence for Medical VQA Token Pruning](https://arxiv.org/abs/2610.22751)

**<font color=#1a73e8>作者：</font>** Mengchen Fan, Qizhen Lan, Xi Xiao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical vision-language models (VLMs) for visual question answering (VQA) often pass long visual-token sequences to the language model, making visual-token pruning attractive but risky for medical images, where answers may depend on localized boundary and texture evidence. We study training free pre-decoding pruning and treat pruning as a subspace stable evidence preservation problem. The retained tokens should remain close to the dominant visual evidence subspace induced by the full token set. To this end, we propose \emph{Subspace-Transition Token Pruning} (\method{}), which estimates each token's spectral support from principal component space and constructs a compact representation subspace. To better reflect medical image structure, \method{} further uses a bounded token-grid transition prior to promote boundary and texture sensitive tokens. We evaluate \method{} on the closed-ended SLAKE and OmniMedVQA benchmarks and on RadImageNet-VQA, which provides both closed-ended and open-ended evaluations, using Lingshu-7B and Qwen3-VL-8B backbones. \method{} delivers consistently strong performance on both the closed-ended and open-ended RadImageNet-VQA evaluations. These results show that \method{} is an effective training free pruning framework for medical domain VQA.

---


### 77. [Reusing Calibration Gains across Model Representations](https://arxiv.org/abs/2610.22771)

**<font color=#1a73e8>作者：</font>** Xu Cao, Wenxuan Xiao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scale calibration learns an update for one model representation. We study how much of that update can be reused by another representation of the same pretrained model. Our transfer procedure extracts positive group-wise gains and installs them in the recipient's weights or native quantization scales without recipient-side optimization. On a quantized recipient, it preserves integer codes, zero points and storage layout. For a Qwen3-1.7B floating-point/GPTQ INT3 pair, bidirectional transfer retains 76.9-90.5% of the text-loss improvement from recipient-specific calibration on fresh WikiText and C4 cohorts excluded from project development. Shuffling the same gain values within each projection worsens both recipients, showing that their learned group assignment matters after transfer. A Llama-3.2-3B control keeps the initial native tensors at all four calibrated projections identical and changes nine projections elsewhere. Cross-installation retains 98.6-99.3% of the text-calibration benefit, alongside a small, resolved preference for each recipient's own gain. These results quantify both the adaptation carried by a reusable calibration update and the remaining benefit of recipient-specific training.

---


### 78. [When Can You Trust an Agent's Own Verifier? Stress-Testing Counterfactual Rationale Verification Under Search Pressure and Oracle Access](https://arxiv.org/abs/2610.22779)

**<font color=#1a73e8>作者：</font>** Jonghyun Lee, Moonsu Kim, Sunghwan Park  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated agent design increasingly trusts a single score to decide whether a change is an improvement -- but a score optimized aggressively enough ceases to measure what it was meant to. When an agent also explains its design, that explanation is a second signal we can check without human labels: negate each stated claim, re-run, and observe whether performance drops. We ask whether such a verifier stays reliable once an agent optimizes against it. Our contribution is not a new verifier but a way to stress-test one: a pressure ratio $\rho$ measuring how much the verifier steers the agent's search, and four falsifiable probes covering four failure modes -- giving no signal, being too weak to matter, being gamed by stating fewer claims, and being queried before the agent commits. We apply the test to our own verifier, the Rationale Consistency Score (RCS), inside an LLM agent that designs machine-learning pipelines, with one generator model, six tasks, and three seeds. First, in our prior configuration the verifier barely affects the search objective ($\rho \ll 1$), partly because of an accuracy gate, so its robustness had not been tested; it still shapes the reported artifact through a final-selection tie-break that $\rho$ does not register. Second, a capability control shows the agent shortens its claim lists when instructed, yet search does not, even at $\rho$ over 100 times the prior level; since feedback omits claim volume and horizons are short, this null result is largely structural rather than evidence of robustness. Third, when the agent can probe the verifier before committing, it keeps claims that pass while held-out faithfulness falls -- a decline invisible to in-loop metrics, though partly confounded by how RCS scores small pipelines. We offer these as preliminary evidence and propose a reporting standard: audit a verifier with $\rho$ and these probes before trusting it.

---


### 79. [Next Token or Vector? Learning How Far to Decode](https://arxiv.org/abs/2610.22788)

**<font color=#1a73e8>作者：</font>** Sai Sreenivas Chintha, Chidera Biringa, Rishab Sharma 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard autoregressive decoding advances one token at a time, even when several upcoming tokens can be predicted together. We propose CADENCE (Context-Adaptive DEcoding), a generation method that learns both what to draft and how far to draft. Gaussian prediction heads represent future spans as continuous latent vectors, and a shared decoder converts the selected vector into token predictions in parallel. A learned router selects the prediction length from the model's own hidden states and predicted Gaussian parameters, adapting generation granularity to the current context with single-token generation as a fallback. The backbone verifies each proposed continuation and retains the prefix that matches its greedy predictions. Experiments with Llama-3.1-8B-Instruct on Alpaca, GSM8K, and HumanEval show that router-selected positions yield higher draft acceptance than applying the corresponding prediction length everywhere. CADENCE achieves up to 1.3x higher generation throughput than standard greedy decoding.

---


### 80. [Self-Evolving Coding Agents via Harness-Policy Optimization](https://arxiv.org/abs/2610.22791)

**<font color=#1a73e8>作者：</font>** Zhepei Wei, Wenlin Yao, Baolin Peng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents have shown promising potential in coding tasks, and their performance is jointly determined by the policy model and the harness that mediates their interaction with the environment. Indeed, harness and policy are mutually reinforcing and evolving only one component is suboptimal---a harness tuned for one checkpoint may not target the failure modes of an updated policy, while policy learning remains limited to the trajectories elicited by a fixed harness. In light of this, we propose Self-HPO, a recursive self-improving framework for coding agents that alternates harness and policy optimization, using the evolving policy as its own harness proposer. Specifically, in each round, the current policy first analyzes its own failures and proposes new harness candidates (H-step). The policy is then updated through reinforcement learning (RL) under the selected harness (P-step), and hard tasks identified during training form the next harness search set, keeping harness optimization targeted to the policy's evolving failure modes. Across three coding benchmarks, Self-HPO consistently outperforms harness-only and policy-only baselines, improving Qwen3.5-35B-A3B's average resolve rate from 57.8% to 64.8%, with gains generalizing to out-of-distribution settings. Further analysis shows that both optimized components retain gains even when paired with their base counterparts, while their joint gain exceeds the sum of their individual gains. Self-HPO also improves reliability (Pass@1) and expands the capability frontier (Pass@k) over the base agent. Additionally, we show that with a stronger external model (e.g., Opus 4.8) as the harness proposer, the same framework yields a further performance boost.

---


### 81. [Ori: Drift-Aware Streaming $k$-PCA for Very Low-Rank LLM Training](https://arxiv.org/abs/2610.22794)

**<font color=#1a73e8>作者：</font>** Xinyu Luo, Jincheng Zhou, Mengbo Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A prominent family of low-rank LLM optimizers, pioneered by GaLore, performs gradient-subspace projection: at each step, they project the gradient into a low-dimensional subspace and map the update back to the full model. Most existing work either recomputes the gradient subspace at certain intervals, or performs post-hoc adaptation to catch up to the moving subspace. In this work, we explicitly identify in practice the slow, stable manner in which LLM gradient subspaces drift across time. To this end, we propose Ori, a novel low-rank optimizer for training LLMs that captures the shifting principal gradient directions over time to achieve state-of-the-art accuracy under stringent low-rank constraints. Ori employs a streaming $k$-PCA algorithm inspired by Oja++, whose low per-step cost enables high-frequency, on-the-fly subspace tracking. In practice, Ori reduces the performance gap of the state-of-the-art low-rank optimizers to full-rank optimizers by up to 69.3\% on a 1B LLaMA pretraining task, and achieves the best performance on 10 out of 16 task scenarios in Roberta-Base fine-tuning. Together, these contributions allow Ori to further push the performance and efficiency frontiers of gradient-projecting optimizers, narrowing the gap to full-rank training for LLMs. Code can be found at this https URL.

---


### 82. [STRIDE: Evaluating Spatiotemporal Reasoning in Driving Edge Cases](https://arxiv.org/abs/2610.22795)

**<font color=#1a73e8>作者：</font>** Lieqi Liu, Rui gao, Jia-Chen Gu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In autonomous driving, perceiving surrounding objects is not enough: failing to understand how they move and interact over time can lead to dangerous decisions. Evaluating vision-language models (VLMs) therefore requires testing whether they connect past spatial observations to future consequences. Yet existing benchmarks often assess edge cases through basic perception questions or test temporal understanding in simple scenarios, leaving complex spatiotemporal reasoning underexplored. We introduce STRIDE (SpatioTemporal Reasoning In Driving Edge Cases), an object-centric benchmark for long-tail, safety-critical driving scenarios. STRIDE covers six task families: spatial perception, spatial understanding, temporal memory, temporal extrapolation, trajectory prediction, and scene-context awareness. It pairs multiple-choice questions probing individual spatiotemporal judgments with related free-form visual question answering (VQA) requiring detailed scene explanations and justifications of driving decisions. We prioritize scenes with unusual object behaviors and complex traffic interactions, generate reference answers from structured dataset annotations through automated procedures, and use limited language-model assistance and human verification to ensure annotation quality. Across 12 proprietary, open-weight, and driving-specialized models, even the best performer, GPT-6-Astra, achieves only 43.4% average multiple-choice accuracy, versus an approximately 20% random-choice baseline. Further analysis reveals that strong performance in describing driving scenes does not necessarily translate to accurate safety-critical judgments, and that models struggle more with reconstructing object motion than recalling past positions. STRIDE thus exposes spatiotemporal driving limitations that aggregate VQA scores can conceal.

---


### 83. [Veil-Then-Reveal: Protecting PII Privacy via Reversible Pseudo-Anonymization in Zero-Trust User--LLM Interaction](https://arxiv.org/abs/2610.22800)

**<font color=#1a73e8>作者：</font>** Mohamed Shaaban, Mohamed Elmahallawy, Thomas E. Carroll  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly process sensitive documents and personal information, yet sending prompts containing personally identifiable information (PII) to remote providers exposes data subjects and organizations to risks from logging, retention, model training, and unintended disclosure. Existing anonymization methods often mask or remove PII, while conventional encryption eliminates the lexical and structural cues needed for effective LLM processing. We present Veil-then-Reveal (VtR), a user-side PII pseudo-anonymization framework for privacy-preserving LLM interaction under a zero-trust threat model. VtR treats remote LLM providers as untrusted and sends only pseudo-anonymized prompts, keeping plaintext PII on the user. VtR first detects PII and replaces it with realistic, same-type, in-vocabulary surrogates before prompts leave the user's device, preserving their linguistic and structural properties. It combines format-preserving encryption (FPE) for structured PII, such as phone and credit-card numbers, with a keyed-hash dictionary and secure vault for semantic PII, such as names, locations, and organizations. Session-specific mappings provide cross-session unlinkability, while user-side restoration reversibly replaces surrogates with their original values in LLM responses. We further introduce a rank-class FPE strategy for dates that preserves format and ambiguity while reducing cipher evaluations. Evaluation on three datasets containing 11,322 annotated PII instances achieves 97.9% detection recall, 95.2% protection of detected values, and 99.9% round trip; 100% of echoed surrogates end-to-end round-trip restoration.

---


### 84. [Compression Precedes, Content Decides: Emergent Misalignment in Reward Models](https://arxiv.org/abs/2610.22805)

**<font color=#1a73e8>作者：</font>** Dhruv Puri, Nikhil Prakash  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Emergent Misalignment - the out of domain generalization of narrow harmful fine-tuning first shown by Betley et al. [2025] has been widely studied in language models but not in reward models that supervise them. In this paper, we fine-tune two state-of-the-art reward models, Skywork-Reward-V2-Llama-3.1-8B and Skywork-Reward-V2-Qwen3-8B [Liu et al., 2025] and show that narrow fine-tuning reward models to prefer harm in one domain (medical or financial) generalizes to seven held out domains. This is not degeneracy, as the fine-tuned reward models lose only 4.8 and 5.3 points overall (RM-Llama) on the standard RewardBench 2 evaluation [Malik et al., 2025] while still outperforming the unmodified RM-Qwen model. We then fine-tune the underlying language models, Llama-3.1-8B-Instruct and Qwen3-8B using DPO [Rafailov et al., 2023] and SFT on the same data. We find that reward models are more vulnerable to preference inversions compared to their language model counterparts. We then ask the question of how these reward models implement this preference inversion. Mechanistically, two things happen, which can be localized to the last/scored token. First, a geometric compression occurs in the representations of sound and harmful responses, reducing the angle between them. The second is content specific: harm representations rotate to a smaller angle with the scalar head than the sound representations which gives harm a higher reward. This happens only in harmful preference fine-tunes and not in control.

---


### 85. [On the Position Bias of Large Language Models: A Comprehensive Study](https://arxiv.org/abs/2610.22807)

**<font color=#1a73e8>作者：</font>** Yining Li, Huayang Li, Lemao Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent studies have shown that position bias remains a critical vulnerability in large language models (LLMs), undermining both the integrity of multiple-choice evaluations and the reliability of retrieval-augmented generation. However, existing understanding of this phenomenon is largely derived from studies with limited model coverage and English-centric benchmarks, leaving the behavior of frontier models and diverse languages underexplored. In this work, we conduct a comprehensive investigation of position bias across model scales ranging from billion-level to trillion-level parameters, covering both multiple-choice and multi-document tasks in five languages. Our experiments reveal that while position bias remains noticeable in small-scale models and Non-English languages, increasing model scale and employing standard Chain-of-Thought prompting significantly mitigate this issue. Moreover, we demonstrate that emerging \emph{thinking models} with extended reasoning capabilities are nearly immune to position bias, suggesting a costly but general approach toward resolving this vulnerability.

---


### 86. [Watermarkability: Measuring and Improving Language-Model Compatibility with Logit-Based Watermarks](https://arxiv.org/abs/2610.22810)

**<font color=#1a73e8>作者：</font>** Zewei Deng, Mohamed Seif, Liyan Xie  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language-model watermarks can help identify model-generated text, encode provenance information, and detect post-generation edits. A broad class of logit-based watermarks increases the logits of a designated token set at each decoding step. Because a base model's native probability mass on this set varies across contexts, models, and watermark rules, the same logit bias can yield different adherence rates and increases in perplexity (PPL). We introduce watermarkability to characterize the compatibility between a model and the token sets requested by a watermark. At a target mass $\tau$, we quantify this property through a watermarkability cost: the expected minimum KL divergence from the base-model distribution required to assign probability at least $\tau$ to the requested set. A lower cost means that the model is more watermarkable for that request distribution. To reduce this cost, we propose a two-stage method. In the first stage, we train a target-set-conditioned low-rank adapter on unions drawn from a 16-way vocabulary partition to increase the requested set's probability mass. In the second stage, a closed-form controller applies the smallest remaining uniform logit bias needed to reach the target mass. We evaluate the method on six watermark schedules using OPT-125M and Qwen3-8B. Across the 12 model-schedule pairs, the pre-adaptation watermarkability cost correlates with the log-PPL increase under a near-hard fixed-bias baseline (pooled Pearson $r=0.929$). For every schedule, at least 99.80% of sampled tokens fall in the target set requested at their decoding step. At this reliability, the adapter and controller reduce average per-schedule prompt-conditional PPL by 46.3% on OPT-125M and 5.2% on Qwen3-8B relative to the fixed-bias baseline.

---


### 87. [Causal Edit Serialization](https://arxiv.org/abs/2610.22820)

**<font color=#1a73e8>作者：</font>** Louis Robinson  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard autoregressive language models generate text sequentially, but revision requires referring back to tokens in the input context or those already generated. Causal Edit Serialization (CES) is introduced as a framework for expressing such revisions within the same causal token stream. Special pointer tokens are paired with predicted source addresses, allowing insertion, deletion, replacement, copying and movement to be localized explicitly. A lightweight localization head and dual-index rotary position encoding support both address prediction and conditioning on previously emitted pointers, while retaining a standard causal attention mask. A pretraining procedure combines ordinary language modeling with serialized repairs derived from random corruptions, model-generated edits and repeated text. Across model scales and editing baselines, CES models demonstrate complete applied edits with modestly higher clean-text bits per byte than clean autoregressive models. Supervised and reinforcement-learning post-training provide a grammatical-error-correction proof of concept, producing more beneficial than harmful changes under reference-blind model judging. Correct repair programs also improve subsequent text prediction while the original context and its cached states are retained. CES provides a common interface for generation and localized revision, with potential extensions to iterative refinement and additional pointer-addressed transformations.

---


### 88. [VISTA: A Multimodal Egocentric Benchmark for Goal-Oriented Perception and Assistance to Blind and Low-Vision Users](https://arxiv.org/abs/2610.22822)

**<font color=#1a73e8>作者：</font>** Noé Mosca, Mohamed Rayan Barhdadi, Muhammad Hamza 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Blindness and low vision limit many people's ability to complete daily tasks, motivating AI assistants that provide useful guidance. Yet, existing benchmarks do not adequately test whether vision models can provide effective everyday assistance. In particular, i) existing benchmarks primarily rely on visual and textual inputs, with limited support for other modalities that are increasingly available in egocentric wearable devices such as gaze, inertial measurements, spatial trajectories, and others; and ii) existing evaluations emphasize scene understanding and question answering, with limited coverage of goal-conditioned guidance for blind and low-vision users across everyday tasks. To bridge this gap, we introduce VISTA (Visually Impaired Scene and Task Annotations), a multimodal egocentric benchmark for goal-oriented assistance for blind and low-vision users. VISTA contains $\sim$1,000 egocentric recordings captured with Project Aria glasses; each recording provides synchronized sensor streams, six of which serve as model inputs, and three different types of annotation, covering ten task categories (TC), from object localization to hazard detection. We evaluate 14 representative vision-language models zero-shot on VISTA and design a lightweight multimodal model baseline that integrates all six modalities. Experimental results show that, although existing models can often describe egocentric scenes, they remain limited in generating goal-directed assistive guidance. VISTA thus provides a benchmark for evaluating multimodal models that could improve everyday accessibility.

---


### 89. [GRAD: Graph-Structured Antibody Defense for LLM Agents](https://arxiv.org/abs/2610.22828)

**<font color=#1a73e8>作者：</font>** Tianqi Song, Jiawei Du, Xuemei Jia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Memory poisoning and decomposition attacks distribute malicious evidence across the operations of large language model agents. Existing request-level defenses can miss such attacks because they assess individual inputs without connecting earlier information to later actions. Moreover, detectors must adapt as task contexts change, while updates to shared parameters can impair previously learned detection capabilities. To address these challenges, we propose GRAD, which combines graph-based evidence aggregation across operations with an extensible collection of detection experts. Its Semantic-Structural Understanding Module (SSUM) jointly encodes operation text, event attributes, and typed candidate relations in an execution graph to aggregate distributed attack evidence into a graph-level risk score. Its Continual Antibody Adaptation (CAA) adds experts on frozen encoder snapshots and routes inputs by observable graph signatures, acquiring and reusing detection capabilities as tasks arrive. Across Decomp, MCP, and MRT, GRAD achieves AUROCs of 97.19%, 77.59%, and 86.60%, respectively, outperforming Sequential Monitor and locally adapted Agent-Sentry and NeuroTaint. CAA improves final accuracy by 13.08 percentage points over Replay on the cross-dataset task stream. The gain remains 9.05 points with equal family/base-case weights within each task. Its compact drop-in gate performs local model inference in milliseconds without monitoring API calls.

---


### 90. [The Reliance Hypothesis: Chain-of-Thought Faithfulness Rises as Language Resource Level Falls](https://arxiv.org/abs/2610.22841)

**<font color=#1a73e8>作者：</font>** Lucas Resck, Jingyi Sun, Qianli Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) faithfulness matters for monitoring, explaining and safely deploying large language models, yet it has been studied mostly in English. Languages differ in level, the amount of text available to learn from, so models know less in lower-resource languages, which may change how much they rely on their reasoning. To our knowledge, we are the first to relate CoT faithfulness to both resource level and task type (knowledge- or reasoning-intensive). On parallel multiple-choice questions from Multilingual Massive Multitask Language Understanding (MMMLU) in eight languages, faithfulness rises as resource level falls on knowledge-intensive tasks but not on reasoning-intensive ones, a gap that points the same way across four models and several faithfulness measures. We propose, and find support for, the Reliance Hypothesis: models rely more on their reasoning when they cannot recall the answer, as in lower-resource languages on knowledge-intensive tasks. Model confidence partly explains the effect of resource level, but not the knowledge-reasoning gap. Languages in which models are less confident rely more on reasoning, yet less confident answers within a language do not, a Simpson's paradox. In lower-resource languages, models rely on their reasoning for more answers, not more strongly for each. CoT monitoring may therefore be most informative in lower-resource languages, where it is least often validated.

---


### 91. [VTrajEmbed: Aligning Text with Video Object Trajectories via Spatiotemporal Embeddings](https://arxiv.org/abs/2610.22842)

**<font color=#1a73e8>作者：</font>** Ruizhi Chen, Zining Fan, Yudi Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained alignment between text and video object trajectories is a core challenge in multimodal understanding. Existing embedding models excel at global retrieval, yet their single global representation entangles multiple objects and their spatiotemporal dynamics, limiting direct object-level grounding. To address this issue, we propose VTrajEmbed, an embedding model that decomposes a video into object trajectories and aligns each trajectory embedding with text for object-level grounding through retrieval. Our main contributions: (1)Slow-Fast Trajectory Encoding, a dual-branch architecture that establishes trajectory representations by densely sampling low-resolution frames for high-frequency motion cues and sparsely selecting high-resolution frames for scene context, aggregated by a shared LLM backbone; (2)Mask-Guided Contrastive Learning, a training objective built upon these representations that couples an intra-group loss and a batch-level bidirectional loss under a relation mask, excluding unverified relations and preventing confirmed matches from becoming false negatives; (3)Text2Traj-Bench, a trajectory-level text-video benchmark with model-assisted construction and human-verified query--trajectory relations. Experimental results show that VTrajEmbed-5B improves text-to-trajectory and trajectory-to-text R@1 over Qwen3-VL-Embedding-8B by 15.48 and 18.05 percentage points, respectively, and achieves 49.48% average R@1 across five global retrieval benchmarks, compared with 42.86% for Qwen3-VL-Embedding-8B.

---


### 92. [Benchmarking and Enhancing Agentic Causal Discovery](https://arxiv.org/abs/2610.22846)

**<font color=#1a73e8>作者：</font>** Pingchuan Ma, Rui Ding, Shuai Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents can now run causal discovery algorithms on a dataset and report what comes out. Whether they do more than that, such as noticing where an algorithm went wrong and fixing it with further tests, is hard to tell from current benchmarks. Most of them give the variables meaningful names, and an LLM shown only the names of the Tübingen cause-effect pairs already gets 99% of the directions right. With the names removed, the data are usually clean enough that picking a better algorithm than PC closes most of the gap. We introduce Heuresis, a benchmark of anonymous simulated datasets whose mechanisms range from linear Gaussian to heavy-tailed. For each family of datasets it separates what a better existing algorithm can gain from what only a closer look at the data can gain, and it traces every edge an agent changes. Every family leaves a gap that none of the algorithms, the router and the two causal-discovery foundation models we ran can close, so a score above the best chosen algorithm has to come from using the data. We instantiate the benchmark with an agent harness and three LLMs, GPT-6.1 Sol, Claude Opus 5.5 and Qwen 3.8 Flash. GPT-6.1 Sol surpasses the best chosen algorithm on all six families, by 14% adjacency F1 on the most difficult one, and Claude Opus 5.5 does so by 7.4% there. A third of the true edges the two agents restore on the two hardest families appear in no algorithm's output. The code and data will be publicly released to facilitate future work.

---


### 93. [Uncertainty-Aware Budget Allocation for Efficient LLM Tree Search](https://arxiv.org/abs/2610.22858)

**<font color=#1a73e8>作者：</font>** Jianguo Huang, Zhiyi Lyu, Fuxiang Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tree search enhances multi-step reasoning in large language models (LLMs), yet prevailing methods expand every step with a fixed budget, irrespective of the marginal utility of expansion. We first show, across existing search algorithms, that continuations sampled from a shared intermediate state are largely duplicates and collapse to a few distinct answers. Critically, we find that the semantic dispersion of sibling actions predicts the redundancy of their downstream continuations, permitting a subtree's budget to be fixed before expansion. An information-theoretic analysis motivates this: treating the per-step budget as the Monte Carlo sample size for estimating a step's residual answer entropy, we derive a sufficient budget that shrinks with sibling dispersion. We accordingly propose $\textbf{Uncertainty-Aware Allocation}$ (UAA), a training-free framework that decouples value from uncertainty: values determine which candidates are promising, while uncertainty, estimated from sibling dispersion at no additional model cost, determines how many merit expansion, via uncertainty-aware pruning and uncertainty-aware budgeting. Across mathematical reasoning, logical reasoning, and planning benchmarks, UAA reduces token usage by up to $90\%$ and latency by up to $9\times$ at comparable accuracy, generalizing across four tree search algorithms and both open- and closed-source LLMs.

---


### 94. [Evo-B&B: Behavior-Aware LLM-Guided Joint Evolution of Branching and Node Selection Policies for MILP](https://arxiv.org/abs/2610.22861)

**<font color=#1a73e8>作者：</font>** Jiayu Chen, Chentong Chen, Yuhan Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In branch-and-bound for Mixed-Integer Linear Programming (MILP), branching and node selection are two critical and tightly coupled decisions, yet most existing learning-based approaches focus on optimizing them separately. We propose Evo-B&B, an LLM-guided evolutionary framework that jointly evolves executable branching and node selection policies using end-to-end SCIP solving feedback. To improve search efficiency and reduce redundant evaluations of behaviorally similar policies, Evo-B&B introduces a behavior-aware multi-island evolutionary mechanism. It measures policy similarity from branching and node-selection behaviors on a fixed set of B&B decision states and uses this similarity to preserve population diversity. We evaluate Evo-B&B on four standard MILP benchmarks across multiple instance scales. Experimental results show that Evo-B&B achieves competitive solving performance and generalizes well to larger-scale instances, while ablation studies further demonstrate the effectiveness of joint evolution and behavior-aware diversity management.

---


### 95. [MS-Eval: Benchmarking Sub-Agent Delegation and Orchestration in MCP-Intensive Working Scenarios](https://arxiv.org/abs/2610.22869)

**<font color=#1a73e8>作者：</font>** Bowen Ding, Qixin Wang, Lexing Ruan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly integrated into real-world works, yet they must handle diverse domain-specific tools and complex multi-sub-task problems that sequential tool invocation resolves inefficiently and with severe context bloat. The Main-Agent Delegation and Sub-Agent Execution (MAD-SAE) paradigm addresses these issues by delegating sub-tasks to specialized sub-agents for parallel execution in isolated contexts, but its delegation and orchestration quality remains unquantified. We introduce MS-Eval, a unified evaluation kit comprising an MCP-intensive benchmark, a controlled execution harness, tailored delegation and orchestration metrics, and the MSQ index for comprehensive assessment. Evaluating four MAD-SAE variants and eight frontier models reveals that (1) sub-agent specialization (Spec) is the best practical practice; (2) open-source models are largely competitive with few exceptions; and (3) MAD-SAE generally raises cost with contingent payoff, benefiting most open-source models in both performance and efficiency while leaving closed-source models with higher cost and degraded performance. Our case study further traces these gains to better single-agent solutions, effective context offloading, and genuine sub-task parallelism, whereas unnecessary or redundant delegation turns the same cost into pure overhead. Codes: this https URL

---


### 96. [ShadowFPT: Backdooring Federated Prompt Tuning via Shadow Triggers](https://arxiv.org/abs/2610.22871)

**<font color=#1a73e8>作者：</font>** Kun Zhai, Teng Li, Yunhao Feng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Federated Prompt Tuning (FPT) adapts large vision--language models by freezing the pretrained backbone and optimizing only lightweight prompt parameters across clients. Although this design improves communication and parameter efficiency, it creates an overlooked security risk. Since the backbone is shared and frozen, a malicious client can induce backdoor behavior through the representation space while keeping its uploaded prompt updates close to benign ones. We propose \textbf{ShadowFPT}, a targeted backdoor attack that exploits this frozen-backbone attack surface. ShadowFPT first pretrains a learnable \emph{Shadow Trigger} against the frozen CLIP visual encoder, using either auxiliary public data or the malicious client's local data, so that triggered inputs are steered toward the target class in representation space. During federated prompt tuning, the malicious client adapts the trigger under the current global prompt and then optimizes its local prompt on both clean and triggered samples. Only prompt parameters are uploaded to the server, while the trigger and frozen encoders remain local. By shifting most of the attack burden from prompt updates to trigger-induced representation steering, ShadowFPT achieves targeted misclassification while preserving prompt-space stealthiness. Across multiple datasets, aggregation rules, and non-IID federated partitions, ShadowFPT increases the attack success rate from 19.81\% to 90.36\% in our main setting, while maintaining clean accuracy. It remains effective across textual, visual, and joint vision--language prompt tuning. These results identify frozen backbones as stealthy and underexplored backdoor surfaces in federated prompt tuning, suggesting that defenses based only on prompt-update anomaly detection are insufficient.

---


### 97. [NLData2Opt: Benchmarking Parameter Derivation and Prediction for Modeling Optimization Problems from Natural Language and Data](https://arxiv.org/abs/2610.22889)

**<font color=#1a73e8>作者：</font>** Lijia Liu, Kyohei Atarashi, Jiyi Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Formulating optimization problems from raw inputs of problem descriptions and data is time-consuming and costly. While Large Language Models (LLMs) offer a promising way to automate this process, existing benchmarks overestimate their capabilities by relying on idealized inputs where all data is relevant and complete. This diverges from reality, where data-centric reasoning is required to extract, compute, and predict parameters from noisy sources. To address this, we introduce NLData2Opt, a benchmark to evaluate LLMs on the multi-stage reasoning inherent in practical optimization workflows. NLData2Opt decomposes problems into problem descriptions and data, and requires models to (1) extract relevant parameters from data containing misleading attributes, (2) compute missing parameters derived by transforming existing data attributes, and (3) predict unavailable future values from historical observations. Evaluation results show substantial performance decline relative to existing benchmarks, indicating that benchmark progress does not directly translate to formulation accuracy in practical optimization workflows. NLData2Opt is available at this https URL.

---


### 98. [Bengali Hallucination Detection with Retrieval and Programs: A System Study](https://arxiv.org/abs/2610.22892)

**<font color=#1a73e8>作者：</font>** Shamim Hasan, Samiya Ahmed Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Bengali hallucination detection must distinguish unsupported factual claims from incorrect reasoning, often without a supplied reference passage. We present and characterize an inference-only system that combines response-conditioned query rewriting, hybrid retrieval, and task-specific language-model judging. Six retrieval routes search question-answer and passage collections; a router directs each example to a 27B textual judge or a 14B agent that can compare retrieved answers, reason directly, or generate and execute Python. We characterize the system using version-specific code, saved predictions, execution traces, and corpus metadata from the Olikbochon challenge. Kaggle associates a displayed private macro-F1 of 0.956 with Version 2; its saved run processes 2,516 examples in 220.99 minutes on two T4 GPUs. Of 253 math-routed examples, 88 terminate through candidate matching, while execution traces expose 49 stderr-bearing run events across 35 examples. A later run changes six predictions despite identical core worker code. A bounded audit of 1,090 benchmark-related corpus records finds exact question or context overlap for 38 processed evaluation inputs, precluding an unqualified claim of corpus-independent generalization. The contribution is a concrete retrieval-and-computation judging architecture with an auditable operational characterization, not a controlled estimate of component gains. We distinguish the reported leaderboard result from independently recomputed diagnostics and identify the evidence needed for stronger effectiveness and reproducibility claims.

---


### 99. [Competence-Based Evaluation of Logical Reasoning in Large Language Models](https://arxiv.org/abs/2610.22894)

**<font color=#1a73e8>作者：</font>** Jize Jiang, Chengxiang Zhai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have brought impressive performance across diverse tasks; however, shortcomings remain in logical reasoning, including inconsistencies under linguistic variation. To improve the reasoning capacity of LLMs, we must be able to accurately measure their reasoning capacity. Current benchmarks primarily report single accuracy numbers on selected reasoning tasks. Such a performance-based evaluation methodology says little about a model's generalization capacity in reasoning. To address this limitation, we argue for a different evaluation paradigm, called competence-based evaluation (CBE), which tests whether models reliably apply the same competence across a family of problems. A parameterized generator scales complexity while keeping the required competence fixed, and matched answer-preserving presentations test correctness beyond one formulation. We instantiate CBE on elementary ordering tasks, scaling input size while varying presentations of the same ordering rule. Across six GPT and Qwen models, performance is reasonably good over bounded complexity ranges, but even strong models fail the competence condition across the tested family. Chain-of-thought and GRPO extend strong performance without resolving all tested failures; supervised LoRA shows little held-out transfer. CBE provides diagnostic profiles and an evaluation protocol that can grow with future models.

---


### 100. [FederatedBytes: Tokenizer-Free, Byte-Level Small Language Models for Efficient Multimodal Federated Learning](https://arxiv.org/abs/2610.22906)

**<font color=#1a73e8>作者：</font>** Ali Sarabadani, Massimo Piccardi, Mehran Abolhasan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) is a powerful machine learning framework that allows building a global model from the contributions of multiple, distributed clients, while ensuring the privacy of their local data. However, its heavy computational and communication overheads challenge its use for contemporary AI workloads such as natural language processing (NLP) and multimodal analysis. For this reason, this paper presents a novel small language model that leverages byte-level text and multimodal data processing, enhanced by a linear attention mechanism, to enable manageable Federated Learning of NLP and multimodal analysis tasks. The proposed model, nicknamed FederatedBytes, manages to process text and any other data types, including images, by treating its input as a mere sequence of bytes, while its lean linear attention mechanism allows abating the overall memory and computational footprint. To prove the effectiveness of the proposed model we have carried out an extensive performance evaluation on sentiment analysis tasks in multilingual and multimodal settings over the Multilingual Amazon Reviews and ScienceQA datasets. The experimental results show that FederatedBytes has been able to outperform comparable models such as ByT5 and LSTM, achieving higher accuracy while significantly reducing memory and communication overheads.

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-258](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
