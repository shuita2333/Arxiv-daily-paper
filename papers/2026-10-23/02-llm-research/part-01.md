# 🧠 大模型相关研究 | 2026年10月23日

> 本类共 **204** 篇论文：已确认 **192** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-204](./part-05.md)

---

### 1. [To Keep or Not to Keep: Learning KV Cache Retention in Disaggregated LLM Serving Systems](https://arxiv.org/abs/2610.28637)

**<font color=#1a73e8>作者：</font>** Dong Liu, Yanxuan Yu, Eric Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Disaggregated \textsc{LLM} serving separates prefill and decode across node pools, placing a network fabric between \textsc{KV}-cache computation and consumption. This breaks a key assumption of classical cache policies: a miss no longer incurs only local recomputation, but also network transfer to the decode node. Likewise, admitting a block to the global cache requires an additional transfer, so poor retention decisions waste both memory and bandwidth. We present \textbf{KVLearn}, a learning-based framework for cost-aware \textsc{KV}-cache retention in disaggregated serving. KVLearn includes: (i) a lightweight Prefix Reuse Predictor (\textsc{PRP}) that estimates reuse probability from structural and temporal prefix features without modifying model weights; (ii) a Cost-Aware Retention Score (\textsc{CARS}) that converts reuse probability into keep/admit decisions using recomputation, transfer, and storage costs; and (iii) an Adaptive Threshold Controller (\textsc{ATC}) that adjusts admission thresholds online from observed hit rates and memory pressure. We integrate KVLearn into a globally disaggregated serving topology and evaluate it on text and multimodal workloads, including large image/video-derived \textsc{KV} blocks with heterogeneous reuse patterns. KVLearn reduces end-to-end time-to-first-token by up to 56% versus No-Cache, 38% versus LRU-Pool, and 33% versus Mooncake-style baselines, while cutting inter-node \textsc{KV} transfer volume by up to 53% versus LRU-Pool. On MM-Session, throughput remains within ${\sim}5%$ of oracle. Code is available at this https URL.

---


### 2. [How Far Can the Gemma 4 Speech Encoder Go Without Changing Its Weights? Saudi and Gulf Arabic Speech Recognition with a Frozen and an Adapter-Augmented Encoder](https://arxiv.org/abs/2610.28673)

**<font color=#1a73e8>作者：</font>** Amr Abdelkhalik  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study the 305M-parameter audio encoder shared by Gemma 4 and EmbeddingGemma 2 (identical except for its final projection) for Saudi and Gulf Arabic speech recognition, without changing any of its weights. A frozen system trains only a 22.6M-parameter CTC reader over a mix of encoder layers; an adapted system adds 3.1M low-rank adapter parameters, a 41.5M-parameter hybrid CTC/attention reader and joint decoding with a sub-word language model. Against Cohere Transcribe Arabic (2.07B parameters), re-run on identical audio, the frozen system trails in word error rate (WER) but is statistically indistinguishable in character error rate (CER) on five of six human-labelled conditions, while running 3.4 times faster on CPU with greedy decoding. The adapted system is statistically indistinguishable in WER on a public Saudi customer-service call (19.20% against 19.27%) and on clean Emirati speech, is significantly better on telephone-coded Emirati speech, has a significantly lower CER on all six conditions of these sets, and beats a 0.6B recogniser fine-tuned on SADA in WER on all six; it still trails Cohere in WER on long-form Saudi speech. On a blind, human-corrected public call-centre sample it ranks 4 of 15 systems, behind three commercial APIs (significantly only one) and ahead of the other self-hostable systems by point estimate. An optimised joint decoder runs it at 139 times real time on one GPU. We also show that references made by correcting machine drafts favour the drafting system. Code and public-set results are released.

---


### 3. [A Small Model Asks Better: Fine-Tuning Query Clarification for Retrieval-Augmented Generation](https://arxiv.org/abs/2610.28686)

**<font color=#1a73e8>作者：</font>** Lihong He, Lucian Popa, Marina Danilevsky  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Query clarification is essential for retrieval-augmented generation (RAG) systems that face ambiguous user queries. We consider multi-turn grounded conversational scenarios where a user query is either ill-formed or ambiguous in the context of the prior dialog or, more interestingly, it may be well-formed but when posed against retrieved documents there are multiple relevant interpretations. The task is to recognize both such cases and then generate an appropriate clarification request to the user. We present ClariEdge, a new dataset of approximately 3,900 examples that include such ambiguous queries along with negative examples that do not require clarification. We also show that a lightweight fine-tuned LoRA achieves 96.6% classification accuracy and outperforms prompted baselines of many larger models on both classification and quality of clarification generation. Our study shows that hard negatives are an essential ingredient to separate out queries that are truly ambiguous from queries that may look ambiguous but are not (i.e., can be resolved from the context). The same LoRA achieves high performance in both pre-retrieval and post-retrieval scenarios; thus, it can be used in two places in a RAG pipeline as a check before answer generation. The ClariEdge dataset is available at this https URL.

---


### 4. [SpecEvo: Speculative Evolution with Large Language Models for Cost-Efficient Scientific Discovery](https://arxiv.org/abs/2610.28706)

**<font color=#1a73e8>作者：</font>** Ha Minh Hieu, Tongyao Zhu, Do Xuan Long 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-driven evolutionary search is a promising paradigm for scientific discovery, but existing methods remain costly and slow, often applying expensive reasoning uniformly while underusing evidence from failed, redundant, and saturated trials. We introduce Speculative Evolution (SpecEvo), a multi-LLM framework that coordinates lightweight and frontier models through continual consolidation of search evidence. Lightweight models power both parallel Speculators, which generate and refine candidate programs, and an Advisor, which distills accumulated successes, failures, and saturated directions into persistent guidance for subsequent exploration. At sparse checkpoints, a frontier-model Navigator inspects the evolving population and intervenes through synthesis, surgical refinement, or reframing according to search stagnation. This speculate-then-consolidate workflow delegates routine exploration and evidence consolidation to inexpensive models while reserving frontier reasoning for strategic interventions whose benefits extend across many subsequent low-cost evaluations. Across 176 tasks spanning four scientific and algorithmic discovery domains, SpecEvo matches or outperforms frontier-model baselines while reducing API cost by up to 80%, achieves up to 1.5x greater evaluation efficiency than cost-efficient baselines on equation discovery, and improves over the strongest CO-Bench baseline by 3.8%. These results support trajectory-conditioned model coordination as an effective approach to cost-efficient scientific discovery.

---


### 5. [SimHack: Predicting the onset of detectable reward hacking before RL training](https://arxiv.org/abs/2610.28707)

**<font color=#1a73e8>作者：</font>** Junwei Deng, Alex Bie, Natalia Ponomareva  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When training LLMs to code with reinforcement learning, reward hacking is often detectable but difficult to prevent, since (a) environment hardening is increasingly difficult as training environments grow more complex; and (b) training-time interventions incentivize models to obfuscate hacking behavior to bypass detection.
We instead study whether we can predict when detectable reward hacking becomes dominant before executing an RL run, enabling us to select lower-risk recipes in advance. We find that the initial hacking rate alone does not determine onset, which varies substantially across training recipes and repeated runs. We thus formulate this problem as predicting the distribution of the reward hacking onset step under a target training recipe.
We introduce SimHack, a simulator that learns reward hacking training dynamics from a handful of smaller-scale reference RL runs and generates counterfactual simulation runs of unseen target recipes without costly retraining. Across unseen target recipes, SimHack predicts the median onset to a relative error of 11.3% and achieves across-recipe rank correlation of 0.85, while generalizing to differences in model scale, curriculum, number of rollouts, and learning rate between reference and target recipes. As an application, we show that SimHack can guide training decisions by screening candidate RL curricula, discovering curricula over the same set of scenarios that train for 96.6% longer without hacking.

---


### 6. [STAR-XPC: Set Transformer for Estimating X-ray Transmission in Polymer Composites](https://arxiv.org/abs/2610.28709)

**<font color=#1a73e8>作者：</font>** Can Erer, H. Birkan Yilmaz, Nebahat Aral  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluating the energy transmission ratio of an X-ray beam through a polymer composite is a challenging task in radiation shielding studies. The reference solution with Monte Carlo transport simulation is highly accurate but computationally expensive: each of our reference simulations is capped at $4\times10^9$ photon histories and a 20,000 s (over 5 hours) time limit, while closed-form analytical methods fail to represent such complex scenarios. We present an artificial neural network model that maps the unordered multi-set of molecular constituents, their mass fractions, and four bulk physical descriptors directly to the transmission ratio $I(t)/I_0$ in 1-3 milliseconds. The model is a Set Transformer, which makes it permutation invariant by construction and accepts mixtures of different sizes up to 11 constituents within a fixed-size padded set. Each constituent is embedded with a chemistry-pretrained transformer language model, ChemBERTa. In our proposed method, training data are produced by an automated PENELOPE/penEasy pipeline using the radiation source at 30, 80, 100, and 120 kV tube voltages over polyethylene-based shielding composite slabs of thicknesses spanning 0.15-2.5 mm. After preprocessing, the dataset contains $n = 4697$ simulated configurations on which a leakage-free, jointly stratified 10-fold cross-validation is performed, attaining mean squared error MSE = $(1.12 \pm 0.56)\times10^{-4}$, normalized-MSE percentage NMSE% = 0.0294% $\pm$ 0.0147%, and $R^2 = 0.9988$. The corresponding per-sample percentage errors give an alpha-trimmed ($\alpha = 0.10$) absolute percentage error (APE) of 1.66% and a median APE of 1.15%. Our model's inference is several orders of magnitude faster than the underlying Monte Carlo simulation (sub-millisecond per query vs. several hours for the reference run) with effective accuracy in predicting $I(t)/I_0$.

