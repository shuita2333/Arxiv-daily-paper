# 🧠 大模型相关研究 | 2026年09月10日

> 本类共 **483** 篇论文：已确认 **447** 篇，待复核 **36** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-483](./part-10.md)

---

### 1. [Seeing Without Understanding: Large Language Model Evaluation of Mobile User Interface Quality, Failure Taxonomy, and Architectural Explanation](https://arxiv.org/abs/2609.05423)

**<font color=#1a73e8>作者：</font>** Md Rejaul Korim Sadi, Golam Mostofa Naeem, Toufiqur Rahman Tasin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Evaluating mobile user interface quality at scale remains a persistent challenge in software engineering and human-computer interaction. Rule-based heuristic methods offer structural reliability but demand significant engineering effort, while human annotation does not scale to the volume of applications produced annually. Large language models present a promising alternative, yet their reliability for structured UI judgment has not been systematically examined, and the patterns behind their failures remain insufficiently characterized. This paper addresses both gaps. We begin with the complete RICO dataset of 66,261 real-world mobile application screens, from which we derive a refined evaluation corpus of 15,000 screens through a rigorous, literature-guided selection process. Each screen is assessed across seven criteria: structural JSON validity, minimum visible element count, clickable component presence, non-zero layout bounds, image integrity, and perceptual duplicate removal. Against this corpus, we apply a heuristic baseline built from severity-weighted usability signals, normalized layout metrics, and pixel-ratio complexity measures calibrated to real user sentiment. Multiple language models independently rate each screen across usability, layout quality, and visual complexity from structured JSON descriptions and raw screenshots. Dimension-level comparison against the heuristic uses agreement rates, Cohen's Kappa, and confidence calibration. Recurring divergence patterns are organized into a failure taxonomy and interpreted through transformer architectural signatures: MLE plausibility bias, attention misgrounding, and autoregressive over-commitment.

---


### 2. [AhaBench: Do Agents Learn from Prior Experience? A Benchmark for Long-Horizon Continual Learning](https://arxiv.org/abs/2609.05435)

**<font color=#1a73e8>作者：</font>** Zerui Cheng, Jiawei Xu, Huacan Chai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern language agents are expected to operate over long horizons: they ask follow-up questions, reuse worked examples, handle tool feedback, and adapt to delayed consequences. Most evaluations still reset the agent after a prompt or score only the final state of one trajectory. AhaBench asks a more operational question: when a fixed model receives useful experience, does its later behavior improve under a related evaluation condition where the obvious support has been removed, changed, or delayed? The suite contains three components. Aha-Puzzle tests no-hint exploration after solved hidden-state puzzles; Aha-Euler turns Project-Euler-style mathematical ideas into generated taught/held-out tasks with exact validators; and Aha-Vending, an open-source implementation inspired by Vending-Bench, tests whether a simulated vending agent remains profitable while handling delayed feedback and operational incidents. AhaBench reports a three-part scorecard: Initial Score measures starting competence, Post-Experience Score measures the later empirical outcome, and Learning Lift is their difference. This decomposition is the main empirical message: models that use visible support well, models that reach high post-experience scores, and models that improve most during a run are not always the same. On the common eight-model panel, Claude Opus 4.6 leads aggregate Post-Experience Score at 64.3 and aggregate Learning Lift at +25.8, with Gemini 3.1 Pro close behind at 63.4. The component results explain the split: puzzle traces raise supported scores but often fail to become no-hint exploration behavior; Aha-Euler full teaching reaches 78.6-100.0% while answer-only transfer ranges from 0.0 to 73.9%; and Aha-Vending separates profitable incident handling from bankruptcy and no-order failure. We release benchmark tasks, rubrics, validators, simulator code, and interfaces for evaluating new agents.

---


### 3. [Beyond Right and Wrong: Evaluating Second-order Social Reasoning in Large Language Models](https://arxiv.org/abs/2609.05437)

**<font color=#1a73e8>作者：</font>** Sunny Rai, Jinyi Kuang, Reyhan Jamalova 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Previous AI alignment efforts have focused primarily on first-order social norms -- teaching models what is socially acceptable or unacceptable (e.g., `do not steal'). However, social intelligence depends not only on norm recognition, but also on anticipating who will enforce it and how (e.g., public shame or even imprisonment). These second-order expectations, known as metanorms, govern how people respond when social rules are broken. We introduce a novel framework for evaluating metanorm reasoning in Large Language Models (LLMs) along two dimensions: emotional appraisal and behavioral response, and propose new classification tasks, namely, predicting self-regulation in violators, and other-regulation in observers. We release a multi-perspective dataset, NormReact, of 450 norm violation scenarios, hand-annotated for emotions and behavioral responses across norm violators' gender and observers' social closeness. Current LLMs portray a harsher social world: across six models, they overpredict negative sanctions where humans would expect inaction, and alignment with human judgments deteriorates as social distance increases. These findings suggest that AI systems in norm-sensitive domains from conflict mediation to policy simulation, may risk producing a distorted picture of social regulation: one that over-represents punishment and under-represents the tolerance, restraint, and relational calibration that characterize actual norm enforcement in real world.

---


### 4. [CriticGen: Generation-Aware Evaluation as Actionable Feedback](https://arxiv.org/abs/2609.05439)

**<font color=#1a73e8>作者：</font>** Huifang Du, Zecheng Zuo, Sen Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current evaluation methods for large language models are coarse-grained and decoupled from generation, producing generic explanations that fail to provide actionable feedback for model improvement. We propose CriticGen, a fine-grained, generation-aware evaluation framework that turns evaluation into actionable control for answer improvement. CriticGen first generates sample-specific evaluation dimensions and scoring criteria under high-level categories such as subjective, objective, and self-derived constraints. These criteria then serve as a dynamic rubric for jointly producing a score, a reason, an executable refinement suggestion, and a refined answer. This rubric-conditioned refinement process enables models to diagnose flaws and perform targeted answer improvement. Experimental results show that fine-grained evaluation should be both instance-specific and actionable. CriticGen induces higher-quality rubrics, improving relevance/coverage from 3.33/4.03 to 3.97/4.24. CriticGen also achieves the best score correlations, with 0.9556 Pearson and 0.9560 Spearman, and raises the F1 of criterion-grounded reasons and executable suggestions from 0.6369/0.5994 to 0.7554/0.7900. Crucially, its feedback translates into reliable answer improvement, improving 73.17% of answers with a 93.28% non-degradation rate.

---


### 5. [When Does Memory Help? A Cost-Aware Evaluation of Long-Term Memory in Tool-Using LLM Agents](https://arxiv.org/abs/2609.05441)

**<font color=#1a73e8>作者：</font>** Shweta Mishra, Shashank Mishra  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory for LLM agents is evaluated today by conversational recall benchmarks (LoCoMo, LongMemEval), which measure question answering over dialogue history, not whether remembered facts change what a tool-using agent does. We present MERIT (Memory Evaluation for Realistic Instrumented Tasks), a benchmark and harness that measures the marginal utility of memory for task-executing agents under explicit cost accounting. MERIT provides episodic tool-use tasks in three domains whose dependence on earlier-episode facts is verified by an automated leak check; a difficulty ladder ending in updated-fact recall; controlled memory corruption; and full token and dollar metering of every memory operation. Across 23,440 scored episodes ($42.57), a two-generation pilot on gpt-4.1-mini and a preregistered 3-model x 3-seed grid (GPT-4.1, Claude Haiku 4.5; memory side held fixed), memory lifts dependent-task success from a leak-verified floor of 0.00 to 0.55-1.00. On updated facts, embedding retrieval collapses unpredictably (0.30-0.95 across models; max seed gap 0.45), and agents act on a correctly retrieved value only 55% of the time, while update-on-write stores (a structured fact store and, notably, LLM summarization) remain at 0.70-1.00; the hybrid is worse than the fact store alone. A latest-generation spot-check (Claude Sonnet 5, gated on a clean full-replay control) reproduces the pattern. Swapping a memory's implementation moves task success by up to 60 points, and full replay is never economical: the best condition per domain delivers 2.7-3.9x its marginal utility per dollar. We release the benchmark, harness, and all traces.

---


### 6. [AutoFyn Technical Report: Non-Parametric Expert Iteration for Long-Horizon Agents](https://arxiv.org/abs/2609.05446)

**<font color=#1a73e8>作者：</font>** Adib Hasan, Daniel Schaffield, Akashnil Dutta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce AutoFyn, an agent harness inspired by the Expert Iteration algorithm, adapting a frozen model across many rounds by updating persistent state from verified reward signals rather than model weights. Each round begins from a fresh model session, and durable information is reintroduced only through explicit interfaces such as persistent memory files, reports, and repository state. Within a round, an orchestrator explores, plans and builds many alternative approaches with specialized agents, while a task-grounded verifier verifies the work and supplies an objective reward for measuring progress. This reward is distilled back into the persistent state, which updates the effective policy for the next round. In this technical report, we formalize this loop and describe its persistent state and verification interfaces. We then demonstrate its use in three domains, namely olympiad mathematics, data science, and cybersecurity. On the six fresh problems of the 2026 International Mathematical Olympiad, every model with room to improve scores higher under AutoFyn than in its provider's own coding agent. AutoFyn also built the top-ranked agent on the Spider 2.0 dbt benchmark, and has produced $16$ maintainer-confirmed vulnerability advisories in this http URL, MetaMask, pnpm, Warp, LiteLLM, Langflow, and Open WebUI.

