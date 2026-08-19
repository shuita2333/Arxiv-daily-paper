# 🧠 大模型相关研究 | 2026年08月20日

> 本类共 **161** 篇论文：已确认 **151** 篇，待复核 **10** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-161**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-161**

---

### 151. [Multi-Agent AI System for Radiology Report Structuring and Quality Assurance with Independent Radiologist Evaluation](https://arxiv.org/abs/2608.18072)

**<font color=#1a73e8>作者：</font>** Iryna Hartsock, Cesar Lam, Christopher Otteni 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Purpose: To develop and evaluate a locally deployed multi-agent AI system for radiology report structuring and quality assurance. Materials and Methods: This retrospective study included 638 radiology reports from CT examinations of the chest, abdomen, and pelvis dictated by 15 board-certified radiologists in 2023 and 2024. A multi-agent AI pipeline was developed to perform report structuring and quality assurance (QA). The system structured the report into standardized anatomical sections at the sentence level using regex rules and local large language models. It also detected mismatches between the Findings and Impression sections, or within sections; gender-anatomy conflicts; and undocumented communication of critical findings. Two board-certified radiologists independently evaluated a 45-report subset. Results: The multi-agent system structured the Findings sections of all reports (22,270 sentences) into a predefined anatomical format while retaining the original report content. The system flagged 90 (14.1%) reports, most commonly for section mismatches (80 reports, 12.5%). In the radiologist evaluation, both reviewers agreed that 31 (69%) were correctly restructured, 2 reports (4%) were incorrectly restructured, and disagreed on the remaining 12 reports (27%). Both reviewers agreed that no clinically important information was omitted and no fabricated content was introduced. Overall QA performance was rated as "excellent" or "good" in 84% of the evaluated reports, with the remaining reports rated as "fair". Conclusion: A locally deployed multi-agent AI system combined radiology report structuring and quality assurance within a single workflow. The system demonstrated favorable performance in radiologist evaluation. Such systems may support standardization of reporting and quality assurance in radiology practice.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 152. [KernelArc: A Multi-Agent Framework for GPU Kernel Optimization](https://arxiv.org/abs/2608.17071)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Joyjit Kundu, Ben Stoffelen, Kaili Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present KernelArc, a multi-agent framework for autonomous GPU kernel optimization across heterogeneous workloads. Strategy-specialized agents run in parallel and coordinate through conclusions-only shared memory, a deterministic benchmark guard, and read-only cross-agent state with plateau-triggered drafting. We evaluate \kernelarc{} on NVIDIA H100 and B200 GPUs using category-representative SOL-ExecBench workloads. The resulting implementations span custom BF16 GEMM, static cuBLASLt Expert-API configuration tables, fused mixture-of-experts backward, shape-gated decoder-layer fusion, native NVFP4 grouped-query attention, and paged prefill attention. At the public SOL-ExecBench leaderboard snapshot recorded on July~30, 2026, these submissions ranked first on representative L1, L2, Quantization, and FlashInfer tasks. The trajectories support the paper's central motivation: shared multi-agent search can broaden exploration and reach stronger incumbents within a fixed candidate budget, while the value of individual coordination features depends on the kernel and optimization stage.

---


### 153. [LiveHouse-TS: An Open-world Living Benchmark for Time Series Foundation Models](https://arxiv.org/abs/2608.17299)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haomin Wen, Ziyu Zhou, Qingxiang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time Series Foundation Models (TSFMs) have recently emerged as a highly promising paradigm for cross-domain zero-shot forecasting. However, existing evaluation protocols predominantly rely on static benchmarks with fixed historical test windows. While these benchmarks provide a valuable baseline snapshot, they evaluate an average performance on a fixed history, failing to capture how models behave in continuously evolving real-world environments characterized by seasonal variations, distribution shifts, and unexpected events. To bridge this gap, we introduce LiveHouse-TS, the first open-world living benchmark infrastructure for TSFMs. By evaluating models prequentially on real future data in open-world environments, LiveHouse-TS shifts time series benchmarking from snapshot accuracy to continuous temporal validity. Rather than acting as a one-off leaderboard, our infrastructure serves as a continuous time series infrastructure designed to explore vital, long-term scientific questions: Can model rankings be maintained over the long term? Which models remain genuinely robust under distribution shifts? Extensive streaming evaluations across 11 domains with 17 datasets demonstrate that static rankings undergo a dramatic reshuffling under a live protocol.

