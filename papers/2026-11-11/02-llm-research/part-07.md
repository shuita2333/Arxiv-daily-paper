# 🧠 大模型相关研究 | 2026年11月11日

> 本类共 **438** 篇论文：已确认 **405** 篇，待复核 **33** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**301-350**（第 7/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-438](./part-09.md)

---

### 301. [Layer Roles Matter: Mitigating Modality Imbalance in Multimodal Emotion Reasoning via Adaptive Layer Profiling](https://arxiv.org/abs/2611.11907)

**<font color=#1a73e8>作者：</font>** Pengyu Huang, Peipei Song, Beier Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Emotion Reasoning (MER) requires perceiving and integrating emotion cues from multiple modalities. Recent advances increasingly leverage Multimodal Large Language Models (MLLMs) to enhance reasoning capacity. However, due to the inherent heterogeneity in conveying emotions across modalities, these models often suffer from modality imbalance and confront flawed emotion understanding. In this paper, we conduct an in-depth analysis on MER models and uncover two key empirical insights. (i) In MER, modality imbalance manifests two distinct failure modes: unimodal over-reliance and insufficient cross-modal utilization, which call for different intervention strategies. (ii) MLLM layers exhibit implicit functional hierarchies in multimodal emotion processing, playing separable roles in stabilizing unimodal representations and integrating cross-modal information. Motivated by these observations, we propose a Layer-Aware Modality Rebalancing (LAMR) framework by explicitly aligning intervention strategies with layer roles. Specifically, we first introduce two quantized metrics for adaptive layer role profiling. In each layer, Modality Entropy (ME) measures the dispersion of modality contributions, and Cross-modal Intensity (CMI) captures the strength of cross-modal interactions. Then, we respectively enhance modality equilibrium in stabilization layers and cross-modal propagation in integration layers. Extensive experiments on two comprehensive MER benchmarks demonstrate that LAMR effectively mitigates modality imbalance and improves emotion reasoning across diverse MLLM backbones, without additional training.

---


### 302. [Late but Valuable: Why Deadlines Change the Measured Value of LLM Reasoning](https://arxiv.org/abs/2611.11910)

**<font color=#1a73e8>作者：</font>** Sina Barazandeh, Benjamin E. Lundell, Jose Lugo-Martinez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly plan and run experiments in automated laboratories. These experiments keep running while the model reasons and run on schedules with hard deadlines. If an LLM-generated answer arrives late, the system executes a safe fallback action instead, such as rejecting a sample. This creates a systems problem that standard serving metrics do not capture. An answer that matches the fallback adds no value, and answers that differ from the fallback may require more reasoning time. Reporting answer quality and latency separately can therefore overstate the value of reasoning. We test this on synthetic sample decisions, where the best choice is known exactly and a runtime enforces the deadline. We compare one LLM's fast mode, which answers directly, with its thinking mode, which reasons first. In a prespecified replay of 1,200 new decisions, thinking answers that missed a deadline were worth about five times as much as on-time ones. Multiplying the on-time rate by the mean answer value predicted about twice the value that thinking delivered. This prediction overstated thinking's advantage over fast mode by 0.0241 per decision, and by 0.0191 in a repeat on 300 new decisions. Both 95% confidence intervals excluded zero. In a single-GPU Qwen3-8B experiment using simultaneous request bursts, raising the number of requests from 8 to 56 reduced the share of thinking answers that met a 45 s deadline from 79.2% to 1.4%, although total output tripled. Evaluations of LLM agents for laboratories should therefore measure each answer's value and arrival time together and score the action that actually runs.

---


### 303. [Can LLM Agents Organize Their Own Memory?](https://arxiv.org/abs/2611.11929)

**<font color=#1a73e8>作者：</font>** Zichuan Fu, Junjia Qi, Wenlin Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In most LLM agents, weights are fixed after deployment, so new information must be retained in external memory. Existing approaches often rely on predefined records and fixed organizational rules, which cannot readily accommodate evolving tasks and interactions. This raises the question: can LLM agents organize their own memory using ordinary documents? We introduce self-organized memory (SoMem), a framework that stores memory in linked documents. The agent decides what to summarize, how to group related information, and when to revise existing topics, and every summary it produces stays linked to the original interactions as evidence. The runtime validates updates and automatically derives temporal, relational, and recent-memory views from the organized content. At query time, the agent chooses what to search and read, following document links and inspecting original evidence as needed. On LoCoMo, BEAM-100K, and LongMemEval-S, SoMem outperforms the strongest baseline by 2.66, 3.10, and 2.00 percentage points, respectively. The constructed memory can be reused across models, and additional reasoning effort can further improve answer quality. These findings demonstrate the feasibility of agents organizing and using their own persistent memory through ordinary documents. Code is available at: this https URL.

---


### 304. [ExCritique: An Interactive Visual Interface to Evaluate AI-Generated Explanations at Scale](https://arxiv.org/abs/2611.11932)

**<font color=#1a73e8>作者：</font>** Meheraj Hossain, Avinash Reddy Mudireddy, Naimul Hoque  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Vision-language Models (VLMs) can generate natural language explanations for complex decision-making scenarios. However, these explanations can sometimes be misleading, sounding convincing while containing incorrect or unsupported information. Automated explanation-quality metrics help researchers and practitioners evaluate large collections of explanations, but their scores alone provide limited support for identifying failure cases and understanding the reliability of these metrics. This paper presents a case study on how interactive visualizations can help researchers and practitioners evaluate both AI-generated explanations and automated explanation-quality metrics across large datasets. Based on formative interviews with nine AI researchers and practitioners, we designed an interactive visualization tool named ExCritique, situated in the task of Visual Question Answering (VQA). ExCritique visualizes the distributions of multiple automated quality metrics, allows users to explore thousands of data items, filter items and inspect the evidence behind individual scores. We compared ExCritique with a baseline interface without interactive visualizations in a controlled study involving 16 AI researchers and practitioners. Our findings suggest that the interactive visualizations in ExCritique helped users identify explanation-quality issues more efficiently and better understand automated quality metrics, supporting an effective way to measure the reliability of AI-generated explanations.

---


### 305. [BharatSynthQA: A Context-Grounded Question Answering Dataset on Indian Temples and Religious Heritage](https://arxiv.org/abs/2611.11952)

**<font color=#1a73e8>作者：</font>** Riya Naik, Shivam Sharma, Swati Agarwal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> India's temples and other places of worship are among its richest repositories of cultural heritage, bringing together religious tradition, history, architecture, and art. Due to the widespread curiosity, people increasingly turn to Artificial Intelligence (AI) assistants for information about them. Current models are rarely trained or evaluated on this domain. We present BharatSynthQA, a passage grounded question answering (QA) dataset focused on Indian temples, which also covers other religious sites connected to them. Our pipeline crawls Wikipedia from topics seeded by authentic heritage sources, filters articles for topical relevance, and locations in India. Further it generates Boolean, factoid, and explanatory QA pairs with a fewshot prompted LLM. An LLM judge filters the pairs on answer correctness, retaining 98,677 of 131,494 generated pairs. Additionally, 300 human-annotated pairs are released separately as a reference set. Human evaluation of the subsample of this dataset showed 89.83% of the questions were formed correctly. Benchmarking five current LLMs shows that factoid token F1 is only 0.18-0.30 without the source passage but 0.73-0.77 with it, indicating that this domain is poorly captured in model knowledge. The dataset is available at this https URL to support research on culturally grounded QA and retrieval-augmented generation for Indian heritage.

---


### 306. [Operation-aware Multimodal Clinical Decision Support System for ICU Discharge Risk Assessment](https://arxiv.org/abs/2611.11960)

**<font color=#1a73e8>作者：</font>** Guoqing Zhang, Rafik Hadfi, Takayuki Ito  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unplanned 30-day intensive care unit (ICU) readmission is a critical benchmark for evaluating healthcare quality. Most predictive models assume readmission risk depends solely on a patient's individual pathophysiological state, ignoring hospital operational context and resource capacity. In practice, discharge decisions are dynamic trade-offs between patient stability and bed turnover pressures. To address this gap, we develop an Operation-aware Multimodal Clinical Decision Support System (CDSS) for ICU discharge risk assessment. The system combines multi-agent collaborative extraction with self-evolving retrieval-augmented generation (RAG) to eliminate template noise from progress notes, while constructing departmental workload indicators alongside admission flow features, continuous vital signs, and sparse medical codes (ICD/DRG). Addressing severe class imbalance (about 10.5% readmissions) and alarm fatigue, we implement data normalization, class reweighting, and decision-threshold calibration. In 20 independent runs across 20,000 ICU stays from MIMIC-III, empirical findings demonstrate that: vital signs alone have limited predictive capacity under real-world class imbalance (PR-AUC of 0.1387 +/- 0.0086); directly concatenating raw text embeddings degrades decision tree performance (XGBoost and LightGBM PR-AUC drop to 0.3893 and 0.4030); whereas an end-to-end multimodal fine-tuning architecture (Transformer E2E FineTune) utilizing layer-wise parameter freezing and differential learning rates reverses text negative transfer, achieving the highest AUROC of 0.8288 +/- 0.0110, PR-AUC of 0.4373 +/- 0.0310, and F1-Score of 0.4757 +/- 0.0196. Operational indicators supply independent risk signals, laying an engineering foundation for high-utility clinical decision support tools.

