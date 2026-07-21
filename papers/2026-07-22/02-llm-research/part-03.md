# 🧠 大模型相关研究 | 2026年07月22日

> 本类共 **204** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-204](./part-05.md)

---

### 101. [Explaining and Tuning Transformer-based LLMs in Arithmetic Tasks with Human Strategies](https://arxiv.org/abs/2607.17166)

**<font color=#1a73e8>作者：</font>** Luyu Qiu, Jianing Li, Hwanhee Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based large language models (LLMs) continue to achieve state-of-the-art performance across various natural language processing tasks. However, their subpar performance on seemingly elementary problems, such as basic arithmetic, raises concerns about model reliability, safety, and ethical deployment. In this study, we demonstrate that the performance of a vanilla Transformer model trained on integer arithmetic tasks can be improved using methods effective for human learners. We begin by decomposing the arithmetic task into well-defined subtasks and conducting loss convergence order analysis together with ablation studies for each subtask. Our findings reveal that LLMs exhibit learning patterns similar to those of human learners, with a faster learning speed for simpler subtasks compared to more complex ones. In addition, we successfully improved the accuracy of LLMs by applying problem-solving strategies and cognitive empowerment methods shown to enhance the performance of human learners. This suggests that transformer-based LLMs may share cognitive processes with human learners in arithmetic. Lastly, we provide a comprehensive demonstration of our method's effectiveness, including significant accuracy improvement experiments, visualization verification, and explanation-based analysis to illuminate the intricacies of LLMs in arithmetic learning. In general, this work explores the potential similarities between transformer-based LLMs and human learners, supported by explainable AI (XAI) verifications, ultimately fostering trust in LLMs for critical and high-stakes applications.

---


### 102. [KyrgyzLLM-Bench: Benchmarking Kyrgyz Language Understanding](https://arxiv.org/abs/2607.17173)

**<font color=#1a73e8>作者：</font>** Timur Turatali, Aida Turdubaeva, Rustem Izmailov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating large language models (LLMs) across languages remains challenging, as most multilingual benchmarks rely on translated English datasets, often obscuring linguistic and cultural specificity in the target language. This issue is particularly pronounced for less-resourced languages such as Kyrgyz, where reliable natively authored evaluation data are scarce. Building on previously introduced Kyrgyz-language evaluation datasets, this work reports the first systematic and large-scale evaluation of LLMs in Kyrgyz using the KyrgyzLLM-Bench benchmark suite. KyrgyzLLM-Bench comprises two natively authored datasets$-$KyrgyzMMLU and KyrgyzRC$-$together with carefully translated and manually post-edited versions of WinoGrande, HellaSwag, BoolQ, and TruthfulQA. We evaluate 26 open- and closed-source LLMs under zero-shot and few-shot settings, analyzing model performance, cross-lingual transfer, and the impact of translation artifacts on evaluation reliability. Across families and tasks, model rankings transfer broadly from English to Kyrgyz on WinoGrande and BoolQ, and to a lesser extent on MMLU, while HellaSwag exhibits a substantial English-Kyrgyz performance gap consistent with translation-induced plausibility shifts. Few-shot prompting improves several open-source models on reading comprehension but behaves inconsistently for proprietary models on translated tasks. We publicly release all datasets, evaluation code, and per-model results, and integrate the Kyrgyz tasks into a widely used multilingual evaluation framework to support future research on Kyrgyz NLP.

---


### 103. [BanClickThumb: A Multimodal Dataset and Transformer Fusion Benchmarks for Clickbait Detection in Bengali YouTube Videos](https://arxiv.org/abs/2607.17182)

**<font color=#1a73e8>作者：</font>** Md. Ariful Islam, Md Tanvirul Islam, Md. Maruf Hossain Miru 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clickbait, where video titles and thumbnails exaggerate or misrepresent content, reduces user trust, wastes attention, and promotes misinformation on video-sharing platforms. Detecting Bengali clickbait remains challenging because publicly available multimodal datasets are limited. To address this gap, we introduce BanClickThumb, a curated dataset of 7,147 Bengali YouTube thumbnail-title pairs from five content domains, annotated by ten annotators with high agreement (Cohen's Kappa: 0.83-0.93). Using this dataset, we benchmark text-only, image-only, and multimodal approaches. Among unimodal models, BanClickTextFormer (XLM-RoBERTa) achieves 0.82 accuracy, while BanClickImageFormer (SwiftFormer) reaches 0.68. Our proposed multimodal model, BanClickFusionFormer, combines ViT and XLM-RoBERTa through intermediate fusion and achieves the best accuracy of 0.84. Error analysis shows that dense thumbnail text, figurative language, and culturally specific slang remain challenging. Our findings demonstrate the effectiveness of multimodal fusion for Bengali clickbait detection and provide a publicly available benchmark to support future research on low-resource multimodal content analysis.

---


### 104. [Is Your Model Thinking or Just Stagnating? PUMA: Diagnosing Reasoning Pathology via Phase-Momentum Alignment](https://arxiv.org/abs/2607.17188)

**<font color=#1a73e8>作者：</font>** Cheng Yan, Guangyang Ye, Wuyang Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time scaling empowers Large Reasoning Models (LRMs) to tackle complex tasks via extensive Chain-of-Thought (CoT). However, this often induces the "overthinking" paradox, where redundant reasoning increases computational overhead without guaranteeing accuracy. Existing test-time efficiency optimization methods primarily fall into two categories: information-theoretic approaches, which are prone to "deceptive convergence" where low uncertainty masks hallucinations, and latent representation analyses, which are often post-hoc, lacking the real-time sensitivity for dynamic reasoning. To bridge this gap, we first posit the Phase-Momentum Alignment Hypothesis, asserting that reasoning correctness hinges on the temporal synchronization between geometric momentum and uncertainty resolution. We then theoretically formulate the Cognitive-Energy Model to characterize these dynamics through two orthogonal dimensions: Geometric Cognitive Effort, quantified by latent velocity and tortuosity, and Entropic Cognitive Uncertainty. To operationalize this, we introduce PUMA (Phase-Uncertainty Momentum Alignment), a training-free framework employing a tiered diagnostic architecture. By coupling lightweight phase monitoring with event-triggered geometric analysis, PUMA effectively distinguishes active exploration from passive stagnation, enabling precise interventions through adaptive truncation or corrective measures. Extensive experiments on LRMs spanning 1.5B to 32B demonstrate that PUMA consistently outperforms state-of-the-art baselines across diverse benchmarks, achieving a superior accuracy-efficiency trade-off and robust cross-domain generalization.

---


### 105. [Toward Anthropomorphic Dialogue: A Closed-Loop Framework for Human-Like Chat Generation, Evaluation, and Preference Alignment](https://arxiv.org/abs/2607.17191)

**<font color=#1a73e8>作者：</font>** Wentao Liu, Siyu Song, Xi Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human-like private chat requires more than fluent response generation: a system must preserve persona, relationship, memory, bounded knowledge, medium-specific timing, and a coherent multi-turn arc. We present AnthroDial, a closed-loop framework that formulates anthropomorphic dialogue as a joint problem of system architecture, executable evaluation, and diagnostic alignment. It combines (1) a role-conditioned scheduled dialogue runtime with persona and scenario cards, long-term memory, virtual time, and single-draft message decisions; (2) an executable benchmark with an L0 validity gate, five per-turn dimensions, and five dialogue-level dimensions; and (3) a post-training pipeline that filters 16,436 scheduled-decision examples for SFT and applies GRPO with a cognitive-diagnostic, ZPD-aware reward. The reward maintains Kalman-filtered capability estimates for each behavioral dimension, upweights dimensions with larger capability deficits, and uses rollout scores as task-level ZPD matches to focus optimization on learnable weak skills. On a benchmark with 55 personas, 50 scenarios, 50 persona-scenario bindings, and 100 role-conditioned cases per model, we evaluate 16 systems spanning frontier baselines, open models, thinking/no-think variants, and SFT/RL ablations. The strongest non-trained baseline reaches 32.00% strict ACC, while Qwen3.6-27B-SFT+RL reaches 39.00% strict ACC and a 98.5 overall score. In the 9B no-think setting, SFT and RL improve strict ACC from 0.00% to 13.00% and 18.37%. These results show that anthropomorphic dialogue benefits when generation, evaluation, and reward shaping share the same behavioral dimensions.

---


### 106. [A Systematic Evaluation of Trajectory Data Curation for LoRA Fine-Tuning of Code Agents](https://arxiv.org/abs/2607.17205)

