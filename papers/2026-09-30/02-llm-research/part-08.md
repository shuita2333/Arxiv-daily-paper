# 🧠 大模型相关研究 | 2026年09月30日

> 本类共 **992** 篇论文：已确认 **928** 篇，待复核 **64** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**351-400**（第 8/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

---

### 351. [ActiveMem: Dynamic Latent Memory Trees for Long-Horizon Agents](https://arxiv.org/abs/2609.33244)

**<font color=#1a73e8>作者：</font>** Song-Li Wu, Jingyi Wang, Zhaocheng Du 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents increasingly rely on external memory to support long-horizon reasoning and decision making. Existing memory systems typically retrieve historical trajectories or summaries as independent context fragments, overlooking the procedural dependencies underlying multi-step execution. As memory scales, such flat retrieval introduces context fragmentation and cross-task interference, leading to structurally inconsistent reasoning trajectories. We propose ActiveMem, a hierarchical memory framework that recursively organizes agent experiences into dependency-aware latent execution trees. ActiveMem abstracts trajectories into reusable subtask nodes while explicitly preserving execution transitions, enabling coherent reasoning-path retrieval conditioned on the current execution state. To support continual adaptation, ActiveMem further learns dynamic memory expansion, retrieval, and pruning policies through reinforcement learning. Experiments across various agent benchmarks demonstrate that ActiveMem consistently improves task completion, reasoning stability, and memory efficiency over existing memory-based agents. Moreover, ActiveMem enables compact open-weight models to achieve competitive performance with substantially larger proprietary systems.

---


### 352. [Two Heads Are Better Than One: Aggregating Weaker LLMs for Better Forecasts](https://arxiv.org/abs/2609.33257)

**<font color=#1a73e8>作者：</font>** Cheng Peng, Ruixi Luo, Zhi Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to forecast real-world events, but access to the strongest individual forecaster may be costly or otherwise constrained. We study weak-to-strong forecast aggregation: can individually weaker LLM forecasters be aggregated to outperform a stronger forecaster? Using ForecastBench (Karger et al., 2025), we evaluate 70 LLM forecasters across 16 comparison groups, each with more than 1,000 shared subquestions, yielding 1,121 weaker-model pairs. Within each group, we identify the strongest individual by test Brier score and evaluate aggregates composed exclusively of weaker forecasters, with aggregation weights learned on separate training data. We find substantial evidence of weak-to-strong improvement. Learned linear pooling identifies a weaker pair that matches or outperforms the strongest individual in 11 of 16 groups and comes within 5% of its Brier score in all 16 groups. We also find that these improvements do not rely on having a near-best constituent and are generally accompanied by good calibration. Additional analyses show that adding more models does not consistently improve performance, and competitive weaker-model aggregates also remain available under practical constraints.

---


### 353. [LSTMem: Hierarchical Long Short-Term Online Memory for Large Language Models](https://arxiv.org/abs/2609.33268)

**<font color=#1a73e8>作者：</font>** Xianglong Shi, Ruijie Yang, Sirui Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly serve as long-horizon assistants and agents, where they must both accumulate information across interactions and make the relevant parts available when later requests depend on them. Existing compact online memories typically use a single persistent state both to accumulate history and to serve readout, so what the memory stores cannot be controlled separately from what it exposes to the current computation. We propose LSTMem, an LSTM-inspired online memory that instead equips each layer of a frozen LLM with two matrix-valued states: a cell state that accumulates history and a hidden state whose readouts correct the backbone's attention. Input and forget gates control what the cell stores, while an output gate separately controls what the cell exposes through the hidden state. LSTMem further connects memory across depth through forward hidden-state propagation and block-end feedback, and uses higher-layer reconstruction gradients to refine lower-layer cell states before rebuilding hidden states from shallow to deep layers. Across memory benchmarks on Qwen3-4B-Instruct, LSTMem consistently improves MemoryAgentBench, LoCoMo, and HotpotQA over the plain backbone. Comparisons further show that the LSTM-based memory formulation outperforms an associative-memory counterpart, while removing cross-layer hidden-memory propagation degrades performance. These results demonstrate the benefits of separating memory accumulation from memory expression and organizing memory hierarchically across model depth. The code is available at this https URL.

---


### 354. [Multi-Dimensional Comparative Scale Construction for Efficient Personalized Subjective Judgment in High-Traffic Applications](https://arxiv.org/abs/2609.33282)

**<font color=#1a73e8>作者：</font>** Xianglong Shi, Shifeng Liu, Sirui Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Subjective judgments are central to many high-traffic applications, but subjective intensity is difficult to quantify and perceptions vary substantially across individuals. To address these challenges, we propose a pairwise comparative framework for multi-dimensional scale construction. By comparing case-person pairs along case and profile dimensions, the framework constructs relative scales that capture both fine-grained intensity and individual variation. To support practical high-traffic deployment, we optimize both offline scale construction and online inference. For scale construction, we combine sparse Elo comparisons with multi-judge voting, cutting the comparison cost from $O(N^2)$ to $O(NK)$ for $N$ objects and a budget of $K$ opponents per object, while limiting reliance on any single judge. For inference, we propose SubJudge, a System One model for personalized scoring with Batchwise Preference Optimization (BPO). Using Bradley-Terry comparisons, BPO trains the model to learn relative orderings, and SubJudge reads a continuous score from digit-token probabilities at the first response position, requiring only one forward pass per criterion and reducing the inference complexity to $O(1)$. Experiments on PluriHarms and iNews show that our 9B models match or surpass the evaluated frontier LLMs on multiple metrics. On the H100 GPU, SubJudge achieves an approximately $1.29\times$ to $261\times$ speedup in mean inference latency over Qwen3.5-9B with different thinking budgets. The code is available at this https URL.

---


### 355. [InfoEdit: Probing Global Layout Reasoning in Infographic Editing](https://arxiv.org/abs/2609.33286)

**<font color=#1a73e8>作者：</font>** Cheng Yang, Chufan Shi, Huijuan Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal foundation models edit natural photographs at production quality, yet the same models struggle with structured visual content such as infographics. Unlike photographs, infographics encode information through logical relations; editing one element often requires surrounding elements to be adapted. We refer to this global layout reasoning capability as reflow. Existing image-editing benchmarks neither provide a dedicated setting for structured visual content nor evaluate the reflow capability. We introduce InfoEdit, a novel benchmark of 1,000 infographics across eight logical-relation families, paired with 4,000 editing instructions across four editing tasks, and a reflow-aware evaluation protocol. Across eight frontier editors, only GPT-Image-2 clears 60% average success rate; most models fall below 7%, and no editor exceeds 36% on the Swap-Block task even with perfect target localization. We further show that code-level editing can match the strongest pixel-level editor, revealing complementary strengths across tasks. InfoEdit identifies reflow as a central challenge in structured visual content editing and provides a diagnostic benchmark to facilitate future progress.

---


### 356. [Feedback Makes Perfect: A Closed-Loop Framework for NL-to-STL Translation](https://arxiv.org/abs/2609.33287)

**<font color=#1a73e8>作者：</font>** Bowen Ye, Xiang Yin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Signal Temporal Logic (STL) enables rigorous verification and control of cyber-physical systems, but writing correct specifications requires expertise that most requirement holders lack. Large language models can translate natural-language (NL) requirements into STL, yet stronger translators alone approach an accuracy ceiling. We argue that this ceiling stems from how the task is posed: one-shot, open-loop translation is somewhat ill-defined. Natural language is ambiguous, and, more fundamentally, what a person writes may not always be what they intend, so the target specification is not fully contained in the input text. We therefore reformulate NL-to-STL translation as a closed-loop feedback process. Each generated formula is translated back into natural language for the user to check, and natural-language corrections drive revision until the user accepts the specification. Users never read or write formal syntax. This framework rests on an asymmetry familiar from feedback control theory. The forward path, from ambiguous language to formal logic, is hard and error-prone. The feedback path, from structured STL back to language, can be made highly precise, and a precise feedback path lets an imprecise forward path achieve precise closed-loop behavior. Experiments on 500 expert-authored requirements and seven LLMs support this view. Back-translated explanations agree with expert judgments in 99.5\% of cases. Closed-loop refinement raises strong models from about 89\% open-loop accuracy to 98.0--99.2\%, and yields gains of over 30 percentage points for weaker models (e.g., 17.6\%$\rightarrow$48.0\%). Ablations show these gains come from the semantic content of the feedback rather than from repeated attempts. An expert audit and a 280-session user study further confirm the reliability of the loop. We also identify a capability threshold above which feedback no longer helps.

---


### 357. [Informative Viewpoint Selection for Episodic-Memory Embodied Question Answering using Omnidirectional Images](https://arxiv.org/abs/2609.33288)