---


### 7. [Big Claims, Small Margins: Do Reported GraphLLM Gains Survive Simple Baselines?](https://arxiv.org/abs/2610.28714)

**<font color=#1a73e8>作者：</font>** Michal Podstawski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-based methods for node classification on text-attributed graphs (TAGs) routinely report state-of-the-art accuracy. We ask how these results compare with inexpensive baselines run on the same splits. On the splits of three recent studies, we tune four baseline representatives with validation-only selection and compare them with the highest mean that each paper reports for an LLM-based method in the matched setting. Correct & Smooth on TF-IDF features trails this reference by a median of 2.3 percentage points, and an MLP on frozen e5-large-v2 embeddings by 2.8 points. Correct & Smooth is within 3 points of the reference or better on 15 of 24 tasks, but the reference is significantly higher on 12 of 22 testable tasks, so several reported gains remain substantial. Reading released code next to the papers, we also document evaluation risks: selection of hyperparameters or checkpoints on the test set, labels of test-pool nodes used in training, baseline numbers reused without disclosure, and a text-label misalignment in a released Cora loader. Reports of the same method on the same split also differ by up to 12.5 points across papers whose configurations are not documented to match.

---


### 8. [Automating ML for Science: Can Frontier Agents Climb Scientific Hills in the Wild?](https://arxiv.org/abs/2610.28763)

**<font color=#1a73e8>作者：</font>** Ming Zhong, Stacy Li, Nicholas Carlini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier coding agents are increasingly framed as end-to-end automated researchers, and ML for science offers a demanding test of that promise: improving a scientific model often requires domain insight beyond routine ML engineering. We introduce Agent4Sci, a long-horizon testbed for measuring how far today's agents can improve the published best models on scientific ML benchmarks, spanning 20 benchmarks across 11 domains. Rather than ranking agents on a leaderboard, Agent4Sci asks what kinds of progress agents can make on these tasks under in-the-wild conditions, and where they fall short. Empirically, today's frontier agents advance the published best on every benchmark, with Claude Opus reaching 10.4% mean relative improvement and no run flagged for academic misconduct. These gains, however, come almost entirely from a bag of ML-engineering tricks rather than research-level insight. Trajectory analysis surfaces three recurring limitations in this setting: novelty miscalibration, resource under-utilization, and rapid collapse into local engineering sweeps. Lightweight plug-in skills for research ideation, experiment management, and scheduled checklists raise Claude Opus from 10.4% to 20.1% and Codex from 4.4% to 8.1%, while yielding more diverse, domain-relevant interventions. Agent4Sci gives the community a way to track and push frontier agents from ML engineering toward domain insight on real-world ML-for-science problems. Code and data are available on GitHub (this https URL) and Hugging Face (this https URL).

---


### 9. [SkillEval: Learning Interpretable Ability Profiles of LLMs via Cognitive Diagnosis Models](https://arxiv.org/abs/2610.28767)

**<font color=#1a73e8>作者：</font>** Berke Arda, Peng Cui, Qiaoyuan Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current evaluation of LLMs on benchmarks typically aggregates performance over individual examples into a single scalar score. This approach is overly coarse and ignores the diverse scope of skills covered by benchmark datasets. To address this limitation and better exploit benchmark data, we propose SkillEval, a new evaluation framework that performs cross-model, skill-level analysis. The framework integrates advances from two areas: (1) it leverages the meta-cognitive capabilities of LLMs to automatically discover interpretable skills from questions, and (2) it applies cognitive diagnosis models (CDMs) from psychometrics to estimate per-skill abilities of LLMs. We conduct experiments on 3,811 LLMs evaluated on 9,523 items across five benchmarks spanning diverse domains (MATH, BBH, GPQA, MuSR, IFEval). Compared to the traditional average-based evaluation paradigm, SkillEval produces reliable, more calibrated and informative yet concise model profiles that more accurately predict model behavior on unseen items. We also demonstrate the utility of SkillEval in two downstream tasks: (1) LLM routing, which dynamically assigns each query to a capable but efficient model, reducing inference cost by over 60% while achieving improved performance, and (2) Computerized Adaptive Testing (CAT), where an unseen model can be efficiently evaluated using a trained CDM. Furthermore, we show that these skill profiles provide useful insights, for example, how benchmarks share skills and how instruction-tuned models differ from their base models.

---


### 10. [ReAPO: Retry-Aware Policy Optimization for Efficient Exploration in LLM Reasoning](https://arxiv.org/abs/2610.28770)

**<font color=#1a73e8>作者：</font>** Nghi Dao, Calder Morton-Ferguson, Noah Golowich 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> RLVR improves language-model reasoning, but commonly relies on independent stochastic rollouts for exploration, which can repeatedly sample similar failed strategies. Prior work has seen success with approaches that guide exploration by introducing dependence into the sampling process by including incorrect solutions in the context for subsequent attempts. Still, these methods introduce the additional question of how to assign credit to each attempt. We propose to view the credit assignment through the lens of Stochastic Shortest Paths, a framework in classical reinforcement learning that seeks to minimize the expected cumulative cost to reach a terminal state (in our case, a verified successful response). We show that, under suitable simplifying assumptions, this perspective naturally leads to a simple modification to GRPO, which we call Retry-Aware Policy Optimization (ReAPO). ReAPO allocates additional generation to failed trajectories, allowing successful retries to be reinforced without rewarding preceding failures, and assigns credit in a theoretically principled way to each attempt. Across Qwen3 and OLMo-2 models from 0.6B to 4B and eight mathematical and scientific reasoning benchmarks, ReAPO improves first-attempt performance over GRPO as well as natural recent baseline algorithms, while additional ablations demonstrate the utility of both serial sampling and ReAPO's credit assignment. On Qwen3-0.6B, ReAPO also outperforms GRPO with twice the group size or twice the training steps, reaching their peak accuracy with 39% and 31% fewer generated tokens, respectively. Taken together, our results suggest that ReAPO is a simple yet effective approach for improving LM reasoning performance through improved exploration and retry-aware credit assignment.

---


### 11. [Scaling Therapy Supervision: Assessing Psychotherapy Fidelity Using Large Language Models](https://arxiv.org/abs/2610.28772)

**<font color=#1a73e8>作者：</font>** Arvind Pillai, Alexis Roach, Jason Holden 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Psychotherapy fidelity assessment measures how faithfully a therapist adheres to a treatment protocol, a critical determinant of positive patient outcomes. However, fidelity assessment is bottlenecked by manual expert review, rendering the process labor-intensive and unscalable. To scale therapy supervision and support clinician self-learning, we present an integrated application of large language models (LLMs) that automates psychotherapy fidelity workflows and generates actionable supervisory feedback from authentic, long-form clinical transcripts. We evaluate three open-weight models across multiple task decomposition configurations and reasoning strategies, demonstrating that evidence-first reasoning improves fidelity estimation. Furthermore, we establish the framework's external construct validity on an independent randomized controlled trial (RCT), where it reliably distinguishes Cognitive Behavioral Therapy (CBT) from non-CBT sessions across core therapeutic skills. Through a user study that evaluates the generated feedback, mental health experts indicate that the pipeline synthesizes actionable clinical feedback. Ultimately, our work offers a practical, scalable solution toward bridging the community mental health supervision gap.

---


### 12. [Building a Nested LADDER for LLM Unstructured Post-Training Pruning](https://arxiv.org/abs/2610.28773)

**<font color=#1a73e8>作者：</font>** Nicolás Mauricio Cuadrado Ávila, Ivo Gollini Navarrete, Martin Takáč 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Non-uniform allocation can improve post-training pruning of large language models, yet quality can still degrade sharply at high sparsity. To control degradation as sparsity increases, we introduce LADDER (Layer-Wise Allocation via Damage-Driven Evaluation and Refinement), which allocates sparsity incrementally. At each step, it evaluates pruning an additional fraction of weights from each eligible layer and commits the layer update that causes the least end-to-end degradation per removed parameter. This process produces non-uniform sparsity profiles and exactly nested masks across multiple budgets. We evaluate LADDER on five OPT, Llama, and Qwen models across 10-90% sparsity, using SparseGPT as its candidate-generation backend and comparing against uniform and adaptive allocation baselines. Results reveal a clear operating-regime trade-off: LADDER is comparable or slightly weaker at benign sparsity but becomes substantially more robust from 70% onward. This high-sparsity advantage largely persists after posterior distillation across four of five models and translates into improved retention of aggregate zero-shot accuracy.