**<font color=#1a73e8>作者：</font>** Yunze Han  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) of open-weight LLMs on expert agent trajectories has emerged as a prominent approach to building capable code agents without reliance on proprietary models. A central yet underexplored question is how trajectory quality and quantity jointly shape model performance. We present a systematic empirical study of trajectory data filtering for LoRA fine-tuning of Qwen2.5-Coder-7B-Instruct on the SWE-trajectory dataset (67,074 trajectories, of which 32,161 are resolved). We propose a two-axis quality scoring framework -- Efficiency and Style -- and evaluate it through 16 controlled experiments spanning strategy, scale, and ablation analyses. Since 7B-scale models attain near-zero SWE-bench resolve rates, we adopt cross-entropy (CE) loss on held-out trajectories as the primary metric, validated via first-action generation: CE loss and ROUGE-L are perfectly rank-correlated (Spearman $\rho$ = -1.00), with limited-sample evidence supporting but not conclusively establishing this proxy. Our results reveal a scale-dependent quality-quantity trade-off: at small scales, doubling the dataset (500 to 1,000) yields ~12.7% CE-loss reduction whereas the TopQ-Random gap stays <1% (Mann-Whitney p > 0.10); at 2,000 trajectories this same gap widens to 3.6% (p = 0.016). Ablation further identifies error-retry rate as the dominant sub-dimension, performing comparably to the full composite ($\Delta$ < 0.2%). Together, these findings establish trajectory-level quality scoring as a viable but scale-sensitive lever for code-agent SFT and offer a proxy-validated evaluation protocol for the regime where end-to-end resolve rate is statistically infeasible.

---


### 107. [Induce to Empower: Improving Lightweight Baselines via Foundation Model Induction for Generalized Polyp Segmentation](https://arxiv.org/abs/2607.17208)

**<font color=#1a73e8>作者：</font>** Shivanshu Agnihotri, Snehashis Majhi, Deepak Ranjan Nayak 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated polyp segmentation in colonoscopy continues to pose challenges due to substantial appearance variations and indistinct polyp boundaries. Although emerging foundation models (FMs) such as DINOv2, SAM, and OneFormer, demonstrate remarkable generalization capabilities, their direct transfer to the polyp segmentation task and deployment in real-time clinical settings are difficult due to lack of large-scale labeled data and high computational demands. In addition, adopting multiple FMs together raises concerns, even though they encode complementary semantic and structural information. While lightweight models, including U-Net, PraNet and U-Net++, are computationally efficient, they often struggle to generalize across datasets due to limited representational capacity. To address this gap, we propose Lite-Polyp Inductor (Lite-Pi), a novel foundation model induction framework that significantly enhances lightweight polyp segmentation baselines. Our proposed framework generates FM-specific prototype representations and aligns them semantically with the corresponding foundation model priors through reconstruction-based supervision. Subsequently, transformer-based fusion is introduced to highlight the polyp relevant representations, including salient boundary information, while preserving complementary semantic cues. Extensive experiments across five polyp segmentation benchmark datasets demonstrate that Lite-{\pi} significantly improves lightweight baselines, achieving superior generalization performance with minimal computational overhead and thereby, offering a practical solution for generalized polyp segmentation. Our code is available at GitHub. this https URL

---


### 108. [Auditing Question-Order Effects in Large Language Models with the QQ Equality: Mechanism Characterization and a Saturation Caveat](https://arxiv.org/abs/2607.17219)

**<font color=#1a73e8>作者：</font>** Pilsung Kang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human survey respondents exhibit question-order effects that satisfy the QQ (quantum question) equality, an a priori, parameter-free prediction of the projective quantum question-order model. We develop the QQ equality into an audit criterion for sequential judgments of autoregressive large language models (LLMs). Theoretically, we characterize which mechanism classes satisfy it robustly: marginal-independent kernels satisfy QQ iff all four mismatch transition rates coincide (a class containing the 2D rank-1 projective model with a fixed measurement pair under state variation); a polarity- and position-dependent repetition family is characterized by an exact cross-symmetry condition with closed-form violations; QQ-satisfying behaviors are closed under order-matched mixing; and the rank-2 Contextuality-by-Default criterion translates into audit coordinates as $|\qQQ|\le\OSS$, where $\OSS$ (the order-sensitivity score) totals the order sensitivity of the two marginals. Methodologically, we develop a pre-specified, audit-logged pipeline applicable to any model exposing next-token log-probabilities; it combines worst-case robustness envelopes, sampling-consistency spot checks, full label counterbalancing, and a saturation diagnostic. Empirically, in a first-signal pilot on an open-weight instruction-tuned model under two framings, all pre-specified health gates passed, yet 17/18 and 7/8 item pairs, respectively, were saturated (near-deterministic), and no item was certified residually contextual. Forced-binary next-token log-probabilities were thus inadequate for distribution-level QQ audits under the tested model and prompting conditions; we recommend pre-specified saturation diagnostics whenever next-token distributions are treated as survey-response distributions.

---


### 109. [Literary Non-Style in LLM-Generated Text](https://arxiv.org/abs/2607.17228)

**<font color=#1a73e8>作者：</font>** Cory Massaro  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prior work on LLM-generated text has demonstrated quantitative and qualitative departures from text produced by humans. LLM-generated texts differ from human writing in style, resulting in a characteristic textual "feel," while the semantic range of LLMs is much restricted compared to that of humans. In this contribution, I note simple but consistent patterns in the statistical distribution of n-grams within LLM-generated text. Via qualitative analysis of these n-grams, I reveal deficiencies in LLM style. Because higher-order n-grams correlate to semantic content, I conclude that questions of style and semantics are not cleanly separable.

---


### 110. [Distilled Reinforcement Learning for LLM Post-training](https://arxiv.org/abs/2607.17247)

**<font color=#1a73e8>作者：</font>** Chen Wang, Zhaochun Li, Jionghao Bai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) post-training is essential for improving reasoning, adaptation, and alignment. Existing methods mainly follow two paradigms: reinforcement learning (RL) and on-policy distillation (OPD). However, RL relies on coarse-grained outcome supervision, resulting in difficult credit assignment and limited capability to acquire new knowledge. OPD, meanwhile, unconditionally matches teacher logits through KL divergence, which creates a dilemma: similar teachers provide little new knowledge, while substantially different teachers often yield ineffective guidance, largely restricting OPD to within-family distillation. We propose Distilled Reinforcement Learning (Distilled RL), which integrates teacher supervision into the RL objective to provide fine-grained guidance, selectively transfer new knowledge and avoid unconditional imitation. Distilled RL contains three components: reverse importance sampling with clipping, negative sample reset, and sequence-level geometric normalization. Through a concise and interpretable case study, we demonstrate that Distilled RL can effectively transfer previously unavailable knowledge from a teacher model to a student model. Extensive experiments across both within-family and cross-family distillation settings show that Distilled RL substantially outperforms standard RL and OPD in terms of both pass@1 and pass@k. Our code is available at this https URL.

---


### 111. [EvolvingWorld: An Open-Schema Framework for Co-Evolving Role-Play Agents and World Model in Interactive Literary World](https://arxiv.org/abs/2607.17250)

**<font color=#1a73e8>作者：</font>** Qing Zong, Yue Guo, Mengxin Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper introduces EvolvingWorld, a framework and benchmark for character and world co-evolution in interactive literary worlds. Existing systems either treat interactive literary simulation as static persona imitation or isolated scene generation, failing to capture how characters and worlds evolve together over time. To address this, EvolvingWorld models literary simulation as a long-horizon process where characters interact, scenes progress, and character and world states are persistently updated. Unlike prior systems relying on fixed schemas, EvolvingWorld adopts an open-schema framework to support simulation across diverse literary worlds. The framework consists of two coupled modules: a Character Agent for multi-character role-play and persistent profile evolution, and an LLM-based World Model for global and location/entity-level state maintenance and scene progression. Based on this architecture, we formulate 7 trainable tasks for scene initialization, interaction generation, and state update. We construct a dataset from 57 books, producing 138,596 supervised training samples and 222 snapshots for testing. Furthermore, we introduce a trajectory-level LLM-as-Judge evaluation protocol spanning 10 dimensions and 20 metrics. Experiments show that EvolvingWorld can improve long-horizon simulation by effectively maintaining persistent, coherent character and world development.

---


### 112. [VecFontLLM: Anchor-Guided Direct Synthesis of Chinese Vector Fonts](https://arxiv.org/abs/2607.17251)

**<font color=#1a73e8>作者：</font>** Hao Yuan, Yuxuan Luo, Xing Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Direct generation of Chinese vector fonts is a challenging and ongoing problem. A Chinese vector glyph contains complex component structure, anchor layout, and Bézier curve details, which work at different scales, but a standard vector sequence writes them together in one long sequence, making the task of vector font synthesis challenging. Existing direct vector generators often fail on complex characters, while raster-domain methods must vectorize the synthesized glyph images afterward. To address the above-mentioned problem, this paper proposes VecFontLLM, an anchor-guided multimodal large language model for direct few-shot synthesis of Chinese vector fonts. Our key idea is to generate vector glyphs through anchors rather than a standard vector sequence. Specifically, the proposed VecFontLLM first predicts and refines an anchor scaffold that fixes the coarse layout of components and contours, and then completes Bézier control points to recover local curvature and style. At test time, a confidence-guided generation chain samples multiple component candidates and continues synthesis from the highest-confidence one, improving stability for complex glyphs. This work demonstrates, for the first time, high-quality few-shot synthesis of complex Chinese vector glyphs directly in the vector domain, without raster generation or vectorization. Experiments on several Chinese font datasets show substantial improvements over existing vector font synthesis methods, competitive glyph rendering quality against raster-domain baselines, and vector command distributions close to real fonts.

---


### 113. [Debate-on-Graph: Reliable and Adaptive Reasoning of Large Language Model on Uncertain Knowledge Graph](https://arxiv.org/abs/2607.17266)