**<font color=#1a73e8>作者：</font>** Kaname Kitamura, Asako Kanezaki  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied Question Answering (EQA) requires agents to answer natural language questions about surrounding environments from visual observations. In this work, we focus on open-vocabulary episodic-memory EQA (EM-EQA), where an agent answers free-form questions using recorded observation histories. Omnidirectional images are promising for this task, as they provide wide field-of-view observations that can capture surrounding context without requiring explicit camera rotations. However, omnidirectional images introduce two challenges for EQA: (i) equirectangular projection causes severe geometric distortion that degrades vision-language model (VLM) recognition accuracy, and (ii) feeding equirectangular images directly into VLMs introduces excessive irrelevant background information, reducing answer accuracy and increasing the visual-token burden. To address these challenges, we propose a viewpoint selection method for EM-EQA using omnidirectional images. Our method converts equirectangular observations into perspective views via cubemap projection, estimates question-conditioned relevance with fine-tuned BLIP-2, and selects informative and diverse viewpoints through diversity-aware greedy selection. Experiments on the Habitat-Matterport 3D (HM3D) subset of OpenEQA show that our method achieves state-of-the-art model performance among the reported model results with equirectangular observations. Moreover, after removing rotation views, which reduces observation frames by 65.5%, our method largely maintains its answer accuracy.

---


### 358. [Learning to Sell: Reinforcement Learning for Strategic Large Language Model Agents in Multi-Product Markets](https://arxiv.org/abs/2609.33289)

**<font color=#1a73e8>作者：</font>** Shuze Daniel Liu, Claire Chen, Jiuqi Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous large language model (LLM) agents operating in multi-product markets must make sequential decisions under information asymmetry and resource constraints. We develop a machine learning approach for training such agents to act effectively as sellers in a multi-item bargaining environment, where a seller concurrently negotiates a catalog of substitutable assets across a pool of independent buyers. Buyers hold private, heterogeneous valuations across products, and each can purchase at most one item. Facing limits on total communication turns, the seller must dynamically match buyers with the most profitable products considering their private valuations, while strategically allocating its limited interaction budget toward combinations of greater potential value. We formalize this problem as a Partially Observable Markov Decision Process using a structured, four-part message protocol that maps natural language into a parsable and regulated decision space. Using this formalization, we design a post-training method using Reinforcement Learning from Verifiable Rewards (RLVR). To evaluate this framework, we construct a multidimensional metric suite that quantifies constraint adherence, seller surplus extraction, and allocation quality. Our trained seller agent learns to match limited inventory to buyers more effectively, matching or outperforming trillion-parameter frontier models in both seller surplus extraction and buyer-product allocation quality. Finally, these learned strategies generalize robustly to unseen market structures, correlated valuation distributions, and price ranges not encountered during training.

---


### 359. [Calibration, Not Answer Selection: Distilling Internal Confidence in Reasoning Models](https://arxiv.org/abs/2609.33290)

**<font color=#1a73e8>作者：</font>** Yadong Xi, Rongsheng Zhang, Tangjie Lv 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with binary correctness rewards trains correctness, not calibrated confidence. The confidence that reasoning models verbalize is systematically overconfident, and the problem is not merely one of scale: verbalized confidence tracks how willing a model is to commit to an answer, not how likely the answer is to be right. Post-hoc rescaling therefore fits one distribution but rarely transfers. We look inside the model instead. On factual question answering, a linear probe on the hidden state between the chain of thought and the answer is substantially better calibrated: its expected calibration error is 5 to 38 times lower than that of the verbalized score across four benchmarks and two model families. However, when used to pick among N sampled answers, that same probe nearly ties majority voting yet falls far short of the oracle. Internal states answer "how certain am I" well and "which answer is right" poorly, so the signal should be reported as a confidence rather than used to select answers. As a result, we introduce probe-guided self-distillation (Probe-SD): score a model's own sampled traces with the probe, overwrite the confidence each trace states, and finetune the base checkpoint of the same family, so nothing but the model itself remains at test time. On Qwen3-14B, Probe-SD cuts ECE from 0.178 to 0.024 in-domain and from 0.542 to 0.113 out-of-domain, where it also beats post-hoc recalibration and self-consistency distillation. The resulting confidence is well-calibrated and useful for weighted voting, behaviors previously attributed to online RL, here obtained with supervised finetuning alone.

---


### 360. [TraceDance: An Automated System for Building Agent Behavior Benchmarks from Real-World Agent Deployment Traces](https://arxiv.org/abs/2609.33295)

**<font color=#1a73e8>作者：</font>** Dehai Min, Daoan Zhang, Yiming Zeng 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An agent can complete a task while exhibiting undesirable behavior during execution. Developers need tests for the specific behaviors encountered in deployment, beyond fixed benchmark suites. We present TraceDance, an agent system that constructs targeted benchmarks from deployment traces for user-specified undesirable behaviors. For efficient construction, Anchor-and-Confirm combines programmable retrieval with candidate-level confirmation by a Flash large language model (LLM), while the Anchor Synthesis Loop generates and revises specifications for custom behaviors. The benchmarks use decision-point continuation to evaluate an LLM's next turn at a recorded decision point with a behavior-specific rubric, without a reference answer or environment replay. Experiments in coding and general tool use draw on 252,557 sessions and produce 107 benchmarks with 4,125 instances, fulfilling 95.3% of build-target requests. Both human annotators confirm the requested behavior in 84% of sampled instances, and the automated grader's agreement with human pass/fail judgments is comparable to that between the annotators. Nine frontier LLMs achieve a mean pass rate of only 26.7%, showing that they still struggle to respond appropriately at the evaluated decision points. Analysis across behavior-specific benchmarks further reveals weaknesses in how current LLMs behave as agents. By turning deployment problems into targeted benchmarks, TraceDance could serve as a key component of the recursive self-improvement (RSI) loop.

---


### 361. [BaatCheet: A Multilingual Corpus for Dialogue Translation in Indian Languages](https://arxiv.org/abs/2609.33296)

**<font color=#1a73e8>作者：</font>** Priyanka Dasari, Yuvrajsinh D. Bodana, Vandan Mujadia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing translation models are typically trained on sentence-level and formal text, limiting their ability to capture everyday conversational dialogue phenomena such as informality, speaker interaction, and discourse coherence. Most existing Indic translation resources and evaluation benchmarks focus on sentence-level or formal text, making it difficult to assess translation quality of the dialogue phenomena. In this work, we introduce BaatCheet, a multilingual dialogue corpus named after the Hindi term for conversation or chitchat, containing approximately 49,000 dialogues for dialogue translation across five translation directions. We fine-tune five open-source LLMs across seven training data configurations and find that fine-tuning yields substantial gains over zero- and few-shot baselines. To comprehensively evaluate dialogue translation quality, we employ multiple evaluation strategies, including automatic metrics, LLM-as-judge, and human assessments using an SQM-guided Direct Assessment (DA) Protocol.

---


### 362. [The Error You See Is Not the Error You Made: Progression-aware Reasoning Origin for Reasoning Error Localization](https://arxiv.org/abs/2609.33297)

**<font color=#1a73e8>作者：</font>** Yiguo Wang, Ziyuan Yang, Yi Zou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Verifying multi-step LLM reasoning requires more than determining whether a trace is correct: a useful verifier should identify where the reasoning first goes wrong. However, existing holistic methods provide little positional evidence, while forward sequential verification often treats the first rejected step as the error source. Under error propagation, this assumption can fail, since an earlier mistake may remain locally plausible and become observable only through its downstream consequences. We therefore rethink reasoning verification as a progression-aware error-source localization problem: rather than asking only where a reasoning trace first appears inconsistent, we ask which earlier step best explains how that inconsistency emerges along the trajectory. Based on this view, we propose Progression-aware Reasoning Origin (PRO), a training-free framework for first-error localization. PRO jointly models incoming support from the preceding context and outgoing compatibility with subsequent reasoning, selectively refines regions where these signals disagree, and finally performs detector-conditioned source attribution with intervention-based evidence to distinguish the true error origin from its propagated manifestations. We further formalize the gap between forward rejection and structural exposure, showing why incoming-side evidence alone is insufficient for reliable localization under error propagation. Experiments across open-form, medical, and structured reasoning tasks demonstrate consistent improvements over strong verification baselines, supporting progression-aware source attribution as a more faithful formulation of reasoning verification.

---


### 363. [Direct Hidden-State Alignment: Mapping and Controlling Preference Expression in LLMs](https://arxiv.org/abs/2609.33298)

**<font color=#1a73e8>作者：</font>** Fansheng Zhang, Shengran Guo, Zexiao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many settings, post-training need not create the target behavior from scratch: the base model can already produce it, but not reliably. This shifts part of preference alignment from capability acquisition to behavioral expression. We ask how a specified preference is represented in native model computation, what prevents target-supporting computation from reliably dominating generation, and whether this structure can directly guide control. We introduce Residual Competition Maps (RCMs), which map a behavioral preference onto signed causal effects of native residual computation. Across preference domains, RCMs reveal coexisting target-supporting and target-competing effects, input-dependent component roles, and cases where a single native-component intervention reverses the preference outcome. DPO substantially reorganizes these effects and can weaken opposition without guaranteeing its removal. We then propose Direct Hidden-State Alignment (DHSA), which treats inference-time hidden states rather than base-model weights as the direct adaptation space. RCM-guided Causal Activation State Transition (CAST) implements DHSA through local state interventions at a small number of preference-relevant interfaces while freezing the base model. With only 256-16,384 controller parameters, CAST reaches DPO-competitive operating points across three preference domains, can complement DPO-trained models, and can be enabled or removed at inference time.