---


### 13. [Complexity-Aware Surgical Video Reasoning Segmentation with Digital Twin and Context Memory](https://arxiv.org/abs/2610.28776)

**<font color=#1a73e8>作者：</font>** Yiqing Shen, Mathias Unberath  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional surgical segmentation relies on closed-set categories or explicit text queries, which cannot resolve implicit queries that require reasoning about workflows, instrument functions, and temporal relationships. To address these limitations, we propose SurgReasonSeg, a complexity-aware method that brings reasoning segmentation over digital twin (DT) representations to surgical video. Specifically, SurgReasonSeg constructs DT representations from surgical foundation models and trains two low-rank adapters (LoRA) of one large language model with reinforcement learning (RL), each specialized for a different query complexity. A lightweight router, also trained with RL, selects between the two adapters to balance latency against accuracy. SurgReasonSeg also sets the temporal context with an adaptive sliding window conditioned on query complexity and workflow phase, and retrieves relevant historical cases from a surgical context memory by workflow similarity and procedural relevance. We further introduce EndoVis-ReasonSeg, a surgical reasoning segmentation benchmark with 1,460 training and 961 test samples across semantic, spatial, and temporal categories. On EndoVis-ReasonSeg, SurgReasonSeg improves J&F over the strongest baseline, ReSurgSAM2, by 0.178, 0.237, and 0.297 on semantic, spatial, and temporal queries, and it also achieves the best results on the Ref-EndoVis17 and Ref-EndoVis18 referring segmentation benchmarks. A backbone-matched attribution protocol separates the contribution of the upstream segmenter from that of the reasoning modules. Our method runs at 18.8 FPS averaged over the query distribution, enabling real-time reasoning segmentation in surgical videos.

---


### 14. [Measure First, Then Allocate: Calibrated Rollout Budgets for MCP Agents in Reinforcement Learning](https://arxiv.org/abs/2610.28785)

**<font color=#1a73e8>作者：</font>** Hieu Tran, Zonghai Yao, Sunjae Kwon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training tool-using language models requires costly interaction, yet identical rewards within a rollout group provide no group-relative learning signal. We use reward disagreement to guide harness evaluation and the allocation of rollouts for policy training in Model Context Protocol (MCP) environments. We first introduce Discord, which tests harness edits using exact paired inference and decision-preserving early stopping: only disagreeing paired outcomes favor one harness over another. This insight motivates prospective allocation in BRACE (Bank-calibrated Rollout Allocation under Correlated Episodes). BRACE combines historical task evidence, uncertainty in task success rates, and a correlated reward model to forecast mixed-reward groups before allocating generation budget. Controlled harness experiments favor Discord, while live MCP experiments expose a retention-cost trade-off. At three Qwen3-VL model scales, BRACE exceeds the strongest plotted baseline peaks with fewer new training rollouts; historical-bank collection is counted separately. It also leads the compared methods on BFCL and NESTFUL without further training. Ablations probe the bank, estimator, and allocation score; prospective evaluation checks forecast calibration. These results support forecasting reward contrast before generation.

---


### 15. [Is Anyone Enforcing the Cartel? What Reinforcement Learning Teaches LLM Agents in Markets](https://arxiv.org/abs/2610.28787)

**<font color=#1a73e8>作者：</font>** Hieu Tran, Hong Yu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluations of large language model (LLM) agents report that pricing agents collude at others' expense. Yet collusion is defined by enforcement: a cartel, in which competitors share monopoly profits, holds only if a member who cheats is punished. We introduce an audit that tests enforcement by forcing a member to cheat in counterfactual copies of a market, and use it to study what reinforcement learning (RL) teaches agents in pricing and trading. Small LLMs trained by RL learn what their training rivals reward, but only what they readily try. In self-play, they learn fixed rules ignoring their rivals; against a punishing rival, to be deterred; against a cheating rival, to match its cuts, never the costly price war that would deter it, which they rarely try. A war forced into training is learned, but mostly only where it was forced. Against their own copies, deterred and matching agents can earn the same cartel profits, but only matching ones can enforce them, and then thinly: as a by-product and only against large cuts. Q-learners enforce collusion only in pricing. Prompted LLMs reach cartel-like outcomes mostly through rules that ignore the market. Outcome measures cannot tell these cases apart; the audit can.

---


### 16. [CALLIOPE: Private Insights into AI Use, Without Embeddings](https://arxiv.org/abs/2610.28797)

**<font color=#1a73e8>作者：</font>** Edith Cohen, Vadym Doroshenko, Badih Ghazi 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce CALLIOPE, a top-down framework for discovering topic hierarchies in large corpora of unstructured data (e.g., LLM conversations), while supporting differential privacy (DP). Unlike traditional and even recent LLM-augmented approaches that ultimately rely on clustering vector embeddings, our framework leverages LLM capabilities directly for the entire pipeline. Experiments demonstrate that this approach provides better utility over existing (embedding-based) methods in the DP setting, especially in the high privacy regime. We evaluate the quality of CALLIOPE outputs using a variety of traditionally studied clustering metrics, as well as some novel utility metrics that we introduce.

---


### 17. [Where Do Legal Factors Live in LLMs?](https://arxiv.org/abs/2610.28799)

**<font color=#1a73e8>作者：</font>** Li Zhang, Kevin Ashley  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In case-based legal reasoning, legal professionals identify legally significant fact patterns in a new dispute and compare them with those of decided cases. In AI & Law, HYPO dimensions and CATO factors represent these patterns symbolically, organizing expert knowledge distilled from case narratives as explicit, structured, interpretable, and auditable legal concepts and relations that support case comparison, legal argument, and precedent-based reasoning. Large language models (LLMs) are increasingly used for legal tasks, yet their internal organization of legal knowledge remains difficult to trace. We investigate whether LLMs form internal representations corresponding to all 26 CATO factors. Two research questions examine linear decodability and sparse localization with sparse autoencoders. Experiments cover three open models, Qwen3-1.7B, Qwen3-8B, and Gemma-2 2B, supported by cross-model comparison and human audit of controlled natural-language passages. Results show that all 26 factors are linearly decodable in all three models. Single-feature sparse readouts cover the complete factor catalog, with best-layer test AUCs ranging from 0.86 to 1.00. Five selected features approach full-vector readout performance. We report 78 model-specific layer-feature coordinates, one for each factor in each model. Together, these results show that information corresponding to expert-defined legal factors can be read from the internal activations of LLMs processing legal narratives. By locating these readouts, our study connects legal language and the symbolic abstractions of HYPO and CATO to learned internal representations.

---


### 18. [JUICE: Unified Multimodal Modeling in Pretrained Representation Spaces](https://arxiv.org/abs/2610.28801)

**<font color=#1a73e8>作者：</font>** Jiahan Li, Huangyuan Su, Shengbang Tong 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most unified multimodal models treat images and text asymmetrically: a pretrained language model generates text, an attached diffusion head generates images, and outputs that contain both are produced in a fixed order, so the first output cannot adapt to the second. We ask whether both modalities can instead be generated by one process that is trained on them jointly from scratch. Pretrained encoder spaces hold both modalities in one continuous form and carry knowledge learned at scale, and recent work finds them effective as generative targets for vision and language. We therefore model the joint distribution directly in these spaces. We introduce JUICE (Joint Unified multimodal modeling In Continuous Encoder spaces), a single flow matching Transformer over frozen image and text representations, in which each modality has its own noise level. Which modalities are clean and which are generated then decides the task: image generation, captioning, visual question answering, or joint generation. Controlled pretraining runs test each design choice. At equal guidance, generating text as continuous states leaves image generation intact (48.41 GenEval, against 47.86 for a model trained only for text-to-image generation), while captions lose some exact wording. Training on joint and conditional denoising together beats either alone, and semantic encoder spaces beat VAE latents and raw pixels as targets. At 2.1B parameters, with no language model initialization and at 224x224, JUICE reaches up to 0.88 on GenEval and 73.1 on VQAv2. By sampling both modalities from the joint distribution (coupled sampling), it can also draw a route on a map while writing out the matching moves. On mazes with several valid solutions, joint success rises from 54.6% with independent sampling to 93.7%, and no modality has to go first. On visual spatial planning, JUICE solves 99.8% of maps at its training sizes.

---


### 19. [How Much Does the Harness Matter, and for Whom? A Multi-Model Study of Context in LLM-Driven Vulnerability Discovery](https://arxiv.org/abs/2610.28802)