**<font color=#1a73e8>作者：</font>** Peiji Yu, Xin Chen, Tianxing Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated remarkable capabilities in natural language processing. However, LLMs often suffer from hallucinations and lack of relevant knowledge when dealing with question answering (QA) tasks. To mitigate these issues, knowledge graphs (KGs) have been utilized to enhance LLM reasoning. Nevertheless, KGs often contain noise and errors, while existing KG-enhanced LLM approaches are generally unable to identify and filter such noisy and erroneous content, which can instead amplify hallucinations and pose challenges for reliable reasoning. Uncertain knowledge graphs (UKGs), which associate each triple with a confidence score to quantify uncertainty, offer a promising direction to address this challenge. Compared with prior work, we investigate how to leverage UKGs to support LLMs for QA. We propose Debate-on-Graph (DoG), a new framework that enables LLMs and UKGs to collaborate adaptively for reliable reasoning. Specifically, we first design a heuristic search algorithm tailored for UKGs to extract reliable and question-relevant subgraphs, thereby reducing noise and errors in retrieved knowledge. We then introduce a Multi-Agent Debate mechanism, which yields reliable answers through adaptive adversarial debates, aiming to fully exploit the knowledge in UKGs while preserving the reliability of retrieved evidence. Extensive experiments on four benchmark QA datasets show that DoG achieves state-of-the-art performance over existing LLM reasoning methods and KG-based baselines, while enabling reliable and adaptive reasoning. Our code is available at this https URL.

---


### 114. [An Explicit World Model Based on Data-First Ontology: DaoQL Multimodal Storage Validation and Counterfactual Reasoning Evaluation](https://arxiv.org/abs/2607.17269)

**<font color=#1a73e8>作者：</font>** Zhanbo Li, Shifeng Wu, Xiangjin Meng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models encode world models implicitly in neural weights, which exposes four structural risks in high-precision domains such as medicine and finance: hallucination, frozen knowledge, poor explainability, and poor modifiability. This paper proposes data-first ontology: LLMs are treated as reasoning and language engines, while deterministic knowledge is moved into an explicit multimodal database, DaoQL. We formalize an explicit world model and show that, under rule independence, deterministic evaluation, and fixed conflict resolution, explicit models provide a sufficient condition for composable counterfactual decomposability; implicit models lack atomic read/delta semantics and therefore provide no comparable architectural guarantee. The implemented system focuses on DaoQL's verified storage layer and explicit Eval path, integrating graph, column, vector, and full-text engines within one process. KVCache graph nodes, expert hot updates, and the DaoQL-Agent runtime remain future work. On an embedded same-machine setup, DaoQL reports graph BFS at 1.20 ms, HNSW at 83.1 us, and a Fluent hybrid query at 105.8 us; these results indicate engineering potential but must be interpreted with deployment-shape differences from client-server systems. Exploratory measurements on LDBC SNB SF1 and ANN-Benchmarks further show 34/34 query coverage with interactive-class queries mostly in the sub-millisecond to millisecond range, but only 1.8 QPS overall due to long-tail BI/IC queries; ANN-Benchmarks reaches Recall@10 >= 99% at thousand-level QPS after a bridge-edge protection fix. In a five-domain counterfactual experiment (n = 1250), DaoQL+GPT-4o achieves 94% composable counterfactual decomposability, 49 percentage points above GPT-4o alone. The paper explicitly separates provable structure, preliminary empirical evidence, and architectural roadmap claims.

---


### 115. [Safety That Does Not Transfer: Cross-Lingual Clinical Correctness Drift in Deployable Medical Language Models](https://arxiv.org/abs/2607.17270)

**<font color=#1a73e8>作者：</font>** Anthonio Oladimeji Gabriel, Dimeji Olawuyi, Toba Ajayi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety evaluation of large language models is conducted predominantly in English and predominantly on frontier systems. Neither condition describes how such models are encountered in low-resource health settings, where small quantised systems are run locally and queried in local languages. We ask whether clinical safety established in English transfers to Hausa, and whether any failure is attributable to the language, the clinical task, or the class of model that low-resource deployment admits. Matched English-Hausa question pairs were built for three conditions of high burden in northern Nigeria: malaria, sickle cell disease, and tuberculosis, probing knowledge recall, emergency triage, a leading question inviting a contraindicated action, and a traditional-remedy claim. Six models were evaluated: five locally deployable systems of 4-9 billion parameters, two medically fine-tuned, and one frontier system. All 128 responses were scored against Nigerian national treatment guidelines by two fluent Hausa speakers working independently and blind to one another. Among locally deployable models, mean clinical correctness fell from 1.57 in English to -0.03 in Hausa, on a scale where 2 denotes a correct answer and -1 an actively harmful one. The frontier model moved from 2.00 to 1.75 and produced no response judged harmful in either language. Drift was consistent across all three conditions. Inter-rater agreement was substantial for clinical correctness (kappa = 0.70); agreement on harm was initially poor (kappa = 0.22) and is examined in detail. Because a frontier model answers the same questions competently in Hausa, the deficit is a property neither of the language nor of the clinical material, but of the deployable tier.

---


### 116. [AIGB-R1: Self-Evolving Generative Auto-Bidding via Hierarchical Planner-Executor Optimization](https://arxiv.org/abs/2607.17281)

**<font color=#1a73e8>作者：</font>** Yuejia Dou, Hesong Wang, Xinyu Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Auto-bidding plays an essential role in online advertising, automatically adjusting bids for advertisers to optimize their commercial goals. The emerging AI-Generated Bidding (AIGB) paradigm widely adopts generative modeling to optimize bidding strategies, yet suffers from the limited mode coverage of offline datasets and inadequate task-state understanding, hindering effective exploration of optimal strategies. Large Language Models (LLMs), with prior world knowledge and reasoning capabilities, offer a promising approach to overcome these limitations. However, directly applying LLMs to auto-bidding tasks faces inherent challenges in limited numerical precision, hallucinations, and inference latency. To address these limitations, we propose AIGB-R1, a hierarchical self-evolving auto-bidding framework aiming to enhance AI-Generated Bidding via LLMs' Reasoning capabilities, comprising a high-level Planner module for macro-level strategy planning and a low-level Executor module for fine-grained decision-making. Building upon this, we design an experience-driven self-evolving loop, enabling autonomous strategy exploration and optimization from accumulated experience. We adopt a two-stage pipeline of offline pre-training and post-training alignment, and build an interactive bidding simulation environment for strategy rollout. Furthermore, we propose Decoupled Group Relative Policy Optimization (D-GRPO) to achieve end-to-end optimization via advantage decoupling. Experimental results on a large-scale public dataset demonstrate the effectiveness of AIGB-R1.

---


### 117. [WAR: Workload-Aware Rollouts for Synchronous Agentic Reinforcement Learning](https://arxiv.org/abs/2607.17299)

**<font color=#1a73e8>作者：</font>** Ryan Xu, Atlas Zhao, David Bao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon rollout generation has become the dominant systems bottleneck in agentic reinforcement learning (RL). As agents interact with environments over many turns, trajectories rapidly grow to tens of thousands of tokens, making synchronous RL training increasingly constrained by rollout. We propose WAR, a workload-aware rollout system that substantially accelerates synchronous agentic RL by jointly optimizing decoding and scheduling. WAR is built on a key observation: the optimal rollout optimization strategy depends on runtime load: (1) Under low load, WAR enables model-free speculative decoding with SuffixDecoding, which reuses suffix patterns from previously completed trajectories as speculative drafts for future rollouts. Unlike model-based drafters, SuffixDecoding introduces no additional draft model and avoids GPU contention with rollout generation. (2) Under high load, where saturated batched decoding leaves limited room for speculative speedup, WAR shifts the optimization focus to cache-aware scheduling. A global scheduler places requests across rollout replicas based on cache locality, trajectory progress and server load, reducing redundant KV-cache recomputation and mitigating load imbalance. By combining decoding-level suffix reuse with system-level rollout scheduling, WAR delivers robust throughput improvements across workload regimes without changing the underlying RL algorithm. WAR improves long-context agentic rollout throughput by 1.4x under low load and up to 1.6x under high load. These results show that WAR removes a major rollout bottleneck in synchronous agentic RL and provides a practical path toward scalable long-context agent training.

---


### 118. [Agentic ERP: Multi-Agent Large Language Model Architecture for Autonomous Enterprise Resource Planning](https://arxiv.org/abs/2607.17331)

**<font color=#1a73e8>作者：</font>** Zhihao Liu, Tianyu Wang, Xi Vincent Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise Resource Planning (ERP) systems record transactions reliably but still delegate almost all operational decision-making to human specialists, because classical rule-based automation cannot reason about exceptions and monolithic AI assistants degrade when asked to coordinate across functional boundaries. This paper presents Agentic ERP, an expert-system architecture that combines role-aligned large-language-model (LLM) agents with a risk-tiered human-in-the-loop harness and a graph-based orchestrator to execute end-to-end business workflows on a production ERP backend. First, autonomous ERP operation is formulated as a constrained sequential-decision problem over a structured enterprise state, with a decomposition argument linking role-aligned agents to a measurable reduction in per-step tool-selection complexity. Second, a graph-based Planner--Executor--Reflector--Responder orchestration decouples generation from evaluation through externalised grading criteria and sprint contracts, packaging recent harness-engineering principles as inspectable expert-system artefacts. Third, the system is evaluated at three levels: a scenario-based task suite, a comprehensive comparison of six orchestration paradigms on cross-functional crisis tasks, and a 365-day agent-in-the-loop simulation against rule-based RPA and no-intervention baselines. Across these levels the proposed multi-agent method is significantly better than the baseline, and the system sustains a simulated year of operation with zero stockouts while the rule-based baseline accumulates hundreds under the same demand stream. The work shows that role-aligned LLM agents under human oversight can move an ERP system from passively recording transactions to actively executing operational decisions, and it provides a reference architecture and an evaluation protocol for autonomous enterprise resource planning.