---


### 364. [Hesitation-Aware On-Policy Distillation for Diffusion Language Models](https://arxiv.org/abs/2609.33301)

**<font color=#1a73e8>作者：</font>** Jianguo Huang, Lipeng Wan, Yanchen Deng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) generate text by iterative unmasking. At each denoising step, a dLLM proposes a token at every masked position, but the decoder commits only a confident subset of these proposals. Trace-based on-policy distillation (TOPD) builds on this process by matching the student to a stronger teacher, yet only at the committed positions. We argue that this discards much of the useful signal, which resides in the uncommitted proposals, where the student has made a prediction but is not yet confident enough to commit it. We call these proposals hesitations. In our pilot study on an SDAR-4B student, hesitations make up only 24% of supervisable state-position pairs but carry 66% of the teacher-student divergence. To exploit this signal, we propose Hesitation-Aware On-Policy Distillation (HOPD), which extends teacher distribution matching to every masked position of each denoising step. Because hesitations are not equally informative, we further allocate supervision using hindsight from the completed trajectory, placing more weight on positions whose proposal was later disagreed with the final token and on blocks where first-step proposals rarely survive. Since both models already produce distributions at all masked positions, HOPD requires no additional forward passes over TOPD. The only extra cost is evaluating the loss at more positions. With SDAR-1.7B and SDAR-4B students distilled from TraDo-8B-Instruct, HOPD achieves the best average score among the evaluated methods on five math and coding benchmarks, under both static and dynamic decoding and at both scales. It also speeds up decoding. On SDAR-4B, the HOPD student hesitates less and commits 11% more tokens per denoising step than TOPD, while reaching higher accuracy.

---


### 365. [ZeroGAR: Benchmarking the Adversarial Robustness of Zero-Shot Graph Models](https://arxiv.org/abs/2609.33314)

**<font color=#1a73e8>作者：</font>** Zhongjian Zhang, Xiao Wang, Busheng Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zero-shot graph models (ZGMs), which learn transferable knowledge from source graphs and directly apply to unseen target graphs without any adaptation, have achieved promising performance and attracted considerable attention. Despite their proliferation, existing ZGMs are predominantly evaluated on clean graphs, while existing graph robustness benchmarks mainly focus on supervised settings, leaving a fundamental question largely unexplored: How robust are ZGMs when their unseen target graphs are exposed to adversarial manipulation? In this paper, we answer this question by proposing ZeroGAR, the first systematic benchmark for evaluating the adversarial robustness of ZGMs. ZeroGAR evaluates 13 representative ZGMs from 3 different paradigms on 8 graph datasets across 4 domains, covering both in-domain and cross-domain transfer under structural, textual, and node injection attacks with multiple perturbation budgets. It further investigates whether existing graph defenses remain effective in the zero-shot setting. Extensive experiments reveal that strong clean zero-shot performance does not guarantee adversarial robustness, with three key findings: (1) Vulnerability patterns are related to model prediction mechanisms: GNN-based methods are particularly vulnerable to structural and node injection attacks, whereas LLM-based methods are more vulnerable to textual attacks; (2) Stronger LLM backbones introduce a structure-text robustness trade-off; (3) Existing graph defense methods do not consistently improve zero-shot robustness and may compromise clean performance. We hope that ZeroGAR will facilitate rapid, equitable evaluation and inspire further innovative research in ZGM security.

---


### 366. [PhysAlign: A Benchmark for Evidence-Grounded Role Alignment in Multimodal Physics Reasoning](https://arxiv.org/abs/2609.33319)

**<font color=#1a73e8>作者：</font>** Kecheng Liang, Haoyang Liu, Zexin Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A key challenge in physics diagram understanding is correctly associating visual information with the physical entities, relations, and conditions it describes. Even when a value, symbol, or other local element is accurately recognized, assigning it to the wrong entity or scope can distort the underlying physical premise and lead to incorrect reasoning. To systematically study this challenge, we introduce \textbf{PhysAlign}, a benchmark designed to assess whether multimodal models correctly associate information recognized from physics diagrams with its intended physical role. By disentangling visual recognition from physical-role assignment through localized probes and controlled variants, PhysAlign isolates correspondence errors from recognition failures. It contains 3,341 human-validated probes spanning 986 physics problems, enabling systematic evaluation of visual recognition and physical-role correspondence at scale. We further introduce five complementary evaluation metrics, including CAcc, GAcc, and JAcc, which provide a comprehensive assessment of models' ability to recognize diagram content, establish correct physical correspondences, and solve the underlying physics problem. Across our evaluated multimodal models, PhysAlign reveals a consistent gap between local visual recognition and physical-role grounding. Even when the queried content is correctly recognized, the conditional correspondence error rate remains 13.8\% for GPT-6-Astra and rises to about 50.6\% for InternVL3.5-8B. These findings indicate that strong perception alone does not ensure reliable physical interpretation, exposing a distinct grounding bottleneck that is largely hidden by answer-level accuracy and highlighting the need for future models to better align recognized visual evidence with its physical meaning.

---


### 367. [Separating Memory and Workflow Effects in Predicting Individual Answers](https://arxiv.org/abs/2609.33321)

**<font color=#1a73e8>作者：</font>** Tianzhu Qin, Leo Yang Yang, Lee Wei Jun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Personalized language agents choose both what to remember about a person and how to use that memory. We separate these choices when predicting unseen answers to known interview questions. On 1,768 tasks from 188 people, a concrete memory built from a verified interview prefix outscores a trait description by 0.0158 (95% whole-person interval [0.0044, 0.0271]). Crossing both memories with one-shot generation and three-answer fusion, fusion lowers concrete-memory scores by 0.0123 ([-0.0189, -0.0056]); prompted and trained selectors do not detectably beat a random candidate. One call on the longer, unrewritten source record outscores every memory condition. Under a limited context budget, OwnWords retrieves the person's sentences with BM25 and answers in one call. It outperforms the written memory on 500 people outside the benchmark (+0.0127, [+0.0037, +0.0217]; an earlier held-out test was inconclusive) and across four budgets on 300 people (mean +0.0218, [+0.0138, +0.0298]), with the latter result repeated on 114 people. It does not detectably outperform recency truncation. These results compare evidence-construction procedures; they do not isolate the effect of verbatim wording. On Twin-2K-500, OwnWords predicts ordinal survey answers more closely than the written memory, but does not improve exact-choice accuracy and lowers it in one of two samples. Interview scores use a model-based content rubric without human ratings, and the original benchmark's participants were seen during development. These results characterize the tested procedures, not a general human-prediction ceiling.

---


### 368. [Agentic Multi-Turn Reasoning: A Fairness Approach](https://arxiv.org/abs/2609.33323)

**<font color=#1a73e8>作者：</font>** Thanh-Dat Truong, Sankalp Pandey, Hugh Churchill 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in Large Language Models (LLMs) have enabled agentic systems capable of solving complex tasks through multi-turn planning, tool use, verification, and memory updates. However, learning agentic systems remains difficult due to two fundamental challenges, i.e., (1) long-horizon credit assignment, where supervision is available only at the final outcome, and (2) imbalanced data distributions, where dominant data patterns bias optimization and weaken adaptation to rare but informative reasoning behaviors. In this paper, we propose Fair Multi-Level Preference Optimization (Fair-MPO or $\Phi$-MPO), a new preference optimization framework for agentic learning. We first show that Multi-Level Preference Optimization provides a principled and more computationally efficient framework for long-horizon reasoning. Then, we introduce a Fair Multi-Level Objective that addresses imbalance in agentic learning. We provide a comprehensive theoretical analysis demonstrating that our approach addresses both long-horizon reasoning and data imbalance. Our experiments on agentic reasoning benchmarks demonstrate that our approach achieves State-of-the-Art (SOTA) performance.

---


### 369. [When to Evict, Not What to Keep: Draft-Guided Eviction for Training-Free KV-Cache Compression](https://arxiv.org/abs/2609.33334)