---


### 307. [ChainCheck: Near-Perfect Evidence-Sufficiency Scores Can Conceal Sensitivity to Construction Artifacts -- Paired Conditional Contrasts that Expose an Evaluation Confound](https://arxiv.org/abs/2611.11965)

**<font color=#1a73e8>作者：</font>** Hyojung Han, Ryangkyung Kang, Youngeun Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evidence-sufficiency benchmarks ask whether a model can tell a complete passage set from one whose reasoning chain is broken. When broken sets are made by editing text, near-perfect sufficiency scores--and even positive crossed-control scores--need not demonstrate multi-hop reasoning. We present ChainCheck, an evaluation-validity audit that pairs validator-certified counterfactual cells with artifact-only baselines. In an exploratory crossed control on 2,214 HotpotQA pairs, a language-model scorer that never reads the chain reaches a nominal AUC of 0.997, and a one-string match reaches the maximum of the crossed chain-sensitivity statistic CS4 (0.500), while the 11 evaluated systems score from 0.308 to 0.484; the two statistics are different metrics. We therefore read positive CS4 as operational bridge-consistency sensitivity, not as semantic multi-hop reasoning. Every system is also sensitive to one extra edit, and the edits are detectable according to model-based naturalness ratings. On an independent HotpotQA set of 2,276 pairs, patterns pre-specified on MuSiQue and 2WikiMultiHopQA did not replicate: 5 of 6 trained readouts were edit-dominated, and the reference judge's selectivity interval [-0.007, +0.042] includes zero. Judge scores also depended on batch layout. The MuSiQue and 2Wiki records are public; the HotpotQA records and the fine-tuned checkpoints are not, so external reproduction is partial.

---


### 308. [Executable Human Study Programs with Silicon Participants](https://arxiv.org/abs/2611.11969)

**<font color=#1a73e8>作者：</font>** Xuan Liu, Haoyang Shang, Yuanjun Feng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We introduce HumanStudyProgram, a framework that represents a documented human study as an executable program with configurable LLM-based silicon participants. Its computational abstraction separates study logic from participant implementation through standardized APIs for presenting information and collecting responses. We implement a researcher-facing authoring tool that reconstructs source-linked study descriptions from papers and supplementary materials, supports researcher review, and generates executable HumanStudyProgram artifacts. Researchers can then configure silicon participants, run the programs, and analyze results from aggregate findings to individual responses. We demonstrate the approach through study cases and evaluate the tool through a hands-on expert review with 12 social science researchers. All completed the workflow and identified potential uses in understanding published protocols, prototyping studies, and examining AI behavior. We aim to improve the reproducibility of human studies by reconstructing their documented procedures as programs that others can reuse and build upon.

---


### 309. [AutoQS: Automated Quantization Strategy Design with Large Language Models](https://arxiv.org/abs/2611.11975)

**<font color=#1a73e8>作者：</font>** Zhen Liu, Zhiqin Yang, Yonggang Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quantization reduces LLM deployment costs, but effective strategies must balance model quality and storage. LLM-driven search can automate strategy design through repeated proposal and evaluation. This process must identify useful strategies within a limited evaluation budget. The key challenge is that \textit{actual quantization is expensive, while inexpensive proxies may not reflect quantized-model performance.} To address this challenge, we present AutoQS, an \textbf{Auto}mated \textbf{Q}uantization \textbf{S}trategy Design with LLMs. AutoQS keeps weight precision fixed and searches group-size allocations across layers and operators under deployment constraints. Evaluation history guides coordinated LLM proposals, while deterministic validation ensures compatible allocations. An inexpensive quality proxy evaluates candidates, and an candidate repository retains alternative allocations to inform subsequent proposals. Periodic actual quantization complements these proxy evaluations with measured quality and checkpoint storage, providing feedback for further search within the evaluation budget. Experiments on Qwen2.5-7B-Instruct show that AutoQS improves seven-task average accuracy over uniform-group GPTQ and AWQ by 0.70 and 1.12 percentage points, respectively, at four-bit weight precision.

---


### 310. [FireGate: Bounding Behaviour Change Before Training in Continual RL Fine-Tuning](https://arxiv.org/abs/2611.11979)

**<font color=#1a73e8>作者：</font>** Md Anwar Hossen, Ali Jannesari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning a deployed language model on one task after another can change behaviour that should stay fixed, such as earlier skills, general chat or refusals. Today, such forgetting is found only after training, on the benchmarks someone chose to run. This work bounds, before training, how often its outputs change on chosen prompt distributions. FireGate places each task's update, such as a new LoRA, behind a gate, which is a classifier on the model's frozen lower layers that decides for each prompt whether the update is used. Where no gate fires, the model computes exactly what the old one computes. As a result, on any prompt distribution, every bounded behaviour score changes by at most the gates' firing rate there over a whole task stream. Calibrating each gate on unlabeled prompts of what must not change fixes that rate before training, with a PAC guarantee, whatever weights training produces. Forgetting is thus bounded by the gate's false-alarm rate, and its price is the gate's power: no update, gated or not, that changes as few protected outputs can change new-task outputs more often than the best test of that level tells new-task prompts from protected ones. On reinforcement-learning streams of up to five tasks, gated training keeps the earlier tasks and changes 3.3% of held-out chat responses, whereas ungated training changes 91.8%. Across seven models, the gain kept behind the gate follows its firing rate on new-task prompts, measured before training. The certificate covers the gated model as deployed, on the prompt distributions sampled for calibration, not against an adversary who searches for prompts that fire the gate.

---


### 311. [When Audio and Video Mislead: Evaluating Multimodal AI for Conversational Emotion Recognition](https://arxiv.org/abs/2611.11987)

**<font color=#1a73e8>作者：</font>** Youngseok Kim, Minjae Kim, Eunsoo Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Emotion Recognition in Conversation (MERC) combines lexical, acoustic, visual and conversational cues, but accepting audio and video does not establish their effective or robust use. We audit off-the-shelf Omni models while holding the target transcript and prior textual context fixed and adding, removing or replacing target audio and video. In the primary evaluation of Qwen2.5-Omni-7B, Baichuan-Omni-1.5 and MiniCPM-o 2.6 on MELD and the full five-session six-class IEMOCAP set, T+A improves Accuracy in all six model-dataset pairs, with four gains significant after false discovery rate (FDR) correction. Across three source mappings, unrelated A/V (RandA/V) lowers Accuracy relative to Full in all 18 comparisons; all 18 remain significant under dialogue-cluster inference and BH-FDR correction, both on common-valid pairs and when invalid/OOM outcomes are treated as incorrect. Comparisons with modality-omission baselines further distinguish replacement penalties from mismatch-specific harm. A Qwen/MELD case study finds significantly greater gold-vs-best-candidate margin recovery in Late than Early or Middle under decision-query audio knockout, relative to an edge-count-matched Video-Sham control, using Holm-corrected tests. These results distinguish genuine-modality benefit from sensitivity and vulnerability to misleading input.

---


### 312. [EmoHarness: Boosting Multimodal Emotion Understanding with Meta-Harness Evolving](https://arxiv.org/abs/2611.11994)

**<font color=#1a73e8>作者：</font>** Fenghai Li, Bingxuan Li, Jiawen Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small multimodal models can misjudge emotion when words, voice, and visual cues conflict. We present EmoHarness, which runs such a model, the frozen student, inside a harness: the prompts, settings, and verification code around its calls. A human-written starting harness, the scaffold, numbers the student's visual observations, transcript, and prosody descriptions as citable evidence and has the student weigh candidate emotions against it. In Meta-Harness Evolving (MHE), a stronger LLM, the Builder, reads the student's errors and execution traces offline and edits the harness; static checks and validation gates decide which edits are kept, and the Builder never sees evaluation items. On 5,507 MME-Emotion items, EmoHarness raises task-macro Recognition by 7.6-13.4 points over a single video-only call for all four students and both Builders. Transcripts and prosody descriptions supply most of this boost (+5.38 to +10.71); the scaffold changes the audio-augmented call by -0.79 to +2.54, partly through extra multi-label predictions, and evolved edits add at most +0.95, although no evolved increment survives Holm correction. The harness's emotion context also transfers to IntentQA, with small gains for three of four students, none of which survives correction. EmoHarness thus boosts small multimodal students chiefly by supplying and organizing audio-derived evidence.

---


### 313. [Infrathon: Benchmarking Language Agents for Real-World, Long-Horizon AI Infra Optimization](https://arxiv.org/abs/2611.11995)

**<font color=#1a73e8>作者：</font>** Zhengyu Hu, Zheyuan Xiao, Yike Wang 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this work, we study whether frontier agent can continually improve real-world AI infrastructure over long horizons. We introduce Infrathon, a benchmark of diverse, long-horizon AI infrastructure optimization tasks across different levels. We evaluate six models across 150 runs with 24-hour budgets, totaling over 10,000 GPU-hours. Our results show that model rankings vary with the evaluation horizon, while 135 of the 150 runs achieve further improvements during the second half of their budgets. These findings indicate that shorter evaluations can overlook both optimization gains and changes in relative model performance. We also find agents can discover solutions that outperform human-designed baselines: Claude Opus 5.5 increases the mean KV-cache compression ratio from 6.82% with the human-designed Quant-VideoGen codec to 19.86%. Analysis of agent trajectories identifies task violations, unreliable testing, and premature completion as barriers to sustained improvement. Together, Our Infrathon framework provide resources for constructing long-horizon tasks, evaluating frontier agents, and discovering good infrastructure solutions.