**<font color=#1a73e8>作者：</font>** Ganni Galea Curmi, Ben Wilde  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> How much does an agent harness affect vulnerability discovery, and does its value depend on the model? We study 24 model-runner configurations using an open-source harness on a production codebase whose vulnerabilities were non-public at scan time. The pipeline combines static screening, LLM investigation, model self-revalidation, root-cause mapping, independent source review, and isolated proof-of-concept confirmation.
Across 265 confirmed security root causes, the largest two-run configuration covers 60.4%, while 14.3% are found by exactly one model. No single configuration covers all observed findings. In a four-model context experiment, moving from a minimal prompt to an engineered prompt with a CodeQL-derived call graph raises criticality-weighted yield by 20-86% for smaller and mid-tier models, compared with 2% for the frontier model. This comparison changes both prompt and context. Separating those effects shows that the engineered prompt improves yield for all four models, while adding CodeQL context beyond that prompt improves yield only for the smallest model. A held-out CyberGym subset shows the same direction of target-recall improvement for the combined treatment.
Frontier models achieve low false-report rates but do not consistently achieve the highest yield. Strong lower-cost models can deliver similar performance at an order of magnitude lower cost. These results support matching models, prompts, and context to the task, and combining configurations for broader coverage.

---


### 20. [A Mechanistic Study of Automated Failure Attribution in LLM-based Agentic Systems](https://arxiv.org/abs/2610.28811)

**<font color=#1a73e8>作者：</font>** Wendy Zheng, Liang Wu, Yinhan He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic systems have demonstrated strong capabilities on complex tasks by enabling multiple interacting large language model (LLM)-based agents to collaborate and execute subtasks in parallel. However, this collaborative structure introduces new challenges for reliably evaluating and diagnosing system failures, particularly failure attribution: tracing a system's execution to identify the agent step responsible for an incorrect final outcome. Because manually performing this task is time- and labor-intensive, recent work has turned to LLMs as judges to automate the process, referred to as automated failure attribution (AFA). These approaches assume that a sufficiently capable model can infer the failing step directly from an interaction transcript. In practice, however, direct prompting often performs poorly, which motivates follow-up work that explores various ways to improve AFA performance, including alternative prompting strategies and inference-time interventions. In this paper, we examine a more fundamental question: whether this weak behavioral performance reflects a genuine capability limitation. Using linear probes applied to internal activations, we uncover a significant \emph{knows-but-won't-say gap:} models encode sufficient information to attribute a failure correctly but fail to explicitly output the responsible step. Building on this finding, we propose \emph{grafting}, a simple manual intervention that exploits knowledge already encoded in the model to improve AFA performance without requiring ground-truth labels at inference time. Extensive evaluations across multiple LLMs and benchmark settings demonstrate that grafting consistently outperforms direct-prompting approaches, underscoring the potential of leveraging latent model knowledge for more reliable failure attribution. Our code is available at this https URL.

---


### 21. [LIFT: Scoped Constraints for Evaluating and Training Instruction Following](https://arxiv.org/abs/2610.28819)

**<font color=#1a73e8>作者：</font>** Eran Goldstein, Yuval Belfer, Yonatan Belinkov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Common instruction following (IF) benchmarks, such as IFEval, evaluate the ability of language models (LMs) to follow simple constraints that can easily be verified programmatically. These same constraints, in turn, are used as reward signals for reinforcement learning. This design may lead to reward hacking of constraints, pushing models away from the main task. Recent attempts to address this resulted in benchmarks with richer constraints, but required expert labor, remained closed-access, and cannot be easily extended. We present Lift-Bench, an IF benchmark that asks a model to draft a document given a topic and a structured outline. Constraints are scoped to certain document sections, providing finer control over constraint density. Lift-Bench includes both verifiable and judged constraints, as well as a training counterpart, Lift-Train. Importantly, Lift-Bench provides both main task and instruction-following constraints, mitigating shallow reward hacking. On experiments with multiple models, we find that frontier models struggle with the harder subsets of our benchmark and analyze model performance along multiple axes. We also find that training on Lift-Train is much less susceptible to reward hacking than training on the common IFTrain. Lift-Bench and Lift-Train are publicly available, as well as the data generating pipeline.

---


### 22. [A Parallel Multi-Dialect Arabic Dependency Treebank](https://arxiv.org/abs/2610.28823)

**<font color=#1a73e8>作者：</font>** Noor Abo Mokh, Mohamed Adel, Jamila El-Gizuli 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dependency parsing resource development for Arabic has largely focused on Modern Standard Arabic, leaving dialectal Arabic comparatively under-resourced. We introduce MADARTB, the first large-scale parallel dependency treebank spanning five city dialects: Beirut, Cairo, Doha, Rabat and Tunis, and extending an existing parallel MSA version. In total MADARTB consists of 5,000 sentences annotated using the CATiB dependency scheme. We analyze syntactic similarity across all city dialects and MSA. Although global construction profiles exhibit high similarity across varieties, local syntactic structures frequently diverge, revealing substantial structural variation across dialects. We further establish a cross-dialect dependency parsing comparison using a supervised parser and four LLMs. The supervised parser achieves 87.5% LAS, while the best LLM setup trails at 85.7% LAS across all six varieties on the test set. We release our annotations and models publicly.

---


### 23. [Decision language models as affordable and rapid alternatives to LLM judges of clinical generative AI](https://arxiv.org/abs/2610.28826)

**<font color=#1a73e8>作者：</font>** Rotem Gershon, Seffi Cohen, Dean Ariel 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated judges of clinical artificial intelligence (AI) outputs are necessary, but large language model (LLM) judges are costly and slow at scale. We compared Jev, a decision language model that returns structured judgments, with frontier and open-weight LLM judges in four use cases. On 118 pediatric answers, Jev's agreement with physicians' ordinal quality ratings (Gwet's AC2 0.50; expected score 0.53) matched or exceeded that of seven of 12 LLM judges, including frontier models, Claude Opus 5.5 (0.49) and GPT-6 (0.38). On physician-graded binary HealthBench criteria, Jev matched or exceeded four of six LLM judges. On MedHELM's open-ended tasks, Jev's agreement with a three-LLM jury approached or exceeded the jurors' internal agreement. On HealthBench Professional, Jev matched the benchmark's reference judge, GPT-5.4, on 91% of criteria (other judges, 91-93%). Frontier judges cost 73-294 times more than Jev and took 7-57 times longer. Jev may enable efficient clinical AI evaluation at scale.

---


### 24. [Beyond Correct Answers: How Compositional Cues Shape Visual Judgments](https://arxiv.org/abs/2610.28843)

**<font color=#1a73e8>作者：</font>** Xiaoyu Ma, Zheyuan Zhang, Kaiwen Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual question answering requires models to assign attributes and relations to the correct objects, a problem known as visual binding. Structured prompts make these assignments explicit through labeled fields. Yet an improvement from the full prompt does not reveal which labels help or how they interact. First, we isolate field-label effects across ten models and six tasks by holding the image and claim fixed. These comparisons reveal differences that overall accuracy can hide. With a relation label present, adding object-role labels helps Qwen3 but hurts Qwen2 on Spatial. Second, we compare auxiliary hints that preserve or swap the question's role assignments against a no-hint baseline. Across two image sets, Qwen3's advantage with preserving hints mainly reflects errors caused by swapped hints. Preserving hints remain near baseline. Field order further affects the harm. Third, we test clearer hint wording and direct selection of the relation shown in the image. Clearer hints improve text matching but do not consistently improve visual judgments. In contrast, relation selection partly reduces errors for some hints in Qwen3 and GPT-4.1-mini.

---


### 25. [How Much Gradient Does Truncated Backprop Lose in Looped Transformers?](https://arxiv.org/abs/2610.28871)

**<font color=#1a73e8>作者：</font>** Aur Shalev Merin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped transformers reuse one block of layers many times and are often trained by backpropagating through only the last k loops. We measure how much of the weight gradient this throws away, exactly and for every k from one backward pass, on nine looped language models, and report three findings. First, on a trained model this lost gradient is set near the output: once the loop count is well above k, it barely changes with the loop count (within about 0.03 from 32 to 64 loops on the three models we tested, as a pre-registered test predicted for Parcae). Where the backward signal shrinks, $\rho^k$, with $\rho$ the signal's fitted shrink per loop, approximates it at moderate loop counts but overstates it at long ones, because the fitted $\rho$ drifts up as the fit takes in more loops. On Ouro the signal grows, and keeping two of four loops still loses 81% of the final output's gradient. Second, the lost gradient falls during fine-tuning, by 0.07-0.22 within 300 steps on three of four models, on held-out problems too. The fall is not just the read-out's share of the gradient; training only the layers outside the loop reproduced up to half of it, and it also falls under truncated training. So a trained model's value overstates what truncation removes later. Third, we could not show that it predicts the training cost of truncation better than rules that need no measurement: on two new models it tied Parcae's cost at the same k, in a test too small to separate them.

---


### 26. [LEAN: Loss-Engineered Modulation of the Model Weight-Sensitivity Distribution for Efficient, Error-Tolerant Neural Networks](https://arxiv.org/abs/2610.28872)