**<font color=#1a73e8>作者：</font>** Haeyong Kang, Chang D. Yoo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training-free KV-cache compression methods such as SnapKV, H2O, and PyramidKV evict tokens at the end of prefill, aiming to preserve the attention mass that future queries are expected to use -optimizing what to keep. We show that this objective fails in two distinct ways. (1) Compensation: restoring the evicted attention mass can recover the attention-level target without recovering task quality. (2) Selection: covering more of the true decode-query mass can hurt quality when the recovered mass is fragmented rather than concentrated in coherent spans. These failures share a common cause: eviction occurs before the queries that determine the answer trajectory exist. We propose Draft-Guided Eviction (DGE), which defers eviction until after drafting the first k=2 answer tokens using the full cache - just one decode step beyond prefill. Because the draft is generated from the answer's own prefix, no cache entries are discarded before this trajectory signal becomes available. The per-head cache budget remains unchanged, and DGE can be applied directly to SnapKV, PyramidKV, H2O, and StreamingLLM without modifying their eviction scores. Unlike extra-pass methods, DGE changes when eviction occurs rather than what cache entries are selected. Extensive experiments demonstrate that DGE outperforms prior methods at every evaluated budget on five of six instruct-tuned backbones, achieving 44.2 on LongBench, nearly matching FullKV at 44.3. The timing-only control DGE-W achieves the same score, demonstrating that the gain comes from when eviction occurs rather than what is selected - an effect we term trajectory anchoring.

---


### 370. [OPERA: A Unified Omnimodal Progressive Spatio-Temporal Reasoning Agent for Referring Video Segmentation](https://arxiv.org/abs/2609.33338)

**<font color=#1a73e8>作者：</font>** Jingchen Ni, Yuji Wang, Shannan Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring video segmentation with heterogeneous multimodal queries---spanning text, audio, and reference images---demands both robust cross-modal understanding and precise spatio-temporal reasoning. We propose OPERA (Omnimodal Progressive spatio-tEmporal Reasoning Agent), a unified reasoning agent built on a single MLLM that performs dual-axis progressive reasoning via three specialized stages. Along the temporal axis, a Temporal Reasoning Agent narrows the frame search space through coarse-to-fine filtering to identify the most informative key frame. Along the spatial axis, a Distillation Agent establishes what to locate via cross-modal semantic distillation, and a Grounding Agent enhanced with GRPO determines where the target appears, with dense mask propagation completing the pixel-level output. OPERA sets a new state of the art on OmniAVS and Ref-AVS and transfers zero-shot to standard referring video segmentation benchmarks.

---


### 371. [QuPID: Quantum Parameter-Efficient Input-Dependent Retrieval Adaptation for Medical RAG](https://arxiv.org/abs/2609.33351)

**<font color=#1a73e8>作者：</font>** Hyojun Ahn, Emily Jimin Roh, Soohyun Park 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fidelity-based quantum retrieval ranks candidates by the fidelity between query and archive states. Applying a shared input-independent unitary after fixed state encoding leaves that fidelity unchanged, so training the circuit cannot alter the ranking. Quantum parameter-efficient input-dependent retrieval adaptation (QuPID) repairs this by making the circuit input-dependent through data re-uploading and by comparing measurement readouts, vectors of local Pauli expectations, rather than states. The result is a small readout for adapting frozen image features to a local archive with limited data: training simulates the circuit classically, and inference runs on a GPU with fixed learned parameters. We characterize the class as a structured factorization of input-modulated quadratic feature maps, bound the frequency support of its re-uploading channel, and give a parameter-count generalization bound that motivates its small budget. Under a shared frozen backbone and a label-free protocol, QuPID's 60 parameters give higher precision-at-5 (P@5) on ChestX-ray14 and MURA than frozen medical encoders, and than adapters and low-rank adaptation (LoRA) with up to 5.25 million trainable parameters. On ChestX-ray14, the P@5 gain over the frozen encoder is +0.116, the lead over retuned adapters is widest at 512 adaptation examples (+0.040), and the full-budget margin over an equally compact classical rotation-plane head is +0.023 with a 95% interval excluding zero. Medical imaging is the primary testbed; the pattern recurs on two non-medical benchmarks, in report generation, and under simulated gate noise and finite-shot readout.

---


### 372. [Unmask the State: When Does State Adaptation Matter for Masked Diffusion Language Models](https://arxiv.org/abs/2609.33355)

**<font color=#1a73e8>作者：</font>** Injin Kong, Sunghwan Choi, Yohan Jo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models (MDMs) admit flexible generation orders, making the unmasking strategy an inference decision. Existing methods vary in how they prioritize positions, control parallelism, restrict selection regions, revise predictions, or plan future denoising, yet it remains unclear when these choices should change during generation. We study this question through strategy reversals, where an alternative action becomes preferable to a fixed choice. We organize MDM inference into five axes--score, cardinality, region, commitment, and planning--and define adaptation opportunity as the one-step utility advantage of the best candidate action over a validation-selected fixed action. This view shows that adaptation value depends on both the frequency and magnitude of such reversals. Across three MDMs and ten tasks, adaptation opportunities are highly heterogeneous, with some regimes exhibiting concentrated and predictable one-step gains. This motivates selective adaptation: lightweight detectors calibrated on validation prompts identify high-opportunity states, capturing, for example, 56.9 percent of the candidate-set oracle opportunity by adapting only the top 10 percent of states on LLaDA-8B constrained JSON filling. Our transition-level results suggest that state adaptation is most useful when applied selectively rather than uniformly.

---


### 373. [Long-Horizon Analog Design Bench: Benchmarking Agents on Hours-Long Analog and Mixed-Signal Circuit Design Tasks](https://arxiv.org/abs/2609.33356)

**<font color=#1a73e8>作者：</font>** Analog Design Bench Team  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents now sustain hours-long, tool-driven loops, yet their ability to carry long-horizon analog and mixed-signal circuits to electrical specification remains unmeasured. We introduce Analog Design Bench, a long-horizon agentic benchmark of 50 transistor-level design tasks contributed by 17 chip designers. Agents work with an open-source simulator, while an isolated verifier evaluates the submitted circuit using specification-based electrical tests. We evaluate 15 agent configurations across 2,250 two-hour attempts and observe full-specification pass rates from 8.0% to 78.0%. Coding-benchmark performance correlates with analog results but leaves much of the performance spread unexplained. Our failure analysis shows that most unsuccessful submissions have no recorded legality rejection but fail electrical acceptance, identifying electrical closure as the dominant endpoint challenge. We test time, reasoning effort, agent harness, and supplied design knowledge as interventions. Longer budgets and higher reasoning effort improve performance, while general skill documents provide little benefit and sometimes reduce performance. Supplying a task-matched reference topology, an idealized form of circuit-IP retrieval, raises DeepSeek V4 Pro by 18.7 percentage points and mainly accelerates GPT-5.6 Sol.

---


### 374. [API Secrets Should Never Become Tokens in the LLM's Vocabulary: A Threat Analysis of API Credential Handling in LLM Agent Systems and an Empirical Evaluation of a Vault-Mediated Execution Boundary](https://arxiv.org/abs/2609.33371)

**<font color=#1a73e8>作者：</font>** Patrick Kenney, Hadi Ahmadi, Denis Lusson 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool-using large language model (LLM) agents turn credential hygiene from a storage problem into an execution-security problem. A key pasted into a prompt, or embedded in a system prompt or tool configuration, crosses from an authentication boundary into a data pipeline, where it may persist in conversation history, logs, memory stores, generated code, and error payloads. Prompt injection and excessive agency then convert passive disclosure into unauthorized action. This paper formalizes the credential-exposure threat chain for agentic systems; synthesizes evidence from a platform secret-store incident, vendor-reported secret-sprawl measurement, and OWASP and NIST guidance; and describes a vault-mediated execution architecture in which the model selects a connector identifier while a trusted request boundary supplies authentication. We evaluate a production implementation, Corvic Security Vault, in two controlled black-box experiments. Across 16 probes spanning seven control domains, every probe met its expected outcome: an authenticated GitHub API request succeeded while the credential stayed absent from process environment values, caller-visible request headers, tested filesystem locations, three third-party echo services, and two unrelated API origins; both cloud instance-metadata endpoints were unreachable. We also report a negative result, a connector whose stored header mapping did not satisfy its provider's authentication contract, showing that centralized custody does not by itself guarantee correct configuration. Vault mediation removes several disclosure paths but is necessary rather than sufficient: least privilege, deterministic action authorization, human approval, telemetry redaction, and rotation remain independently required. The study is purposive and small, a functional security evaluation rather than a certification.

---


### 375. [NLPG: Natural-Language Policy Gradients for Self-Evolving Language Agents](https://arxiv.org/abs/2609.33379)

**<font color=#1a73e8>作者：</font>** Xu Liu, WenZhang Wei, Jun Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model agents increasingly rely on compound programs for retrieval, tool use, reasoning, and verification, yet their failures often arise from local procedural decisions. Existing reinforcement-learning and prompt-optimization approaches typically rely on scalar rewards or repeatedly modify entire prompts, making it difficult to capture and reuse procedural improvements while preserving a frozen agent. To address this problem, We propose Natural-Language Policy Gradients (NLPG), an external policy-memory method for improving a fixed agent without changing its model parameters or program structure. NLPG diagnoses execution traces, propagates downstream feedback backward through the module graph, and converts recurring failures into route-local natural-language corrections that are aggregated into bounded policy updates for subsequent executions. Across six benchmarks covering memory, reasoning, instruction following, and evidence verification, NLPG also outperforms the strongest listed baseline for each benchmark by 8.71 percentage points on average. These results provide evidence that evaluated procedural experience can be transformed into local and interpretable policy updates, enabling continual improvement of frozen agents.