---


### 7. [Damage-Aware Bandit Pruning for Vision and Language Transformers](https://arxiv.org/abs/2609.05448)

**<font color=#1a73e8>作者：</font>** Salem Ameen, Sunil Vadera  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Structured post-training pruning of transformers requires selecting complete functional units whose suppression causes limited degradation. We formulate structured-unit selection for language and vision transformers as a damage-aware multi-armed bandit problem under a fixed candidate-evaluation budget. Attention heads and MLP channel groups are temporarily masked on calibration batches. Paired damage is the masked loss minus the base loss on the same batch, reducing batch-to-batch variation. A smooth bounded reward drives either a UCB-style policy or fractional-Beta Thompson Sampling, and the final mask is constructed sequentially by adding one unit at each step. The selected units are functionally zeroed in the original dense checkpoint; therefore, the reported parameter effects represent effective structural suppression rather than physical compression or measured speedup. Experiments on WikiText-2, LAMBADA, and Imagenette cover GPT-2, OPT, Pythia, Qwen2.5, SmolLM2, ViT-B/16, DeiT-Tiny, and Swin-Tiny, with comparisons against random, magnitude, static-saliency, and budgeted-greedy selection. Across five seeds, the bandit methods usually reduce degradation relative to budgeted greedy in the paired language-model comparisons. Of 28 comparisons highlighted in the paper, 23 bootstrap confidence intervals exclude zero and 11 paired tests have p < 0.05; six have q < 0.05 after Benjamini-Hochberg correction across the full family of 116 dataset-wise tests. Matched-evaluation results for ViT-B/16 and Swin-Tiny indicate that their gains are not explained solely by a larger candidate-evaluation budget.

---


### 8. [Compiling VGDL into Causal Models](https://arxiv.org/abs/2609.05459)

**<font color=#1a73e8>作者：</font>** Mohit Jiwatode, Bodo Rosenhahn, Alexander Dockhorn  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning and large language models often struggle to accurately capture the causal mechanics of game environments. Standard reinforcement learning agents tend to rely on spurious correlations, while large language models are prone to hallucinating game rules. Although causal reinforcement learning improves interpretability, there is currently no formal methodology to map complex game mechanics directly into causal models. To address this, we propose a deterministic framework that compiles games specified in the Video Game Description Language into Dynamic Structural Causal Models. Rather than inferring causal structures from gameplay traces or noisy large language models' outputs, our methodology directly translates game components, including sprite dynamics, interaction rules, and termination conditions, into explicit structural equations. Each game tick represents a causal transition from state variables at time $t$ to $t+1$. By establishing this grounded mapping, the approach guarantees absolute causal fidelity to the ground-truth game mechanics. The resulting models offer transparent causal pathways that support counterfactual reasoning, causal reinforcement learning agent training, and procedural content validation. This framework provides a principled bridge between symbolic game descriptions and causally grounded game AI.

---


### 9. [SciLitBench: Benchmark and Design Principles for LLM-Powered Systematic Literature Reviews](https://arxiv.org/abs/2609.05505)

**<font color=#1a73e8>作者：</font>** Miguel Zabaleta, Baihan Lin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Systematic reviews require sustained human judgment across thousands of records, yet existing evaluations of large language models (LLMs) typically examine review stages in isolation. We introduce SciLitBench, a multi-stage benchmark spanning title and abstract screening, full-text screening, and schema-guided data extraction, with 42,981 retrieved records, 1,012 full texts, and annotations for 888 included papers. Across 22 open-weight LLMs from six model families, explicit inclusion and exclusion criteria improve title and abstract screening $F_2$ by 28.8\%, while researcher-authored rationales improve full-text screening by 15\%. Data extraction reveals a different reliability regime: performance declines from 0.97 accuracy for publication year to 0.37 Jaccard overlap for computational approach, while the strongest models recover only 30\% of annotated evaluation evidence and 25\% of limitations. SciLitBench identifies a practical boundary between high-recall screening and evidence-complete extraction and provides a reproducible resource for evaluating LLM-assisted evidence synthesis.

---


### 10. [Reasoning-Aware Compression: Identifying and Protecting Vulnerable Reasoning Circuits for Energy-Efficient LLM Deployment](https://arxiv.org/abs/2609.05512)

**<font color=#1a73e8>作者：</font>** Leonard Twagirayezu, Prasenjit Mitra  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) impose substantial energy costs during deployment, yet current compression methods apply uniform quantization across all components, risking damage to critical reasoning circuits. We present a reasoning-aware compression framework that benchmarks quantization conditions across five reasoning benchmarks, GSM8K, FOLIO, MATH-500, ProofWriter, and MuSiQue, with hardware-level GPU energy measurement; profiles per-module INT4 vulnerability across all 196-224 (layer, projection) pairs via a perturbation sweep on a held-out calibration split, then selectively restores the most sensitive circuits to FP16. Three findings emerge. First, INT4 quantization can increase energy by extending reasoning chains; a 25% power reduction becomes a net energy increase on GSM8K. Second, vulnerability is task-dependent: attention projections are more critical for mathematical reasoning, and sensitivity patterns differ by architecture in logical inference. Third, selective compression achieves Pareto-optimal points inaccessible to uniform methods: R1-Qwen-7B Top-10% on ProofWriter gains +12 pp over FP16 at -9.7% energy, validated on held-out data across five reasoning benchmarks.

---


### 11. [The Failure Happens Before the Drift: The Social Dynamics of Values in LLM Agent Societies](https://arxiv.org/abs/2609.05514)

**<font color=#1a73e8>作者：</font>** Farah Atif, Sougata Saha, Monojit Choudhury  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM)-based agents are increasingly used as proxies for human participants in social science research, yet it remains unclear whether they can faithfully simulate diverse and conflicting human value systems. We present a World Values Survey (WVS)-grounded simulation framework where culturally diverse agents with different communication styles engage in longitudinal, value-laden discussions. Across approximately 4,000 conversations involving 1,200 personas, 15 topics, and three models (GPT-4o, Gemini-2.5-Flash, and Gemma-4-E4B), we evaluate value faithfulness, value drift, and conversational realism. We find that more than 50\% of personas fail to express their assigned WVS profiles from the outset, while 2-7\% drift after repeated conversations. Ablations removing demographic details improve faithfulness for some models but do not change the broader trend: simulated value distributions still systematically deviate from the assigned WVS profiles. Compared to human discussions, simulated dialogues show a different trade-off between stylistic consistency and semantic diversity, often producing content-wise varied but stylistically repetitive exchanges. These findings suggest that current LLM agents can generate plausible conversations, but remain limited proxies for representing and preserving diverse human value profiles over time.

---


### 12. [Emergent Goal-Directed Attention in Large Vision-Language Models](https://arxiv.org/abs/2609.05517)

**<font color=#1a73e8>作者：</font>** Han Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human observers prioritize visual information according to task goals. Most computational models of naturalistic viewing are gaze-trained for free viewing, leaving open whether goal-directed attention can emerge in systems without gaze supervision. We tested two off-the-shelf vision-language models (VLMs), Qwen3-VL-32B-Thinking and Gemma-4-26B-A4B-it, on 4,887 naturalistic scenes under visual-search and free-viewing instructions. Model predictions were compared with human fixations on the same images under corresponding tasks. Both models aligned more closely with human fixations under matching goals than under mismatched goals. This crossover persisted in target-absent scenes, where alignment could not be explained by simple visual grounding, and appeared in decoder-layer readouts. Furthermore, model-thinking traces were grounded in target semantics during search and in visual prominence during free viewing. These findings show that general-purpose VLMs can generate human-aligned, goal-directed spatial priorities without gaze-specific training, informing theories of goal-directed attention and offering scalable tools for predicting where people look across tasks.

---


### 13. [CrossModalQA: A Cross-modal and Multi-hop Benchmark for Multimodal Retrieval-augmented Generation](https://arxiv.org/abs/2609.05518)

**<font color=#1a73e8>作者：</font>** Jiacheng Cai, Zijin Hong, Zheng Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the strong capabilities of multimodal large language models (MLLMs), their parametric knowledge remains incomplete and difficult to update, motivating multimodal retrieval-augmented generation (RAG) to ground responses in external text and images. However, existing benchmarks face two major limitations: (i) they typically emphasize single-hop retrieval or reasoning over a small set of provided contexts rather than open-domain evidence discovery; and (ii) they provide fragmented coverage of cross-modal reasoning paths, leaving complex multi-hop and multi-image reasoning underexplored. In this paper, we introduce CrossModalQA, an open-domain benchmark for evaluating multimodal retrieval and reasoning over heterogeneous corpora. CrossModalQA contains 1,863 question-answer pairs constructed from 4,987 Wikipedia articles and 4,431 Wikimedia Commons images. It covers five complementary reasoning paths: vision-to-text, text-to-vision, vision-to-text-to-vision, multi-image intersection, and image-set reasoning. Every question requires retrieving and composing distributed textual and visual evidence, with an average reasoning depth of 3.50 hops. We construct the benchmark through multimodal knowledge graph-guided subgraph sampling and apply rule-based consistency checking and LLM verification to ensure multimodal dependence and traceable evidence. Extensive experiments demonstrate that existing multimodal RAG systems struggle to recover complete evidence chains and can underperform closed-book models when incomplete retrieval introduces distracting context. Further analysis reveals that complete cross-modal retrieval contributes more to answer accuracy than generator scaling, while multi-image retrieval and reasoning remain the primary bottlenecks limiting end-to-end performance.