**<font color=#1a73e8>作者：</font>** Habibur Rahaman, Swarup Bhunia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The weights of a trained network do not have uniform sensitivity to model accuracy: the 1% most sensitive weights carry about a fifth of the damage a bit flip can do. This distribution decides the bit-flip tolerance of a model, the fraction of weights a code must cover and the bits each weight needs; existing schemes work with the distribution training leaves. We show that we can systematically modulate or alter the weight sensitivity distribution of a trained model, thereby shifting weights from one sensitivity bin to another. The sensitivity of a stored weight is the product of its gradient and the step a flip takes in the storage format, and LEAN adds a composite regularizer on both factors, a range term that bounds the flip step and a tail term that lowers the gradient of the most sensitive weights, with one coefficient {\lambda} setting how far the distribution moves. Ten epochs with the term, as a fine-tune or as the last epochs of training, shrink the sensitive tail 5 to 13 times on nine vision models (ResNet-18, ResNet-50, VGG-16 on CIFAR-10, CIFAR-100, ImageNet) within 0.5 points of accuracy; real flips confirm that the reshaped weights do less damage, a plain gradient-norm penalty does not reproduce the effect, and a preliminary extension to three small language models shows the same tail shaping. With a BCH code over 1% of the weights the model then survives 300 progressive bit-search flips in every training seed and 500 in two of three, where three of four published defenses with the same code fail by 300 and WCAT falls to 75% at 500. The reshaped distribution also cuts the parity for a fixed guarantee 3.7 times and makes a sensitivity-ordered 8/6/4/3-bit format affordable, which stores ImageNet ResNet-50 at a 3.29-bit weight payload, 2.4 times smaller than INT8, above the accuracy of LSQ at 3 bits.

---


### 27. [To Manipulate or Not: Opinion Dynamics in LLM Interactions](https://arxiv.org/abs/2610.28875)

**<font color=#1a73e8>作者：</font>** Mohammad Siahkamari, Phuoc Dat Nguyen, Stephen MacNeil  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly take part in extended conversations where they can both shape and be shaped by another party's views, yet most persuasion research measures only one side of that exchange. We introduce a controlled LLM-LLM debate framework in which two language-model roles repeatedly discuss a contested topic (climate-change attribution): one is given an assigned stance and, in some conditions, an explicit instruction to persuade, while the other receives no assigned position. Across four ordered model combinations involving GPT-6 Luna and Gemini 2.5 Flash Lite, we track both each role's explicitly reported position and a separate measure of its turn-by-turn behavior inside the conversation. Opinion dynamics differ substantially across model combinations: same-model interactions narrow the opinion gap on average, clearly for only one of the two models, while cross-model interactions widen it. Explicit reports and in-dialogue behavior capture distinct aspects of opinion dynamics, and a blanket instruction to persuade does not reliably increase influence. These findings suggest that conversational influence depends not only on assigned roles and initial positions but also on the participating models, with implications for how opinion change is measured in extended LLM interactions.

---


### 28. [SANE: Automated Scorer-Specific Metamorphic Testing for LLM Judges](https://arxiv.org/abs/2610.28886)

**<font color=#1a73e8>作者：</font>** Ethan Ludwick, Yu-Chung Hsiao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM judges increasingly mediate benchmark evaluation, model selection, data curation, and training. Their decisions are useful only when each judge responds reliably to changes affecting its scoring criterion. Existing methods for reliability testing perturb inputs with known expected effects on judge scores. Prominent LLM-judge testing harnesses combine human-authored perturbation recipes with synthetic test generation, leaving scorer-specific recipe ideation outside the automated pipeline. This limits their use to fixed perturbations and pre-assumed scorer types. We introduce SANE, an agent-based framework that encodes behavioral requirements for stochastic evaluators as reusable agent instructions. Given a scorer specification, implementation, and representative inputs, the pipeline first identifies scorer-specific capabilities, then automatically derives perturbation recipes and expected score relations for each. SANE also defines a scorer-independent validation framework for generated judge tests. It determines whether each recipe agrees with scorer intent and whether each instantiated case realizes the recipe and supports its expected relation. Because SANE generates a recipe inventory tailored to each scorer, the number of aligned recipes grows as scorers are added. Across five domains, SANE produces 3.7 times as many validated test families as the Judge Reliability Harness (JRH) at comparable end-to-end validity and detects scorer deficiencies in every domain, including professionalism and toxicity, where JRH detects none. On faithfulness, SANE achieves strong human alignment in judge ranking: its test-suite scores rank 11 judge models consistently with human-labeled FaithBench performance (Spearman rho = 0.852), while JRH does not (rho = 0.100).

---


### 29. [Combating Catastrophic Forgetting in Continual Domain Adaptation via Knowledge Recasting](https://arxiv.org/abs/2610.28892)

**<font color=#1a73e8>作者：</font>** Zijie Liu, Zhen Tan, Charles Fleming 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adapting language models to new domains during post-training risks degrading previously acquired capabilities, a phenomenon commonly known as catastrophic forgetting. Existing mitigation methods largely treat forgetting as a consequence of excessive model drift. They therefore constrain updates by preserving old outputs, replaying old data, or regularizing changes to parameters and representations so that the updated model remains close to its previous state. We take a different view: Rather than pulling the updated model back toward its old state, we translate the new domain into the model's pre-existing knowledge space, making unfamiliar knowledge learnable through familiar procedures. Therefore, we propose Skill Schema Transport (SST), a post-training framework that transports new knowledge into the model's existing skill space. SST abstracts each example type into a skill schema, preserving its essential operations, dependencies, and verification steps while removing domain-specific surface forms. By recasting new examples as instances of reusable procedures, SST turns knowledge update from trajectory memorization into procedural reuse. In continual domain adaptation settings, SST consistently reduces forgetting while improving generalization to related tasks. Across two 3B instruction-tuned backbones, SST improves average final performance on streamed domains by 2.53 to 5.75 points over sequential post-training. It also lowers max-drop forgetting in all evaluated settings, with the largest reduction from 42.41 to 7.10 points on the Qwen-3B MATH stream, while substantially recovering the OOD degradation induced by sequential updates.

---


### 30. [CSD: Common-Support Distillation for Cross-Tokenizer Knowledge Transfer](https://arxiv.org/abs/2610.28895)

**<font color=#1a73e8>作者：</font>** Mingyu Yang, Sharath Turuvekere Sreenivas, Adithyakrishna Venkatesh Hanasoge 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-tokenizer logits distillation enables knowledge transfer across model families, allowing students to learn from stronger or more specialized teachers. However, differences in vocabulary and segmentation make teacher and student next-token distributions difficult to align. Existing logits-based methods are easy to integrate into standard distillation pipelines, but often rely on restrictive heuristics or tokenizer-pair-specific choices. They may restrict supervision to shared vocabulary subsets, require manually selecting different objectives for different tokenizer pairs, or match only the observed chunk and its complement rather than individual alternative continuations. We introduce Common-Support Distillation (CSD), a unified logits-based framework that constructs a shared support between the teacher and student at each aligned input chunk and matches the induced distributions with a single objective. For one-to-one alignments, CSD uses explicit common-token pairs as the shared support. For other alignments, it constructs a virtual support whose probabilities are computed using the autoregressive chain rule. A residual event captures probability mass outside the explicit support, ensuring that both induced distributions remain normalized. Across four teacher-student settings comprising Llama-3.2-1B and Gemma3-1B-PT students with Qwen and Phi teachers, CSD consistently achieves the highest average performance among the evaluated cross-tokenizer methods, outperforming the strongest alternative by up to 1.8 points and surpassing both continued pretraining and same-tokenizer distillation. For Llama-3.1-8B, CSD improves average accuracy over the strongest evaluated baseline by up to 4.2 points for the base student and 1.6 points for the instruction-tuned student.

---


### 31. [Is Refusal Direction Universal across Low-Resourced Languages?](https://arxiv.org/abs/2610.28897)

**<font color=#1a73e8>作者：</font>** Anastasiia Ivanova  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Refusal directions have been shown to transfer cross-lingually with near-perfect effectiveness across safety-aligned languages (Wang et al., 2025), reportedly regardless of resource level. However, the only truly low-resourced language evaluated is Yoruba, which is strongly misaligned and shows limited transfer, leaving open how refusal directions behave for other low-resourced languages. We extend PolyRefuse to three additional low-resourced languages (Belarusian, Bashkir, and Tajik) and replicate the pipeline of (Wang et al., 2025) on Qwen2.5-14B-Instruct. We find that universality is graded rather than binary: directions from safety-aligned and partially-aligned languages transfer broadly, while those from strongly misaligned languages fail to reliably modulate refusal behavior on any target tested, including other misaligned languages, once ceiling effects are accounted for. Geometric alignment and behavioral transfer are further shown to be partially dissociated. These findings complicate the universality claim and suggest that users of the least-resourced, most strongly misaligned languages may face weaker safety guarantees.