---


### 376. [From Position Risks to Block Survival: Faster Generation for Diffusion Language Models](https://arxiv.org/abs/2609.33390)

**<font color=#1a73e8>作者：</font>** Siwei Chen, Yuxiang Wan, Yifan Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) can accelerate generation by predicting multiple tokens in parallel, but there is a mismatch between how these tokens are predicted and how they ultimately contribute to generation. Parallel predictions can hardly condition on the tokens selected earlier within the same block, even though their validity depends on this realized prefix. Under the popular proposal-verification decoding, this mismatch makes errors highly asymmetric: an early rejection prevents all subsequent proposals from contributing decoding progress. We introduce BRISK-DLM, a framework that addresses both mismatches by optimizing proposal learning and selection for verified progress. BRISK-DLM trains on self-generated sequences, using risk-reward weighting to dynamically prioritize positions by their impact on verified progress and decoding cost. During inference, a lightweight prefix-conditioned corrector reranks existing candidates using previously selected tokens and preferences distilled from the model's own verifier. The corrector reuses the backbone's parallel representations and requires no additional backbone evaluation, while fused execution keeps its overhead small. BRISK-DLM improves end-to-end throughput by up to 37.4% while preserving task quality, establishing a new quality-throughput frontier for DLM generation.

---


### 377. [Beyond Timestamps: Decision-Aligned On-Policy Distillation for Long-Horizon Agents](https://arxiv.org/abs/2609.33391)

**<font color=#1a73e8>作者：</font>** Mingju Chen, Can Lv, Jinrong Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) often relies on sparse outcome rewards, providing coarse supervision for long-horizon agents. On-policy self-distillation (OPSD) complements this signal with dense privileged feedback. However, we identify \emph{Decision--Timestamp Mismatch}: privileged guidance may be misaligned with the student's functional decision because the corresponding decision can occur at a different timestep, while the student's decision itself may span multiple timesteps rather than being tied to a single timestamp. Thus, timestamp-local supervision can misalign both the context and the temporal scope of credit. To address this mismatch, we introduce \textsc{AlignOPSD}, following the principle of aligning supervision before assigning credit. Decision-Aligned Supervision Rectification re-scores the same student-sampled response in functionally matched contexts across sibling rollouts to calibrate local teacher evidence. Semi-Markov Hierarchical Credit Assignment then derives variable-duration decision spans from correspondence changes and uses rectified evidence to allocate outcome-grounded credit across spans and their constituent turns. We evaluate \textsc{AlignOPSD} with Qwen2.5-3B and Qwen2.5-7B on ALFWorld, WebShop, and Search-QA against representative baselines. \textsc{AlignOPSD} outperforms both GRPO and StepOPSD across all eight backbone--aggregate-metric comparisons, improving on GRPO by 5.5--8.7 \% and ranking first in six. Additional analyzes examine the two alignment stages and hyperparameter sensitivity between tasks. Our code is avaliable at this https URL

---


### 378. [Preserving Morphemes: Morphology-Guided Pre-Tokenization for Nepali](https://arxiv.org/abs/2609.33395)

**<font color=#1a73e8>作者：</font>** Kalash Shrestha, Nikhil Pradhan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A byte-level BPE vocabulary learns each inflected form of a Nepali word as a separate string, so a noun stem is spelled differently in each of its case-marked forms. We test whether splitting words into stem and affixes before BPE helps, with the corpus, vocabulary size, model and number of training steps held fixed. Our pre-tokenizer, Papaya, uses a finite-state transducer built from a published grammar of Nepali, falls back to regular expressions, and leaves the BPE trainer unchanged. On 607 words annotated by seven native speakers its segmenter reaches 0.96 boundary F1, and the resulting tokens keep stems intact far more often than plain BPE does. In a 17M-parameter language model it lowers bits per byte by about 1% at equal training steps; most of the larger gain seen at equal epochs comes from the extra steps that longer token sequences buy, and an unsupervised Morfessor segmentation gives the same improvement. Downstream the effect is small: NER improves only on entities that contain words unseen in training, POS tagging and news classification do not change, and published Nepali tokenizers perform about as well. We release the annotated boundary set, a 556-affix dataset and the code.

---


### 379. [CoViST: Visual Token Compression via Composable States](https://arxiv.org/abs/2609.33397)

**<font color=#1a73e8>作者：</font>** Qi Zhang, Xiandong Meng, Ronggang Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Visual token compression lowers the inference cost of vision--language models by representing images with fewer tokens. However, most existing methods compress visual tokens to a reduced set, leaving the amount of visual evidence represented by each token and its original spatial context implicit. Therefore, the compressed representation does not explicitly encode how much visual information each representative carries or where it lies in the original image. This limitation arises even after a single reduction and becomes more pronounced when compression is repeated across decoder layers. To address this issue, we propose CoViST, a training-free framework that represents a compressed image as a composable visual state. Specifically, the state combines representative features with original positions, effective contribution weights, and reusable selection metadata. CoViST constructs this state through coverage-guided selection and conservation-based contribution composition, and explicitly incorporates its contribution and positional information into decoder attention. Each component of the state retains its interpretation under successive reductions, enabling the same formulation to support both fixed compression before prefill and progressive compression within the decoder. Experimental results on seven LLaVA-1.5-7B benchmarks show that CoViST-Fixed retains 99.9\%, 99.5\%, and 98.1\% of uncompressed performance at 192, 128, and 64 tokens, respectively, and CoViST-Pro retains 99.8\%, 99.9\%, and 99.1\% at the corresponding layer-average budgets, outperforming state-of-the-art methods under their respective budget settings. Code will be released publicly.

---


### 380. [COEVO: Co-Evolving Context and Parameters for Recursive Self-Improvement](https://arxiv.org/abs/2609.33398)

**<font color=#1a73e8>作者：</font>** Siwei Chen, Xinping Bao, Xinyu Cai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement (RSI) seeks to move large language models beyond static training pipelines toward systems that can participate in improving their own future behavior. Existing approaches largely follow two directions: updating model parameters through online learning, or improving the external context through search, reflection, and prompt optimization. Although both mechanisms can support continued improvement, they are typically studied independently. This separation overlooks an important interaction: the context shapes the experience from which a model learns, while an evolving model may interpret and utilize the same context differently over time. We therefore formulate RSI as a problem of parameter--context co-evolution, where model parameters and the learning context adapt within a shared feedback loop. We introduce COEVO, a framework that updates model parameters from on-policy experience while adapting contextual guidance according to the state of the evolving policy. Policy entropy and prompt-conditioned attention are used as complementary signals to guide this adaptation. Experiments show that COEVO consistently improves task performance over fixed-context reinforcement learning and produces policies that are more robust to changes in system prompts. More broadly, our results suggest that external context should be viewed not merely as a fixed interface to a large language model, but as an adaptive component of recursive self-improvement.

---


### 381. [Evaluating System One Models for Agent Security Decisions: Reliability, Calibration, and Selective Automation](https://arxiv.org/abs/2609.33401)

**<font color=#1a73e8>作者：</font>** Yixuan Liu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Model-based judges support agent security by detecting prompt injections, assessing interaction risks, and screening harmful requests. System One models expose typed decisions with probabilities that software can use to allow, block, or escalate inputs, but whether these probabilities support reliable automated security decisions remains unclear. We evaluate Jev, Laya, Decider, and Bespoke Nimble against specialized classifiers and language-model judges, examining decision accuracy, probability calibration, and selective automation. We identify three main findings. (1) Strong overall performance and favorable average calibration can hide systematic failures on particular attack groups, including attacks that models confidently classify as safe. (2) Under strict limits on missed attacks, the evaluated policies allow few inputs automatically, and choosing separate allow and block thresholds increases automation mainly by blocking more inputs. Even policies that meet error limits during validation can exceed them on unseen inputs. (3) A second judge can detect some missed attacks, but it may also reject more benign inputs and repeat the first model's high-confidence errors. These findings show that model accuracy, probability calibration, and the behavior of the resulting decision policy must be evaluated together.

---


### 382. [DataMagic: Authoring Data Videos through Declarative Multi-Agent Orchestration](https://arxiv.org/abs/2609.33403)