---


### 14. [Beyond "AI Helps Humans": Decision-Targeted Evaluation Design for Human-Agent Teams in the Agentic Era](https://arxiv.org/abs/2609.05527)

**<font color=#1a73e8>作者：</font>** Hamed Khosravi, Xiaoming Huo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Wherever a coding agent works under engineer supervision, or a clinical model assists a radiologist, the deployment question is whether to keep the human-AI workflow or replace it with the human alone or the agent alone. The human-AI workflow is worth keeping only if it beats both of those alternatives. Yet once it is deployed, neither alternative outcome is observed: recovering one means replaying the task under that alternative, and every replay costs expert time or compute. Under a fixed replay budget, the design question is therefore which tasks should be more likely to receive a human-only replay, and which an agent-only replay. Existing methods do not directly target this decision. Agent benchmarks do not choose which missing baseline to measure, variance-based sampling ignores which of the two comparisons is closer to failing, and Bayesian information methods focus on learning model parameters instead of making the deployment decision. We propose TEAM-Design, a rule that gives every task two replay probabilities, one per baseline. It raises a probability where the missing baseline outcome is hard to predict from what is already known about the task and where that comparison is harder to establish, and lowers it where replay is expensive. We prove that the rule solves this budgeted design problem, and that drawing the replays at random from recorded probabilities still controls the chance of wrongly declaring that the workflow beats both. We reanalyze 6 clinical settings, where no human-AI workflow beats both alternatives, and a coding benchmark, where one does, then evaluate TEAM-Design on synthetic designs and on a semi-synthetic design built from a real chest X-ray reader study. TEAM-Design works best when one of the two comparisons is clearly harder to settle than the other, and can do worse than variance-based allocation when the two are similarly difficult.

---


### 15. [DART: A DAG-Based Reputation and Incentive Framework via Blockchain-Enabled Governance for Trustworthy LLM Multi-Agent Collaboration](https://arxiv.org/abs/2609.05529)

**<font color=#1a73e8>作者：</font>** Manoj Kumala, Xinyun Liua, Ronghua Xu  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based multi-agent systems (MAS) predominantly rely on centralized orchestration and lack formal verification mechanisms for agent reliability, participation, and system-level behavioral alignment. These shortcomings leave open environments severely vulnerable to uncooperative or malicious agents. This work proposes DART, a Directed Acyclic Graph (DAG)-based reputation and incentive regulation framework for trustworthy multi-agent collaboration, combining centralized operational orchestration with blockchain-enabled decentralized governance and accountability. DART unifies DAG workflow orchestration, capability and reputation-aware task allocation, dynamic behavior updates, multi-factor incentives, and smart contract accountability paired with IPFS storage. Under this paradigm, agent selection dynamically balances task alignment, historical reputation, and workload, while post-execution behavioral evidence continuously calibrates agent trust and the probability of future participation. Evaluated across four axes, DART achieves 93.6% Pass@1 on GSM8K and builds a full-stack application in 142 s using two agents, outperforming centralized baselines. Across five independent 150-round longitudinal trials, Full DART achieves a mean task success rate of 93.33 +/- 2.26%, output quality of 0.9357 +/- 0.0117, retry rate of 0.2307 +/- 0.0816, and allocation delay of 1.1153 +/- 0.0408 s, consistently outperforming its ablated configurations DART isolates persistent and intermittent malicious agents, obtaining a 99.3% output containment rate and restoring system success to 99.8%. These results demonstrate the potential of coupling reputation, incentives, DAG-based coordination, and verifiable blockchain-enabled governance to support adaptive and accountable multi-agent collaboration.

---


### 16. [A Specialized Large Multimodal Model for Interpreting PET/CT in Head and Neck Cancer](https://arxiv.org/abs/2609.05532)

**<font color=#1a73e8>作者：</font>** Haengbok Chung, SunGyu Kim, Joo hyun Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background: Diagnosing head and neck cancer using PET/CT is clinically challenging and time-consuming due to the anatomical complexity of the region, motivating computer-aided diagnosis (CAD). Generalist Large Multimodal Models (LMMs) remain limited in medical contexts by insufficient domain-specific knowledge, privacy and security concerns, and verbosity, motivating specialized standalone LMMs. Purpose: We evaluated the feasibility of a specialized LMM for automated PET/CT interpretation in head and neck cancer using a large-scale multi-institutional PET/CT dataset, a tailored training curriculum, and autoregressive training. Methods: LLaVA-NeXT was fine-tuned using a two-level curriculum with image-conversation pairs curated by two radiologists from public data. The dataset included clinically important annotations such as primary tumor presence and metastatic lymph node location. Level 1 used 28,000 image-conversation pairs to learn basic information, including modality type and hypermetabolism. Level 2 used 12,975 pairs to learn primary tumor presence and the existence and anatomical location of cervical lymph node metastases. External validation included four institutions with diverse imaging devices. Results: The specialized LMM substantially outperformed ChatGPT and LLaVA-NeXT. In Level-2 external validation, ROUGE-L, ROUGE-S, Cosine Similarity, Precision, Recall, and F1 were 0.8751, 0.8794, 0.8324, 0.8794, 0.8711, and 0.8751, while generalist models consistently scored below 0.1. Primary tumor classification accuracy was 83.14 +/- 1.15% internally and 69.03 +/- 0.81% externally. For lymph node localization, the corresponding scores were 0.6389, 0.6257, 0.5287, 0.5782, 0.6371, and 0.6648. Conclusion: Specialized LMMs show promising results for fast, accurate PET/CT-based diagnostic support and medical education, highlighting their potential for clinical translation.

---


### 17. [SimpleMemVLA: A Simple but Effective Native-Video Memory for Vision-Language-Action Models](https://arxiv.org/abs/2609.05533)

**<font color=#1a73e8>作者：</font>** Cheng Yin, Wang Xu, Junpeng Yang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon manipulation is partially observable: the information needed to choose the next action may appear only in observations from minutes earlier. Existing memory mechanisms: retrieval banks, learned compressors, recurrent states must decide what to keep from the past before knowing what a future decision will require. This was motivated by the assumption that minute-scale history is too large to process directly, which modern VLM backbones no longer make true. In this work, we introduce SimpleMemVLA, a VLA without a dedicated memory module. It keeps the sampled history intact and passes it to the backbone in the timestamped video format the backbone was pretrained to process; the hidden states of a generated sub-task then form the only channel from history to a standard flow-matching action head. Since consecutive decisions share most of their history, prefilling the shared prefix during action execution keeps latency close to a single-frame VLA. SimpleMemVLA sets a new state of the art on four memory benchmarks without cost on general-purpose control. Holding the backbone and training setup fixed, it outperforms retrieval, compression and recurrent-state mechanisms by a wide margin, and causal interventions confirm that the policy genuinely reads its history. Code available at this https URL

---


### 18. [Dual-Latent Memory Routing for Vision-Language Reasoning](https://arxiv.org/abs/2609.05539)

**<font color=#1a73e8>作者：</font>** Hao-Xuan Ma, Jin-Fei Qi, Yicheng Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have recently made strong progress in vision-language reasoning, yet their performance often degrades as generations grow longer. A key factor is that they frequently lose track of earlier visual evidence and intermediate constraints under a monolithic growing context. Inspired by how humans separately recall what they see and what they infer when solving complex tasks, we propose DLMR, a parameter-efficient mechanism that equips MLLMs with Dual Latent Memories: a visual memory that compresses image evidence and a reasoning memory that tracks intermediate conclusions and constraints. A Router then dynamically decides which memory and how much to reuse during inference, preserving visual grounding while maintaining coherent long-horizon reasoning. DLMR is trained in three stages, from latent memory construction to selective router learning, while keeping the base MLLM frozen, yielding substantial gains on both general and reasoning benchmarks with only a small number of additional trainable parameters. Analyses further show interpretable, state-dependent routing with specialized memory roles and reduced decoding tokens over long generations. Code is available at this https URL.

---


### 19. [Knowing When Not to Answer: Abstention and Refusal Reasoning in Vision--Language Models](https://arxiv.org/abs/2609.05540)

**<font color=#1a73e8>作者：</font>** Karan Dua, Amit Agarwal, Hitesh Laxmichand Patel 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many medical conditions require diagnosis through detailed, multi-context clinical assessment rather than from visual appearance alone. Despite this, vision-language models (VLMs) are increasingly queried to interpret images in ways that touch on medical or diagnostic judgments, raising safety concerns when such inferences are unsupported. ASD diagnosis requires behavioral and developmental evidence, not static facial photographs. We audit whether VLMs abstain from this unanswerable paired-image query, and whether expressions sway non-abstaining choices.
We introduce PARITY (Paired Assessment with Reused Identity), a synthetic, demographically balanced set of identity-controlled neutral/expression portrait pairs with neutral-neutral controls. All identities are synthetic and have no ASD status; because the query is unanswerable from images, any non-abstaining selection is treated as a harmful attribution. Across contemporary VLMs, we find a clear split between refusal-first models and speculative models; in the latter, certain expressions disproportionately trigger harmful selections. Clinical guardrails and single-image framing substantially increase abstention, suggesting actionable mitigations in both prompting and interface design