---


### 32. [Hidden Messages Between Diffusion Language Model Agents: Causal Evidence for Latent Communication](https://arxiv.org/abs/2610.28905)

**<font color=#1a73e8>作者：</font>** Alan-Barsag Gazzaev, Alexey Gavrilov, Sergey Muravyov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion language models form answers through a sequence of revisable continuous states, but multi-agent systems usually discard those states and make agents communicate only after decoding text. We ask whether one independent diffusion trajectory can pass a compact hidden message into another and, crucially, whether the receiver uses what that message means. In Hidden Messages, a sender compresses its denoising state into four signed dense vectors; the receiver consumes them while retaining its own context, canvas, and trajectory. Removing a message tests whether the channel matters; replacing it with a message from another example tests whether its content matters. Across controlled tasks, derangement removes a +63.6-point advantage on Tiny-A2D and a +100.0-point advantage on Dream-7B, while targeted substitutions steer the receiver toward the substituted fact. On QASC with the two supporting facts split across agents, matched communication reaches 80.8%, but a wrong-example message lowers accuracy to 46.8%, a content effect of +34.0 points. The surprising result is temporal: one late transfer reaches 87.8%, exceeding four recurrent exchanges by +7.0 points. These experiments provide causal evidence for continuous hidden communication between diffusion-LM agents and show that when information is transferred can matter more than how many times agents exchange it.

---


### 33. [DiffResearch: Accelerating Deep Research with Diffusion Language Models](https://arxiv.org/abs/2610.28909)

**<font color=#1a73e8>作者：</font>** Alan-Barsag Gazzaev, Alexey Gavrilov, Mikhail Mozikov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep research systems iteratively plan, gather evidence, synthesize, and revise, making end-to-end latency a key bottleneck for interactive use. Almost all production systems are built on autoregressive (AR) language models and inherit left-to-right decoding in planning and long-form writing. We present DiffResearch, an open multi-agent deep research framework that places a diffusion language model (dLLM) at the core of every stage, and measure how a diffusion backbone changes latency and report quality. Holding the agentic scaffold, retrieval code, prompts, and evaluation fixed, we swap the backbone between an open diffusion model and a comparable AR model. Across 100 Deep Research Bench tasks, the diffusion backbone is roughly 6 times faster end-to-end, driven by order-of-magnitude reductions in planning and writing. We further introduce dFast, a decomposition mode that reads intermediate denoising states and extracts subqueries before generation finishes, providing a 1.99 times median speedup for decomposition in isolation with no loss of report quality. On the benchmark's RACE rubric, dFast obtains the best overall score among the three configurations. Finally, in a public system-level leaderboard snapshot, an instance built on a stronger diffusion model ranks above several commercial systems. We release DiffResearch under an Apache-2.0 license.

---


### 34. [D-Skill: Distilling Teacher Knowledge through Agent Skills](https://arxiv.org/abs/2610.28914)

**<font color=#1a73e8>作者：</font>** Shuo Yuan, Dacheng Li, Joseph E. Gonzalez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier language-model agents excel at complex tasks, but high inference costs make transferring their capabilities to smaller models essential. Traditional knowledge distillation achieves this through parameter updates, requiring access to the student's weights and additional training compute while encoding the transferred knowledge implicitly in the parameters. We introduce D-Skill, a framework that treats the teacher as a black box and distills its behavioral advantage into an interpretable natural-language skill by analyzing paired rollouts and identifying behavioral divergences and agreements. The resulting lessons are consolidated offline, with any compatible skill-update backend, into a skill document that is provided to the student at inference time. D-Skill constructs the skill entirely offline from fixed trajectories, without labels, further environment interaction, or weight updates after rollout collection. Across SpreadsheetBench-Verified, ALFWorld, and chess puzzles spanning multiple teacher-student pairs, D-Skill closes 75%-95% of the teacher-student gap without touching model weights. After a single offline pass over the paired traces, D-Skill outperforms one-epoch SFT baselines and remains competitive with multi-epoch SFT. Under the same model family, the resulting student also incurs 5.7x-8.3x lower inference cost per task than the teacher. Our results demonstrate that natural-language skill distillation offers a performant, interpretable, and efficient alternative to weight-based capability transfer.

---


### 35. [Scriptorium: System Design and Implementation of a Multi-Human, Multi-AI Collaborative Digital Library Search Platform](https://arxiv.org/abs/2610.28929)

**<font color=#1a73e8>作者：</font>** Abbas Pirmoradi, Milad Momeni, Anna Chu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This technical report documents the design and implementation of Scriptorium, a digital library search interface designed to support multi-human, multi-AI collaboration: full cross-user transparency of search activity combined with a Manager--Worker architecture of seven role-specialized generative AI agents. A companion short demonstration paper describes Scriptorium's interaction design; because a demonstration format is constrained to a few pages, it necessarily omits most implementation detail. This report documents Scriptorium's complete system architecture, data model, collaborative-interaction design rationale, and AI orchestration mechanism, including verbatim agent prompts, the deterministic guardrails that constrain them, the language model and retrieval configuration, and the steps needed to run the system, so that the design can be inspected, critiqued, reproduced, and reused by other researchers. We also discuss the system's current limitations and the user study we are planning to evaluate its central hypothesis: that combining collaborative transparency with scoped multi-agent AI assistance increases serendipitous cross-pollination between collaborators' research threads.

---


### 36. [Back Up Before You Regret: Measuring Backup Awareness and Automating Backup in Coding Agents](https://arxiv.org/abs/2610.28934)

**<font color=#1a73e8>作者：</font>** Xu Li, Simon Yu, Minzhou Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents now complete tasks autonomously, modifying real-world state such as artifacts, software environments, and configurations along the way. Yet they show limited backup awareness: recognizing that an action will modify state that may later be needed, and preserving it beforehand. To evaluate backup awareness, we introduce RegretBench, a benchmark of 205 executable tasks grounded in regret moments reported on platforms such as this http URL, GitHub, and Stack Overflow, where users explicitly regretted not preserving state they later needed. Across six frontier models, agents complete 86.1% of tasks on average yet back up before these moments in only 15.2%, showing that task completion ability does not imply backup awareness. Because it is hard to predict which changes will be regretted, we propose BackUpper, a harness plug-in backup layer that checks every tool call and preserves affected state before modification. It combines rule-based strategies for common operations with a lightweight subagent for complex cases, and its rule table can expand with subagent decisions over time. On RegretBench, BackUpper covers every regret moment action and restores states with 92.2% average similarity to the original. Achieving this costs only $0.014 per task, with 7x fewer tokens than the main-agent self-backup baseline. When users have preferences on what to back up, BackUpper can also narrow its scope accordingly, matching human annotations on whether an action is worth preserving with an 84.5% F1 score. These results suggest that agents can keep actions reversible at low cost while respecting users' preferences.

---


### 37. [Auditing Conformal Prediction for Language Models Under Inference-Time Model Shift](https://arxiv.org/abs/2610.28937)

**<font color=#1a73e8>作者：</font>** Achref Doula, Max Mühlhäuser  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conformal prediction (CP) for language models is typically evaluated under a matched protocol, in which calibration and deployment use the same post-training inference configuration, such as quantization mode and inference temperature. In deployment, these choices often differ from those used at calibration to meet memory or throughput constraints or serving policies. We argue that this exposes a limitation in current CP evaluation protocols for language models. We formalize the underlying phenomenon as inference-time model shift: a change in the conformal score distribution induced by inference configuration rather than by the input--label distribution, and theoretically characterize how it breaks split-conformal exchangeability even when the task distribution and trained model are unchanged. We then evaluate its consequences across 8 language models, 4 finite-label benchmarks, and 12 inference configurations. We find that matched evaluation can substantially overstate deployment-time coverage, and that the effect is heterogeneous across models and datasets. We argue that inference configuration should be reported as a first-class experimental axis in CP evaluations for language-model systems.

---


### 38. [Self-Improving Agents with World Model Predictive Paths](https://arxiv.org/abs/2610.28945)

**<font color=#1a73e8>作者：</font>** Haori Lu, Tianyu Gao, Yaoyao Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly expected to interact with environments and improve their decisions during deployment. However, how anticipating future outcomes and drawing on accumulated interaction experience can jointly support decision-making remains underexplored. We propose a test-time framework, inspired by Model Predictive Path Integral (MPPI) control, that combines multi-branch predictive analysis with experience-based adaptation. At each step, the agent proposes multiple candidate actions and imagines their outcomes with a world model, so that alternatives can be compared without being executed in the environment. Since language environments provide neither explicit dynamics nor costs, the predicted outcomes are evaluated for task progress and risk, and MPPI-style weights over the resulting costs guide the final decision. A dual-branch experience memory enables self-improvement: the planner branch refines candidate generation and action selection, while the world model branch improves next-observation prediction. Experiments on ALFWorld and ScienceWorld across three backbones demonstrate the strong overall performance of our method and the effectiveness of experience-guided predictive control. Our code will be made publicly available.