**<font color=#1a73e8>作者：</font>** Yupeng Xie, Zhenyang Wang, Liangwei Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Data videos communicate data insights through dynamic charts, voice narration, and synchronized animations, and have become a widely adopted form of data storytelling. However, producing them requires expertise in data analysis, narrative design, and video editing. Static visualization tools lack narrative and animation capabilities; authoring tools rely on pre-prepared charts rather than raw data; and pixel-level models generate videos end-to-end but cannot guarantee data accuracy or provenance. End-to-end automatic generation faces two core challenges: how to uniformly represent charts, narration, and animations together with their temporal relationships, and how to efficiently search a vast design space for narrative-coherent compositions. We present DataMagic, which authors data videos from raw tabular data through declarative multi-agent orchestration. First, the declarative specification DVSpec unifies charts, narration, and animations with data-bound references and declarative synchronization, ensuring data provenance and automatic audio-visual alignment. Second, a "Generate-then-Orchestrate" multi-agent strategy generates candidate scenes in parallel and then optimizes narrative coherence through global orchestration. DVSpec provides a shared state for three complementary interaction modes, bridging full automation with fine-grained human control. Evaluations on 109 real-world samples show that even the most advanced LLM (e.g., GPT-5) achieves only 2.13/5 with execution success rates between 48.62% and 86.24%; DataMagic improves quality to 3.89 (+83%) with success rates above 95%, with the most significant gains in animation and narrative dimensions. A user study shows that, compared to a conversational LLM workflow, DataMagic improves creation efficiency (79.7% reduction in task time) and reduces perceived cognitive load. Project page: this https URL.

---


### 383. [Decoupling Token Roles in Autoregressive Pretraining](https://arxiv.org/abs/2609.33405)

**<font color=#1a73e8>作者：</font>** Suqin Yuan, Runqi Lin, Kevin Qinghong Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive pretraining increasingly draws on heterogeneous data, making it important to understand how a model learns from an individual token. The next-token prediction objective naturally identifies a token's contribution with its own loss. However, each token is not only a prediction target but also context for what follows. Using controlled corruption, we decouple these two roles and find a reversal: making a noisy token easier to predict reduces its damage as a target but increases it as context. The same decoupling helps explain text generated by language models: generation selects each token by its fit to the prefix, while its role as context is never tested against an independently determined continuation, because that continuation is generated to fit it. At known corrupted positions, acting through the context can reduce damage that removing the token's own loss does not. Understanding and controlling what a model learns from a token therefore requires decoupling its roles.

---


### 384. [Dense Is Not Enough: Hierarchical Supervision Allocation for Long-Horizon On-Policy Distillation](https://arxiv.org/abs/2609.33409)

**<font color=#1a73e8>作者：</font>** Yuhao Sun, Binrui Wu, Zhuoer Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) transfers the capabilities of a large language model to a smaller student by providing teacher supervision on the student's own rollouts. In long-horizon agentic tasks, however, uniform token-level matching can allocate supervision poorly: a large local discrepancy need not improve future behavior, while consequential guidance may be beyond the current student's reach or fail to persist without privileged input. We formulate long-horizon OPD as hierarchical supervision allocation and argue that productive guidance lies at the intersection of future utility and current learnability. Crucially, this intersection evolves as the student learns. Based on this principle, we propose LENS-OPD, a coarse-to-fine framework that organizes supervision through Locate, Validate, and Refine. Locate adapts trajectory exposure to the student's evolving competence and proposes a candidate decision for intervention. Validate tests whether teacher guidance at that decision improves the same student's subsequent behavior. Refine internalizes the beneficial guided behavior into the deployable policy and concentrates token-level supervision on decisive teacher-student conflicts within the validated turn. These stages are nested: each finer allocation is conditioned on the coarser decision, rather than being optimized as an independent importance score. Experiments across multiple long-horizon agent benchmarks and student-teacher configurations show that LENS-OPD consistently improves task performance over vanilla OPD and strong curriculum- and selection-based baselines. Our results suggest that effective long-horizon distillation requires teaching at the right depth, the right decision, and the right token.

---


### 385. [FoldAttention: Declared-Reference Softmax for Fast Decode and Deterministic Backward](https://arxiv.org/abs/2609.33410)

**<font color=#1a73e8>作者：</font>** Sriman Achanta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive decode repeatedly streams a growing KV cache, making attention a major cost at long context. Existing high-performance kernels use online softmax, which discovers a row's normalization reference as it scans keys. Earlier contributions therefore remain provisional and may require rescaling. We argue that the reference need not be discovered: softmax is invariant to a common shift, so the reference only has to keep the weights in range. We present FoldAttention, an additive formulation of softmax attention that fixes a finite reference $Z_i$ before scanning the KV cache. Each weight $2^{s_{ij}-Z_i}$ is then final when computed, so contributions add across disjoint key ranges and their quotient equals softmax attention in real arithmetic. We use this property to develop two techniques for Hopper decode: (1) final weights gate key and value reads before the bytes are fetched, and a per-call depth $T$ cuts keys below $2^{-T}$ while keeping their mass, and (2) additive partials compose split KV and shared-prefix cascades without rescaling. On H100 at $T=16$, FoldAttention decodes seven real-model generations 1.36-2.30$\times$ faster than the fastest BF16 baseline, and up to 3.09$\times$ faster across MHA and GQA shapes, at an error within 1.5% of the lowest BF16 error on six of the seven; reading every key, it is 1.14-1.30$\times$ faster at matched error. We validate on Qwen3-8B that a whole decode step is up to 1.46$\times$ faster while likelihood and long-context accuracy match those under BF16 kernels. The same principle makes the backward deterministic: CTAs round bounded partial gradients onto an integer grid declared before the reduction and add them in any order. FoldAttention thereby removes the determinism tax: its deterministic backward is up to 1.84$\times$ faster than deterministic FlashAttention-3/4 and 1.05$\times$ faster than the fastest nondeterministic kernel.

---


### 386. [MetaBench-Harness: Unlocking End-to-End Optimization of Benchmark Harnesses](https://arxiv.org/abs/2609.33411)

**<font color=#1a73e8>作者：</font>** Xuanjun Chen, Hua-Hsuan Chen, Wei-Chung Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rapid progress in Large Language Models (LLMs) is saturating static benchmarks faster than they can be designed. While existing automated evolution frameworks attempt to generate harder questions by perturbing individual tasks, they remain constrained by rigid, hard-coded generation rules. Moving beyond the evolution of isolated tasks, we propose to optimize the benchmark generation workflow itself end to end with MetaBench-Harness, a dual-loop search framework. Specifically, the inner loop utilizes a benchmark harness to generate a new benchmark in each round, while the outer meta-harness orchestration layer iteratively refines and searches over harness implementations based on historical evolution trajectories. By applying MetaBench-Harness to the competitive programming CodeContests and Olympiad mathematics AIME-2024 datasets, we demonstrate that the evolved benchmarks are challenging and discriminative for frontier models. Trajectory and quality analyses verify that MetaBench-Harness enables multi-dimensional evolution, steadily improving evolution reasonableness, benchmark competency, and evaluator robustness across successive rounds. Furthermore, case studies reveal its effective utilization of diverse difficulty levers to reframe problems and elevate required capabilities. Ultimately, this work provides a solution to the pressing challenge of benchmark saturation.

---


### 387. [Resolving State-Representation Mismatch: State-Space Visual Reasoning for Open-Loop VLA Planning](https://arxiv.org/abs/2609.33412)

**<font color=#1a73e8>作者：</font>** Junhao Xiao, Haoxiang Zhao, Menghao Fang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite rapid progress in vision-language-action (VLA) models, existing reasoning paradigms still face a fundamental \emph{state-representation mismatch} in open-loop planning. Given only an initial observation, models must internally simulate action-conditioned state transitions, whereas text-, pixel-, and latent-space reasoning can suffer from lossy spatial compression, error-accumulating visual generation, and bypass of intermediate latent tokens, respectively, undermining reliable long-horizon planning. We propose \textbf{State-Space Visual Reasoning} (SSVR), which decouples static visual context, language constraints, and a recurrent latent state. SSVR encodes the initial image and instruction once, then conditions each action prediction on the latent state and updates it with an action-conditioned GRU. Using Qwen2.5-VL as the backbone, SSVR achieves 99.5/99.6, 96.3/98.0, and 83.9/90.6 EM/PR on FrozenLake, Maze, and MiniBehavior, substantially outperforming prior methods. Extensive experiments support the effectiveness of recurrent state modeling for VLA open-loop planning across input transformations and transfer settings. By reusing static visual-textual context and updating a compact recurrent state, SSVR supports efficient multi-step inference, achieving up to $98.58\times$ faster Maze decoding rollouts than the evaluated baselines with the prefix cache prebuilt.

---


### 388. [TTRSD: Test-Time Reinforcement Learning with Self-Distillation for Vision-Language Models](https://arxiv.org/abs/2609.33414)