---


### 20. [EdgeMem: LLM-Free Agent Memory Construction and Retrieval via Evidence-Preserving Multi-Anchor Hypergraph](https://arxiv.org/abs/2609.05553)

**<font color=#1a73e8>作者：</font>** Zeyang Cui, Jiannong Cao, Zhiyuan Wen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent memory allows LLM agents to use earlier interactions when answering new queries. Existing methods often compress interaction histories into summaries or other LLM-generated representations. Repeated generation adds cost and can discard answer-bearing details before the system knows what a future query will require. We propose EdgeMem, an agent-memory method built around a simple principle: preserve original interaction turns and organize them through complementary content, temporal, and episodic cues. EdgeMem realizes this principle with a multi-anchor hypergraph constructed by lightweight local processing. Retrieval directly returns source evidence and reserves LLM use for final answer generation, combining structured access to multi-session histories with faithful retention of the original conversation. Experiments on LoCoMo and LongMemEval-S show strong retrieval and memory-grounded question answering; on LoCoMo, EdgeMem achieves the highest strict-judge score among seven reproduced systems under a shared prompt (61.01 versus 58.70), while construction and retrieval require no generative-LLM calls. Overall, EdgeMem shows that preserving and organizing source evidence provides an effective and efficient foundation for agent memory without generative memory management.

---


### 21. [EnvCraft: Synthesizing Executable Environments in Agentic RL for Claw-like Agent](https://arxiv.org/abs/2609.05576)

**<font color=#1a73e8>作者：</font>** Yirong Zeng, Shen You, Jinhang Feng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The paradigm of LLMs has rapidly shifted from passive language interfaces to autonomous Claw-like agents that execute long-horizon tasks across stateful workspaces. While Agentic Reinforcement Learning (Agentic RL) provides a promising path to optimize these agents, its scaling is heavily bottlenecked by the severe scarcity of interactive training environments. Existing synthetic environments are strictly limited to tool-calling endpoints, rendering them insufficient for accommodating the end-to-end real-world demands of claw-like agents. To bridge this gap, we introduce EnvCraft, an automated framework for synthesizing executable environments and scalable training data. Specifically, EnvCraft employs an environment synthesis engine to build sandbox-isolated workspaces, alongside a topology-aware data generation engine to produce coherent task trajectories. Overall, we synthesize 139 interactive environments comprising approximately 20K complex tasks for Agentic RL training. Experiments on Qwen3/3.5 models (8B-32B) show that our method yields gains of up to +11.9% on Claw-style benchmarks and +8.0% on general tool-use benchmarks, with concurrent reductions in inference token cost. The results confirm that synthesized executable environments provide robust and generalizable learning signals for training.

---


### 22. [An overview of 3D Vision-Language Models](https://arxiv.org/abs/2609.05583)

**<font color=#1a73e8>作者：</font>** Márcus Lobo, Vitor Matias, Afonso Paiva 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are reshaping computer vision by aligning visual and textual embeddings, allowing models to recognize visual concepts and reason about them using natural language. Traditional 3D deep-learning models, however, are typically trained for specific tasks, such as classification, segmentation, or detection, and do not naturally support cross-modal retrieval from their embedding spaces using text or images as queries. To address this issue, Contrastive Language-Image Pretraining (CLIP)-based methods align 3D embeddings with pretrained image and text representations, giving rise to 3D Vision-Language Models (3D VLMs) that support zero-shot classification, cross-modal retrieval, and open-vocabulary recognition of 3D shapes. This tutorial provides an overview of 3D VLMs, ranging from basic definitions of 3D representations and their encoding into embeddings to cross-modal contrastive alignment, modern multimodal frameworks, and 3D Vision-Large Language Models (3D VLLMs). We present the main definitions of contrastive learning for multimodal embedding alignment and highlight recent advances in language-guided 3D Gaussian splatting, 3D shape generation, and embodied AI for robotics.

---


### 23. [Agents Trust Tools Too Much: Measuring Reliance on Unreliable Tools](https://arxiv.org/abs/2609.05587)

**<font color=#1a73e8>作者：</font>** Hoyeol Yang, Woojung Song, Taewon Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing evaluations of tool-using agents primarily measure whether an agent can successfully complete diverse tasks with tools. These evaluations generally assume that tools return reliable information. However, tool returns in real-world systems can be plausible yet incorrect. We investigate how agents respond to unreliable tool returns by evaluating fourteen LLMs using three tools-web search, LLM sub-agent delegation, and code execution. For each tool, we corrupt its returns and measure whether agents adopt the corrupted content in their final answers. Agents exhibit high levels of overtrust across all three settings: the mean adoption rate exceeds one third for every tool and reaches 68.0% for web search. Analysis of reasoning traces reveals a particularly concerning failure mode: agents often recognize conflicts and even recover the correct answer internally, yet present only the corrupted answer without warning the user. To mitigate agents' overtrust in tool returns, we intervene at three levels: prompting by the user, metadata from the tool provider, and post-training by the agent builder. Although some interventions help for particular models or tools, none consistently mitigates overtrust across tools. These findings identify overtrust in unreliable tools as a serious and persistent failure mode, motivating evaluations and interventions that enable agents to validate tool outputs and transparently communicate unresolved conflicts.

---


### 24. [SceneMosaic: Efficient and Diverse Simulation-Ready Scene Generation via Hybrid Agentic Layout Evolution](https://arxiv.org/abs/2609.05594)

**<font color=#1a73e8>作者：</font>** Xingjian Ran, Xiaoye Mo, Sihao Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diverse and simulation-ready indoor scenes are essential for interactive entertainment and embodied AI, yet their scalable generation remains challenging. Recent agentic text-to-3D scene pipelines that rely on vision-language models (VLMs) can generate scenes of high fidelity but require costly iterative object placement and refinement. Another mainstream paradigm, parametric image-to-3D scene models, produces scenes efficiently from strong priors learned from 2D images but often leads to imprecise and physically invalid scenes. More importantly, both paradigms struggle to output diverse scenes for a single input, making it hard for them to reflect the dynamically changing nature of real scenes. In this paper we propose \textbf{SceneMosaic}, a framework that combines the merits of both paradigms. It obtains the initial candidate from the learned image-based prior, and subsequently evolves the result through VLM agents, ensuring both efficiency and physical validity. Within the evolution process, SceneMosaic exploits the locality of natural scenes and decomposes a scene into independent local units, allowing separate evolution within each unit before composing the global scene via Cartesian product. On SceneEval-100, SceneMosaic matches the strongest agentic baseline in semantic layout quality with a 24x speedup, substantially reduces physical violations, and receives the highest human ratings. Our code is publicly available at this https URL.

---


### 25. [Time-Aware Assistive Navigation](https://arxiv.org/abs/2609.05596)

**<font color=#1a73e8>作者：</font>** Masaki Kuribayashi, Zhongkai Shangguan, Eshed Ohn-Bar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Can interactive vision-and-language agents learn not just what to say but also \textbf{\textit{when}} to say it? Current language models rarely plan over whether and when to realize a real-time response to a user. However, providing accurate and timely support for human decision-making, such as when guiding visually impaired individuals through urban environments, requires careful real-time responsiveness--poorly timed responses can distract users or add unnecessary cognitive load. As a machine intelligence challenge for Multimodal Large Language Model (MLLM)-based agents, we introduce a large-scale multimodal benchmark for an egocentric, assistive navigation task in complex outdoor environments. Using this benchmark, we uncover a fundamental limitation of off-the-shelf MLLMs in delivering safe and time-sensitive navigation instructions, even with model fine-tuning on substantial amounts of data. We then demonstrate that a simple yet effective modification of the model, including direct supervision to predict the underlying reason for each instruction, yields significant performance gains across open-loop, closed-loop, and sim-to-real generalization settings. However, our analysis highlights persistent challenges in temporal reasoning, safety-critical object awareness, and relational and distance understanding. To advance the development of scalable assistive agents, we will release our simulation, benchmark, and code (available at the project website: this https URL).

---


### 26. [TamilEOT: A Dataset and Model for Semantic End-of-Turn Detection in Tamil Telephone Speech](https://arxiv.org/abs/2609.05631)