---


### 39. [Is 2:4 Sparsity Still Worth It? Semi-Structured Sparsity versus Quantization in LLM Inference](https://arxiv.org/abs/2610.28947)

**<font color=#1a73e8>作者：</font>** Xiuyi Qin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> NVIDIA tensor cores have supported 2:4 semi-structured sparsity since Ampere, and the pattern composes with quantization. When the two are combined, the practical question is which step to take next: from a given precision, add 2:4 sparsity or drop to the next lower precision? We compare the two at equal bits, with sparsity metadata counted, and at equal nominal tensor-core tiers, over all six GEMM operands of a transformer layer, with kernels measured on three GPU generations and online pruning and quantization included. Our results show that as long as a lower precision is available, adding 2:4 is the worse step, both less accurate and slower, because the energy that 2:4 discards from each group of four along the hardware-forced axis does not shrink with bits, while quantization error does. Once quantization reaches the lowest precision the hardware supports, 2:4 still speeds up linear layers by 1.3--1.7\x{}, and on an H100 a retrained 2:4 model served in FP8 by vLLM reaches 27\% higher prefill throughput than the dense FP8 model, with GSM8K accuracy on par. Its quality has to be won back by retraining, however, which restores perplexity long before reasoning; on Blackwell, whose sparse FP4 uses a pairwise 4:8 pattern, the loss is larger and our retraining budget did not recover it.

---


### 40. [Scan or Index? large Evidence Coverage, Answer Quality, and Cost in Long-Document RAG](https://arxiv.org/abs/2610.28957)

**<font color=#1a73e8>作者：</font>** Juan Terven, Diana-Margarita Córdova-Esparza, Julio-Alejandro Romero-González 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scanning every passage in a long document seems thorough, but does it preserve more useful evidence or produce better answers? We compare 11 retrieval configurations spanning lexical and dense search, hybrid reranking, and full-document scanning with Jev, OpenAI Decisions, and Cloudflare Clef. Our evaluation uses 396 QASPER questions and 80 questions from eight complete textbooks, with common passages, a five-passage limit, and a fixed answer generator. On books, Hybrid + Jev achieves the highest observed evidence coverage (94.1%), compared with 88.7% for Jev full scan and 81.3\% for OpenAI dense retrieval. Full scans examine every passage initially, yet later reduction steps can discard relevant evidence. Higher evidence coverage also does not consistently produce better answers: Hybrid + Decisions achieves the highest observed book Answer Accuracy among retrieval methods (0.892), despite recovering less reference evidence. Full scanning incurs substantially higher latency on books under the tested deployments, while reusable dense retrieval has lower projected API cost than paid decision-based methods as queries accumulate. Most QASPER articles already fit within the hybrid candidate pool, limiting the benefit of scanning. These results highlight evidence retention, answer quality, and reuse cost as complementary criteria for choosing a long-document retrieval strategy.

---


### 41. [How Does Orthogonalization Adapt to the Neural Network Hessian Structure? A Gradient Self Outer-Product Analysis at Initialization](https://arxiv.org/abs/2610.28975)

**<font color=#1a73e8>作者：</font>** Shenyang Deng, Garvit Goyal, Tianyu Pang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon orthogonalizes a weight matrix's momentum before each step, and on neural networks this simple preconditioner beats AdamW in a wide range of tasks. Existing analyses explain Muon within general optimization frameworks or on a few specific models, and many of them view orthogonalization as a preconditioner. Since the Hessian is the optimal preconditioner under a quadratic approximation of the loss, these works leave a basic question open: what makes orthogonalization suited to the Hessian of a neural network? Prior work shows that the layer-wise Hessian of a neural network is row-block diagonally dominant, and Muon's implicit preconditioner, the Kronecker product $(\mathbf{V}\mathbf{V}^\top)^{1/2}\otimes\mathbf{I}$ with $\mathbf{V}$ the momentum, has the same row-block structure exactly when $\mathbf{V}\mathbf{V}^\top$ is diagonally dominant. Diagonal dominance of $\mathbf{V}\mathbf{V}^\top$ has been observed in language models, but why a neural network produces it has not been explained. This work provides a quantitative asymptotic theory for neural networks at initialization, and points out the intuition that the overparameterization of the weight matrices drives the diagonal dominance. We analyze $\mathbb{E}[\mathbf{G}\mathbf{G}^\top]$, which equals $\mathbb{E}[\mathbf{V}\mathbf{V}^\top]$ at initialization, in four canonical models: symmetric matrix factorization, deep linear networks, two-layer ReLU networks, and single-layer linear attention. In each case the diagonal entries outgrow the off-diagonal ones at explicit rates as the hidden dimensions grow; for the query, key and value weights of attention the off-diagonal vanishes altogether. Simulations of the four models and experiments on language models at initialization confirm the predicted scaling.

---


### 42. [SSMCGM-Stream: A Streaming State-Space Model for Personalized Diabetes Management](https://arxiv.org/abs/2610.28976)

**<font color=#1a73e8>作者：</font>** Shakson Isaac, Chirag Patel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous glucose monitoring supports diabetes management but requires forecasting models that are accurate, interpretable, and efficient enough for real-time deployment. We present SSMCGM-Stream, a streaming state-space model that maintains a personalized hidden state updated with each incoming glucose reading to provide constant-time forecasting, physiologically structured counterfactual reasoning, and interpretable forecasts through hidden-state attribution. Built on this foundation, SSMCGM-Agent delivers risk-aware, natural-language decision support by translating forecasts, explanations, and counterfactuals into grounded recommendations through a guarded language-model interface. Evaluated on the T1DEXI cohort, SSMCGM-Stream achieves forecasting performance comparable to strong neural baselines while substantially reducing computational cost, enabling continuous on-device diabetes decision support.

---


### 43. [The Butterfly Effect in LLM Social Simulations: From Architecture Sensitivity to Robustness Audits](https://arxiv.org/abs/2610.28981)

**<font color=#1a73e8>作者：</font>** Jinyi Ye, Lei Cao, Ding Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> A butterfly effect occurs when a local perturbation propagates through a system and produces divergence in its collective outcome. In LLM social simulations, this creates a particular challenge for scientific inference: sensitivity to implementation choices can enter agent interactions and alter the collective outcomes on which scientific claims are based. We study this problem through a repeated Prisoner's Dilemma and a social-media echo chamber, spanning representation- and design-level perturbations across four LLM families. We find that controlled perturbations can substantially alter collective outcomes, with sensitivity varying across both perturbations and models. In the Prisoner's Dilemma, changing only the representation of a matched persona shifts two-agent cooperation by 75.2 percentage points for GPT-5.2, while game framing and memory representation produce smaller or less consistent effects. Multi-agent interaction further reshapes representation sensitivity, producing amplification or attenuation depending on the model and perturbation. In the echo-chamber simulation, persona representation changes interaction targeting and is accompanied by divergence in collective interaction structure, extending representation sensitivity from agent behavior to network-level outcomes. These results show that robustness cannot be inferred from a single simulation configuration and that local sensitivity can change as it propagates through interaction. We introduce TRAILS (Taxonomy for Robustness Audits In LLM Simulations) and the Social Simulation Audit Card as a framework for systematically auditing these dependencies and calibrating the scope of scientific claims to the robustness evidence that supports them.

---


### 44. [Behavior Beyond Text: Evaluating Refusal Transfer Failure in LLM Agents](https://arxiv.org/abs/2610.28982)

**<font color=#1a73e8>作者：</font>** Ekagra Gupta, Raj Saha, Aniekan-Abasi Inyang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While large language models are increasingly deployed as tool-calling agents, their safety evaluations still focus primarily on their ability to refuse harmful requests in text. We investigate whether the refusal behavior in text transfers to tool use. We construct a benchmark of 2,304 prompts across four domains, consisting of matched triplets that present the same harmful or benign request in text-only, standard tool-enabled, and adversarially framed tool-enabled settings. We then assess tool-call safety using 20 predefined forbidden actions. Testing five models of varying sizes and families, we find that requests refused in text frequently result in unsafe tool calls. Under standard tool-enabled prompting, this divergence occurs for 10-52 percent of harmful requests refused in chat. To mechanistically investigate this gap, we identify a refusal-associated direction in the residual stream of each of the five models. We find that in tool-enabled contexts, the activations along this direction decrease in four of five models. Furthermore, lower activation predicts unsafe tool calls across all five models (AUC 0.76-0.86). However, restoring the signal to the respective text-only value through activation patching only prevents a subset of unsafe calls, primarily by suppressing tool use rather than by producing safer calls. Steering along the refusal direction nearly eliminates unsafe calls only at strengths that also suppress benign tool use or degrade the output quality. Our findings indicate that the identified refusal direction contributes to whether a model acts, but only partially explains the refusal divergence. Therefore, evaluating the safety of tool-calling agents requires directly examining their actions along with their textual responses.