---


### 314. [HyPLM Technical Report](https://arxiv.org/abs/2611.12000)

**<font color=#1a73e8>作者：</font>** Haowei Lin, Cai Zhou, Xiangxin Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein language models (PLMs) are standard tools for variant-effect prediction, protein annotation and design, but the compute needed to train and serve them keeps growing. We present HyPLM-Flash, an efficient and open PLM trained by Hyra 2.0, the research agent developed by our team. HyPLM-Flash is a 650-million-parameter masked language model trained on 726 billion tokens, 0.73 times the data of ESM-2 650M and a fifth to an eighth of the data of E1-600M and ESM C 600M. It runs on an inference engine with fused kernels and INT8 matrix multiplication, embedding about 130,000 residues per second on a single NVIDIA H20 GPU, 1.9 to 2.7 times faster than other 600M-class encoders. In a matched evaluation against 28 public checkpoints on 32 tasks, HyPLM-Flash reaches a ProteinGym zero-shot Spearman correlation of 0.409, statistically tied with ESM-2 650M, ESM C 600M and E1-600M, and the highest organismal-fitness score among self-supervised single-sequence models. It gives the best long-range contact precision of all models evaluated, including ESM-2 15B and ESM C 6B, and a lower masked-residue loss than ESM-2 650M, ESM C 600M and E1-600M on held-out sequences and on recently released PDB chains. Matching state-of-the-art accuracy at a fraction of the training and inference cost, HyPLM-Flash sets a new Pareto frontier for protein language models. We have released the model weights and the inference engine at this https URL.

---


### 315. [Robust Domain-Mixture Scheduling for Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2611.12012)

**<font color=#1a73e8>作者：</font>** Yankai Chen, Sida Lin, Yifan Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-teacher on-policy distillation (MOPD) merges the capabilities of multiple domain-expert teachers, such as mathematical reasoning, code generation, and instruction following, into a single compact student. Since all domains share a limited training budget, how to allocate it across domains directly determines the quality of distillation. Existing methods allocate the budget by each domain's learning progress, but offer no guarantee for lagging domains. We therefore introduce distributionally robust optimization (DRO) into MOPD to prioritize the worst-performing domain. However, the per-domain training signals are estimated from a few rollouts and are inherently noisy, so directly applying DRO mistakes noise for the worst case, lets occasional spikes hijack the budget, and protects inherently hard domains rather than truly regressing ones. To address these issues, we propose RDS-MOPD, which keeps the DRO objective and redesigns its three parts: it shifts the allocation only when differences clearly exceed the noise, bounds the influence of any single anomaly, and defines the worst case as the regression from each domain's own best level, all with theoretical guarantees. Experiments show that RDS-MOPD outperforms recent competing methods and ranks first on most mathematical reasoning, code generation, and instruction-following benchmarks.

---


### 316. [Enhancing Multi-Step Chemical Mechanism Prediction with Graph-Guided Preference Data](https://arxiv.org/abs/2611.12013)

**<font color=#1a73e8>作者：</font>** Yu Zhang, Ruijie Yu, Xuelin Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predicting multi-step chemical reaction mechanisms requires identifying plausible intermediates and correctly ordering the elementary reaction steps. Existing computational methods focus on single-step elementary reaction prediction, limiting their ability to generalize to unseen reaction spaces. We introduce a graph-guided framework for multi-step chemical mechanism prediction that leverages a chemical mechanism knowledge graph (ChemMechKG) to guide large language models (LLMs). To improve pathway prediction, we develop a graph-aligned reaction mechanism predictor (GRMP) that uses graph neural networks to generate synthetic candidate pathways for pathway optimization. During inference, we design a relation retrieval (RR) module to extract relevant graph evidence from the KG for pathway refinement. Experiments show that GRMP achieves the highest pathway accuracy among all compared methods on ChemMechQA and oMe-Gold, reaching 48.1% and 57.9%, respectively. On a fixed sample of 110 out-of-distribution reactions from ChemMechQA-Hard, GRMP achieves 36.4% top-1 pathway accuracy. LLM-as-Judge and human assessment further demonstrate its ability to generalize to unseen reactions.

---


### 317. [Benchmarking language models and agents for scientific reasoning in evolving materials laboratories](https://arxiv.org/abs/2611.12014)

**<font color=#1a73e8>作者：</font>** Xuyu Dong, Yixuan Li, Jianguo Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models and the multi-agent systems built around them could accelerate materials discovery by connecting scientific knowledge with experimental decisions. Existing benchmarks establish capabilities in domain knowledge, multimodal interpretation and scientific tool use. As language models increasingly support materials research workflows, their ability to distinguish closely related material states and reason accurately with quantitative evidence remains insufficiently evaluated. These abilities are essential for comparing material responses, assessing mechanisms and maintaining reliable judgements as experimental evidence accumulates. We introduce MatScope to evaluate three connected capabilities. M1 tests unaided, condition-specific reasoning through 200 tasks spanning ten research functions, using aluminium and high-entropy alloys as representative material systems. M2 tests agent-assisted transfer of related knowledge to unresolved materials questions. MatEvoBench-20 tests initial forecasts across scientific dependency chains and revisions of still-hidden responses as observations accumulate. Across eleven model deployments, including GPT-6 Astra and Claude Fable 5.1, given-input calculations and many physical explanations are handled well. Fine-grained response estimates, comparisons between similar states and quantitatively supported choices remain substantially weaker. Related literature improves selected estimates, while condition and baseline mismatches limit transfer. Progressive observations calibrate some downstream responses and destabilize earlier accurate predictions. MatScope establishes measurable targets for developing reliable scientific reasoning in future self-evolving materials laboratories and materials-aware world models.

---


### 318. [Speculative Self-Distillation enables Efficient Knowledge Internalization](https://arxiv.org/abs/2611.12016)

**<font color=#1a73e8>作者：</font>** Shayan Talaei, Agam Bhatia, Arshia Soltani Moakhar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many real-world applications require language models to internalize knowledge that was absent from pretraining, to incorporate continually updated facts, or to learn new domain skills. Self-distillation has emerged as a natural approach for this task. A model conditioned on the source material acts as the teacher, and an unconditioned student is trained to reproduce the teacher's behavior closed-book. We propose Speculative Self-Distillation (SSD), an efficient per-token mixed-policy method for self-distillation. The student generates each rollout by default, while the teacher intervenes only at positions where its next-token distribution substantially diverges from the student's. Unlike off-policy distillation with teacher-generated prefixes, this design keeps training rollouts close to the student's test-time behavior, while avoiding the low-signal states that fully on-policy rollouts drift into. In effect, SSD lets the teacher steer the rollout exactly where the privileged context changes the prediction. On three closed-book QA benchmarks measuring fact recall, knowledge updates, and skill acquisition, SSD nearly matches on-policy distillation while using 38-69% fewer supervised tokens and consistently outperforms off-policy distillation on the held-out test set. On a forgetting stress test, SSD retains the most general capability while also achieving the best in-domain accuracy and using less supervision than the on-policy baseline. Overall, SSD establishes a new accuracy-efficiency-forgetting Pareto frontier for self-distillation.

---


### 319. [SMO: Compiling Natural Language Skills into Graphs of Reusable State-Move-Outcome Bricks](https://arxiv.org/abs/2611.12041)

**<font color=#1a73e8>作者：</font>** Chao Chen, Jiashuo Zhang, Yunhang Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model agents increasingly rely on reusable natural-language skills, yet growing skill collections remain accumulations of isolated text artifacts that are difficult to compare, deduplicate, and compose. We argue that the reusable content of a skill lies not in its surface wording but in its procedural transitions: which operation to execute under a given state and which observable outcome to produce. Based on this observation, we propose State-Move-Outcome (SMO), a compilation-like framework that decomposes raw skills into reusable procedural bricks and organizes admitted bricks as an externalized symbolic structure. When compiling a skill, SMO first retrieves and composes existing bricks, dynamically connects them through Outcome-to-State conditions, and creates a candidate brick only for an uncovered procedure; the candidate becomes reusable only after validation and admission. Experiments on SkillsBench v1.1 demonstrate that SMO represents 232 rawSkills from 87 underlying tasks with 95 shared bricks, reducing the corresponding skill representations from 366,472 to 149,154 tokens--a $\mathbf{59.3}\times$ reduction and $\mathbf{2.46}\times$ compression. Across 232 skill-conditioned evaluation instances, SMO raises the average task score from $\mathbf{0.6379}$ to $\mathbf{0.7478}$ and increases 5/5 Pass instances from $\mathbf{138}$ to $\mathbf{164}$, while matching or outperforming rawSkill on $\mathbf{208}$ of $\mathbf{232}$ instances. It also reduces average runtime token consumption by $\mathbf{38.38\%}$. These results show that compiling natural-language skills into shared procedural units can jointly improve skill reuse, representation efficiency, and downstream execution.

---


### 320. [Four-Step Text-Bearing Image Generation via Distillation with Local Response Regularization and Teacher-Guided Training](https://arxiv.org/abs/2611.12042)