**<font color=#1a73e8>作者：</font>** Shuning Wang, Zhiheng Wu, Xun Zhou 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time reinforcement learning enables vision-language models (VLMs) to adapt using unlabeled inputs. However, repeated sampling under fixed visual conditions can reinforce shared perceptual errors, while sequence-level rewards fail to isolate visual perception the foundational bottleneck that anchors multimodal reasoning risking the degradation of pre-trained reasoning capabilities. We propose TTRSD, a test-time reinforcement learning framework combining multi-view answer-level self-distillation with visual contrastive token selection. A shared policy aggregates teacher predictions across original, cropped, and downsampled views into an answer distribution. Student trajectories generated from the original image receive rewards based on the support for their final answers in this distribution. To allocate this feedback precisely toward perceptual bottlenecks, we compare the log-probabilities of the same sampled tokens under original and visually ablated inputs while holding their textual prefixes fixed, selecting visually sensitive positions for policy-gradient updates. TTRSD separates update direction, determined by group-relative advantages, from update position, determined by visual sensitivity, without requiring ground-truth labels, external verifiers, or a separate teacher. With only 20 unlabeled adaptation samples, TTRSD improves performance across seven benchmarks and three VLMs, raising InternVL3-2B's MMMU accuracy from 35.79% to 49.32%(+13.53%), demonstrating cross-dataset generalization while preserving inherent reasoning integrity.

---


### 389. [APEX: An Extensible Model for Agent-Assisted Production Scheduling](https://arxiv.org/abs/2609.33430)

**<font color=#1a73e8>作者：</font>** Felix J. Grumbach, Stefan Görlitz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Production scheduling requires realistic models that reflect operational constraints and efficient methods that balance competing goals. Putting these methods into use also requires data integration, model adaptation and specialist expertise. We present APEX, an extensible production scheduling framework built around a general model and hybrid multiobjective search. Agent assistance supports both scheduling and model refinement: agents prepare data and explore scenarios in natural language, while coding agents help implement and test new constraints and objectives. Shared construction and checking procedures connect these adaptations to the scheduling core. We benchmark eight APEX configurations against NSGA-II, SPEA2, MOEA/D and SMS-EMOA on 69 public job-shop, flexible job-shop and permutation flow-shop instances, assessing workload completion time (makespan), total job flowtime and computation time. Hybrid configurations achieve the best aggregate solution quality, although the leading method depends on the problem class and objective. A separate synthetic workflow study uses OpenAI's GPT-6-astra as an interaction layer between the human planner and the algorithmic core, testing rule additions, plan and objective changes, and what-if comparisons. All 24 sessions completed the requested changes and passed independent checks of saved models and schedules. A separate coding evaluation produced six native implementations of an additional objective or hard constraint through predefined extension hooks. All passed independent checks without modifying the core.

---


### 390. [MoGround: Measuring and Mitigating Modality Distraction in Vision-Language Models](https://arxiv.org/abs/2609.33431)

**<font color=#1a73e8>作者：</font>** Luca Zhou, Bo Zhao, Rose Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We release MoGround, a vision-language dataset spanning four visual domains in which the answer to every question is guaranteed to be available from exactly one modality. This guarantee enables us to measure modality distraction, the failure in which a model answers a question correctly from one modality alone and then flips to a wrong answer once irrelevant content from the other modality is added. Existing probes rarely establish single-modality answerability this way, making it hard to isolate distraction in the first place. Across seven open-source VLMs, we find that modality distraction is not universal but model-dependent. The weaker-grounded modality is the more distracted one (r = +0.86), and distraction scales inversely with grounding strength (r = -0.90). The single-modality guarantee also enables a mitigation method that needs to distinguish between relevant and irrelevant context. Trained on one split of MoGround alone, a weight-space robustness vector reduces distraction on all seven models by 9% to 51%, at a cost of only 0.1 average points of accuracy on standard multimodal tasks.

---


### 391. [SchemaMem: Schema-Indexed Recurrent Memory for Delayed State Retrieval](https://arxiv.org/abs/2609.33436)

**<font color=#1a73e8>作者：</font>** Sungwoo Goo, Hwi-yeol Yun, Sangkeun Jung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention provides direct access to past representations, but retaining an ever-growing history is costly. Recurrent models bound persistent state, yet must preserve selected information while processing subsequent inputs. We introduce SchemaMem, an attention-based recurrent memory architecture combining chunk-local attention with a persistent, schema-indexed phase state. Learned schema embeddings provide a shared representational reference for reading and writing. Reads use the current state, whereas writes use the layer input and static schema embeddings, excluding direct feedback from that layer's own state. Chunk-boundary commits aggregate bounded phase increments through forward computation. The same parameters also support full-history attention training before and during recurrent training. We studied selective updates, preservation, and delayed retrieval in a controlled address--value task, comparing three-layer models with approximately matched parameter counts and persistent-state dimensions. Across nine address/value settings and three training seeds, SchemaMem has higher mean written-value retention at four times the maximum training delay than both baselines, which are trained toward a higher in-range accuracy target. Updated-value recovery favors SchemaMem in all nine settings against Mamba-3 and seven against Gated DeltaNet. Defaults consistently favor Gated DeltaNet over SchemaMem at that delay, and SchemaMem requires substantially more optimization steps. These results identify a promising retention--optimization trade-off in schema-indexed recurrence.

---


### 392. [Raven: The Harness of Harnesses for Composable Agentic Intelligence](https://arxiv.org/abs/2609.33439)

**<font color=#1a73e8>作者：</font>** EverMind AI  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models advance, AI agents are moving beyond isolated, domain-specific tasks toward long-horizon, cross-domain workflows. This transition exposes two challenges: increasing harness complexity makes manual design difficult to scale, while tighter coupling to specific domains limits the generality of a single harness. The central question thus shifts from how to engineer a stronger harness for one domain to how to autonomously construct specialized harnesses, improve them through experience, and orchestrate them across domains. We introduce Raven, \emph{The Harness of Harnesses}, an open-source multi-agent ecosystem that automatically constructs and evolves modular harnesses for specific models and domains, treating each executable model--harness pair as a composable unit of intelligence. To support an \emph{All-Domain Collaboration Network}, its Host Agent decomposes goals, matches subtasks to specialized agents, coordinates execution dependencies, and integrates results, while a host archive and EverOS preserve experience across tasks and Skill Forge makes that experience available as reusable procedures. Our theory establishes sufficient conditions for such composition to expand reliable task coverage beyond that of the available individual agents under a shared resource budget. On complex and long-horizon tasks, Raven significantly outperforms the state-of-the-art agent systems, pushing the frontier of composable agentic intelligence.

---


### 393. [Context Spanning: A Communication Framework for Full-Duplex Speech Models and External LLM Backends](https://arxiv.org/abs/2609.33443)

**<font color=#1a73e8>作者：</font>** Seonghyeon Go, Yongwoo Kim, Hyeonjin Cha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Full-duplex spoken dialogue models can listen and speak simultaneously like the real-time dynamics of human conversation. For natural dialogue, the ability to search for external information in real-time is also an important capability. Many models remain trapped in parametric knowledge, leaving them unable to access real-time information and tool execution. Furthermore, even when Large Language Models (LLM) retrieve information, many duplex speech models process it within a compressed latent space rather than in its raw text form, which can lead to information loss from compression. To address this issue, we propose Context Spanning, a framework for information injection between a full-duplex speech model and an external LLM backend via real-time chunked prefill. The injected frame is encoded in a single forward pass inside the real-time frame budget. It feeds the retrieved information to the speech model as-is, enabling it to reason over the information independently and generate responses. With this approach, our model achieves high performance on Full-Duplex benchmarks and strong results on Question Answering tasks, demonstrating its conversation potential. Context Spanning shows that external information can be injected directly into a duplex speech model, introducing a new simple and powerful mechanism for duplex systems.

---


### 394. [HESP: Separating What to Probe from When to Stop in Local LLM Alert-Triage Agents](https://arxiv.org/abs/2609.33446)

**<font color=#1a73e8>作者：</font>** Zhuowen Liu, Zhixuan Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security operations centers receive far more alerts than analysts can investigate, and organizations that cannot send their telemetry to hosted models must automate triage with small open-weight LLMs on their own hardware. Current LLM agents leave the investigation procedure to the model, and small local models fail at it: they probe without converging, never commit to a verdict, or dismiss real attacks. In this paper, we present HESP, a controller that holds the investigation procedure outside the model. HESP keeps a ledger of competing explanations, selects read-only probes by expected information gain per cost, accepts only verdicts backed by current evidence, can end an investigation itself, and journals every prediction before its observation. We evaluated HESP in four pre-registered studies with five open-weight models from two families (7B to 72B), totalling 7,272 audited episodes in a controlled triage environment. With likelihood tables counted from LLM-free runs, HESP lifts Qwen2.5-7B from 0.125 to 1.000 verified completion, matching oracle tables. The information-gain ranking adds +0.26 to +0.35 on every model that concludes, and a controller-side stop lifts Llama-3.1-8B, which never concludes on its own, from 0 to 0.917. What to probe and when to stop are therefore separate failures, and different small models exhibit different ones. Because HESP and its planner run entirely on local hardware, it suits environments where telemetry cannot leave the premises. We release all code, protocols, and episode journals at this https URL.