---


### 119. [Quantifying Diversity of Thought: A Predictive Law of Weighted LLM Ensemble Lift](https://arxiv.org/abs/2607.17384)

**<font color=#1a73e8>作者：</font>** Junade Ali  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper provides an experimentally verified formal law for calculating the uplift that diversity of thought provides in Large Language Model (LLM) ensembles. From first principles, we derive an exact decomposition of LLM ensemble lift into rescue and damage masses, which yields a compact heuristic for calculating uplift. From this we extract the metrics which predict ensemble performance: an accuracy adjusted correctness correlation, $\phi_{\mathrm{adj}}$, together with the accuracy gap and collective accuracy of the pair. We test the law on 767,520 inferences from ten open-weight models over two graduate-level science benchmarks, together with a novel agentic cybersecurity benchmark in which each model conducts digital-forensics investigations by multi-turn tool use in a network-isolated sandbox (23,520 graded trials including abstentions); all votes are released openly. Calibrated once on SuperGPQA at a 40:60 vote split, the heuristic predicts lift on the calibration set with Spearman's $\rho=0.84$ and, with its coefficients frozen, transfers to two datasets never used in calibration ($\rho=0.51$ on GPQA Diamond and $0.84$ on the forensic tasks), whilst the measured swap mass tracks realised lift with $R^2\ge 0.96$ throughout. Raw $\phi$ has almost no predictive power ($R^2\le 0.09$ throughout); the accuracy-adjusted $\phi_{\mathrm{adj}}$ is markedly superior ($R^2=0.67$ on SuperGPQA), and the heuristic combining these metrics is the most stable pre pooling predictor across the three datasets.

---


### 120. [SkyVLaM: Multimodal Large Language Model for UAV Video Understanding in Remote Sensing](https://arxiv.org/abs/2607.17386)

**<font color=#1a73e8>作者：</font>** Kaiwen Jing, Ruixu Jia, Bingyao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Multimodal Large Language Models (MLLMs) have significantly improved remote sensing (RS) multimodal understanding. Language-conditioned segmentation is crucial for fine-grained target understanding in Unmanned Aerial Vehicle (UAV) videos. However, this task remains challenging due to the prevalence of small, visually ambiguous targets and dynamic aerial perspectives. In this paper, we propose SkyVLaM, a multimodal large language model for UAV video understanding. SkyVLaM constructs sparse tokens directly from patch-level video representations through a temporal basis perceiver, regularizes the sparse basis to encourage complementary temporal cues, and adaptively selects a temporally coherent dense segment for high-resolution inspection. The resulting sparse and dense tokens are jointly processed by a large language model for query-conditioned segmentation. We further build SkyVid, consisting of SkyVid-VGCG and SkyVid-RVOS for video grounded conversation generation and referring video object segmentation, respectively. SkyVid contains 101 videos, 33.6K frames, and 1.53M pixel-level object instances. Experiments show that SkyVLaM provides a more effective allocation of the visual token budget and improves language-conditioned video segmentation in UAV scenarios.

---


### 121. [TaskArtisan: Designing Composable Generative Widgets for LLM-Assisted Analysis](https://arxiv.org/abs/2607.17394)

**<font color=#1a73e8>作者：</font>** Meng Chen, Amy Pavel  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People increasingly use chatbots such as ChatGPT for everyday analysis tasks. While chatbots unify many analysis functions (e.g., scripts, visualizations, summaries), long conversations become hard to navigate, making it difficult to revisit prior steps or reuse successful workflows. LLMs now generate high-fidelity GUI code that enables people to create customized analysis tools beyond text. Yet, what new opportunities generative UIs bring to analysis work remain unclear. We interviewed six professionals about analysis with chatbots, analyzed publicly shared LLM-generated GUI tools, and conducted a comparison study (N=12) between a chatbot and TaskArtisan, a technology probe that enables people to create and assemble generative analysis UI widgets for sequential and fan-out composition. We find that GUI improved clarity and visual presentation but also introduced rigidity and additional prompting challenges. We summarize the trade-offs into a provisional design framework (malleability, specification, interoperability) to inform future generative UI in LLM-assisted analysis workflows.

---


### 122. [CoEvoP&R: Co-Evolving Placement Objectives with Routing Feedback via Large Language Models](https://arxiv.org/abs/2607.17398)

**<font color=#1a73e8>作者：</font>** Ruogu Chen, Weihua Xiao, Ramesh Karri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Analytical placers rely on differentiable objective functions to guide placement, typically combining intermediate surrogate metrics such as half-perimeter wirelength (HPWL) and cell-density penalties. However, these placement-stage surrogates remain misaligned with downstream routed and timing quality. Prior work reduces this gap with human-designed terms or learned black-box surrogates, but the former requires expert retuning and the latter is difficult to explain, debug, or deploy in analytical placement flows. CoEvoP&R addresses these limitations with a large language model (LLM)-based framework that automatically evolves analytical placement objectives. At each generation, the prompt combines the restricted objective interface, baseline context, and archived prior candidates with routing-related feedback from placement, timing proxy, and routing tools. The LLM proposes readable differentiable objectives, which are embedded and validated in DREAMPlace, evaluated through a timing proxy and an actual router, and stored with their feedback to guide later generations. Across eight ChiP-Bench Nangate45 designs and three seeds, CoEvoP&R reduces post-route routed wirelength and congestion by 16.9% and 36.7%, with gains of 0.70 ns in worst negative slack and a 912 ns reduction in total negative slack magnitude over native DREAMPlace. Across eight ICCAD 2015 Superblue designs, it reduces post-route routed wirelength and congestion by 5.4% and 23.2%. Code is available at this https URL.

---


### 123. [The Librarian Who Refused to Code: Model-Dependent Identity Enactment in LLM Code Generation](https://arxiv.org/abs/2607.17420)

**<font color=#1a73e8>作者：</font>** Shayell Aharon Salomon, Noam Israel, Ido Safruti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biographical personas are widely used in system prompts, but their effects on code generation are rarely evaluated under controlled, pre-registered conditions. We tested four prompt conditions (no persona, two engineer personas, and a research-librarian persona), 12 code-generation tasks, two frontier models, and five runs per cell (480 completions). Persona effects differed between the two tested models. Under the pre-registered mixed-effects analysis, the condition-by-model interaction was significant for provider-reported output tokens; a post-hoc visible-character measure showed the same qualitative pattern. Six GPT-5.5 completions were length-capped and are reported separately. On Claude Opus, the minimalist engineer persona reduced visible output by 30% (33% in provider tokens) without improving correctness, while the thorough engineer persona increased output without a correctness gain. In an exploratory post-hoc analysis, the librarian persona elicited in-character disclaimers in 55 of 60 Opus responses and 12 genuine no-code responses, lowering mean correctness from 0.92 to 0.67. GPT-5.5 produced neither behavior in its 59 non-truncated responses. These results are consistent with personas acting as Model-Dependent behavioral-policy biases rather than universal quality interventions. We release raw completions, derived scores, analysis artifacts, a pre-registration document, and an execution gate log; end-to-end test-based rescoring requires an unreleased task harness.

---


### 124. [TimeLens2: Generalist Video Temporal Grounding with Multimodal LLMs](https://arxiv.org/abs/2607.17423)

**<font color=#1a73e8>作者：</font>** Yuhan Zhu, Changlian Ma, Xiangyu Zeng 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video multimodal large language models (MLLMs) can describe what happens in a video, but rarely identify when the supporting evidence occurs. We study generalist video temporal grounding, in which one model predicts a variable-cardinality set of evidence intervals across video lengths, domains, query forms, and viewpoints. Existing training strategies are misaligned with this set-valued task: long-video labels often rely on brittle one-pass annotation, while reinforcement-learning rewards either fail to distinguish non-overlapping predictions or require fragile segment matching. TimeLens2 treats temporal evidence as an interval set throughout supervision and optimization. TimeLens2-93K constructs reliable multi-span supervision through caption-derived proposals, independent localization, cross-agent consensus, semantic verification, and boundary refinement. Our temporal Wasserstein reward computes exact one-dimensional \(W_1\) between uniform distributions over merged interval supports, providing dense, matching-free feedback under unequal cardinalities and equivalent fragmentation; temporal IoU complements it with precise-overlap feedback. Across seven benchmarks, TimeLens2-2B outperforms all size-matched baselines on every benchmark, while the 4B and 8B variants achieve state-of-the-art performance, surpassing open-source models with up to 397B parameters. The 2B, 4B, and 8B variants improve over their Qwen3-VL backbones by 14.2, 13.0, and 18.1 mIoU points, respectively.

---