---


### 154. [Wuying-Browser-Agent: Real-World Centric Fundamental Long-Horizon Browser Agents](https://arxiv.org/abs/2608.17319)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** AIMAE Team, Tianxiang Chen, Yan Cheng 等 42 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Browser agents perform well on short, clean demonstrations, but real deployment is fundamentally different: agents must sustain dozens of decisions on live websites while recovering from mistakes and navigating complex UIs. We argue that closing this gap requires alignment at every level of the pipeline, including execution, supervision, optimization, and evaluation, rather than scale alone. We present Wuying-Browser-Agent, a unified framework that addresses each of these levels. A structured browser harness provides stable execution primitives and decision-oriented context management. Reflection and UI-specialized Curriculum SFT (RUIC-SFT) explicitly trains on recovery trajectories and complex-UI interactions. Divergence-Aware Online GRPO (DAO-GRPO) improves long-horizon credit assignment through potential-based reward shaping and divergence-aware step weighting. Finally, we introduce BrowserBench, a bilingual real-web benchmark of 350 tasks averaging 37.9 steps, because most existing benchmarks are too short to expose long-horizon failure modes. Wuying-Browser-Agent-27B achieves 80.6\% on WebVoyager, 66.7\% on Online-Mind2Web, and 65.1\% on BrowserBench, establishing a new open-source state of the art on browser-use benchmarks. The same pipeline also transfers beyond browser use, demonstrating strong general agentic ability and reaching an average score of 73.8 on Tau2-Bench, Claw-Eval, and BFCL-v4.

---


### 155. [Towards Better Agents for Multi-Turn User Interaction: The Next User Turn Is More Than Context](https://arxiv.org/abs/2608.17499)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yiwen Zhao, Zhihao Wen, Yuchen Mao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> User-facing tool agents must coordinate dialogue and tool use as user goals unfold over multiple turns. Yet interactive reinforcement learning typically reduces each rollout to a terminal reward, assigning the same credit to effective elicitation, errors, and later repair. The next user turn is more than context: it also provides noisy, temporally local evidence about the preceding user-to-user segment. We introduce \textbf{F}eedback-\textbf{A}ware \textbf{C}redit \textbf{A}ssignment (\textsc{FACA}), which aligns each reaction with that segment, derives a locally normalized reaction advantage, and adds it to verified terminal outcome advantage without an extra critic or rollout. Against an outcome-only Interactive GRPO control matched in simulator, visible dialogue, initialization, rollout, and optimization, \textsc{FACA} improves the nine-domain $\tau$-family average across three independently trained runs by 5.91 and 10.22 percentage points at 8B and 14B, respectively. Gains concentrate in Telecom; at 8B, randomizing reaction polarity removes the Telecom gain. The same ordering holds zero-shot on Pare-Bench and Co-Gym. These results demonstrate that next-turn user reactions provide actionable local credit for improving multi-turn user-interacting agents.

---


### 156. [BrainNorm: A Foundation Model that knows Normal via Semantic Atlas Pretraining](https://arxiv.org/abs/2608.17521)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Madhumitha Venkatesh, Shanawaj S Madarkar, Konda Reddy Mopuri  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce BrainNorm, a normative foundation model, trained and tested on ~66,000 T1-weighted structural MRI (T1w sMRI) scans. By leveraging language-image style contrastive pretraining on healthy cohorts across ages, BrainNorm learns a Semantic Atlas Latent space (SAL), where each scan is represented as a set of atlas-parcel embeddings. This yields parcel-specific healthy aging template trajectories that support age-consistent template matching and localized deviation scoring relative to a subject's chronological age. Across 6 downstream cohorts, BrainNorm demonstrates generalization evaluated across 25 task-setting combinations spanning age estimation, brain-age gap estimation, parcel identification, and single- & multi-disease classification tasks under direct inference, zero-shot, few-shot & full-data linear-probe settings. The resulting deviation patterns in SAL space enable zero-shot tasks for disease prediction using parcel-wise abnormalities. Fine-tuning on healthy-only cohorts of downstream datasets further improves the performance of various tasks. Across all classification tasks, linear probing on BrainNorm's frozen embeddings outperforms 9 baselines finetuned under end-to-end supervision. Furthermore, the localized deviations identified by BrainNorm across various neurodegenerative disorders closely align with established neurodegeneration pathology in clinical literature.