---


### 395. [A Visual Classification Dataset and Model Evaluation for Historical Manuscript Illustrations](https://arxiv.org/abs/2609.33449)

**<font color=#1a73e8>作者：</font>** Yoav Evron, Michal Bar-Asher Siegal, Michael Fire  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Historical manuscript illustrations preserve rich visual evidence of past cultures. They depict people, animals, plants, diagrams, music notations, and decorative forms. Although large digitization projects have made many manuscripts available online, the material itself remains difficult to explore at scale. Extraction systems can find illustrations on manuscript pages, but without meaningful categories, large collections remain hard to search and explore. We address this gap by introducing a manually labeled dataset of 15,000 illustrations from manuscripts dating back hundreds of years across 22 categories, and evaluating modern vision models for image classification on this task. The problem is challenging due to stylistic diversity, degradation, and semantic ambiguity, with many images that fit more than one category. We compare fine-tuned CNN and Transformer-based classifiers, zero-shot CLIP, embedding-based classifiers, and direct vision-language models. Results show that fine-tuned image classifiers perform best overall, with ConvNeXt reaching 88.9% accuracy and 81.3% macro-F1. Using CLIP embeddings with XGBoost provides a strong alternative. In contrast, zero-shot CLIP and direct vision-language classification perform substantially worse, highlighting the limits of general-purpose models in this domain. Beyond overall performance, the analysis reveals which categories are visually separable and where errors reflect genuine semantic overlap, suggesting that some limitations arise from the taxonomy itself.

---


### 396. [Native Association: Confidence-Aware Human Perception in the Wild with a Foundation VLM](https://arxiv.org/abs/2609.33450)

**<font color=#1a73e8>作者：</font>** Igal Dmitriev, Ofir Liba  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Extracting who is where, on which team, wearing which number from a broadcast frame is typically done by stitching a detector, an OCR engine, and classifiers together -- and the stitching step swaps identities under occlusion. We make association native instead: a 0.77B vision-language model (Florence-2) is fine-tuned to emit all per-person attributes as one grammar-constrained sequence, with each attribute generated inside its owner's block. Output is therefore schema-valid on every frame by construction, and no post-hoc binding step exists to attach a correctly read number to the wrong player: residual misassociation is pure perception error, $\approx4\times$ rarer than zero-shot-prompted frontier APIs' (0.057 vs. 0.21-0.24). On a frozen multi-sport test set, this single pass reaches 0.95 detection F1 (APIs: 0.65-0.75). A single extra forward pass yields a per-field confidence that supports a reject option (jersey precision $0.71\rightarrow0.96$ at half coverage) and routes a training-free zoom-and-re-read for small players. Surprisingly, once the grammar is learned, further parameter-efficient tuning yields no measurable gain under the adaptation configurations we test; the identical recipe on WIDER-Attribute reaches 93.1 mAP given-box, yields the first detection-coupled end-to-end results under its standard test protocol (84.5 mAP), and reproduces the same tuning result. In this regime, the gains live in the structure, not in added weights.

---


### 397. [What Shared Prefixes Hide: Trajectory Dropout for On-Policy Distillation](https://arxiv.org/abs/2609.33455)

**<font color=#1a73e8>作者：</font>** Zzizhuo Lin, Quanling Liu, Yi Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student model on its own trajectories using dense token-level feedback from a stronger teacher model. Since each update is conditioned on the reasoning prefix already generated by the student, the prefix also shapes how effectively teacher feedback is converted into learning. We find that shared prefixes can lead to weak token-level updates, a phenomenon we call Prefix-Induced Supervision Attenuation (PISA). This attenuation arises in two common cases. (i) High student confidence can weaken corrective gradients even when the teacher disagrees. (ii) Tokens that rely on earlier reasoning can receive learning signals as weak as those for simple local continuations. To solve this problem, we propose Trajectory Dropout, a simple training-time intervention that exposes these weakened signals. The student first performs a standard full-context rollout to generate a complete trajectory. During training, we randomly drop a certain proportion of the student's reasoning trajectory, while the teacher continues to observe the complete trajectory for token-level supervision. This intervention strengthens corrections for overconfident predictions and introduces additional supervision at prefix-sensitive positions. Trajectory Dropout consistently improves average performance across teacher--student model pairs of different scales and six mathematical reasoning benchmarks, while also yielding gains on two out-of-domain benchmarks. It can also be flexibly integrated into existing OPD variants with negligible computational overhead, further improving their performance. These results demonstrate that Trajectory Dropout provides a simple mechanism for strengthening token-level supervision across model scales and OPD objectives.

---


### 398. [When Does the Concept of "Dog" Emerge in an Audio LLM?](https://arxiv.org/abs/2609.33458)

**<font color=#1a73e8>作者：</font>** Zhe Wang, Shiqi Liu, Ruiyun Zhong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models answer audio questions, but how they represent auditory semantics and use them in decisions remains unclear, limiting our understanding of response formation. We study dog barking in Qwen2.5-Omni-7B using Jacobian lens (J-lens) readout and directional interventions. We define the dog direction as a J-lens-derived hidden-state vector associated with dog; adding or removing its component modulates dog-related information. We find this information decodable without dog/bark prompt cues or animal-identification requirements. Directional interventions change response tendencies and some final answers, with effects concentrated in late-layer states immediately before generation across species classification, vocalization classification, and sound description. The dog direction shows no comparable advantage over controls in animal/other classification. These results provide causal-intervention evidence that the dog direction affects output scores in a task-dependent manner, most consistently at L22 and L24 immediately before generation.

---


### 399. [SphMind: Towards Robust, Training-Free VLM-based Spatial Reasoning with a 360 Camera](https://arxiv.org/abs/2609.33462)

**<font color=#1a73e8>作者：</font>** Shriram Damodaran, Soumyaratna Debnath, Cheston Tan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omnidirectional or 360 cameras provide embodied AI agents with a holistic, wide field-of-view (FoV) view of their surroundings, motivating the use of Multi-modal Large Language Models (MLLMs) for omnidirectional spatial reasoning. However, most MLLMs are trained on conventional 2D perspective images and struggle with the severe distortions and wrap-around discontinuities induced by spherical geometry. Enabling them to generalize to non-Euclidean 3D spaces without retraining therefore remains challenging. We propose SphMind, a training-free, plug-and-play framework that decouples semantic perception from geometric reasoning. Rather than requiring MLLMs to learn spherical geometry internally, SphMind preserves their semantic capabilities while handling geometry externally. We introduce a Spherical Harmonics-based Spatial Graph (SHSG) that models spatial relationships through equivariant transformations on the sphere, together with Inference-Time Geometric Grounding (IGG), a model-agnostic closed-loop optimization process that aligns MLLM representations with spherical geometric constraints during inference. Experiments on three benchmarks show that SphMind achieves over 21.4% average improvement in directional reasoning on MP3D and Stanford2D-3D, outperforms prompt-engineering baselines by 8.7% on the real-world ODI-Bench, and improves rotational invariance by 5.9% under panorama rotations, without additional training or dataset-specific tuning. In-the-wild evaluations further show that SphMind resolves directional reasoning queries that baseline vision-language models fail to answer correctly.

---


### 400. [Rethinking Token Reweighting for SFT: Suppress, Reverse, and Extrapolate Learned Features](https://arxiv.org/abs/2609.33463)

**<font color=#1a73e8>作者：</font>** Cunchun Li, Haonan He, Yifan Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) learns most aggressively from tokens that the model deems least likely. This helps acquire new behaviors, but also amplifies noisy or conflicting supervision and can overwrite useful pretrained knowledge. Through a unified policy-loss view, we revisit existing token-reweighting methods and show that they assign nonnegative coefficients to demonstrated tokens. Consequently, they can suppress or amplify supervised updates, but cannot reverse harmful features once learned. Moreover, larger training weights do not amount to feature extrapolation, since they change the optimization trajectory rather than scale a fixed SFT direction. We argue that reversal and extrapolation require a stable reference frame defined by a fixed SFT delta. Motivated by this, we propose SCALE (Selective Control of Adaptation via Local Entropy), an entropy-guided adaptation-strength-control method that freezes the pretrained model and the SFT delta and learns bounded token- and module-specific gates by minimizing predictive entropy alone. These gates suppress, reverse, or extrapolate frozen SFT features according to their alignment with entropy reduction. Across Qwen2.5-Math-1.5B, Qwen2.5-Math-7B, and Qwen3-4B-Base, SCALE achieves mathematical-reasoning averages of 37.84, 43.60, and 36.57, exceeding the strongest corresponding baselines while remaining competitive on general-retention benchmarks. It also attains the best average code-generation performance across HumanEval, HumanEval+, and MBPP for all three models. These results suggest that effective SFT correction can benefit from controlling how already learned residuals are used, rather than only modifying how they are learned.

---


> [!TIP]
> 当前位于：**351-400**（第 8/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