### 125. [Empirical Grounding Improves the Realism of LLM Agents Simulating Human Behavior During Disruptions](https://arxiv.org/abs/2607.17437)

**<font color=#1a73e8>作者：</font>** Chen Xia, Zexi Kuang, Yuqing Hu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents offer a generative approach to simulating human behavior under conditions that may have few or no direct historical analogues, a common challenge in disaster and infrastructure-disruption planning. However, this generative capacity creates a validity problem: individually plausible agent reasoning may fail to reproduce empirical population behavior. We evaluate whether empirical grounding improves the statistical realism of LLM-agent simulations during disruptions. Specifically, we develop an empirically grounded LLM-agent framework that embeds demographic profiles from the American Community Survey, baseline routines from the American Time Use Survey, and urban spatial context into agent initialization, memory, decision prompts, and activity execution. An independent household survey conducted during the July 2024 Philadelphia heatwave is reserved as an external validation benchmark. Compared with an ungrounded LLM-agent baseline, the grounded model improved reconstruction of normal daily routines, increasing mean correlation with empirical activity profiles from 0.528 to 0.912 and reducing mean squared error from 0.066 to 0.008. Under heatwave conditions, the grounded model better reproduced survey-derived activity profiles, increasing mean correlation from 0.349 to 0.836 and reducing mean squared error from 0.098 to 0.012. The grounded model captured 46.4% of observed heatwave response amplitude, compared with 20.6% for the ungrounded baseline. These findings show that empirical grounding can make LLM agents more statistically credible simulators of population behavior while revealing remaining gaps in modeling human adaptation during disruptions.

---


### 126. [How Reliable Are Multimodal Signals of Conversational State? Evidence from Remote Dyadic Collaborative Tasks](https://arxiv.org/abs/2607.17452)

**<font color=#1a73e8>作者：</font>** Tahiya Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Measuring conversational states such as cognitive load and conversational power from multimodal behavior requires characteristic features that are not only predictive but also reliable across task contexts. We present a three-dimensional evaluation framework assessing predictive accuracy, cross-task generalizability, and test-retest reliability, applied to interactional, acoustic, and linguistic features extracted from dyadic conversations during collaborative tasks performed over a video-conferencing platform (AVCAffe dataset; 53 dyads, 9 tasks). Our results show that no single feature family dominates all three dimensions. Linguistic features show the highest predictive accuracy for cognitive load but collapse under cross-task evaluation, revealing sensitivity to task-specific vocabulary. Additionally, acoustic reliability, often reported as evidence of feature stability, degrades once speaker identity is controlled, confirming that standard prosodic features measure vocal characteristics rather than conversational state. Interaction features provide the only genuinely reliable signal, unchanged after speaker normalization. Interestingly, classifying power role remained near chance baseline across all conditions, indicating limitations of task-level aggregated behavior for predicting power role in conversation. Our findings reveal three insights: (1) linguistic features predict best but generalize poorly across task contexts; (2) acoustic reliability collapses to near-zero once speaker identity is controlled, challenging standard evaluation practice; and (3) interaction features provide the only genuinely reliable signal, with floor dominance predicting within-dyad cognitive load asymmetry. These results argue for speaker normalization and multi-dimensional evaluation as prerequisites for context-aware, robust multimodal feature selection in conversational systems.

---


### 127. [Bio-SFT: Asymmetric Cortical Guidance and Retinal Adaptation for Robust HDR Reconstruction](https://arxiv.org/abs/2607.17456)

**<font color=#1a73e8>作者：</font>** Tingyu Cheng, Ting Zhang, Chongyi Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering high dynamic range (HDR) radiance from a single standard dynamic range (SDR) image is highly ill-posed. Extreme luminance variation and severe quantization in dark regions make accurate reconstruction challenging, often leading to visual artifacts and color distortions. To address this problem, we propose Bio-SFT, a bio-inspired spiking frequency transformer for single-image HDR reconstruction. Bio-SFT incorporates three biologically motivated components. First, a learnable Naka--Rushton retinal adaptation frontend stabilizes the input under complex lighting conditions. Second, an explicit Parvo--Magno split introduces asymmetric Parvo-to-Magno guidance, allowing high-frequency structural cues to modulate low-frequency reconstruction. Third, an event-driven SNN hard gating module applies all-or-none spiking to suppress dark-region noise while preserving structural details. The module is trained with a sparsity prior to encourage efficient feature utilization. Built for end-to-end training within a transformer backbone, these lightweight components provide strong parameter efficiency. Experiments on HDRTV1K show that Bio-SFT achieves competitive perceptual quality and consistently improves HDR-VDP-3 and $\Delta E_{ITP}$ while reducing artifact propagation in symmetric guidance pipelines.

---


### 128. [AEC-DS: Adaptive Erasure Coding with PDP-Triggered Reputation and QoS-Aware Migration for Decentralized Storage](https://arxiv.org/abs/2607.17460)

**<font color=#1a73e8>作者：</font>** Shuaiwen Li, Weihang Yu, Ke Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In decentralized storage systems, audit results are often not used directly to guide later redundancy and shard-placement decisions, which can lead to inefficient resource allocation and delayed recovery. We propose AEC-DS, a closed-loop adaptive erasure coding mechanism driven by Provable Data Possession (PDP) feedback. PDP audits continuously update node reputation, while a QoS-aware migration policy adjusts shard placement according to node reliability and data priority. The policy moves high-priority shards from unstable nodes to more reliable nodes in the cold tier and penalizes unstable nodes in subsequent placement decisions. Simulations with 800 nodes and 500 files show that AEC-DS maintains 100% data durability under the evaluated fault model with a redundancy factor of 1.25x. Compared with Static-EC, Dynamic-EC, and DRD-EC, AEC-DS reduces cumulative recovery operations by 66.8%-75.2%. Ablation results further show that class migration plays a major role in preventing data loss, improving the measured loss-prevention capability by 176.8%. These results indicate that PDP feedback can connect integrity auditing with redundancy and placement adaptation, providing a practical path toward self-healing decentralized storage while accounting for the additional cost of migration.

---


### 129. [Pailitao-MMSearch: Building Native E-Commerce Multimodal Search Foundation](https://arxiv.org/abs/2607.17499)

**<font color=#1a73e8>作者：</font>** Xiaohan Ye, Xu Chen, Zihan Gong 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The evolution of e-commerce has fundamentally transformed how users search for products, shifting from simple text-based keyword queries to complex multimodal interactions that seamlessly combine product images, natural language descriptions, and mixed-intent instructions. However, existing approaches face a critical dilemma: single-modal specialist models, deployed independently for text retrieval, visual search, and voice recognition, operate in isolation and cannot handle cross-modal queries, while general-purpose vision-language models lack the domain-specific knowledge necessary for fine-grained product understanding, user behavior modeling, and commercial intent reasoning. In this work, we present Pailitao-MMSearch, one native e-commerce multimodal search foundation model designed to bridge this gap. Our approach introduces three key innovations: (1)HybSID (Hybrid Semantic ID);(2)a two-stage continual pre-training strategy; and (3)a hybrid reasoning post-training pipeline. Built upon Qwen and deployed on Taobao's Pailitao multimodal search platform, Pailitao-MMSearch achieves substantial improvements in online A/B testing, including up to +13.61\% in Gross Merchandise Volume (GMV) and +8.21\% in transaction volume compared to traditional multi-modal search pipeline, demonstrating the effectiveness of our native e-commerce multimodal search large language models.

---


### 130. [Residual-Guided Multi-Resolution Refinement of Foundation Models: A Case Study in Drought Forecasting](https://arxiv.org/abs/2607.17507)

**<font color=#1a73e8>作者：</font>** Wentao Gao, Jiuyong Li, Lin Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Regional climate prediction presents unique challenges for time series foundation models, which typically process temporal patterns through single-pass inference. Expert climatologists, in contrast, employ multi-scale temporal analysis and iterative refinement based on systematic error diagnosis. We present RGMR (Residual-Guided Multi-Resolution Refinement), an inference-time framework that adapts pre-trained foundation models to perform structured coarse-to-fine refinement for climate forecasting without updating backbone parameters. Applied to drought forecasting using the Standardized Precipitation Evapotranspiration Index (SPEI), RGMR is architecture-agnostic across the three TSFM backbones evaluated per site (TimesFM, TimeGPT, TabPFN) and consistently lowers test-set MSE on three South Australian sites and three additional regions outside South Australia. Applied to TimesFM, the wrapper reduces one-month-ahead SPEI MSE by up to 18.9\% across the three South Australian sites (mean reduction $\approx$18.7\%). Overall, RGMR provides a practical route for deploying frozen TSFMs in regional climate forecasting workflows.

---


### 131. [Lightweight Wrappers for Adapting Time Series Foundation Models to Regional Drought Forecasting](https://arxiv.org/abs/2607.17511)