**<font color=#1a73e8>作者：</font>** Kairui Wen, Sheng Ye, Yong-Jin Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating text-bearing images requires coherent scenes and accurate characters. Large text-to-image models improve both capabilities through repeated denoising, at substantial sampling cost. Few-step distillation reduces this cost but requires the student to organize scenes and refine glyphs within a short trajectory. We present a four-step distillation framework combining local response regularization with teacher-guided text training. Built on distribution matching, the framework distills the GLM-Image DiT while retaining its autoregressive visual prior, glyph encoder, and VAE. A path-length penalty promotes consistent local responses of the conditional denoising field. Progressive training combines synthetic strings with teacher-generated imagery to preserve character accuracy and scene-integrated typography. The student achieves GenEval Overall 0.84 and CVTG-2K word accuracy 0.5045, compared with 0.81 and 0.1690 for four-step TDM. A coefficient study favors $10^{-5}$, and Qwen-Image experiments show additional gains from response regularization and text supervision. Single-image inference takes 1.742 s, compared with 5.818 s for the teacher, yielding a $3.34\times$ speedup at the same 40 GB GPU memory requirement.

---


### 321. [Evaluating AI Agents for Industrial-Level Chip Floorplanning: A Framework and Empirical Study](https://arxiv.org/abs/2611.12048)

**<font color=#1a73e8>作者：</font>** Nova-Silicon Team  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Floorplanning is an early step in turning a logical circuit into a physical chip: it positions large circuit modules and constrains the space available for subsequent logic placement and wiring. These decisions affect congestion and timing, but their physical consequences emerge through downstream implementation. For AI agents, the task requires translating engineering constraints into spatial decisions whose quality cannot be judged by successful tool execution alone. We present an evaluation framework that connects submitted layouts to a prescribed downstream implementation flow, checks geometric validity, measures physical quality, and reports resource use. On one industrial design whose 99 macros occupy approximately 71\% of a fixed L-shaped layout region, we compare our specialized system Nova-SI with general-purpose engineering agents and agents restricted to file access, obtaining complete physical measurements for 39 layout outputs. Under our 0--100 composite quality score, Nova-SI achieves a mean of 57.97 without online feedback from the prescribed power-grid and placement evaluation, compared with 31.17 for the strongest measured general-purpose configuration, GPT-6 Astra. The difference is supported by raw congestion and timing measurements and persists across scoring-sensitivity checks. Layout-level analysis further shows that similar global utilization can conceal substantially different local congestion. Together, the protocol and case study assess agents through the physical consequences of their delivered layouts and provide evidence about system performance on this industrial instance.

---


### 322. [COMPASS: Composable Policy-Amortized Structured Search for LLM-Based Optimization Modeling](https://arxiv.org/abs/2611.12060)

**<font color=#1a73e8>作者：</font>** Nguyen Le Minh Hoang, Van Duc Cuong, Bui Trong Duc 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models offer a promising technique for translating natural-language optimization problems into solver code, but their reliability remains constrained by the quality of template retrieval. While recent structured methods improve over flat prompting through hierarchical taxonomy search, their traversal rules remain fixed or LLM-driven at inference time, leaving retrieval unable to improve from past successes and failures. This motivates treating template retrieval as a policy that can be learned from modeling experience, rather than as a static inference-time rule. We propose COMPASS, a policy-amortized framework for retrieving optimization templates in LLM-based solver modeling, which represents the template library as a directed acyclic graph and formulates retrieval as a sequential decision process over template nodes. A deep Q-network learns a reusable traversal policy from template-level judgments and execution feedback, reducing reliance on fixed heuristic traversal through feedback-driven graph navigation. To support extensible retrieval, COMPASS embeds problem descriptions and template nodes in a shared semantic space, allowing newly inserted templates to be scored from their text descriptions without redefining the action space. Experiments across multiple LLM backbones and optimization-modeling benchmarks demonstrate that COMPASS consistently improves over heuristic structured retrieval, with the largest gains on complex and mixed-category problems.

---


### 323. [Translating KV Caches Between Hybrid-Attention Language Models: MLA Latents, Linear-Attention States and Sparse-Attention Indexers](https://arxiv.org/abs/2611.12062)

**<font color=#1a73e8>作者：</font>** Povilas Kvedaras, Tomas Rasymas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A model that takes over another model's conversation must normally re-read the whole history; a text hand-off shortens the re-read only by dropping content. KV-cache translation instead maps the source's cache into the target's own format, so the target continues from the full context without re-reading it. It works for grouped-query attention (GQA), but open-weights frontier models now cache compressed latents (MLA), sparse-attention indexer keys and fixed-size linear-attention states. We replicate KV-Lingo on a GQA pair and then give, for each of these objects, where to capture and inject it and a mechanism that reaches native quality. We study two hybrid pairs at 16-48B scale in both directions, Kimi-VL-A3B - Kimi-Linear-48B (MLA - MLA + Kimi Delta Attention) and Qwen3.5-27B - Qwen3.8-27B (Gated DeltaNet hybrids), plus a sparse-attention target (Qwen3.8-27B - Qwen3.8-Flash-Next). MLA latents translate with token-wise linear maps; recurrent states are copied with a closed-form correction or synthesised by replaying the target's own recurrence. Exact long-range recall needs token identity: decoding token ids from the source's layer-0 MLA latent raises needle recall from 0.09 to 0.99 at 2-32K and to 0.83-1.00 at 64K, eight times the longest training prompt. The hybrid full-MLA direction is within the paired confidence interval of native quality on every task metric, and same-shape GDN hybrids reach the native level in both directions (apart from 6% refusals inherited from the source), with time to first token 18.7 and 46.8 times shorter than a re-read at 64K tokens. Segment-wise multi-turn transfer stays at the re-prefill level; naive re-translation collapses. On the sparse-attention target, predicted indexer keys recall the needle as well as the target's own keys (one seed). We state as a hypothesis how the recipes transfer to 300B+ hybrid flagships.

---


### 324. [Weight-Space Programming for Medical Imaging: Do We Still Need Training Data?](https://arxiv.org/abs/2611.12066)

**<font color=#1a73e8>作者：</font>** Maximilian Lindholz, Richard Ruppel, Annette Milnik 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Can a large language model (LLM) write the parameters of a medical image classifier from medical knowledge alone, without any training data? Such classifiers normally require labelled images, which are costly and often unavailable. We investigate this question through weight-space programming (WSP), in which an LLM writes or adapts the weights and biases of a neural network directly, without optimisation on training data. Claude Opus 5.5 and GPT-6 Astra each generate the parameters of a small LeNet-style CNN in a single reply, without tool use and without access to any image. We compare these networks against zero-shot MedSigLIP and against the same architecture trained on labels using the Adam optimiser, across 7 classification tasks in four modalities: chest X-ray, breast ultrasound and abdominal CT (all from MedMNIST), and pelvic MRI (SynthUterus). The LLM-written networks perform above chance on all six MedMNIST tasks, with a mean test AUC of 0.719 for Opus and 0.711 for Astra. Both models outperform MedSigLIP on 5 of 6 tasks while using more than 10,000 times fewer parameters. However, the same network trained with Adam on only 256 labelled images achieves a higher AUC on every MedMNIST task (mean AUC 0.828). On SynthUterus, Opus attains an AUC of 0.764, whereas Astra falls below chance (AUC 0.136) owing to a systematic error. These results show that LLMs can write functional medical classifiers, but that they do not yet replace training data. We release the protocol, logs and all generated weights at this https URL.

---


### 325. [MIRIX-2.0: Multi-Agent Memory System](https://arxiv.org/abs/2611.12068)

**<font color=#1a73e8>作者：</font>** Wei-Chieh Huang, Weizhi Zhang, Jiayan Nan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory lets LLM agents personalize, stay consistent, and reuse what worked before. Parametric memories need training, consolidation can lose details for good, and keeping every record leaves a growing store to search. We present MIRIX-2.0, a multi-agent memory system designed to be practical, accurate, and efficient at once. It is the most accurate of the compared systems on four of five QA benchmarks. It reaches 91.4% on LoCoMo and 72.6% on LongMemEval-S, where it leads the strongest baseline by 14.3 points, and with AutoDream disabled it gains 31.0 and 22.0 points over HyperMem on single-hop and multi-hop document QA. As procedural memory, it yields the highest mean success among the compared memory methods on ALFWorld and WebShop and reaches 49.2% on MetaClaw-Bench, against 44.0% for MetaClaw's skill library. Six typed memory agents keep complete records as the system of record, and a provenance hypergraph indexes episodic and semantic records with n-ary frames that cite their rows. Retrieval runs under explicit budgets, so the evidence a question inspects does not grow with the history. AutoDream merges duplicate anchors outside the write path without rewriting any record, and it distills task sessions into skills. With AutoDream disabled, MIRIX-2.0 answers faster than HyperMem on all five timed benchmarks. It needs no fine-tuning, runs with closed and open models, and its code is public.

---


### 326. [SadaqahStories: A Verified English-Arabic Corpus of Charity Stories for Children, with an Audit of Errors in AI-Drafted Religious Narratives](https://arxiv.org/abs/2611.12078)