---


### 157. [Thinking in a Low-Resource Language: What SFT Builds, What RL Fixes, What Accuracy Cannot See](https://arxiv.org/abs/2608.17744)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ayoub Kirouane, Christos Petrocheilos  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Take three frontier mixture-of-experts models (Alibaba, OpenAI, NVIDIA; 3.6-4.0B active parameters each) and fine-tune them to reason in a low-resource language. On accuracy benchmarks almost nothing happens, and the benchmark itself is noise at this scale: changing only the random seed moves the score by 7.7 points, more than every data and recipe effect we measured. That null is our first result. The real changes live where accuracy cannot see. Base models never think in Greek: 0 of 1,000 reasoning traces, even when the question is Greek, so the model answers correctly while reasoning in a form its user cannot read, audit, or correct. After supervised fine-tuning (SFT), every released checkpoint reasons in the language of the question on ~98% of items, one family at 3x fewer tokens, with judged grammaticality improving on all four models and general ability within a few points of each base: nothing was forgotten, and fluency was gained. We propose six behavioural dimensions that make such changes measurable, each gated to reject any metric that correlates with output length, and we report how our own instruments lied: six failures, each caught by a control. What SFT cannot do is fix its own defects: a quarter of answers skip the requested format, answers leak into the reasoning channel, and an explicit "think in English" is obeyed under half the time. Reinforcement learning with verifiable rewards, pre-registered before training, fixes the first two outright (fallback 24% to 2.5%, leak 3.5% to 0.0%, both against a flat random-reward control) and moves the third (+9.1pp), while the Greek reasoning habit survives an accuracy-only gradient untouched. We release five checkpoints. The instruments, the controls and the pre-registration travel to any low-resource language; Greek is the case that let us measure them.

---


### 158. [MoRAX: Mobility-based Representation Augmentation for Geospatial Foundation Models](https://arxiv.org/abs/2608.17848)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ya Wen, Jixuan Cai, Yulun Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Geospatial Foundation Models (GFMs) are emerging as a powerful paradigm for learning semantically rich and geographically consistent visual and physical representations. However, their reliance on Earth-observation (EO) data leaves information about human activity largely underrepresented. Human mobility data reveals the functional and relational structure between regions that is missing from EO data, but is often limited only to the city where it is observed, making it challenging to use for transferable urban representation learning. We introduce MoRAX, a lightweight framework for augmenting geospatial embeddings with functional structure derived from human mobility. MoRAX preserves the coverage and consistency of a GFM while providing information about the functional connectivity among urban regions, permitting zero-shot deployment in unseen cities with or without available mobility data. Across four target cities spanning two countries, the MoRAX teacher model, which observes mobility, consistently outperforms GFMs and strong urban representation baselines in eight socioeconomic and environmental prediction tasks. Meanwhile, the student model, which never takes mobility data as input, approaches the teacher in performance on most tasks. Transfer results across countries further demonstrate that modulation conditioned on mobility flows provides a general mechanism for grounding geospatial foundations in the human dimension of cities.

---