---


### 45. [PerMIT: Securing Persistent Memory for LLM Agents via Machine-Checked Integrity Theorems and Scalable Community Trust](https://arxiv.org/abs/2610.28987)

**<font color=#1a73e8>作者：</font>** Tanqiu Jiang, Min Bai, Sadat Shahriar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persistent memory is a largely undefended surface for injection and poisoning, and the same risk limits memory sharing among agents. We present PerMIT, a memory architecture with provable integrity guarantees under an explicit trust assumption: only user-typed inputs and values confirmed at a gate are trusted. PerMIT mediates the release and use of untrusted environment-derived values through a finite memory interface, while preserving agent-driven multi-turn planning and tool choice. Over this finite interface, we prove two integrity theorems that are also machine-checked in Lean 4, which together ensure that environment-derived memory reaches a sensitive action only if confirmed at the gate and influences the agent's behavior only through what the gate displays. Every attack in our threat model thereby reduces to a single auditable decision, which a human, an LLM verifier, or both can make in practice. On Trojan Hippo, PerMIT records zero observed attack success with self-verification and lightweight verifiers. Because each confirmation is a logged verdict on exact content, endorsements accumulate across users, and sufficiently endorsed items become community-confirmed with no further verification required. Under explicit assumptions, we prove and corroborate in simulation a co-scaling property: as the community grows, the risks of promoting poison and of wrongly evicting benign knowledge fall, while per-user verification effort does not rise. On $\tau^2$-bench, communities of up to 90 autonomous agents use PerMIT to build shared knowledge bases with no direct memory injection promoted, and the resulting knowledge significantly improves new agents on held-out tasks, suggesting a path toward agents that safely self-improve at test time.

---


### 46. [Language Impairment as a Lens onto Large Language Models](https://arxiv.org/abs/2610.28992)

**<font color=#1a73e8>作者：</font>** Muxuan He, Wang Bill Zhu, Yue Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although large language models (LLMs) encode language in highly distributed spaces, they remain vulnerable to focal disruptions---a phenomenon strikingly similar to how localized brain damage causes clinical aphasia in humans. To investigate this theoretical tension, we ask whether LLMs possess a functional structure analogous to the human language system, by introducing a novel mechanistic interpretability framework inspired by aphasia. Through two complementary approaches, classifier-guided lesioning and continuous activation steering, we systematically induce aphasia-like breakdowns in LLMs. We find that language functions can be successfully isolated to discrete structural circuits and continuous representational vectors, yet these functions remain densely entangled with significant circuit overlap and vector similarities across distinct aphasic profiles. Furthermore, while steering generalizes robustly across downstream tasks, structural lesioning remains asymmetrically constrained. By bridging neuropsychology and mechanistic interpretability, we demonstrate that LLMs, functionally analogous to biological brains, rely on a densely entangled architecture that can be systematically mapped through clinically-informed interventions.

---


### 47. [FlashNext-RL: A System Optimization Study for Long-Horizon Agentic RL of Qwen3.8-Flash-Next](https://arxiv.org/abs/2610.28998)

**<font color=#1a73e8>作者：</font>** Zhewei Yao, Yuxiong He  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon agentic reinforcement learning (RL) requires both efficient rollout generation and training on long sequences. However, the memory requirements and model-specific operators of Qwen3.8-Flash-Next make this difficult with existing open-source implementations. To resolve these limitations, we introduce FlashNext-RL, a model-specific RL training optimization framework based on prime-rl, with vLLM for software engineering (SWE) rollout generation. Our main focus is BF16 training of the full 48-layer model on a single 8xB200 node, with the first two layers, the n-gram table, the sparse-attention indexer and the multi-token prediction head frozen. We optimize host offload, gradient accumulation and the kernels for mixture-of-experts, sparse attention and the gated residual stream. In the full-model development study, non-padding training throughput increases from approximately 395 tokens/s/GPU in the initial 32K-token configuration to 4,438 tokens/s/GPU in the optimized 131K-token configuration, with hardware matmul throughput (aka without considering the cost of attention components) increasing from approximately 20 to 213 TFLOPs/GPU. A controlled cumulative study on an 8-layer model further quantifies the contributions of individual optimizations. Together with three inference nodes, the system supports a live SWE RL run with a target batch of 1,024 trainable rollouts and a 131,072-token context limit. Over steps 5-15, an iteration takes 22.4 minutes on average, with bounded entropy and trainer-sampler mismatch KL. These results highlight the importance of tailoring RL training to the model's architecture, memory layout and kernel requirements, rather than relying only on general-purpose RL infrastructure.

---


### 48. [T-DIG: Text-Conditioned Diversity for Image Generation](https://arxiv.org/abs/2610.29003)

**<font color=#1a73e8>作者：</font>** Simran Khanuja, Rohit Gandikota, Gaurav Parmar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) platforms typically return several images per prompt so users can explore different visual interpretations and choose one that matches their intent. However, T2I models are usually optimized for single-image quality which comes at a cost of multi-image diversity, limiting this exploration. Diversity is also contextual: one user wants variations in background, while another wants them in artistic style, and the same user may later want variations in clothing. The generated images should differ along whatever axis the user cares about. In this paper, we introduce T-DIG, a text-conditioned diversity framework for image generation and editing. T-DIG is an iterative framework comprising multiple modules that lets users type prompts, inspect default generations, request variations using natural language, and continue refining outputs until they're satisfied. At its core, T-DIG uses an LLM policy that produces K axis-conditioned prompts or edit instructions for a frozen generator or editor. We train this policy with GRPO using a text-conditioned diversity reward and alignment penalties. Because the image generator remains frozen, T-DIG applies to open-weight, distilled, and proprietary models. We also release the first dataset for text-conditioned prompt diversity in image generation, with the training and validation splits built from human-written axes and a test set drawn from real user interactions with T-DIG. T-DIG far exceeds baselines in improving text-conditioned diversity, while preserving base-prompt alignment across a variety of metrics and human judgements. We show that user-directed diversity exploration can be added to a wide range of image generation models, open and closed, without the need to access their weights. Website: this https URL

---


### 49. [An Evidence-Driven Multi-Agent Compound AI System for Head and Neck Proton Radiotherapy Planning](https://arxiv.org/abs/2610.29010)

**<font color=#1a73e8>作者：</font>** Qingqing Wang, Liqiang Xiao, Chang Chang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Radiation treatment planning requires balancing competing objectives to satisfy clinical criteria while accommodating physicians' preferences. This study aims to develop an evidence-driven, multi-agent compound AI system that integrates DRL-based automated treatment planning with LLM-based conversational plan refinement for proton PBS therapy. A policy network trained using PPO first generates multiple plans without human intervention, from which one is selected as the target plan and the others serve as references for subsequent refinements. For challenging cases requiring further adjustments, an LLM-based multi-agent system enables plan refinement through natural language interactions. The system comprises a planning agent that recommends evidence-supported adjustments, a chatbot providing a unified conversational interface, and an evaluation agent that retrieves clinical metrics and identifies constraint violations. To enhance domain-specific reasoning, the planning agent based on Qwen3-14B is designed to justify its recommendations using evidence from previously generated plans and post-trained on task-specific data using SFT and GRPO. The framework was trained and evaluated using 21 patients with H&N cancers, with 5 PPO-generated plans per patient. Of these, 50 plans were selected for instruction-guided refinement. Compared with the base LLM, the post-trained Qwen3-14B demonstrated improved instruction-following, information retrieval and domain-specific reasoning capabilities. The resulting adjustments more effectively improved user-prioritized objectives while limiting deterioration in competing objectives, yielding more clinically appropriate trade-offs in patient-specific plan refinement. The proposed compound AI system provides a user-friendly planning platform, offering a promising approach to personalized proton PBS treatment planning.

---


### 50. [Target Regeneration Shrinks the Gains of Draft-Training Objectives in Speculative Decoding](https://arxiv.org/abs/2610.29013)

**<font color=#1a73e8>作者：</font>** Jungseob Lee, Hogun Seong, Euijun Choi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates large language models by verifying drafted tokens in parallel. New draft-training objectives are usually credited with the acceptance they add over cross-entropy on externally written responses, yet many pipelines let the target rewrite them. We ask how much of that gain survives. With a vision-language target and a block drafter, we train three objectives on four versions of one corpus: cross-entropy on corpus tokens, token-level distillation from the target, and distillation gated to positions that would survive verification. Distillation and the gate add large gains on external responses, but after greedy regeneration, distillation adds a smaller gain and the gate little or none. The shrinkage persists across data orders, position weights, verifiers, decoding temperatures and, for distillation, initializations and learning rates. Most of it remains at matched supervised length and at each objective's best measured training length. A second vision corpus shows the shrinkage, as does a text-only replication, for distillation also with an autoregressive drafter. Objective gains should therefore be measured against a target-regenerated baseline and across training lengths. Our code is available at this https URL.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-204](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