**<font color=#1a73e8>作者：</font>** Wajdi Zaghouani, Spencer Striker  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present SadaqahStories, a parallel English-Arabic corpus of 41 illustrated four-page stories about charitable giving in Islam (Sadaqah, Zakat and Waqf), written for readers aged 7 to 18. The stories were first drafted with large language model (LLM) assistance, then audited against hadith collections, Qur'an references and historical sources, and finally rewritten for children and signed off by an Islamic scholar. Every story carries an evidence label and links to its sources. We release all three versions of each story (AI-assisted draft, audited text, final child-oriented text) together with the correction log, so the corpus can be used to study how AI drafts of religious and historical content go wrong. The audit found substantive errors in 39 of the 41 drafts. The most frequent were unsupported specific details (dates, figures, prices, names), invented quotations, institutions or anecdotes, and conflation of separate events or people; six drafts contained errors in the wording, grading or ruling of a religious text. Rewriting cut the estimated Flesch-Kincaid grade of the English text from 14.0 to 6.1. We also release an 81-entry charity lexicon covering Modern Standard Arabic and Qatari Arabic, and describe the free, account-free website that serves the corpus (this https URL).

---


### 327. [Correct First, Fast Second: What a Local 7B Code Model Can and Cannot Do for GPU Kernel Optimization](https://arxiv.org/abs/2611.12079)

**<font color=#1a73e8>作者：</font>** Jui-Chien Tsou, Po-Yi Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study how much the interaction strategy around a fixed, locally hosted 7B-parameter code model (Qwen2.5-Coder-7B-Instruct) affects its ability to replace PyTorch operators with custom CUDA kernels. On 30 KernelBench tasks (levels 1-3, first 10 each, evaluated on a V100), we compare four regimes of increasing structure: zero-shot prompting, profiling-guided prompting, iterative refinement on execution feedback, and a multi-agent loop (analysis, retrieval, generation, evaluation, feedback triage) in which the same model fills four roles around a non-LLM evaluator. Three findings stand out. (1) Correctness, not speed, is the binding constraint: even correct generated kernels average 0.97-0.99x the speed of eager PyTorch, because a 7B model cannot out-write cuBLAS/cuDNN on dense GEMM and convolution; the only real wins are fused memory-bound epilogues. (2) The best strategy depends on difficulty: profiling-guided prompting is strongest overall (43% correct, 27% faster than baseline), but the agent loop is the only method that solves any level-2 fusion problem (3/10 vs. 0/10 for all others). (3) Naive agentic scaffolding is actively harmful: our first agent scored 3% correct, below zero-shot's 30%, and the decisive repairs were matching the agent's ambition to the model's competence and spending compute on best-of-n sampling under a real execution oracle (3% to 33% correct from n=1 to n=8), not on more reasoning steps.

---


### 328. [Zero-Search Reinforcement Learning for Slay the Spire 2 with Failure-Driven Restarts](https://arxiv.org/abs/2611.12088)

**<font color=#1a73e8>作者：</font>** Xiangqin Chen, Zhengxuan Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Slay the Spire 2 (STS2) is a deck-building roguelike in which a winning run at the highest difficulty takes several hundred decisions, and most losses happen in late boss fights that a learner seldom reaches. We train agents that choose every action with one forward pass of a 6.6M-parameter entity transformer, without lookahead. Training and evaluation run the game's own compiled assembly (v0.107.1) in a headless .NET host. The host replays a run exactly from its seed and actions, so training episodes can restart from states the learner has visited, and a failure-driven curriculum allocates these restarts in proportion to where complete runs are lost. On 12,800 held-out games at Ascension 10 (A10), the released policies win 8.05% averaged over the five characters (Ironclad 15.6%, Regent 12.5%), and AlphaSpire's released networks used without search win 0.55% on a common panel. Longer A10 training raised Ironclad from 12.4% to 15.6% and Defect from 3.0% to 8.1% on these games. At Ascension 0 the released policies win 80.2%, level with the 80.3% that the tree-search agent Spire Mentor reports, while Mentor leads by 5 to 8 points from A4 upward. Run in our host on the same 2,000 A10 games, Mentor's search wins 8.8% against 8.2% for our policies, which need 21-27 ms per decision on one CPU core. GPT-6 Astra at maximum reasoning won none of 11 A10 games through our text interface. In a controlled study of 18 training runs from six random initializations, failure-driven allocation exceeds uniform restart allocation on each of three Regent initializations, by 3.6 percentage points on average, while the Silent effect is small and changes sign. Code, trained policies, an in-game mod and the records behind every table are at this https URL.

---


### 329. [From Fluent Text to Ontology-Compatible Definitions: A Quality-Control Agentic Workflow](https://arxiv.org/abs/2611.12095)

**<font color=#1a73e8>作者：</font>** Kun Feng, Chenchen Chu, Yan Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Biomedical ontologies are structured knowledge systems that must evolve continuously to represent newly emerging knowledge, but their manual maintenance remains time-consuming and laborintensive. Textual definitions are especially costly because they must be readable to humans and compatible with controlled entities, relations, and logical constraints. Large language models (LLMs) offer a promising way to assist ontology engineering tasks, including definition generation. However, textual plausibility does not guarantee knowledge-system compatibility. A generated definition may be fluent and close to a reference definition, yet still fail to ground its implied entities or violate ontology-level constraints. Directly inserting such definitions into ontology libraries may therefore introduce entity-level hallucinations and logical inconsistencies. To address this problem, we propose two structured-knowledge incompatibility metrics, Entity Error Rate (EER) and Logical Inconsistency Rate (LIR), to quantify entity grounding and logical consistency for LLM-generated ontology definitions. We further develop an agentic quality-control (QC) workflow that treats definition generation as an iterative process rather than a direct decoding step: it generates definitions, extracts axioms, checks entity existence and logical consistency, and uses the resulting diagnostics to drive repair loops. Comprehensive experiments on Disease Ontology, Uberon Ontology, and Uberon-ConstraintStress demonstrate that EER and LIR complement conventional reference-based metrics by evaluating whether generated content can be grounded and checked inside the target ontology. The workflow effectively decreases EER while maintaining strong conventional text-generation performance. LIR further exposes sparse ontology-level logical failures that are invisible to text similarity metrics, although their repair remains limited.

---


### 330. [SkillDuet: Co-Evolving Models and Skills through Response Feedback](https://arxiv.org/abs/2611.12109)

**<font color=#1a73e8>作者：</font>** Xingguang Ji, Ziqiang Dong, Yubo Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> During reinforcement learning, experience can be both internalized in LLM parameters and retained externally as reusable textual skills. Parameter updates alter the model's behavior and the interaction experience from which new skills are extracted. These skills, in turn, guide the model's subsequent interactions and parameter updates. As the model's capabilities evolve, previously beneficial skills may become redundant or detrimental. We present SkillDuet, a framework that coordinates parameter updates and skill evolution through model response feedback. Skills extracted from on-policy trajectories guide parameter updates through OPD at every step. A response-based score, Strength, ranks candidate skills by the magnitude of the shift they induce in the current model's responses, and the highest-scoring skills are periodically consolidated into a persistent global skill set (Global). The updated model and Global jointly guide subsequent interactions, generating experience for further parameter and skill updates. With Qwen3-4B, SkillDuet achieves success rates of 98.57% on ALFWorld and 92.97% on WebShop, exceeding the matched SEED-API baseline by 2.86 and 5.47 percentage points, respectively. Ablations show that response-based skill selection and Global consolidation improve task performance. Further experiments show that the benefits of retained skills depend on both their content and their compatibility with the model. SkillDuet provides a concrete mechanism for model-skill co-evolution and skill-level recursive self-improvement.

---


### 331. [OGDA: Ontology-Grounded Data Agents for Reliable Analysis over Heterogeneous Data Lakes](https://arxiv.org/abs/2611.12114)

**<font color=#1a73e8>作者：</font>** Boyi Zhang, Hong Ting Tsang, Yisen Gao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Full-pipeline data analysis over real-world data lakes requires LLM agents to locate and integrate information across large collections of tables with different schemas. Existing data agents follow task-specific exploration, which exhausts the context window in massive lakes. As the context fills, the agent's reasoning degrades, leading it to locate and process incorrect data files. These errors propagate into the final answer. To overcome these limitations, we introduce Ontology-Grounded Data Agent (OGDA), which utilizes a compact ontology to reduce exploration overhead and constrain data processing. OGDA constructs the ontology through agentic hypothesis testing. At each step, a proposer agent induces schemas, concepts, and relations from raw sources, and a verifier checks each proposal against the underlying data. During task execution, the ontology serves as a representation of the data lake for the agent to explore. Every data-processing action is constrained by a task graph, which the agent can extend only after observing the semantic meaning of the data. Across KramaBench and DiscoveryBench with three LLM backbones, OGDA outperforms the strongest baselines by up to 10.82 points. These results suggest that explicitly modeling the data lake is a key step toward reliable end-to-end data agents.

---


### 332. [SCALE: Small-Model-First Concept Abstraction with LLM-Guided Experience Internalization](https://arxiv.org/abs/2611.12120)