**<font color=#1a73e8>作者：</font>** Wentao Gao, Jiuyong Li, Lin Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large \emph{Time Series Foundation Models} (TSFMs) demonstrate strong zero-shot forecasting capabilities across diverse domains. However, their application to regional climate forecasting faces practical challenges: model weights are often proprietary, local training records are limited, and computational budgets are constrained, making traditional fine-tuning approaches infeasible. To address these constraints, we introduce a lightweight, black-box adaptation framework (requiring no access to backbone parameters and no backbone fine-tuning) that enhances frozen TSFMs at inference time through two plug-and-play wrappers: \textbf{SMR\textsuperscript{2}} (Stationarity aware multi-resolution Residual), which decomposes the input into multi-resolution temporal views, learns stride specific residual corrections that capture regional dynamics, then adaptively ensembles them into a single forecast, and \textbf{MBB} (Moving Block Bootstrap), which preserves temporal dependencies through block resampling and ensembles over temporally coherent residual perturbations to stabilize the point forecast. Both wrappers instantiate the same bagging style principle: they build diverse views of the input or its residuals, forecast each with the same frozen backbone, and aggregate, so all adaptation comes from inference time ensembling rather than any weight update. Evaluated on one month ahead Standardized Precipitation Evapotranspiration Index (SPEI) prediction across multiple sites in South Australia, our framework consistently improves forecasting performance across several backbone models, demonstrating up to 26\% mean squared error (MSE) reduction over the corresponding frozen backbone while enabling practical deployment in resource constrained regional forecasting systems.

---


### 132. [FailureAtlas: A Taxonomy of Failure Modes in Multi-Provider LLM Serving Infrastructure](https://arxiv.org/abs/2607.17525)

**<font color=#1a73e8>作者：</font>** Vishal Pandey, Gopal Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-provider LLM gateways reverse proxies that route, load-balance, and rate-limit requests across foundation-model APIs have become critical production infrastructure. Yet the failure modes specific to this architectural layer remain undocumented, scattered across issue trackers and post-mortems with no unifying framework. We introduce \fa{}, a two-axis taxonomy that classifies failures by their \emph{origin layer} (Network/Transport, Streaming/Protocol, State/Session, Model~Behavior, Governance/Cost) and their \emph{detectability} (Loud vs.\ Silent). We populate this taxonomy with five verified catalog entries sourced from public bug reports and first-hand stress testing, each accompanied by a mechanistic root-cause analysis. Three entries include standalone reproduction scripts. Our principal finding is that the most operationally severe failures are \emph{silent}: they return HTTP~200, pass every standard health check, and corrupt application state in ways that require semantic-level observability to detect. Two such silent failures a concurrency race condition causing history loss and a streaming index collision corrupting tool-call payloads were discovered first-hand during \cb{} evaluation campaigns.

---


### 133. [Can AI Agents Really Complete RTL-to-GDS? Lessons from Benchmarking Tool-Interactive EDA Workflows](https://arxiv.org/abs/2607.17528)

**<font color=#1a73e8>作者：</font>** Jinyuan Deng, Zhengrui Chen, Xufeng Wei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-driven agent systems have emerged as a promising paradigm for electronic design automation (EDA), demonstrating strong potential for automating complex design workflows. However, existing evaluations primarily examine individual language models on isolated EDA tasks, providing limited insight into how different agent systems perform across complete EDA flows. In this work, we present FluxBench, a systematic evaluation of AI agents on end-to-end EDA workflows under unified prompts, tool environments, and technology library settings. Our evaluation covers representative scenarios, including RTL generation with open-source toolchains and an RTL-to-GDS flow using closed-source commercial EDA tools for industrial applications. Through these workflows, we assess agents' capabilities in RTL code generation, iterative repair, tool-feedback utilization, logic synthesis, placement and routing (P&R), and Engineering Change Order (ECO) automation. To further characterize the efficiency of agent systems, we introduce Token ROI, a cost-efficiency metric that measures effective improvements in EDA artifacts relative to token usage and runtime cost. Experimental results show that, even when built on the same foundation model, different agent system architectures can exhibit performance gaps of up to 86.27%. Moreover, among systems with comparable task performance, Token ROI can differ by as much as $105.92\times$. In the RTL-to-GDS flow using PicoRV32 as a case study, FluxEDA achieves an end-to-end score of up to 97.94, outperforming Claude Code equipped with domain-specific EDA skills by up to $8.39\times$. These results indicate that domain-specific skills alone are insufficient to improve agent performance in large-scale EDA scenarios. Instead, both agent system design and foundation model capability play critical roles in enabling effective automated EDA workflows.

---


### 134. [Retain or Consolidate? Budget-Dependent Operator Selection for Language Agent Memory](https://arxiv.org/abs/2607.17545)

**<font color=#1a73e8>作者：</font>** Qingcan Kang, Mingyang Liu, Shixiong Kai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language agents depend on memory across interactions. However, the limited context windows of large language models (LLMs) and their inference costs constrain how much memory can be used at once. Existing systems mainly follow two strategies: memory retention and memory consolidation. Retention keeps raw records and preserves exact details, but relevant evidence may not fit under a tight budget; consolidation compresses and combines records, improving coverage per token but risking the loss of query-critical details. Neither strategy is universally preferable. This raises two central questions: when should consolidation replace retention, and which operator -- Merge, Abstract, or Rewrite -- should be selected? We formalize this decision by decomposing each operator's utility into a coverage effect on evidence omitted by retention and a signed replacement effect on raw evidence that already fits. Their balance explains why the preferred action changes with relative budget pressure. We implement this mechanism with Offline Abstraction-Safety (OAS), a lightweight learner that estimates action utilities from pre-generation features with held-out harm calibration. The public LongMemEval and LoCoMo benchmarks show the same budget-dependent pattern. On LongMemEval, consolidation improves absolute accuracy by up to 48% under tight budgets, whereas retention is preferable under loose budgets; LoCoMo replicates this crossover at a smaller budget, consistent with its shorter evidence. On both datasets, cross-note abstraction and merging generally outperform local rewriting when compression is necessary.

---


### 135. [Why Does Feedback-Augmented Self-Distillation Fail to Improve Retrieval-Interleaved Search Agents?](https://arxiv.org/abs/2607.17558)

**<font color=#1a73e8>作者：</font>** Fan Yang, Rui Meng, Yuxin Wen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) offers a promising approach for training large language models without relying on a separate teacher model. However, its effectiveness on complex agentic tasks remains largely unexplored. In this work, we instantiate Feedback-Augmented Self-Distillation (FA-SD), a self-distillation algorithm for agentic search that leverages successful demonstrations as privileged information. We identify that models can rely on recurring reasoning-and-search output templates, producing trajectories that appear diverse but are largely agnostic to the input question, making the KL-based self-distillation signal uninformative. We term this phenomenon decoding collapse, a failure mode that can be missed by existing evaluation metrics. To understand its underlying cause, we show that although the self-teacher achieves stronger performance, learning remains inherently unstable due to inconsistent supervision signals. We further decompose this inconsistency into model inconsistency and prompt inconsistency, and show that the latter can significantly degrade the quality of the supervision signal, limiting the effectiveness of self-teacher learning. To mitigate this inconsistency, we introduce an exponential moving average (EMA) teacher to stabilize the self-teacher and provide more consistent supervision signals. Although the EMA teacher requires a warm-up phase during which performance may temporarily regress, it ultimately improves model performance by providing more stable supervision.

---


### 136. [Reinforcement Learning: From Algorithms To Foundation Models](https://arxiv.org/abs/2607.17560)

**<font color=#1a73e8>作者：</font>** Zihan Ding  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) provides a framework for sequential decision making under explicit objectives. In its classical form, RL studies how an agent should act to maximise long-term reward in a dynamic environment. In richer settings, the problem extends beyond a single agent and fixed environment: intelligent behavior may require strategic interaction, adaptation to uncertainty, and reasoning over high-dimensional worlds. This thesis studies RL from two perspectives: algorithms in games and RL in the era of foundation models.
The first part focuses on multi-agent RL in games. It examines how incentives, policies, and equilibrium concepts interact in competitive and general-sum environments, spanning two-player zero-sum games, large-scale video games, and multi-player settings with general structure. These works investigate learning in multi-agent systems and the behavior of RL methods in interactive environments. The second part studies RL with generative and foundation models, motivated by the idea that prior knowledge can enrich sequential decision making. Pretrained generative models and learned world models serve as representation tools and structured priors for planning, control, and policy optimization. The thesis develops diffusion-based world models, investigates RL for efficient video generation, explores generative models as policy classes, and studies interactive video world models in which actions shape future observations. It also addresses long-horizon modeling through architectures with memory. Together, these contributions present a unified view of RL as objective-driven adaptation in complex sequential domains. From strategic games to generative world models, the thesis highlights how RL connects decision making, environment modeling, and emerging foundation-model capabilities, offering a broader perspective on the principles underlying intelligent behavior.

---


### 137. [CoCurve: Cross-Module Co-Pruning Curvature for Training-Free Structured LLM Pruning](https://arxiv.org/abs/2607.17568)

**<font color=#1a73e8>作者：</font>** Zhiren Gong, Zihao Zeng, Zijie Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structured pruning compresses large language models (LLMs) by removing whole computational units, such as attention heads and feed-forward (FFN) channel groups. Most training-free methods, however, rank these units independently, implicitly treating the loss from pruning a set as the sum of its individual losses. This view fails for Transformers, whose sublayers are coupled through a shared residual stream. Two individually weak units can thus be jointly indispensable, yet independent scoring is blind to such dependence and removes them together. We introduce CoCurve (Cross-Module Co-Pruning Curvature), a calibration-only, fine-tuning-free method that prunes attention and FFN units jointly. A second-order Taylor expansion of the token-level KL between the frozen model and its masked copy yields a single Fisher matrix whose diagonal is classical node saliency and whose off-diagonal entries are co-pruning curvature edges: the extra damage of removing two units together. Under a single-ablation additivity approximation this matrix reduces to a Gram product of single-unit ablation features, so the full M x M interaction is recovered from M forward passes, with no pairwise sweeps or gradients. Pruning then reduces to one budgeted quadratic program, solved in a single shot under a shared attention--FFN budget, with no labels, fine-tuning, or recovery.