**<font color=#1a73e8>作者：</font>** Santhoshkumar V  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A voice agent has to decide, at every pause, whether the user has finished speaking. Without a model of the language that decision falls back to a fixed silence timeout: set it short and the agent interrupts, set it long and every turn pays the full wait. Open semantic end-of-turn detectors exist, but to our knowledge none covers a South Indian language. We release TamilEOT: 18,485 labelled turn boundaries cut from 116 real Tamil telephone conversations, and two audio-only detectors fine-tuned from Smart Turn v3. On a held-out split of 4,168 clips from 30 unseen calls, accuracy rises from 70.30% zero-shot to 83.71% (8.7 MB) and 86.13% (21 MB); ROC-AUC rises from 0.751 to 0.921. Both models run in under 150 ms single-threaded on a laptop CPU. We also report what building it cost. Rule-derived labels, checked against a blind human listening pass, were right 95.9% of the time on the positive class and 44.4% on the negative class, which is below chance, because the rule answered a different question than the model is asked. Replacing them with an audio-LLM labeller measured at 97.5% human agreement cost US$5.69. Of every training lever we measured, only encoder capacity moved the result; three runs at identical config and seed span 0.87 accuracy points, which is the floor below which none of our other deltas mean anything. Replaying the same labelled boundaries through the production VAD and streaming adapter costs a further 2.60 points, and 7.8% of boundaries are never surfaced to the model at all. Data, weights, code and every negative result are public.

---


### 27. [Unsupervised Transfer Clustering for Mitigating Cold Start in Active Prompt Learning](https://arxiv.org/abs/2609.05636)

**<font color=#1a73e8>作者：</font>** André Camargo Portella, Samuel Felipe dos Santos, Jurandy Almeida  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are able to achieve impressive zero-shot classification performance by aligning visual and textual representations, but each new task still demands handcrafted prompts. Active Prompt Learning (APL) combines Active Learning (AL) and Prompt Learning (PL) into a single framework, allowing for the usage of the VLM prior knowledge for iteratively querying the most informative images to be labeled. However, the cold-start problem is still relevant for APL methods, where the performance of the initial query can be worse than random sampling. While recent state-of-the-art APL methods mitigate with balanced sampling and multimodal features, they rely on rigid, distance-based clustering to group these features. This simplistic approach can struggle to capture the complex, high-dimensional semantic distributions inherent to VLMs, leading to suboptimal query representativeness. Unsupervised transfer can be applied to these features as a possible alternative, since it is capable of inferring the underlying human labeling of a task without any form of supervision. This way, samples can be grouped in semantically coherent clusters. This paper proposes Unsupervised Transfer Clustering with Selective Querying (UTC+SQ), a framework that enhances a recent APL approach by leveraging state-of-the-art unsupervised transfer model. These models generate high-fidelity pseudo-labels that establish semantically meaningful clusters, allowing for the selection of more relevant samples. Experimental evaluations demonstrate that shifting from distance-based to projection-based clustering improves the representativeness of the queried subset, achieving accuracy gains in 6 of the 8 datasets tested.

---


### 28. [Better Together: Complementary Query Rewriting Under a Strong RAG Baseline](https://arxiv.org/abs/2609.05637)

**<font color=#1a73e8>作者：</font>** Sara Shanian, Xiaoqin Yi, Pavlo Ruban 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A popular way to improve Retrieval-Augmented Generation (RAG) is to rewrite the user's question into several variants and search with all of them. We test whether this actually helps once the underlying search is already strong. Under one fixed, competitive pipeline (BGE dense retrieval, cross-encoder reranking, and MMR diversification), we compare four query-rewriting strategies (S1-S4) against two strong LLM baselines (HyDE, Query2Doc) on three datasets (HotpotQA, AmbigNQ, and the 512K-document EnterpriseRAG-Bench) over three seeds with paired-bootstrap significance tests. Our headline result is that rewriting alone is at best competitive with a strong baseline, but combining methods yields outsized gains because different strategies fail on different questions. A post-hoc union of four methods (S1+S3+S4+HyDE) improves HIT@10 over the baseline by +12.5 points on enterprise data (51.70 vs 39.22), and a five-method union reaches 52.98 (+13.8). Budget-matched controls capture only ~40% of this gain, confirming that complementarity, not retrieval budget, is the primary driver. On HotpotQA the union adds +1.6 to +1.8 points (p<0.001), saturating the all-method oracle; on AmbigNQ the same fusion hurts (-2.4 below the best solo, p<0.001), and we analyze when and why. Because rewriting is expensive, we evaluate in simulation a confidence-gated router that runs rewriting only when the baseline's own top-1 score is low. It captures about half of the enterprise full-merge gain (+4.3 HIT@10) while paying rewriting cost on <40% of queries, and automatically declines to rewrite on AmbigNQ. A downstream answer-quality evaluation confirms the router improves F1 by +1.92 (p<0.01) at roughly 40% of the expansion cost. In short: treat query rewriting as a complementary coverage source, applied through cost-aware routing, not as a standalone replacement for a strong baseline.

---


### 29. [Facial Age Estimation for Age Fraud Detection in National ID Systems](https://arxiv.org/abs/2609.05638)

**<font color=#1a73e8>作者：</font>** Sharib Athar, Arka Koner, Chetan Naik 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identity fraud during biometric enrollment and updates remains a major challenge for large-scale national identity systems. A common fraud vector is misrepresenting one's age to access age-restricted services or welfare schemes. In this work, we present SwinAge, a facial age estimation system designed for use within the Aadhaar biometric enrollment pipeline, to assist quality-check (QC) operators to flag potential age-related fraud. This is critical for a system like Aadhaar (the world's largest national identity programme), that holds about 1.5 billion unique identities, with 22.4 million new enrollments and 283 million updates in the last year. Building upon the SwinFace architecture with landmark-based similarity (warp affine) alignment, we train on a large in-house dataset of 1.45 million face images and evaluate on an independent, age-stratified test set of 283K images, both drawn from an ethnically diverse population of 716K unique subjects. We investigate three Aadhaar-specific operational thresholds (5, 18, and 60 years) and propose a deployment triage framework that flags suspected cases for manual review. Following NIST FATE, we report false acceptance/rejection rates (FAR/FRR) at each threshold rather than aggregate accuracy: at 1% FAR the model achieves an FRR of 3% (<5yrs), 0.4% (>18yrs) and 11.0% (>60yrs). SwinAge achieves a mean absolute error (MAE) of 2.94 years on the same test set, outperforming three zero-shot vision language models on all benchmarks, and improving the state-of-the-art on 5 out of 7 public benchmark datasets. We further report per-gender errors and distill lessons for national identity programs.

---


### 30. [Robustness of LLM-Generated SystemVerilog Assertions to Semantics-Preserving RTL Transformations](https://arxiv.org/abs/2609.05658)

**<font color=#1a73e8>作者：</font>** FNU Aditi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly being explored for automating SystemVerilog Assertion (SVA) generation, yet most evaluations report correctness on a single syntactic representation of an input. Such point accuracy does not reveal whether a model's correct output is stable when the same RTL behavior is written differently. This paper presents a controlled metamorphic evaluation of LLM-based SVA generation under semantics-preserving RTL transformations. Starting from the VERT dataset, we construct a quality-filtered conditional-control pool and a stratified 40-program evaluation set containing 295 assignment behaviors. We evaluate two open code models, Qwen2.5-Coder-7B and DeepSeek-Coder-V2-Lite, with an identical evaluation prompt and greedy decoding. Three transformations are studied: operand reordering, deterministic identifier renaming, and redundant parenthesization. Beyond baseline and transformed accuracy, we measure conditional robustness, invariance failure, and any-flip rate, with 10,000-sample clustered bootstrap intervals at the RTL-program level. Across all six model-transformation conditions, 9.7%-27.0% of behaviors that were correct on the original RTL become incorrect after a semantics-preserving transformation. Aggregate accuracy can therefore hide substantial instability: under identifier renaming, DeepSeek-Coder-V2-Lite improves from 53.9% to 63.7% accuracy while 19.5% of its originally correct behaviors fail. Manual review of 30 sampled correct-to-wrong transitions identifies dropped path predicates, branch-polarity errors, Boolean-structure corruption, and output-contract violations. The results show that point accuracy alone is insufficient for characterizing LLM reliability in assertion generation and motivate robustness-aware evaluation for AI-assisted hardware verification.

---


### 31. [What LLM Trading Agents Actually Do in Production: A Six-Month, Population-Scale Record from Two Fleets](https://arxiv.org/abs/2609.05663)

**<font color=#1a73e8>作者：</font>** T.J. Barton, Chris Constantakis, Patti Hauseman 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a continuous, population-scale measurement record of autonomous language-model trading agents operating in production across two systems with one design lineage: DX Terminal Pro (3,505 user-funded vaults trading real ETH in Base memecoin markets for 21 days, February to March 2026) and the DXAP live alpha fleet (500 to 599 user-created agents all-history, 91 to 117 concurrently active, trading Hyperliquid perpetuals, June to August 2026). The record spans roughly six months, 7.5M single-model invocations with about 300K onchain actions, and a further 231,638 multi-tool turns producing 14,596 fills. Four findings carry the paper. First, the operating layer determines behavior more than anything written in strategy text: a risk slider explains leverage (+0.425 per level), agent fixed effects absorb 60% of variance, and a leaderboard render boundary causally routes selection (regression discontinuity 1.75x at the top-3 cut). Second, sizing is volatility-blind: median leverage is 5.0x in every volatility sextile, and one posture-slider cell (11% of the book) holds 62% of liquidations. Third, agents capture almost none of the upside they reach: 43.2% of positions saw at least +300 bps of favorable excursion within 24h, yet 49.3% of those closed with a negative trade return; a mechanical bracket recovers +39.0 bps per position. Fourth, neither fleet shows a directional edge. The DXAP fleet is not profitable and trails a matched Hyperliquid retail benchmark (41% vs. 50% roundtrip win rate). A paired-replay league of frontier models on 416 captured production scenarios finds decision quality statistically indistinguishable at this horizon, while choice stability differs sharply across model families. Every headline survives day-clustered inference, permutation nulls, and a common-fee restatement; the paper closes with a 17-rule methodology canon bought with our own retractions.