### 159. [DistillPath: An Efficient 22M Distilled Pathology Encoder Approaching Large Foundation Model Performance](https://arxiv.org/abs/2608.17872)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ramon Kaspar, Andrey Ignatov, Valentina Boeva  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many high-performing pathology tile encoders are now foundation models with hundreds of millions to over a billion parameters. Encoding and storing the thousands of tiles in each whole-slide image with such models is costly on commodity hardware, so compact encoders that retain useful downstream performance are a valuable alternative. We present DistillPath-KS16, which starts from the existing 22M kaiko ViT-S/16 encoder and improves it by distilling from released pathology encoders used as frozen teachers. The recipe reads only the teachers' final class and patch tokens and trains on 6,000 public slides, needing neither their DINO nor iBOT pretraining heads nor a billion-tile corpus, so it applies to any released encoder that exposes backbone tokens. We distill four teachers spanning 86M to 1.1B parameters into the same student. Every variant improves the kaiko baseline on all three benchmarks we use, EVA, HEST, and PLISM, and the strongest teacher is task-dependent. On the seven-task EVA mean, DistillPath-KS16-Virchow2 reaches $0.795$, within $0.015$ points of Virchow2, the top-scoring model in our evaluation, at about $29\times$ fewer parameters; it also scores above H0-mini and GPFM on this aggregate metric, though that advantage is task-concentrated rather than uniform. Because it remains a 22M ViT-S/16 with 384-dimensional features, DistillPath-KS16 runs more than $25\times$ faster than Virchow2. Code is available at this https URL, and released model weights are available at this https URL.

---


### 160. [Understanding the Surprising Generalization Properties of Tabular Foundation Models](https://arxiv.org/abs/2608.17957)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Nour Shaheen, Junwei Ma, Alex Labach 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular Foundation Models (TFMs) increasingly rely on in-context learning, where a model receives labelled examples at inference time and predicts labels for new inputs without updating its weights. Existing TFMs are typically trained on either massive synthetic corpora or very large collections of real datasets. In contrast, we show that surprisingly strong transfer can emerge from self-supervised pre-training on just a single real table. In this setting, we also find that tables tend to be either broadly useful or broadly poor regardless of downstream prediction task, and that the strongest predictor of usefulness is the number of features rather than the number of instances. This leads to a task-centric interpretation of tabular pre-training: the number and the quality of tasks are essential for the pre-training of TFMs.
We show that the same task-centric perspective can help corpus design at scale: fine-grained column-level pre-processing consistently improves downstream performance, while no improvements are observed when we filter or deduplicate at the dataset level.
Finally, we offer a new perspective for how TFMs generalize: we believe that tabular in-context generalization is largely retrieval-based, and good models are those that learn to identify relevant examples in the provided context and aggregate them well. The mechanics of TFMs have been relatively understudied; our task-centric, retrieval-based perspective offers a new framework to guide future model and corpus design.

---


### 161. [Deep Academic Survey: Stateful Agentic Closed-Loop Paradigm for Academic Survey Automation](https://arxiv.org/abs/2608.18034)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhikai Xu, Zhucun Xue, Teng Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Academic surveys play a central role in organizing rapidly expanding scholarly literature, yet their construction requires extensive paper analysis, coherent knowledge organization, fine-grained citation support, and reliable manuscript assembly. Existing Deep Research and automated survey generation systems address parts of this process, but typically do not coordinate paper understanding, literature organization, evidence-grounded drafting, and manuscript validation through a shared, revisable state. We introduce DAS, a stateful agentic framework for generating publication-oriented academic surveys. Its key idea is to separate reusable paper analysis from topic-specific manuscript construction. DAS builds on DAS-2M, a dynamically updated metadata lake containing survey-oriented representations of approximately two million papers. Its agents maintain explicit literature, organization, writing, and finalization states through candidate-grounded taxonomy planning, reverse paper-to-section routing, and hierarchical claim and citation planning. Semantic review reactivates only the affected writing states for repair and reevaluation, forming a scoped closed loop with deterministic validation. We further introduce DAS-Bench, a 30-topic benchmark, together with DAS-Eval, which assesses scholarly citation quality, taxonomic synthesis, hierarchical discourse, and manuscript assembly reliability through 16 criteria. Among systems evaluated on all 30 topics, DAS achieves the highest average in all four dimensions, with an overall score of 4.34 compared with 4.03 for the strongest competitor, and the same ordering is preserved on the matched 21-topic CS subset. Blinded expert evaluation further prefers DAS to Naive RAG on 27 of 30 topics and to AutoSurvey on 19 of 21 shared CS topics. The project page is available at this https URL.

---


> [!TIP]
> 当前位于：**151-161**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-161**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