---


### 138. [A Dual-Hypothesis Reasoning Framework for LLM Guardrails](https://arxiv.org/abs/2607.17575)

**<font color=#1a73e8>作者：</font>** Md Asiful Islam, Mihai Surdeanu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose ARBITER, a novel LLM guardrail framework that introduces two key ideas: (i) dual-hypothesis reasoning, a reasoning method for LLM guardrails that explicitly considers both safe and unsafe interpretations of a prompt before making a safety decision, and (ii) multi-component supervised fine-tuning (MC-SFT), a structured training loss for reasoning-based guardrails that decomposes LLM outputs into logical components and weights them according to their importance. Existing reasoning-based guardrails often rely on expensive procedures, such as generating reasoning traces using larger or closed-source teacher models and applying full-parameter fine-tuning. In contrast, ARBITER uses a cost-effective self-generation strategy for reasoning traces and LoRA-based parameter-efficient fine-tuning while still achieving better performance than these expensive approaches. Additionally, ARBITER provides faithful evidence-phrase explanations for unsafe decisions, enabling a more transparent and interpretable guardrail method. Experiments on three safety moderation benchmarks show that ARBITER outperforms existing reasoning-based and non-reasoning guardrail baselines, with clear gains in out-of-domain evaluations.

---


### 139. [ConsiSpace: Learning Geometric Consistency Matters for Video Spatial Reasoning](https://arxiv.org/abs/2607.17599)

**<font color=#1a73e8>作者：</font>** Ting Huang, Zhenyu Zhang, Wenyuan Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video spatial reasoning is essential for navigation-oriented perception and long-video question answering, where models must infer spatial relations across long horizons under changing viewpoints. However, existing multimodal large language models (MLLMs) remain largely semantic-centric, and often fail to reliably aggregate consistent spatial evidence from redundant video observations, leading to inefficient or unstable reasoning. To address these issues, we propose ConsiSpace, a geometry-consistency-aware framework for geometry-sensitive video spatial reasoning that turns spatial consistency into both an evidence organization principle and an explicit post-SFT learning signal. We build a geometry-consistent memory (GCM) including implicit evidence tokens and explicit geometric cues, and leverage efficient organization strategies to compactly preserve task-related spatial evidence. Furthermore, we utilize unified consistency self-supervised reinforcement learning (UC-SSRL) after supervised fine-tuning to improve cross-view stability, with answer-, metric-, and topology-consistency rewards. Extensive experiments on three spatial-reasoning benchmarks, VSI-Bench, OSI-Bench, and MMSI-Video-Bench, show consistent gains, improving the average score by 12.6 points over the strongest baselines.

---


### 140. [Verify, Repair, Repeat, or Stop? Robust Stopping for Noisy Verify-Repair Loops in LLM Agents](https://arxiv.org/abs/2607.17641)

**<font color=#1a73e8>作者：</font>** Yitao Wu, Si Shen, Rui Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Verify-repair loops are a standard means for large language model (LLM) agents to correct faulty plans in code generation, mathematical reasoning, and tool use. When both the verifier and the repairer are noisy, repair can damage already-correct plans, and reported acceptance keeps rising while true validity falls, so existing methods lack a principled basis for deciding when repair should stop. We propose VRR-Stop, a robust stopping framework for noisy verify-repair-repeat (VRR) loops. A four-parameter noise model separates verifier false acceptance and false rejection from the repair and damage behavior of the repairer. Belief filtering turns repeated verification votes into an estimate of committed validity, and the loop commits or repairs according to the sign of the true marginal gain, which requires only sign identifiability rather than accurate recovery of all parameters. When verifier discrimination approaches zero, calibration itself fails and estimation error can flip the stopping sign, so we pair VRR-Stop with VRR-Guard, an estimation-free fallback that replaces the incumbent candidate only under a sufficient verification margin. On a GSM8K stress setting, VRR-Stop improves final true validity by 60.6 percentage points over fixed five-round repair at an average cost of 0.72 repair rounds. Across settings, stopping reliability is governed jointly by verifier discrimination and the decision margin rather than by the absolute size of estimation error.

---


### 141. [Informal Learning Emerges in Everyday Human-LLM Interaction](https://arxiv.org/abs/2607.17643)

**<font color=#1a73e8>作者：</font>** Zixin Chen, Haotian Li, Ziang Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As LLMs become increasingly capable of completing tasks for users, a central concern is that everyday AI use may become primarily cognitive offloading, eroding the opportunities through which people develop their own capabilities. We analyse large-scale human--LLM conversations to ask whether informal learning behaviors also emerge in this setting: whether users engage in exchanges in ways that preserve opportunities to learn. Across 128,569 naturalistic conversations, we translated learning-science constructs into turn-level behavioural signatures. Cognitive engagement, users' cognitive effort as reflected in the exchange, appeared in 31.9% of 491,685 user turns, whereas constructive engagement, the deepest observable form of learning-oriented engagement, appeared in 4.9%, showing that deeper sense-making was recurrent but selective. Our study further identifies factors associated with these forms of engagement. Scaffolded assistant support consistently marked richer constructive participation, with associations varying by user framing, task ecology, support form, timing and prior user state. Together, these findings show that everyday human--LLM interaction is not only answer delivery or cognitive offloading; it also contains measurable, selective and conditionally organized behavioural signatures of informal learning. They shift AI evaluation from answer-delivery efficiency toward the preservation of cognitive opportunities for users to reason, test ideas and construct understanding in the course of everyday problem-solving.

---


### 142. [FlowBlock: Wavefront-Parallel Decoding for Self-Correcting Diffusion Language Models](https://arxiv.org/abs/2607.17652)

**<font color=#1a73e8>作者：</font>** Bing Tian, Haikun Liu, Xiaocheng Zhong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Block-wise diffusion large language models (dLLMs) decode sequentially at the block level, enabling effective KV-cache reuse across blocks but making inter-block decoding strictly serial. Prior work has attempted to unlock inter-block parallelism through post-training methods, but achieves only modest speedups and often degrades accuracy. We observe that self-correcting dLLMs offer a training-free alternative: token-to-token (T2T) editing can repair tokens drafted with a slightly stale upstream context, so a downstream block requires only an informative draft rather than a finalized predecessor. This turns block finality from a hard dependency into a scheduling resource. We propose \textbf{\flowblock{}}, a training-free parallel decoding framework built on two mechanisms. (i) \emph{Gated Wavefront Decoding} admits blocks into a bounded wavefront only when a readiness gate is satisfied, jointly refines active blocks via T2T editing, and commits blocks in order under a windowed block-causal mask that preserves exact frozen-prefix KV caches reuse. (ii) \emph{Heterogeneous Wavefront Packing} assigns each request an independent wavefront while packing asynchronous windows into dense, shape-stable batched forwards. Across different benchmarks, \flowblock{} improves tokens per second (TPS) over LLaDA-2.1 and LLaDA-2.0, two serial block-wise dLLMs, by up to 2.95$\times$ and 4.01$\times$, while reducing latency by up to 53.6\% and 77.1\%, respectively. It also improves average accuracy by 1.3 points. Compared with D2F, a training-based inter-block-parallel baseline, \flowblock{} achieves higher accuracy and up to 16$\times$ higher batched serving throughput.

---


### 143. [LFM: Leveraging Foundation Models for Source-Free Universal Domain Adaptation](https://arxiv.org/abs/2607.17653)

**<font color=#1a73e8>作者：</font>** Jing Li, Pan Liu, Meng Zhao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Source-free universal domain adaptation (SF-UniDA) adapts a pre-trained source model to an unlabeled target domain under both covariate and label shifts, without access to source data. However, existing SF-UniDA methods rely on inefficient techniques such as threshold tuning and clustering. Foundation models (FMs), known for their generalization and zero-shot capabilities, remain underexplored in SF-UniDA. In this paper, we propose a framework that leverages foundation models (LFM) for SF-UniDA. We use a vision-language model (VLM) to compute similarities between target samples and text labels, including those for unknown classes generated by prompting a large language model. The label shift type is determined by analyzing the coefficient of variation of a similarity-based sample-level score. Unknown samples are identified using a binary Gaussian mixture model fitted to another similarity-based metric. Under a consensus strategy, the pseudo-labels generated by the VLM are refined by the target model initialized with the pre-trained source model, integrating knowledge from both the source domain and foundation models. Finally, these refined pseudo-labels are used to train the target model. Extensive experiments across all possible label shifts and multiple benchmarks demonstrate the effectiveness and superiority of our proposed LFM framework. Our code is available at this https URL.

---


### 144. [OrientSAM: Mitigating Camera-Centric Shortcut in Multimodal Spatial Reasoning via Orientation-Aware Spatial Alignment](https://arxiv.org/abs/2607.17657)