**<font color=#1a73e8>作者：</font>** Hong Su  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous agents must continually acquire reusable knowledge from experience without relying on costly large language model (LLM) reasoning for every decision. However, existing experience-based approaches often struggle to transform accumulated observations and reasoning into compact knowledge that lightweight models can independently apply. This paper proposes SCALE, a small-model-first framework that integrates selective LLM reasoning, experience-driven concept abstraction, and knowledge internalization. A lightweight model handles routine predictions, while prediction errors and accumulated cross-episode evidence selectively trigger LLM reflection. The LLM analyzes relevant historical experiences, generates positive and negative counterfactual examples, and proposes reusable concept hypotheses. Independently validated concepts are progressively incorporated into hierarchical neural representations, enabling lightweight models to exploit increasingly abstract knowledge. Meanwhile, mastered experiences are excluded from active memory while their original records remain available in a complete archive. Experiments across ten random seeds show that historical recall improves held-out accuracy from 87.11% to 98.28%, hierarchical concept knowledge increases difficult-case accuracy from 55.33% to 66.47%, and abstract archiving reduces active experience records from 6,000 to 1,528.

---


### 333. [System Optimizations for Cost-Efficient Agent Harnesses](https://arxiv.org/abs/2611.12122)

**<font color=#1a73e8>作者：</font>** Jongseok Park, Jiaxiang Yu, Eric Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agent harnesses play the critical role of providing LLMs with an interface to a computing environment. Recent studies show that AI agents' task-execution accuracy depends mostly on the LLM used, while harness-side variances such as system prompts or tools have minimal impact. Rather, such harness-side variances show a larger impact on the cost of agent executions, achieving cost reductions up to 2.6 times on the same model and task. To further explore these harness-side cost optimization opportunities, we analyze the cost accumulation patterns across various agent traces and identify system opportunities to reduce token use and LLM calls without modifying the model or affecting task accuracy. Based on this analysis, we design Agency, a harness interposition platform that provides a unified abstraction and allows easy and portable implementation of harness-side system optimizations on existing off-the-shelf harnesses such as Claude Code or OpenAI Codex. Using Agency, we implement proof-of-concept optimization techniques based on our analysis and achieve cost reductions up to 35% across various real-world benchmarks on existing harnesses without compromising accuracy.

---


### 334. [CARE-PO: Controllable Tool-Call Efficiency for LLM Agents](https://arxiv.org/abs/2611.12125)

**<font color=#1a73e8>作者：</font>** Xiaoyang Ye, Xiao Yao, Hairui Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> External tool calls are a major running cost of an LLM agent, while its training objectives align almost exclusively with task completion. In a step-level diagnosis of Qwen3.5 trajectories at two model sizes on GAIA, a long-horizon tool-use benchmark, we find that most contain removable calls, at a similar rate at both sizes. Some methods add an efficiency reward to the objective to reduce the call count, but introduce problems of their own: the anchor they price calls against is computed from the policy's own rollouts (e.g., the group's shortest correct rollout) and so moves with the policy; training can drift toward a collapsed policy that issues no tool call at all, a degeneracy seen in published reports and in our 27B baseline; and a training run delivers a single operating point, so the user cannot trade efficiency against capability. We present CARE-PO (Controllable Anchored Relative Efficiency Policy Optimization) to mitigate these problems. The efficiency reward prices calls against a reference budget anchored to the task's own difficulty and fixed before training. Injecting a successful trajectory from the training data into each online GRPO rollout group and charging for evidence a trajectory never gathers ease the drift toward a collapsed call count. Shaping the cost curve by an effort tag in the prompt yields an efficiency and a capability operating point from a single training run. On GAIA, five of the six operating points across three model sizes improve on their base model in success rate and call count at once. On four held-out multi-hop benchmarks the result is size-dependent: at 27B and 4B success rate is held or raised at a lower call count, while at 9B both operating points trade success rate for fewer calls. The call count remains well above zero throughout training at all three sizes.

---


### 335. [Lost in Rounding: bf16 Recurrent State Makes Hybrid Reasoning Models Think Longer](https://arxiv.org/abs/2611.12127)

**<font color=#1a73e8>作者：</font>** Yuchuan Weng, Xin Chen, Chi Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hybrid reasoning models interleave attention with recurrent mixers such as Mamba-2 and Gated DeltaNet, whose state is cached between decoding steps. Prior work showed that storing this state in FP16 or INT8 with round-to-nearest (RTN) makes Mamba-2 and GDN hybrids more verbose, and that stochastic rounding (SR) fixes it. We study the other 16-bit format that serving engines expose, bf16, on six open hybrid reasoning models and 590 competition-math problems. With bf16 RTN state, five of six models reason longer (geometric-mean length 1.07x to 1.27x; also under greedy decoding in the two models tested) and hit the 32K token cap more often. On Qwen3.5-9B, cap hits rise from 118 to 223 and accuracy falls from 85.6% to 70.8%. On LiveCodeBench, both models tested also reason longer and lose 12.6 and 13.4 points of pass@1. Rerunning the capped items with a 128K budget halves the accuracy gap but does not close it (93.6% vs. 86.6%): bf16 runs that never finish are twice as common, and 85% of them are exact repetition loops. On Nemotron-Nano-9B-v2, by contrast, 30 of 31 extra caps finish at 128K, so the cost there is mostly extra tokens (exploratory). Same-width bf16 SR removes the length increase in four of five affected models, restores Qwen3.5-9B to 87.6% and brings code length and pass@1 near FP32 levels, so the failure is mostly rounding bias, not missing resolution. With an integer-hash random generator, SR on Qwen3.5-9B matches FP32 on cap hits and accuracy (113 vs. 118; 85.6% for both) at the memory and decoding speed of bf16 RTN. In the Nemotron-Nano-v2 lineage, SR on 25% of heads (an intermediate-decay band) removes the effect, while random heads and the top teacher-forced-KL octiles do not; in Nemotron-3 and Qwen3.5-9B the effect is spread across heads. We recommend that evaluations of hybrid models report the state dtype, cap rate and output length alongside accuracy.

---


### 336. [Toward Sustainable Agentic AI: Carbon Tradeoffs Across Iterative Self-Refinement and Tool-Augmented Coding](https://arxiv.org/abs/2611.12128)

**<font color=#1a73e8>作者：</font>** Boris Ruf, Adrien de Mailly Nesle, Marcin Detyniecki  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic language model systems can improve performance either by iterating on their own outputs or by using external tools in grounded environments. While these strategies can reduce error rates and substitute for larger models in some settings, their environmental cost remains relatively underexplored. We present two complementary empirical studies that estimate the energy and carbon footprint of agentic AI across settings of increasing complexity. Study~1 evaluates iterative verbal self-refinement: GPT-4.1-mini at $k = 1$--$5$ steps versus a GPT-4.1 single-pass baseline on two MATH benchmark splits. Study~2 evaluates tool-augmented agentic coding: GPT-4.1-mini, Claude Opus~4.6, and GPT-5.3-codex on SWE-bench Lite, where agents operate inside Docker-isolated environments with access to code execution and file editing tools. In Study~1, $k=3$ refinements close a 16-percentage-point accuracy gap to within 1~point, but nearly triple the carbon footprint relative to the cheap single-pass baseline while remaining below the GPT-4.1 single-pass baseline under the current token-based carbon scenario. In Study~2, GPT-5.3-codex achieves the highest resolution rate in this sample (81.2\%), ahead of Claude Opus~4.6 (68.9\%) and GPT-4.1-mini (25.0\%), but resolved-task-normalized efficiency remains mixed: GPT-4.1-mini is lowest on estimated carbon and cost per resolved task, while GPT-5.3-codex delivers substantially higher task success. All carbon estimates cover output-token inference only; prompt tokens, which exceed 99\% of tokens in Study~2, and tool execution are not charged, so the figures are lower bounds on the full agentic footprint.

---


### 337. [Good Views Are Not Enough: Global Counterexamples for Gaussian-Regularized JEPAs](https://arxiv.org/abs/2611.12137)

**<font color=#1a73e8>作者：</font>** Anran Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Good views do not suffice to guarantee scene invariance or uniqueness up to rotation at the global optima of Gaussian-regularized JEPAs. We give globally certified counterexamples showing that the uniqueness premise of the Gaussian extension in Good Views fails for specified soft objectives. Gaussian marginal matching can reward retaining independently resampled observation variation, and this benefit can exceed its prediction cost. In a four-state model, comparison against the entire scene-only class proves that every global minimizer splits a scene and admits an equal-value partner outside its rotation orbit. In a 512-dimensional model with a complete scene basis, a spectral gap, and exact population whitening, pooled Epps-Pulley regularization still forces every global minimizer to retain nuisance and yields positive cross-modal alignment error even after the best rotation when modality nuisances are independent. Better scene alignment can also accompany worse prediction. With matched 512-label readout budgets and 1% observation noise, whitened prediction JEPA aligns better to the scene than next-token prediction but incurs 0.2872 nats/token higher linear-readout test NLL. A Bayes-risk decomposition distinguishes information lost through the observation channel from the fitted readout's difficulty using retained information. These results connect three determinants of learned representations: what views share, what regularization favors, and what a prediction task can use.

---


### 338. [DisasterVL: Evidence-Based Visual Reasoning Dataset and Model for Disaster Scene Understanding](https://arxiv.org/abs/2611.12144)