---


### 32. [Who Maintains Agent Skills? A Longitudinal Study of Human-Governed, AI-Assisted Skill Maintenance](https://arxiv.org/abs/2609.05677)

**<font color=#1a73e8>作者：</font>** Chen Shen, Estevam Hruschka  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Lifelong LLM agents increasingly rely on external skill artifacts as one element for preserving and reusing capabilities over time. These skills (usually portable Markdown files such as this http URL) describe when and how to apply a capability and must be corrected, expanded, and consolidated as tools and usage patterns shift over deployment. Recent work seeks to automate skill curation, but it largely evaluates against automated baselines and treats human maintenance as an unmeasured bottleneck. We study that missing process directly. We mine the full commit histories of five public AI-skill repositories, a purposive sample of AI-tooling organizations, covering 873 commits, 143 skill files, and 254 substantive post-creation edits from October 2025 to June 2026. We code each edit with pre-registered governance, operation, and trigger-evidence codebooks. Three findings emerge. First, every substantive edit is authored or merged through a named human account, while 62% carry an AI co-author trailer, with large repository-level variation. Second, these edits are genuine curation: an audited sample shows that most change skill content, and the coded operations are dominated by additions and corrections. Third, a pre-registered rule-likeness axis fails its reliability gate; reliably coding rule-likeness from commit artifacts remains an open measurement problem. We release the corpus, codebooks, mining scripts, and a replay protocol for automated skill curators. For self-evolving agents, public skill maintenance currently looks less like an autonomous pipeline than a human-governed, AI-assisted loop that future curators must measure against and operate within.

---


### 33. [A Rubric-Guided Large Language Model Solution for Opioid Use Disorder Computable Phenotyping](https://arxiv.org/abs/2609.05682)

**<font color=#1a73e8>作者：</font>** Mengxian Lyu, Paredes Pardo, Cheng Peng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Opioid use disorder (OUD) remains a public health crisis in the United States, yet it is difficult to identify from electronic health records (EHRs) because missing diagnosis codes and supporting evidence are buried in clinical narratives. Accurate OUD identification is critical to support interventions and improve health outcomes. This study developed a rubric-guided large language model (LLM) that incorporated Optimization by PROmpting (OPRO) for OUD computable phenotyping (CP). The framework used an 18-item, expert-identified rubric to instruct LLMs to automatically extract critical text with supporting evidence to determine OUD flags. Two UF Health physicians (GMR and WMG) chart-reviewed 253 patients, including 68 OUD-positive cases. Our LLM-based computable phenotype (CP) achieved the best F1 score of 0.774 and an AUROC of 0.934, outperforming the machine learning-based CP using EHR and natural language processing-extracted variables, and zero-shot LLMs by relative F1 improvements of 12.8% and 44.4%, respectively. The proposed LLM-based CP could link LLM-extracted evidence to OUD phenotyping for better explainability.

---


### 34. [GraphNOSE: A Graph Transformer in Olfaction](https://arxiv.org/abs/2609.05694)

**<font color=#1a73e8>作者：</font>** Mrityunjay Sharma, Sarabeshwar Balaji, Valentina Parma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting olfactory qualities from molecular structure is an open problem in chemoinformatics. Although linear models can link molecular features to odor descriptors, they often fail when extrapolating to novel chemical scaffolds, extreme molecular weights, or complex odor mixtures. To address this, we introduce GraphNOSE, an open-source graph transformer framework that predicts multi-label odor descriptors from simplified molecular-input line-entry system (SMILES) strings for single molecules and binary mixtures. By integrating positional and structural encodings within a transformer-based graph architecture, GraphNOSE achieves strong performance with six times fewer parameters than standard graph neural network (GNN) baseline while consistently outperforming linear models, molecular language model embeddings, molecular fingerprints, and baseline GNNs by an average area under the ROC curve (AUROC) margin of 4.52% (p < 0.01). GraphNOSE achieves an AUROC of 84% on out-of-distribution compounds (OODs). This exceeds the current state-of-the-art GNN for OOD in olfaction (Open-POM: 81%, p < 0.001), and identifies conditions under which linear models empirically fail. Finally, we apply XAI (explainable AI) methods to identify which substructures and molecular features drive odor predictions, yielding insights consistent with chemical intuition and grounded in the model's learned representations. Together, these results establish GraphNOSE as a scalable and interpretable architecture for olfactory prediction that generalizes to structurally distinct compounds underrepresented in current perceptual databases.

---


### 35. [Intra-Prompt Parallel Decoding for Common-Context Question Answering](https://arxiv.org/abs/2609.05707)

**<font color=#1a73e8>作者：</font>** Theodore Glavas, Nikhita Vedula, Dushyanta Dhyani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In common-context question answering (CCQA) tasks, multiple input questions share a common context to base their answers from. However, Large Language Models typically generate each answer using an independent prompt. While existing batching and caching techniques help improve parallelism and reduce repeated computations, the separation of questions across prompts limits the achievable speedup, as modern GPUs are underutilized due to a memory bottleneck during attention. We present Intra-Prompt Parallel Decoding (IPPD), a novel inference method that answers multiple common-context questions in parallel within a single prompt. IPPD directly addresses the bottleneck by efficiently sharing both memory and computation during the attention process, as the next token for every question is decoded in a single inference step. IPPD uses virtual position IDs and attention mask manipulation to generate the same output as standard prompting without requiring fine-tuning or any changes to the LLM architecture. Since all parallelism occurs within a prompt, IPPD is fully compatible with batched inference, even when each prompt features a different context. Our experiments show that IPPD delivers up to 7X the effective throughput as standard decoding without quality degradation, and outperforms prefix caching with PagedAttention in most settings.

---


### 36. [CUSP: Decomposable Collective Uncertainty for Multi-Agent Multimodal Reasoning](https://arxiv.org/abs/2609.05708)

**<font color=#1a73e8>作者：</font>** Chung-En Johnny Yu, David Garcia, Brian Jalaian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aggregating heterogeneous vision-language models (VLMs) can improve multimodal reasoning, but neither an individual model's confidence nor that of the aggregated answer measures reliability at the system level. We present CUSP (Collective Uncertainty through Semantic Opinion Pooling), a training-free uncertainty quantification framework that maps multiple VLM responses to a shared semantic response space, pools them into a pooled semantic opinion, and reports two complementary system-level signals: collective uncertainty, the dispersion of the pooled opinion, and Jensen-Shannon divergence (JSD), the conflict among the model-level opinions. Within this pooled semantic opinion, the unnormalized collective entropy decomposes exactly into the mean of the models' individual semantic entropies and the JSD, separating total dispersion from model conflict. Requiring neither token logits nor calibration labels, CUSP applies to open-weight and commercial VLMs alike. In static multi-VLM ensembles, collective uncertainty is the strongest signal in the small-model regime (0.764 AUROC for prediction-error detection, 0.889 AUARC for abstention), outperforming uncertainty baselines majority voting and naive selection by 4.7 to 15.8 points and widening its margin as the ensemble grows; JSD is strongest in the evaluated commercial regime (0.819 AUROC, 0.910 AUARC) and ranks hard-answer model conflict with AUROC up to 0.982. The pooled prediction also improves accuracy over the average single model by 5.6 to 13.0 points. Over the full trajectory of a multi-step, multi-agent system, subagent collective uncertainty ranks system failures above chance (0.619 AUROC) and gives the best abstention ordering among the evaluated signals (0.699 AUARC).

---


### 37. [Recovering Temporal and Geographic Signals from Language Model Embeddings](https://arxiv.org/abs/2609.05721)

**<font color=#1a73e8>作者：</font>** Esteban Feuerstein, Victoria Klimkowski, Juan Manuel Ortiz de Zarate 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding whether language-model embeddings encode structured real-world information is important for both representation analysis and information retrieval. We study this question for temporal and geographic signals using a simple projection-based method that operates directly on output embeddings. Given a small set of seed examples, the method defines an axis in embedding space and ranks texts or entities by their projection onto that axis. Our approach is fully black-box and model-agnostic: it requires only embeddings, without access to model weights, internal activations, auxiliary probes, or additional training. This makes it applicable to modern embedding models available only through APIs and provides a lightweight way to analyze whether temporal and spatial dimensions are present in their representation spaces. We apply the method to temporal and geographic datasets and find that embedding projections recover meaningful chronological and spatial structure. These results provide evidence that output embeddings encode signals relevant to time and space, while also offering a practical tool for interpretability and for downstream temporal and geographic information retrieval tasks, such as temporal ordering, geographic ranking, and tagging.

---


### 38. [Beyond Prompts: Measuring and Optimizing LLM Tool-Agent Harnesses](https://arxiv.org/abs/2609.05736)