**<font color=#1a73e8>作者：</font>** Wenxiao Fan, Hang Yin, Kan Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) still struggle with spatial reasoning that requires perspective transformation. In particular, they often rely on camera-centric cues rather than reasoning from the reference object's viewpoint, leading to systematic errors in non-camera reference settings. In this paper, we first analyze this failure mode and show that object orientation is a key factor underlying such camera-centric shortcut behavior. To address this issue, we propose OrientSAM, an orientation-aware spatial alignment framework for multimodal models. OrientSAM injects explicit orientation information into multimodal representations through orientation-aware tokens and Fourier-based angle encoding, and further adopts a curriculum learning strategy to progressively improve perspective-aware reasoning. In addition, we build a spatial data construction pipeline to generate orientation-aware spatial supervision from large-scale images. Experiments on Spatial-MM, ViewSpatial, and 3DSRBench show that OrientSAM consistently outperforms strong baselines, especially on non-camera-view, person-centric, and orientation-sensitive tasks. The results further demonstrate that explicit orientation modeling is important for mitigating camera-centric shortcut behavior and enabling more robust allocentric spatial reasoning in multimodal models.

---


### 145. [Attention from Above: A Multimodal Model for Drone-Based Object Localization](https://arxiv.org/abs/2607.17669)

**<font color=#1a73e8>作者：</font>** Hyun-Ki Jung  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Drone-based object detection technology has advanced rapidly, becoming increasingly sophisticated and efficient. Recently, research trends have expanded beyond the detection of predefined objects toward the identification of specified target objects. For example, desired targets can be specified through textual prompts, enabling accurate detection of objects of interest. To address this demand, this paper proposes an efficient multimodal-based object detection model aimed at improving small object detection performance. The proposed method is built upon the YOLO-World framework and replaces the C2f layers used in the YOLOv8 backbone with attention-based A2C2f layers. This modification enables more precise representation of local features, particularly for small objects or objects with well-defined boundaries. In addition, the incorporation of attention mechanisms and parallel processing structures significantly enhances the model's computational accuracy. Comparative experiments conducted on the VisDrone dataset demonstrate that the proposed model outperforms the original YOLO-World model. Specifically, precision increases from 43.0% to 45.1%, recall from 32.8% to 35.0%, the F1 score from 37.2% to 39.4%, mAP@0.5 from 32.5% to 35.2%, and mAP@0.5-0.95 from 18.5% to 19.9%, confirming a substantial improvement in detection accuracy. These results verify that the proposed approach provides an effective and highly accurate solution for object detection in drone-based image and video application environments.

---


### 146. [Beyond Objective Expressivity: Geometry Preservation in Multimodal Contrastive Learning](https://arxiv.org/abs/2607.17673)

**<font color=#1a73e8>作者：</font>** Tillmann Rheude, Roland Eils, Benjamin Wild  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contrastive learning is increasingly moving toward settings with three or more modalities instead of image-text pairs. Yet, extending models from pairwise to higher-order multimodal alignment can introduce optimization and representation challenges. We identify encoder Jacobian conditioning as a key factor in trimodal contrastive learning: poorly conditioned encoders exhibit collapsing or amplified singular-value spectra, leading to exploding Jacobian condition numbers and degraded multimodal alignment. We introduce geometry-preserving encoders (GPEs) by directly conditioning the Jacobian through regularization and demonstrating that simple modifications like LeakyReLU activations and residual paths recover these geometric benefits. Across a synthetic benchmark and four real-world datasets including missing modalities, improving Jacobian conditioning boosts retrieval and linear probe performance across multiple contrastive objectives, whereas expressive objectives yield little benefit in linear probes. More broadly, our results show that multimodal contrastive learning depends not only on objective expressivity, but also on the geometric and optimization properties of the underlying encoders.

---


### 147. [Uncovering Latent Reasoning Strategies in Language Models](https://arxiv.org/abs/2607.17674)

**<font color=#1a73e8>作者：</font>** Awni Altabaa, John Lafferty  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A language model $p_\theta(y \mid x)$ trained on reasoning tasks learns to solve problems via multiple distinct strategies, yet these strategies are implicit and entangled within the model's response distribution. We study the problem of decomposing the response distribution of a given pretrained language model into a structured, strategy-conditioned representation. Specifically, we learn a latent-variable factorization $p_\theta(y \mid x) \leadsto (r_\phi(z \mid x), g_\phi(y \mid x,z))$, where a router $r$ maps each input to a distribution over latent strategies $z$ and a generator $g$ produces the response conditioned on that strategy. A key challenge is that the generator, initialized from the base model, already represents $p_\theta(y \mid x)$ without using $z$. Standard variational inference therefore gives the model no incentive to route information through $z$ and can yield a severe form of posterior collapse. To address this, we propose a variational objective that measures fractional information gain relative to the base model's response loss and concentrates reconstruction pressure on tokens with high base model surprisal, encouraging $z$ to encode strategy-relevant response variation. We introduce a benchmark of multi-strategy algorithmic tasks and show that this objective recovers latent codes aligned with distinct reference strategies while preserving the base model's response distribution.

---


### 148. [Memory-Supported Synergistic Adaptation for Training-Free Test-Time Medical Image Segmentation](https://arxiv.org/abs/2607.17693)

**<font color=#1a73e8>作者：</font>** Lingrui Li, Nan Pu, Dong Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) aims to mitigate distribution shifts by adapting models with unlabeled target data at inference time. While TTA with vision-language models (VLMs) has shown promising results in classification, extending it to medical image segmentation remains challenging. In this setting, the adaptation gains from optimizing on VLM-generated predictions are often outweighed by the degradation to the VLM's strong pretrained features caused by noisy, update-driven learning, resulting in limited and unstable improvements. We therefore propose Memory-Supported Synergistic Adaptation (MSSA), a novel training-free TTA framework for medical image segmentation. Without updating model parameters, MSSA dynamically selects reliable image-text predictions to construct an online memory, uses them as text-guided semantic priors, and couples them with cross-image structural alignment for robust adaptation. Specifically, MSSA consists of (i) a noise-aware memory construction module that filters and stabilizes cross-modal predictions, and (ii) a relevance-driven prototype alignment module that aligns the target sample with structurally consistent memory samples and their reliable predictions to improve adaptation. Extensive experiments on multiple medical segmentation benchmarks demonstrate that MSSA consistently improves VLM-based segmentation models and outperforms existing fine-tuning-based TTA methods by a clear margin, with gains of up to 12.2% DSC and 11.7% mIoU. Project page: this https URL .

---


### 149. [LaT: LLM-as-Trainer for Multi-Task Vehicle Routing Solvers](https://arxiv.org/abs/2607.17708)

**<font color=#1a73e8>作者：</font>** Yang Wang, Ya-Hui Jia, Wei-Neng Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-task neural solvers aim to handle multiple Vehicle Routing Problem (VRP) variants within a unified model, avoiding separate training for each constraint combination. However, VRP variants differ in optimization difficulty, while existing methods lack stage-wise feedback on their training status, making the model biased to some specific variants. Although meta-learning can support adaptive training, it typically requires bi-level optimization and additional gradient updates, increasing computational cost. To address this limitation, we propose LLM-as-Trainer (LaT), a plug-and-play training paradigm that uses a pretrained large language model as an external trainer. LaT periodically analyzes cross-task validation metrics to generate a stage-wise guidance vector. This vector is combined with the current task's constraint vector and injected into each encoder layer, providing the neural solver with additional training information during subsequent policy optimization. Experiments on 16 VRP variants show that LaT improves the solution quality of several state-of-the-art multi-task neural solvers on both trained and unseen variants, supporting the effectiveness and generality of the proposed training paradigm.

---


### 150. [Planning with Transformers: Chain of Computation and Structured Context Windows](https://arxiv.org/abs/2607.17710)

**<font color=#1a73e8>作者：</font>** Ehsan Futuhi, Nathan R. Sturtevant  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have had a remarkable impact across many areas of machine learning. However, recent studies have shown that they struggle to reliably solve planning problems. At the same time, theoretical results have shown that transformers, the core architecture underlying modern LLMs, are Turing-complete. In this work, we investigate this apparent gap between the theoretical computational power of LLMs and their empirical planning performance. We propose Chain of Computation (COC), a computational architecture that places a transformer-based LM inside an iterative loop, leveraging its strength as a pattern-matching system. The COC uses a Structured Context Window (SCW) which provides a constant-sized context window with support for choosing which window is used at each planning step. Within this architecture, the LM is able to learn a planning policy, predicts the world model, and performs the arithmetic operations required during planning. We show that, when given an append-only SCW (resembling a Turing Machine tape), even relatively small LMs trained from scratch can learn planning policies and generalize from a small number of training instances within each planning domain, achieving success rates above 99.89\% on BlocksWorld and the Pancake puzzle. Our analysis of failure cases in Tower of Hanoi (TOH) reveals that they arise from arithmetic operations or from encountering previously unseen tokens. We show that COC can solve TOH problem instances with up to 20 disks, requiring over 1 million actions, while requiring substantially less training data by either (1) planning with symbolical support for arithmetic or by (2) using a deterministic pushdown automaton (PDA) formulation for the SCW.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-204](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