**<font color=#1a73e8>作者：</font>** Ali Diba, Aisha Al-Mohannadi, Yin Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce DisasterVL, a dataset and benchmark for evidence-grounded reasoning about disaster imagery. It contains approximately 1.2 million images from 142 countries, paired with 25 million structured annotations covering scene captions, incident and location assessments, spatial relationships, and visual question answering (VQA). The VQA annotations link answers to visible evidence and include questions about both present and absent cues, multiple answer formats, and difficulty labels. Region-level annotations link caption phrases to bounding boxes and spatial relationships to the regions they connect. The test set contains 38,254 images spanning 75 countries and 28 hazard types. Gemini 3.1 Pro audited the test annotations, and human reviewers validated a stratified subset. On this benchmark, the 9B DisasterVLM model outperforms the evaluated general-purpose baselines on captioning, open-ended VQA, incident reasoning, and region-level grounding. Gains in text overlap are larger than gains in evidence scores. We plan to publicly release the dataset, trained models, and code.

---


### 339. [Let the Fixer Decide: Training a Code Localizer from the Fixer's Likelihood](https://arxiv.org/abs/2611.12164)

**<font color=#1a73e8>作者：</font>** Khalil Hennara, Muhammad Hreden, Zeina Aldallal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Code localizers are usually trained to predict the files a reference patch edits, but the code a fixer needs to read is not the same as the code it changes. We propose Fixer-Guided Localization (FGL): the localizer proposes several localizations, a frozen fixer scores each by how likely it makes a verified patch, and the localizer is trained on these scores with weighted supervised fine-tuning, without running tests and without reinforcement learning. We build the full pipeline on Gemma 4 E4B for the Kaggle Gemma-4 Developer Agent competition, from 1,629 test-verified Kimi K3 trajectories. The FGL target helps the fixer find the bug as often as the teacher's localization while using 27.5% less code. On the development set, one EM round moves the agent in the expected direction compared with a matched control: more tasks reach a patch (53 vs. 46), fewer tasks get stuck reading files that do not exist (43 vs. 54), and more tasks are solved (8 vs. 6). Training also changes how the agent works: trained agents explore about three times more than the base model and write far fewer wrong patches, and the single agent solves up to 11 of 78 tasks, against 8 for the base model. An analysis of 13 evaluation runs identifies what limits a 4B agent under an 8-minute budget (time, repetition loops and edit quality) and gives practical lessons for training small coding agents. All data, code and adapters are publicly available.

---


### 340. [FraudBench: A Legal Evaluation of AI Deception](https://arxiv.org/abs/2611.12167)

**<font color=#1a73e8>作者：</font>** Kevin Wei, Sumaya Nur Adan, Stephan Llerena 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce FraudBench, an evaluation of large language models' (LLMs) propensities to recommend, assist, or directly take actions that would constitute fraud under U.S. law. Our evaluation contains a novel dataset of 159 scenarios based on real-world U.S. court cases and validated by legal experts. We present each scenario to LLMs via three tasks at varying levels of autonomy: advising users, drafting messages for users to send, and acting directly on behalf of users (477 tasks total). In each scenario, FraudBench re-enacts the facts of a court case to give LLMs an opportunity, but no explicit instruction, to either misrepresent or conceal a material fact in a high-stakes commercial setting--e.g., whether to describe company-funded product testing as "independent" to customers (misrepresentation) or whether to hide unfavorable regulatory investigations from clients (concealment). We evaluate 20 LLMs across 25 experimental conditions (totaling >300,000 generations) and include a preregistered human baseline ($n_{\texttt{annotations}} = 2{,}957$, $n_{\texttt{humans}} = 996$). We score a response as fraudulent when it engages in, assists with, or recommends misrepresentation or concealment. Key findings include: (1) across LLMs, fraud rates ranged from near 0% to over 40%; (2) LLM fraud rates increased with autonomy, with overall rates of 3.0% when advising, 14.7% when drafting, and 21.4% when acting directly, without applying pressure; (3) LLMs sometimes engaged in fraud despite recognizing legal risks; (4) LLMs more often engaged in fraud by concealment than by misrepresentation; and (5) prompt-based interventions substantially affected fraud rates, with a prompt to obey the law reducing fraud rates, while prompts to maximize profits and act agentically increased fraud rates.

---


### 341. [Harnessing Vision-Language Models for Federated Unsupervised Visual Recognition](https://arxiv.org/abs/2611.12187)

**<font color=#1a73e8>作者：</font>** Jian Liang, Kuangpu Guo, Ran He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) is a promising research paradigm that enables collaborative model training across distributed clients without data sharing. To handle unlabeled data in local clients, existing unsupervised FL research has primarily focused on tasks like clustering and self-supervised representation learning, leaving the critical problem of unsupervised visual recognition largely unexplored. To bridge this gap, we introduce FedUR, the first framework designed for unsupervised recognition by leveraging the zero-shot capabilities of pre-trained vision-language models like CLIP. Specifically, FedUR addresses data heterogeneity through a pseudo-labeling mechanism with a class-aware data selection strategy. This strategy first estimates a global pseudo-label distribution, then allocates pseudo-labeled data to clients accordingly. To handle the uncertainty of conventional positive pseudo-labels, FedUR further incorporates class weights and a negative pseudo-labeling strategy. Furthermore, FedUR proposes a personalized prompt aggregation protocol where general visual prompts are aggregated on the server, and personalized text prompts encoding local knowledge are retained on clients. Extensive experiments demonstrate that FedUR consistently outperforms baseline methods under both label-level and feature-level distribution shifts. We believe this work paves the way for further advances in federated unsupervised recognition. Code will be available at {this http URL}}.

---


### 342. [Co-Creating Neurorehabilitation Technology Alongside Lived Experience Experts: A Participatory Design Workshop](https://arxiv.org/abs/2611.12202)

**<font color=#1a73e8>作者：</font>** Irene L. Y. Beck, Salvatore L. Cucinella, Johannes B. J. Bussmann 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Involving patients' lived experience (LE) early in neurorehabilitation technology design can improve the relevance and effectiveness of solutions, yet LE experts are often involved only when finished prototypes are tested. We present and evaluate a participatory design (PD) workshop for early LE involvement, examine how LE contributions influence design processes and outcomes, and provide recommendations for similar approaches. We conducted a PD workshop at the 6th International Conference on NeuroRehabilitation. Five people who have had a stroke (LE experts) and 18 workshop attendees (including the LE experts' caregivers) were organized into five groups. Following the Discover, Define, and Develop phases of the Double Diamond model, each group used Journey Maps and Data Collection Notebooks to co-create a solution for an objective specified by an LE expert. Journey Maps were thematically analyzed, and group audio transcripts underwent structured extraction using a large language model. LE input shifted discussions from discipline-based assumptions toward priorities grounded in lived experience, including fear, confidence, sensory discomfort, fatigue, aesthetics, and independence. Narrow objectives, such as opening a blister pack, produced task-specific solutions, whereas broader objectives generated device concepts, including sensory feedback for cycling and a stimulation-equipped cooking splint. Satisfaction was high among attendees and LE experts. All workshop tools and protocols are shared to support adoption. The workshop offers a practical foundation for involving LE experts early in neurorehabilitation technology development. Future iterations should better capture psychological and social dimensions, allow more reflection, and include the full range of relevant stakeholders through sustained transdisciplinary engagement between researchers and the LE community.

---


### 343. [A Geometric Invariant of Attention Predicts Head Specialization from Weights Alone](https://arxiv.org/abs/2611.12206)

**<font color=#1a73e8>作者：</font>** Miguel P. Bento  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers are built with continuous symmetries in the attention mechanism. We derive $\rho$, a scalar invariant that measures each head's capacity to couple to rotary positional encodings. This framework allows us to analyze heads without forward passes, opening a new research direction into data-independent analysis of modern LLMs. Empirically, we find that $\rho$ predicts induction heads, the most-studied circuit type in mechanistic interpretability, with Spearman correlation between $-0.55$ and $-0.74$ across four bias-free RoPE models spanning $135$M to $7$B parameters. As a preliminary proof of concept, we use $\rho$ to apply YaRN to only the top-50% positional heads, which degrades perplexity less than uniform application. Code is available at this https URL.

---


### 344. [PARIS: A multi-agent LLM framework for end-to-end, PRISMA-guided systematic literature reviews with pre-synthesis corpus quality assessment](https://arxiv.org/abs/2611.12222)

**<font color=#1a73e8>作者：</font>** Christophe Cruz, Hussam Ghanem, Samir Jabbar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Systematic literature reviews (SRs) remain slow and labor-intensive, and most automation tools address single stages of the workflow. We present PARIS (PRISMA Agentic Research Intelligence System), an open-source framework in which a conductor agent running in Claude Code orchestrates 15 specialized large language model (LLM) agents, from scoping a research question to exporting a manuscript draft. Agents are specified declaratively, coordinate exclusively through persisted artifacts that the conductor validates before every transition, and delegate retrieval, bibliometric analysis and scoring to deterministic Python utilities. Three human checkpoints gate study inclusion, corpus adequacy and the synthesis outline. We also introduce QualityScore, a pre-synthesis index that aggregates normalized network, bibliometric, semantic and process sub-scores into a 0-100 grade. Two case studies illustrate both: AI chatbots and university students' learning (388 records, 100 included) and AI-assisted SR methods (131 records, 123 included, QualityScore 69.1 recomputed with a proxy network sub-score). They show end-to-end feasibility across domains and the diagnostic use of QualityScore: in the first run, corpus improvements chosen at the corpus-adequacy checkpoint raised the score from 74.6 to 81.9 and the number of pre-2023 studies from 1 to 19. Audits of both runs exposed failure modes: incomplete retrieval, counts that drifted between agents, unrecorded or delegated checkpoint decisions and a grade that depends on how citation data are handled. PARIS fully supports 8 of the 27 PRISMA 2020 items and partially supports 11. Output quality has so far been judged only by an internal reviewer agent; independent validation against human reviews is the next step.