**<font color=#1a73e8>作者：</font>** Zhao, Haibo Ruan, Wenjie Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM tool agents can be improved without retraining by modifying the runtime harness around a fixed model: prompts, tool interfaces, middleware, state handling, and recovery logic. We study this setting as resource-bounded harness selection for fixed-model multi-turn tool agents, with the search surface scoped to prompts and tool-boundary middleware: edits are guarded intercepts at the tool boundary, not arbitrary rewriting of agent execution logic. Our optimizer-agnostic protocol reports mean held-out lift, worst-condition lift, repeatability, logged cost diagnostics, and RelLift95(B), a conservative estimate of the held-out gain of the harness selected under budget B. We instantiate the protocol with prompt-only and prompt-plus-middleware optimizers, including PRISM, which clusters failures and routes repairs to prompt, tool-boundary middleware, or joint edit surfaces within a Pareto search. On BFCL multi-round, tau2-Retail, and tau2-Telecom, PRISM obtains mean held-out lifts of 14.2, 14.9, and 10.1 percentage points and positive empirical RelLift95 on all three benchmarks, and a component ablation attributes the margin chiefly to failure-surface routing and the edit-pattern constraint. Across optimizers, the results show that some search procedures can occasionally find large gains but still choose brittle updates, so the reliability of the chosen harness should be reported alongside average held-out lift.

---


### 39. [SimTIO: A Simulation-Grounded Multi-Agent LLM Framework for Compositional Traffic Intervention Optimization](https://arxiv.org/abs/2609.05740)

**<font color=#1a73e8>作者：</font>** Shuyang Li, Ruimin Ke  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Traffic analysts must translate diagnosed bottlenecks into executable interventions without allowing local improvements to degrade network-wide performance. This study presents SimTIO, a simulation-grounded multi-agent large language model framework for composing and selecting traffic interventions under explicit operational constraints. SimTIO first simulates an unmodified SUMO scenario to identify a baseline-frozen set of ten bottleneck edges. A grounded sampler then initializes signal-control, corridor-speed, and demand-preserving routing actions, while three specialist agents use measured simulation feedback to select one-parameter refinements from validator-confirmed mutation catalogs. Compatible actions are combined and re-simulated so that their interaction effects are measured rather than inferred. Final selection minimizes bottleneck time loss while constraining network-wide delay, neighboring-road spillover, throughput loss, and teleport events, with the unmodified scenario retained as a no-operation guard. Across 15 cases covering five U.S. urban networks, three synthetic-demand seeds, and 2,400 origin-destination trips per scenario, SimTIO reduced Top-10 bottleneck time loss by an average of 9.18 percent and network-wide delay by 2.78 percent. It found a feasible improving plan in 86.7 percent of cases, compared with 73.3 percent for grounded random search and 80.0 percent for a deterministic heuristic under the same seven-simulation budget, although the differences in Top-10 improvement were not statistically significant. These results support using LLMs as constrained, feedback-guided local search operators while reserving final decision authority for executable tools, microscopic simulation, and explicit safety constraints.

---


### 40. [SeRV: Semantic-Aligned Residual Vector Quantization for American Sign Language Generation](https://arxiv.org/abs/2609.05742)

**<font color=#1a73e8>作者：</font>** Hongyu Wu, Xu Wu, Tianhao Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> American Sign Language (ASL) generation remains challenging due to limited paired text-ASL motion data and the difficulty of learning motion representations both precise for reconstruction and predictable from linguistic input. Existing methods rely on motion tokenizers optimized for reconstruction, without explicit semantic supervision from paired text. As a result, the learned tokens remain limited in supporting semantically consistent and fine-grained ASL motion generation. To address this limitation, we propose SeRV (Semantic-Aligned Residual Vector Quantization), a semantic-aligned RVQ tokenizer for ASL generation. SeRV learns a semantically structured residual token space by combining sentence-level motion-text alignment with token-level text-conditioned supervision. Building on this tokenizer, a Hierarchical GPT predicts residual motion tokens in a coarse-to-fine manner, generating structurally coherent and semantically aligned 3D ASL motion. We further construct a large-scale reconstructed 3D ASL motion-text benchmark by recovering paired 3D motion from YouTube-ASL videos. Experiments across 375 hours of ASL video show that SeRV achieves state-of-the-art pose accuracy on both How2Sign and YouTube-ASL datasets, while producing semantically consistent 3D ASL motion directly from text.

---


### 41. [Some Tokens Behave like Magnets: Revealing Linguistic Organization in the Layers of Language Models](https://arxiv.org/abs/2609.05743)

**<font color=#1a73e8>作者：</font>** Andrew Liu, Devan Srinivasan, Gerald Penn  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We identify a special group of token vectors inside large language models (LLMs), which we term magnetic vectors, that organize the surrounding tokens by either attracting or repelling them. Particularly, tokens pointing the same way as an attracting magnet are elongated; tokens pointing the same way as a repelling magnet are compressed. Just as physical magnets pull or push away the iron filings around them, these vectors organize their surroundings through two opposing polarities. Moreover, we identify a statistically significant pattern in linguistic category where function words consistently act as repelling magnets in early layers, and we also find magnets consistently reorganize their polarities in unique ways deeper in the model. In a further case study we find this observation may unveil a deliberate, layer-wise organization in how LLMs process language.
This pattern is consistent across different LLM architectures, sizes, and layer configurations. It is also causally relevant. When the LLM is fine-tuned for a downstream task, the task-functional tokens emerge as magnets. E.g., in question answering, the answer-span tokens become uniquely repelling magnets in the final layer, geometrically carving the answer out of the surrounding context. Furthermore, removing early-layer repelling magnets devastates syntactic tasks (POS tagging accuracy drops from 91% to below 10%) while sparing semantic ones, and removing late-layer attracting magnets does the reverse. We believe this phenomenon warrants further investigation, as it opens the first probe-free path to understanding how language models geometrically organize linguistic computation across their layers.

---


### 42. [CrisisKD: Five-Stage Knowledge Distillation for Aspect-Level Sentiment and Emotion Analysis in Crisis Discourse](https://arxiv.org/abs/2609.05757)

**<font color=#1a73e8>作者：</font>** Marko Haralović, Onat Akca, Salih Eren Yücetürk 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Identifying the target of emotional words or phrases in crisis situations, especially health-related ones, is important for understanding public concerns across cultural and linguistic contexts. We propose CrisisKD, a five-stage teacher--student knowledge distillation framework for aspect-level sentiment and emotion analysis on unannotated social media data. A teacher LLM generates aspect-level labels and reasoning traces that supervise a smaller student model across aspect extraction, syntactic parsing, opinion extraction, sentiment classification, and emotion classification. Using this framework, we construct and release a dataset containing 50,615 aspect-level labels, together with the annotation and fine-tuning scripts as open-source resources. The resulting student supports end-to-end ABSA and emotion detection at substantially lower inference cost than the teacher. On a manually annotated 500-tweet gold set, the 5-task Qwen2.5-7B student improves over the untuned model by 7.9 F1 points on aspect extraction, 17.0 points on emotion accuracy, and 6.5 points on sentiment accuracy. On the external ABEA benchmark, CrisisKD improves the same-model Qwen2.5-7B ICL baseline by 2.8 F1 points on ATE and 3.8 F1 points on joint ATE+AEC.

---


### 43. [From Monolithic Blending to Agentic Orchestration: Dynamic Response for Conversational Assistants at Scale](https://arxiv.org/abs/2609.05758)

**<font color=#1a73e8>作者：</font>** Zhao, Peng Wang, Chuan Shi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conversational assistants can blend retrieval, action selection, escalation, and wording in a single model path, or separate those roles. We report a production migration of a customer-support assistant at a large accommodation marketplace (millions of conversations per month, 11 languages, 10-second P90). Dynamic Response (DR) replaces a single Qwen3-235B-A22B blended responder with a bounded ReAct orchestrator over typed tools plus a smaller generator that writes from a backend-validated context contract. Because the migration also changed prompts, alignment, and serving, we attribute each effect to its cause and claim as architecture effects only those measured on identical replayed turns: typed entity selection moves the reservation selector to a precision-first operating point (precision 8.3% to 89.1%, recall 75.2% to 67.3%), and typed action IDs with a membership check remove observed structured-action hallucination (2.14% to 0.0%). A low-ramp A/B test reproduces the replay escalation reductions: hard-escalation responses fall from 5.60% to 3.08% and soft-escalation responses from 9.56% to 2.49%, while production handoff volume holds roughly steady; self-solve is directional (+5.1 points, 95% CI [-2, +12]). Serving optimizations cut orchestrator P90 latency from 3.87s to 2.24s on a GPU footprint reduced by roughly one-third, and self-hosting reduces estimated annual model-serving cost by more than an order of magnitude.

---


### 44. [GeoContext: One Context Ladder, Two Failure Modes in Vision-Language Geolocation: Flat Reliance on User-Provided Location Context and False Confirmation of Location Claims](https://arxiv.org/abs/2609.05761)