---


### 345. [ECOS: Environment-Calibrated On-Policy Self-Distillation for Language Agents](https://arxiv.org/abs/2611.12232)

**<font color=#1a73e8>作者：</font>** Chenhao Zhang, Zhongan Wang, Mingxuan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation lets a language agent act as its own Teacher by conditioning on privileged context such as skills written from its own trajectories. Its guidance, however, is weighted by how much this context shifts token likelihoods rather than by whether it improves behavior, so errors in self-written skills return through later updates. We propose environment-calibrated on-policy self-distillation, which uses environmental outcomes to decide how much to trust the Teacher's current guidance and which self-written skills to reinforce. Command-level advantages, estimated by comparing commands executed at similar observations, scale each Teacher preference and reward reflections and skills whose induced preferences favor higher-advantage commands. Without skills at inference, 3B and 7B agents reach 90.5% and 93.3% macro success on seen ALFWorld tasks and 75.5% and 80.5% success on WebShop. On unseen ALFWorld tasks, they outperform GRPO under the same protocol by 11.0 and 7.6 percentage points, respectively. In an ablation study, supervising only executable commands rather than the Actor's full response raises 3B WebShop success from 52.3% to 75.0%.

---


### 346. [Prune, Don't Merge: Expert Compression of Mixture-of-Experts LLMs on Multilingual Production Tasks](https://arxiv.org/abs/2611.12240)

**<font color=#1a73e8>作者：</font>** Tomas Rasymas, Povilas Kvedaras  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts language models are cheap to run per token but expensive to hold in GPU memory, which drives the cost of serving them in production. One-shot expert compression shrinks them after a single calibration pass. Its two current state-of-the-art methods are REAP for expert pruning, which deletes the least salient experts, and REAM for expert merging, which merges them into the most salient ones. Both have been evaluated only on academic benchmarks. We compare the two on five multilingual production tasks of a web-hosting company, from classification to the generation of marketing HTML email templates, with two 30B-parameter models (Qwen3-30B-A3B-Instruct-2507 and the hybrid Mamba-attention Nemotron-3.5-Lightning) at 25% and 50% of experts removed and the same calibration data. Pruning wins: on the same rows, REAP is significantly better in 16 of 20 comparisons and REAM in 2. At 25%, REAP keeps 93.6% of Qwen3-30B's generative quality and REAM 62.5%, although on benchmarks the two are within a point for the same model. The damage concentrates in the output contract rather than the content: 89.8-95.2% of each significant loss on email templates comes from hard-gate failures such as invalid JSON, broken mobile layouts and runaway generation, and most failed non-English domain descriptions copy the prompt's English opening phrase. Cross-perplexity and logit divergence, two diagnostics from the REAP paper, also track production quality, as does the rate of repetition loops; n-gram diversity does not. We close with practical guidance for compressing MoE models for production.

---


### 347. [SNAPRAG: Cost-Efficient Knowledge Extraction Attack on RAG Systems via Adversarial Perturbations](https://arxiv.org/abs/2611.12241)

**<font color=#1a73e8>作者：</font>** Melih Coşğun, Mehmet Emre Gürsoy, Alptekin Küpçü 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) systems improve Large Language Model (LLM) responses by incorporating information from external knowledge bases. However, recent studies have shown that attackers can extract substantial portions of private knowledge bases from RAG systems through repeated querying. Yet, state-of-the-art extraction attacks either rely heavily on external LLMs to generate adversarial queries or require a large number of queries. In this paper, we propose SNAPRAG, a novel and cost-efficient attack for extracting RAG knowledge bases through adversarial perturbations. Our approach algorithmically generates adversarial queries without relying on external LLMs and allows for a strictly configurable query budget. In particular, SNAPRAG uses a discrete token-mutation algorithm to generate novel queries in a strict black-box setting. Our adaptive dissimilarity threshold calibration systematically forces queries into unexplored semantic regions of the target database, enabling extraction with fewer queries. Specifically, to extract half of the target knowledge base, our method requires up to 6.77$\times$ fewer queries than existing approaches. Furthermore, within a fixed query budget, our method recovers up to 96.9%, outperforming the closest approach by 7.7-19.9%. We further evaluate SNAPRAG against active defenses, where it remains the leading attack on four of five defended targets, achieving 50.7-96.3% extraction rate.

---


### 348. [Agent4Crypto: A Dual-Reflective and Market-Feedback-Aligned LLM-Based Multi-Agent System for Cryptocurrency Trading](https://arxiv.org/abs/2611.12269)

**<font color=#1a73e8>作者：</font>** Guangyan Gan, Jiahao Li, Jiashun Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Cryptocurrency markets provide a natural testbed for autonomous AI agents because they are digital-native, high-frequency, and machine-speed environments, yet existing methods often struggle with non-stationary market regimes, opaque decisions, and fixed aggregation rules. In this paper, we propose Agent4Crypto, a dual-reflective and market-feedback-aligned multi-agent system. The framework coordinates specialized agents for data collection, analysis, risk assessment, reflection, and trading, synthesizing heterogeneous signals from prices, indicators, news, and charts in an interpretable decision pipeline. Our central design is a trader-centric decision mechanism: three style-specific trader agents, Aggressive, Neutral, and Conservative, generate candidate actions and natural-language rationales from the same market context, while their influence is learned rather than manually fixed. A PPO-based gating policy dynamically allocates trader weights through a dual-reflective feedback process. One reflection stream evaluates post-trade decision quality from realized portfolio outcomes and distills reusable lessons into a Financial ReasoningBank for retrieval in subsequent trader prompts, while the other estimates trader-level counterfactual contribution, indicating which style has recently aligned better with market movements. The PPO state combines Counterfactual Contribution Memory with market features, previous trader weights, and current trader actions, so trader influence adapts across bull, sideways, and bear regimes. Experiments on BTC, ETH, and XRP show that Agent4Crypto improves total return and Sharpe ratio over traditional strategies, machine learning and reinforcement learning baselines, and existing LLM-based trading systems, demonstrating the value of interpretable trader competition and market-feedback-driven adaptation in volatile cryptocurrency markets.

---


### 349. [Learning Evidence-Grounded Reasoning for Context-Aware Time Series Forecasting](https://arxiv.org/abs/2611.12285)

**<font color=#1a73e8>作者：</font>** Xingpeng Gao, Mingyue Cheng, Daoyu Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-driven time series forecasting has become increasingly promising by leveraging contextual features to generate future values directly or refine forecast priors. However, incorporating contextual features alone does not ensure that models can identify which features matter for forecasting and understand what they suggest about future dynamics. We argue that the fundamental challenge is how to extract predictive evidence from contextual features and when and how to leverage it to guide forecasting decisions. In this paper, we propose CastReasoner, an evidence-grounded reasoning model for context-aware time series forecasting. Specifically, CastReasoner uses a structured chain of thought (CoT) to extract predictive evidence from contextual features, infer the future dynamics suggested by this evidence, and assess these dynamics against the forecast prior to guide adaptive forecasting decisions. To enable this capability, we design a reasoning-centric two-stage post-training framework including supervised fine-tuning (SFT) and reinforcement learning (RL). First, we synthesize reasoning trajectories through controllable multi-teacher guidance and select high-quality ones using a novel student-aware difficulty metric. Second, we design fine-grained multi-objective rewards to further improve reasoning and forecasting. To address heterogeneous learning needs across domains in both stages, we introduce a convergence-guided data balancing strategy. Through this two-stage training, CastReasoner improves both reasoning quality and predictive accuracy. Extensive experiments across multi-domain forecasting benchmarks demonstrate that CastReasoner achieves superior forecasting performance.

---


### 350. [Depth as a Candidate Source: Portfolio Allocation for Recurrent Test-Time Scaling in Large Language Models](https://arxiv.org/abs/2611.12293)

**<font color=#1a73e8>作者：</font>** Chaoyuan Hao, Wentao Yue, Yanyan Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recurrent latent reasoning in large lanugage models (LLMs) scales test-time computation by increasing recurrent depth, naturally framing inference as a problem of deciding when to stop. We identify a previously overlooked limitation of this single-depth view through systematic preliminary analysis: deeper recurrence can lose correct solutions found at shallower depths, while depth-specific success sets remain broadly non-nested even after controlling for marginal accuracy. This suggests that depth determines not only computation cost, but also access to distinct candidate solutions. Motivated by this finding, we propose Depth Portfolio Allocation (DPA), which reformulates recurrent test-time scaling as budgeted allocation across depth-specific candidate sources. DPA supports both fixed portfolios and feedback-guided sequential allocation under a shared inference budget. Experiments on GSM8K, SVAMP, MultiArith, and MBPP show that mixed-depth portfolios expand oracle coverage under matched candidate counts and nominal costs, while feedback-guided allocation generally matches or improves uniform allocation and can reduce computation in high-budget settings. Code and data are avaible at : this https URL.

---


> [!TIP]
> 当前位于：**301-350**（第 7/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-438](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