**<font color=#1a73e8>作者：</font>** Yifan Zhang, Kai Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual geolocation benchmarks typically ask a model where an image was captured without accounting for the location context that users often provide. We introduce GeoContext, a resource supporting two complementary tasks: GeoHint, open-ended localization given a true but coarse location hint, and GeoVerify, binary verification of whether an image was taken within 150 m of a claimed place. GeoContext constructs a context ladder by stratifying nearby reference points according to distance and referenceability, allowing the image to remain fixed while the supplied context varies. The benchmark covers 109 sites in 30 cities and evaluates five vision-language models using 21,933 GeoHint responses and 6,270 GeoVerify responses.
Our evaluation reveals three main patterns. First, hint repetition varies by only 1.5 percentage points across referenceability tiers and by less than 3 points across distance bands, while the resulting localization error increases steadily with hint distance. Second, behavior depends strongly on no-context performance: at sites with low no-context accuracy, the median ratio between localization error and hint distance is approximately 1.00, whereas at higher-accuracy sites it ranges from 0.24 to 0.69. After correcting for bias introduced by the site grouping procedure, only one of the five models retains a negative accuracy estimate when given a nearby hint. Third, in GeoVerify, no model reaches d' = 1 for decoys immediately beyond the 150 m tolerance. Model rankings also change when sensitivity is separated from response bias, and 83.8% of false acceptances are reported with confidence of at least 0.8. We release the benchmark, construction pipeline, audit decisions, and scoring code.

---


### 45. [Data Scout: Targeted Web Crawling for Domain-Specific Pretraining Corpora](https://arxiv.org/abs/2609.05766)

**<font color=#1a73e8>作者：</font>** Chirag Garg, Eelaaf Zahid, Farhan Ahmed 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The dominant approach to building domain-specific pretraining corpora is to filter large web archives such as CommonCrawl. This works well for popular domains but breaks down for specialized ones, where relevant content is sparse and often beyond the reach of popularity-driven crawlers. We present Data Scout, which inverts this: instead of filtering an archive, it directs a targeted crawl. An LLM expands a root topic into a taxonomy and thousands of search queries; the returned URLs (seeds) are grouped by subdomain and screened with a user-supplied classifier (the probe), admitting each subdomain on the basis of a small sample. This works because relevance has a sharp boundary at the subdomain level: in mathematics, a page is 21x more likely to be relevant than one on a sibling subdomain. With the FineMath classifier as the probe, 21.9% of crawled pages are high-quality math content, 70x the 0.31% rate from filtering a comparable web sample, so the crawl wastes far less effort. But the payoff is not just efficiency: 63.2% of these pages are missing from CommonCrawl altogether, yet just as useful for training. Continued pretraining of Llama-3.2-3B on 1.9B Data Scout tokens matches FineMath corpus on GSM8k. Because the probe is the only domain-specific component, Data Scout can in principle apply to any domain with such a classifier.

---


### 46. [Will My Assistant Remember My Allergy? What Personal LLM Assistants Forget When Conversation Memory Is Compressed](https://arxiv.org/abs/2609.05767)

**<font color=#1a73e8>作者：</font>** Lichen Zhu, Yueqian Lin, Yiheng Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Personal LLM assistants (health companions, elder-care agents, accessibility aides) are judged by what they remember about a person: a medication or an allergy mentioned in passing and needed days later. Privacy pushes them on-device, where a month of conversation can outgrow the model's own weights, so an eviction policy must decide what the cache forgets. Benchmarks report that eviction keeps such facts at a 20% budget, but they compress a prompt that already contains the user's future question, foresight no cache-reusing assistant has. Hide the question until after compression and the advantage vanishes: on PA-Bench, 100 assistant conversations we construct, an allergy mentioned in passing survives to the question that needs it 0--1% of the time, against 97% with full memory. The cause is the budget, not the scorer: none of the training-free policies we evaluate ranks the fact high enough, and the budget that would keep it is too large to bother compressing. A compressed cache is an inference-reuse mechanism, not a persistence layer: safety-critical facts need an auditable episodic store alongside it, and an interface that asks rather than invents.

---


### 47. [RAPTOR: Role-Aware Private Training for Mixture-of-Experts](https://arxiv.org/abs/2609.05770)

**<font color=#1a73e8>作者：</font>** Duc Dm, Khai Le-Duc, Nguyen Do 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differentially private (DP) fine-tuning methods treat sparse Mixture-of-Experts (MoE) models as a single dense block, ignoring that shared layers see all data while experts only see routed records. We identify and formally characterize three resulting failure modes: global clipping suppresses expert gradients, batch-level normalization dilutes sparse expert updates, and fixed privacy noise degrades signal-to-noise ratio on low-load experts. We introduce RAPTOR - a Role-Aware Private Training framework, which alternates shared and expert optimization and targets each failure directly, using expert-specific clipping and noise together with a public expected-owner denominator and a count-independent update schedule that avoids conditioning on private, realized expert counts. We prove the resulting mechanism satisfies $(\varepsilon,\delta)$-DP: because each record is assigned to exactly one owner expert, per-expert mechanisms within a layer compose in parallel, so updating all $E$ experts costs no more, in privacy terms, than updating one, with shared and expert streams composing sequentially across training. We further derive a bias-variance decomposition of the public-denominator estimator showing its bias grows predictably with routing imbalance, yielding a privacy-free rule for selecting which layer to protect from routing entropy measured on a small public corpus. Experiments on Switch Transformer and OLMoE fine-tuning across GLUE tasks, and on DeepSeek-VL2-Tiny, show consistent gains over standard DP baselines across several privacy levels ($\varepsilon$), with the largest margins typically at the tightest budgets. Code and models are publicly available: this https URL

---


### 48. [Inference-Time Graph Engineering for Multi-Agent LLM Workflows](https://arxiv.org/abs/2609.05774)

**<font color=#1a73e8>作者：</font>** Katherine Tieu, Dongqi Fu, Yinglong Xia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent multi-agent LLM systems increasingly rely on graph-structured communication to coordinate specialized agents. We revisit multi-agent orchestration from a graph-engineering perspective: rather than optimizing a static topology, we synthesize a task-conditioned temporal workflow graph that jointly specifies agent connectivity and edge-level communication semantics. We introduce ReActNet, a training-free framework that compiles a query and a set of role-specialized agents into a sequence of directed communication graphs. Each graph snapshot corresponds to one reasoning stage, and each edge carries a natural-language instruction specifying the message that a source agent should provide to a target agent. The compiled temporal graph is then executed through structured message passing: agents update their reasoning states by integrating their previous states with messages from controller-assigned neighbors, and a final aggregator synthesizes the resulting states into the answer. This design separates graph compilation from graph execution, making multi-agent coordination explicit, inspectable, and task-conditioned without requiring reinforcement learning or gradient-based topology optimization. Across knowledge reasoning, mathematical problem solving, code generation, and GAIA-style assistant tasks, ReActNet consistently improves over fixed-topology and learned-topology baselines while maintaining competitive inference cost. These results suggest that effective multi-agent orchestration depends not only on which agents communicate, but also on engineering executable workflow graphs that encode when, why, and how information should flow during reasoning.

---


### 49. [DI-Bench: Systematically Generating In-Domain Data Intelligence Benchmarks for Enterprise Agents](https://arxiv.org/abs/2609.05776)

**<font color=#1a73e8>作者：</font>** Jiangyun Zhang, Kristen Surrao, Torpong Nitayanont 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating enterprise agents on domain-specific benchmarks is critical, yet public benchmarks rarely evaluate whether agents can integrate business knowledge with analytical computation, and constructing such benchmarks manually is costly. We present DI-Bench, a pipeline for generating realistic benchmarks for data intelligence (DI), the practice of extracting insights from large volumes of enterprise data. To emulate realistic DI tasks that require both computation and knowledge retrieval, DI-Bench builds an artifact linkage graph over data tables, dimensions, metrics, and documents to form questions involving structured data and associated knowledge. Ground truth answers are derived via query execution, followed by LLM question generation and validation. Applied to two public datasets, the pipeline produces a 731-task benchmark covering knowledge retrieval, analytical computation, and rule-grounded reasoning. To show the discriminatory capability and difficulty of the benchmark, we evaluate four models, revealing a substantial finding: models achieve only 32% accuracy when doing computational tasks where retrieved business rules modify the computation.

---


### 50. [Distilling Vision-Language Models for On-Device Fire Understanding](https://arxiv.org/abs/2609.05782)

**<font color=#1a73e8>作者：</font>** Mohammad Kazzazi, Zixuan Liu, Siavash Khajavi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) offer a promising alternative to conventional fire detection systems by reasoning about the semantic context of a scene and thus reducing false alarms, yet their large model size makes deployment on embedded fire sensors impractical. In this paper, we study how domain-specialized VLMs can be compressed for fully on-device deployment without losing the safety-critical behavior required for fire detection. We develop a teacher-student knowledge distillation framework in which large VLMs fine-tuned for fire understanding can be distilled into lightweight students. Experiments across multiple VLM families and model scales show that compact students preserve most of their teachers' fire-understanding capability. We further deploy the distilled models on our commercial Detectium fire detection sensor and jointly evaluate reasoning accuracy, latency, and memory usage. The results show that compression and deployment affect not only accuracy but also model failure modes, with Qwen2.5-0.5B providing the strongest overall deployment trade-off. Our findings provide broader guidance for deploying domain-specialized VLMs in resource-constrained, safety-critical settings.

---


> [!TIP]
> 当前位于：**1-50**（第 1/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-483](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
