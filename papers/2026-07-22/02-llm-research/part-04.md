# 🧠 大模型相关研究 | 2026年07月22日

> 本类共 **204** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-204](./part-05.md)

---

### 151. [Learning to Detect Cross-Modal Negation: An Analysis of Latent Representations and an Attention-Based Solution](https://arxiv.org/abs/2607.17712)

**<font color=#1a73e8>作者：</font>** Ali AbuSaleh, Leon Hammerla, Alexander Mehler  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Detecting high-level semantic concepts like negation across modalities remains a challenge for current multimodal systems. We analyze this as a fundamental representation learning problem, providing the first evidence that negation does not form a linearly or non-linearly separable class in the latent spaces of standard vision-language models (VLMs). We demonstrate that pretrained embeddings primarily encode modality-specific features, lacking a generalizable negation signal. To overcome this, we propose a novel cross-modal attention architecture that explicitly models inter-modal dependencies, achieving performance gains of up to +7.03% F1 over unimodal baselines. Our analysis reveals a key asymmetry: while textual negation often appears independently, visual negation is semantically dependent on linguistic context, a finding validated through our statistical analysis of 3,222 political video-text pairs automatically annotated via \textsc{Qwen2.5-VL}. By combining this analysis with self-supervised video representations (JEPA2), we advance the modeling of temporal negation. This work provides new methods and insights for learning robust, semantically-aligned representations in multimodal systems.

---


### 152. [C$^2$KV: Compressed and Composable KV Cache Reuse for Efficient LLM Inference](https://arxiv.org/abs/2607.17715)

**<font color=#1a73e8>作者：</font>** Chuheng Du, Junyi Chen, Hanlin Tang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context inference is central to modern large language model (LLM) applications such as retrieval-augmented generation and multi-document reasoning. To mitigate the growing inference cost, recent work has explored key-value (KV) cache reuse to reduce redundant prefill computation. However, existing reuse methods primarily focus on computation savings and overlook a critical bottleneck in long-context LLM serving: the cost of storing and accessing large KV caches. While KV compression appears to be a natural complement, naively combining compression with non-prefix KV reuse often leads to severe accuracy degradation. In this work, we propose C$^2$KV, a unified framework for non-prefix KV reuse that jointly optimizes KV extraction and inference-time concatenation. C$^2$KV learns a composable and compressed KV cache manifold that is explicitly designed to be position-agnostic. Our approach introduces a lightweight sidecar Extractor with learnable compression tokens and a structured attention flow, enabling modular KV representations that can be flexibly reused and concatenated without modifying the frozen base model. We further employ a compression-concatenation co-training strategy to align extraction-time representations with their downstream reuse behavior. Extensive experiments across multiple long-context benchmarks and model families demonstrate that C$^2$KV significantly reduces KV cache storage and transfer costs, achieving up to 17$\times$ inference speedup under long contexts, while preserving generation quality.

---


### 153. [SR-Agent: An Experience-Driven Agentic Framework for Post-Ranking Strategies Refinement in E-Commerce Recommendation](https://arxiv.org/abs/2607.17719)

**<font color=#1a73e8>作者：</font>** Hanchen Yang, Kaiwen Yang, Junpeng Zhuang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> User experience is a first-class objective in industrial e-commerce recommender systems (RS). Post-ranking strategies, which govern diversity, similarity, and exposure over a ranked list, are widely deployed in industrial RS for their simplicity and low serving cost. However, as the online recommendation environment evolves continuously, these statically configured strategies gradually become stale, degrading the user experience. Refining them typically relies on manual inspection, diagnosis, and updates, a process that is slow, costly, and hard to reuse. Although recent LLM-based agents (e.g., RecUserSim, SimUSER, and Self-EvolveRec) offer promising directions, none of them close the full loop of automated, self-evolving strategy refinement. To bridge this gap, we introduce SR-Agent, a Strategy Refinement agentic framework that, to the best of our knowledge, is the first deployed for refining post-ranking strategies in industrial RS. SR-Agent unifies three components: (i) a UserSim agent that applies staged inspection skills to surface user-perceived bad cases; (ii) an Analysis agent that consolidates recurring bad cases into structured, reusable diagnoses; and (iii) a constrained Strategy Refinement Harness that maps diagnoses to typed and bounded actions, gated by a four-stage reward pipeline with reversible rollback. Deployed on the Kuaishou e-commerce platform, SR-Agent continuously runs this refinement loop and, in a one-month online A/B test, increases order volume by 0.71%, browsing depth by 0.34%, and clicked-category diversity by 0.48%, while markedly shortening the refinement cycle and lowering operational cost.

---


### 154. [MXSens: Sensitivity-Aware Mixed-Precision Quantization for Efficient LLM Inference](https://arxiv.org/abs/2607.17733)

**<font color=#1a73e8>作者：</font>** Simla Burcu Harma, Danila Mishin, Zhengyuan Su 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> 4-bit quantization enables efficient LLM inference, but suffers from significant accuracy degradation due to outliers. Prior work addresses this problem via data rotation or mixed-precision integer quantization, but often relies on software-managed scaling and frequent dequantization, incurring substantial overhead. Microscaling formats, such as MXINT, eliminate these inefficiencies by encoding scales in hardware, yet remain incompatible with rotation-based methods. Our analysis reveals that outliers vary in severity, from rare extremes to frequent mild deviations, and that quantization sensitivity is unevenly distributed across layers and columns. These insights motivate a fine-grained, sensitivity-guided approach. We introduce MXSens, a training-free method that assigns mixed mantissa bitwidths (4/6/8) based on column- and layer-wise sensitivity, naturally leveraging the block-wise structure of MXINT. MXSens outperforms state-of-the-art quantization methods across a range of models and tasks. Under the W4A4KV4 setting, MXSens achieves perplexities of 3.77 and 7.63 on LLaMA-2-70B and LLaMA-3-8B, respectively, substantially improving over existing baselines on WikiText-2. Our work establishes a new balance between accuracy and resource efficiency for LLM quantization.

---


### 155. [Large Language Models for Citation Function Classification](https://arxiv.org/abs/2607.17738)

**<font color=#1a73e8>作者：</font>** Daniel Vodička, Jakub Šmíd, Pavel Král 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Citation function classification plays a crucial role in understanding the relationships between scientific publications and advancing bibliometric analysis. This study presents one of the first comprehensive evaluations of multiple state-of-the-art (SOTA) large language models (LLMs) for citation function classification, achieving new SOTA results on the ACL-ARC dataset. We systematically compare five models (Mistral 7B, Orca 2-7B, LLaMA 3.1-8B, Falcon 7B, and SciBERT) across zero-shot, few-shot, and fine-tuning approaches. Our fine-tuned Falcon 7B model achieves a 73.3% macro F1 score on ACL-ARC, representing a significant improvement over previous methods. Additionally, we introduce AC3, a novel dataset featuring a seven-category annotation scheme that distinguishes between neutral acknowledgments and explicit evaluative stances (more opinion-oriented citations - criticizing, complimenting, contradicting). The dataset is implemented across four context extraction variants to systematically evaluate the impact of contextual scope on classification performance. We also provide detailed analysis of model performance, experimental configurations, and limitations to guide future research in this domain. To our knowledge, this is one of the first studies dedicated to comprehensive model comparison for citation function classification, addressing a gap identified in recent surveys.

---


### 156. [Semantically Similar, Logically Distinct: Diagnosing the Semantic-Answerability Gap in Table RAG](https://arxiv.org/abs/2607.17742)

**<font color=#1a73e8>作者：</font>** Jiaming Tian, Liyao Li, Wentao Ye 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tables are a critical knowledge source in retrieval-augmented generation (RAG), but a retrieved table may lack sufficient evidence to answer a query, a property we call answerability. While answerability broadly concerns whether a source or collection of sources contains sufficient evidence, retrieval models optimized for semantic relevance do not guarantee it even in the single-source case, creating a fundamental mismatch. To study this, we introduce TCR-Bench, a diagnostic benchmark for Table Content-level Answerability in RAG, built around sibling tables, i.e., tables with highly similar schemas but subtle content differences. On TCR-Bench, the dense retrievers we evaluate persistently exhibit a Semantic-Answerability Gap: they often retrieve the correct sibling group yet struggle to pinpoint the uniquely answerable table within it, dropping QA performance from 0.755 (oracle) to 0.330 (top-5 retrieved). Our analysis suggests this gap is associated with semantic accumulation, schema-level cue dependence, and weak row-column binding. As a diagnostic probe into the source of this gap, we test whether a lightweight two-stage pipeline, Answerability-Aware Reranking (AAR), applying direct query-table answerability judgment, can recover performance: it raises top-1 target retrieval from 18.2% to 57.4%, and this large gain is itself evidence that much of the observed failure reflects a missing answerability verification step, rather than an inherent limitation of model capacity alone.

---


### 157. [WuYu-EnvLE-Bench: A Benchmark for Evaluating Large Language Models in Environmental Law Enforcement](https://arxiv.org/abs/2607.17745)

**<font color=#1a73e8>作者：</font>** Ziliang Yang, Yi Zhang, Kaijun Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly considered for environmental enforcement, but their ability to produce traceable enforcement decisions remains unclear. We introduce WuYu-EnvLE-Bench, a benchmark built from real enforcement cases, regulatory standards, and expert review. It contains 2,521 benchmark instances, 14 tasks, and 12 pollution-medium subdomains across pre-enforcement, in-enforcement, and post-enforcement workflows. Using Absolute Environmental Enforcement Score (AES) and Intelligent Enforcement Index (IEI), we evaluate open-source and closed-source LLMs across capability, response quality, and resource efficiency. Results show that LLMs perform well on rule-bounded tasks but remain unreliable in evidence-chain construction, contradiction detection, multi-source integration, and procedural judgment. Model scaling also shows diminishing returns: medium-sized models approach leading models in structured tasks, while larger models do not reliably overcome evidence-reasoning bottlenecks. WuYu-EnvLE-Bench highlights the need for evidence-grounded, rule-aware, and task-adaptive enforcement reasoning.

---


### 158. [Towards Reliable Zero-Shot Crowd Forecasting: Evaluating Time Series Foundation Models for Special Event Pedestrian Forecasting](https://arxiv.org/abs/2607.17758)

**<font color=#1a73e8>作者：</font>** Ziteng Li, Yanan Xin, Tina Comes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Managing massive crowds during infrequent special events requires reliable real-time pedestrian-flow forecasting to ensure public safety and operational efficiency. However, supervised forecasting methods face limitations in these contexts due to scarce historical data, heterogeneous data distributions, and short in-event observation windows. To effectively support operational decision-making, forecasts should provide not only accurate point estimates but also informative predictive uncertainty. Probabilistic uncertainty quantification plays a critical role in this aspect, particularly capturing sudden volatility and tail risks. This paper investigates pretrained time series foundation models as a lightweight approach for zero-shot probabilistic forecasting without extensive local retraining. Using decision-oriented metrics tailored to short events, we conduct a comprehensive assessment of two time series foundation models on crowd forecasting, with the SAIL2025 event as a use case. We then distill practical insights for crowd managers, specifying when zero-shot forecasts remain operationally reliable.

---


### 159. [FIFA World Cup 2026 as a Contamination-Free Benchmark for LLM Forecasting Agents: Four Models, a Bookmaker, and 104 Matches](https://arxiv.org/abs/2607.17765)

**<font color=#1a73e8>作者：</font>** Jiacheng Ding, Cong Guo, Jason Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce WC2026-Agents, a benchmark and dataset for evaluating large language models (LLMs) as autonomous forecasting agents on real, future events. For every one of the 104 matches of the 2026 FIFA World Cup, four frontier models -- Claude Opus 4.8, ChatGPT (GPT-5.5, high reasoning), Gemini 3.1 Pro, and Grok (Expert Mode) -- ran an identical search-act-reflect loop: gather evidence with a web tool, commit to a 1X2 (team-A win / draw / team-B win) distribution and a virtual 100-USD bet, and, after the match, reflect given only the final score. Because every match kicked off after the models' training cutoffs, the benchmark is contamination-free by construction. Crucially, we pair the four agents with a fifth competitor drawn from the same information environment -- the pre-match betting market -- collected as per-match 1X2 odds, giving an economically grounded baseline and letting us score not just what an agent predicts but what it does with money. The release contains 416 forecasts and 414 reflections with verbatim reasoning, ground truth (including penalty shootouts), odds, and a reproducible evaluation suite. A reference evaluation surfaces findings that raw accuracy hides: the four agents issue an identical top pick in 92% of matches and none beats the market's Brier score; indeed, a naive flat stake on the market favorite out-earns all four agents. Yet the agents diverge sharply as decision-makers: betting return-on-investment ranges from -18% to +10%, fading the market is unprofitable for all four, the share of forecasts that cite the market ranges from 12% to 100%, and self-reported error rates on wrong picks range from 36% to 86%. The benchmark thus measures calibration, decision quality, and self-knowledge -- axes on which frontier models differ even when their predictions do not. Data and code: this https URL

---


### 160. [BrainNext: A General-Purpose Self-Supervised Foundation Model for Brain MRI Analysis](https://arxiv.org/abs/2607.17782)

**<font color=#1a73e8>作者：</font>** Moona Mazher, Abdul Qayyum, Steven A. Niederer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models pretrained using self-supervised learning have transformed computer vision by learning transferable representations from large-scale unlabeled data. However, existing foundation models for neuroimaging remain limited by task-specific training, slice-based learning strategies, or relatively small pretraining datasets, restricting their generalizability across diverse brain MRI applications. In this work, we present BrainNext, a general-purpose self-supervised foundation model for volumetric brain MRI analysis. BrainNext combines masked autoencoder (MAE) pretraining with a native three-dimensional Bi-Directional xLSTM-UNet architecture to learn rich anatomical representations from 60,551 unlabeled brain MRI examinations spanning multiple MRI modalities. The pretrained model is subsequently adapted to downstream tasks through lightweight task-specific fine-tuning. We evaluate BrainNext on the Foundation Models for Medical Imaging (FOMO) 2025 Method Track, encompassing classification, segmentation, and brain-age estimation, where it achieved second place overall and ranked first in the meningioma segmentation task on the official FOMO 2025 challenge leaderboard, demonstrating strong transferability across heterogeneous neuroimaging tasks. These results highlight the potential of large-scale self-supervised pretraining to learn robust and transferable volumetric representations, establishing BrainNext as a scalable foundation model for diverse brain MRI applications.

---


### 161. [PGN: Design and Implementation of a Vision-Language Navigation System Based on Pangu Multimodal Foundation Model](https://arxiv.org/abs/2607.17806)

**<font color=#1a73e8>作者：</font>** Li Xian, Mingxi Li, Yizheng Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language Navigation (VLN) requires an embodied agent to interpret a natural-language instruction and predict actions from temporally ordered visual observations. Adapting a multimodal large language model to VLN requires visual-language alignment, compact temporal inputs, action-space grounding, and stable training on the target hardware. This technical report presents PGN (Pangu Navigator), an offline VLN action-prediction system built on OpenPangu-7B. Training proceeds in two stages. First, PGMM aligns a frozen EVA-ViT-G/14 vision encoder with the frozen language backbone by training a Q-Former and a two-layer MLP projector. Second, PGN adapts the aligned model to expert navigation trajectories using five-observation windows, epoch-dependent temporal sampling, and a reasoning-then-action output format; this stage freezes the aligned visual pathway and updates three structural-token embeddings and LoRA adapters. The implementation combines mixed-precision computation, selective FP32 computation, and DeepSpeed ZeRO-2 on eight Ascend 910B NPUs. Under teacher-forced, open-loop evaluation on 500 held-out expert trajectories, V9 reports a 62.29% Normalized Action Match (NAM) and a 100.00% Non-empty Rate (NER). These metrics quantify offline expert-action alignment rather than closed-loop navigation success; evaluating error accumulation, path efficiency, and goal completion remains future work.

---


### 162. [When a Name Is Not a Name: A Benchmark Dataset and Distilled Reasoning for Culturally Entangled Bangla Homographs in Low-Resource LLMs](https://arxiv.org/abs/2607.17828)

**<font color=#1a73e8>作者：</font>** Md. Asaduzzaman Shuvo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many Bangla words are at once personal names and culturally loaded common nouns, "Maya" is both a girl's name and a word for affectionate compassion. Choosing the right reading demands cultural knowledge that is scarce in the pretraining data of modern language models. We introduce Culturally Entangled Homograph (CEH) disambiguation and build a Bangla benchmark of 1,516 expert-verified sentences (3,032 labelled occurrences) in which one word appears twice with two distinct readings, each labelled with a culturally grounded category and an explanation of the reasoning behind it. Across open- and closed-source models, we find a systematic dominant-meaning bias: models default to the common-noun sense and overlook the name. A Bangla-specific model fails under every prompting regime we test, showing that language-specific pretraining alone does not confer cultural grounding. We further show that contrastive chain-of-thought prompting can sharply reduce this bias without training, and that distilling cultural explanations teaches small (1-3B) models to reason toward the correct reading rather than memorise labels, cutting dominant-meaning bias from as high as 100% to under 5% and turning the failed Bangla-specific model into our strongest system. Dataset and code are available at this https URL.

---


### 163. [Leveraging Dissimilarity Invariance as a Robust Anchor for Learning with Noisy Labels](https://arxiv.org/abs/2607.17857)

**<font color=#1a73e8>作者：</font>** Wenxiao Fan, Kan Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models excel in visual recognition but suffer severe performance drops when training labels are corrupted by noise. Under label noise prior work cannot learn accurate similarities and thus misguide the learning process. In this paper, we uncover a complementary and novel phenomenon, Dissimilarity Invariance, whereby semantic dissimilarity between unrelated samples remains stable despite label noise. Leveraging this insight, we propose NegScale, a plug-and-play framework that shifts focus from fragile similarity to robust dissimilarity. NegScale integrates: (1) Structured Negative Orthogonality Penalty (SNOP), enforcing subspace orthogonality for unrelated samples; and (2) Dissimilarity-Calibrated Similarity Adjustment (DCSA), suppressing spurious similarity using dissimilarity anchors. We also give theoretical analysis that proves Dissimilarity Invariance and the effectiveness of NegScale. Empirical results demonstrate that NegScale consistently outperforms state-of-the-art baselines, establishing new benchmarks on CIFAR with synthetic noise and real-world datasets.

---


### 164. [ST-Veto: Spatio-Temporal Token Veto for Diffusion MLLMs via Taylor Prediction and Visual Grounding](https://arxiv.org/abs/2607.17884)

**<font color=#1a73e8>作者：</font>** Keuntae Kim, Beomseok Lee, Hyunwoo Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision Language Models (VLMs) achieve strong reasoning with Chain-of-Thought (CoT) prompting but incur high sequential-generation cost, error accumulation, and limited self-correction. Diffusion Multimodal Large Language Models (dMLLMs) unmask tokens in an order-agnostic process, improving efficiency and enabling iterative refinement, yet their reasoning and how to enhance it remain underexplored. We propose a training-free method, Spatio-Temporal Token Veto (ST-Veto), which leverages the ability to observe all token positions at each diffusion step. Rather than relying only on current-step confidence, ST-Veto vetoes temporally unstable tokens via second-order Taylor prediction of confidence dynamics and filters weakly grounded tokens using image-attention mass, swapping them with safer candidates. Across multiple dMLLMs and multimodal reasoning benchmarks, ST-Veto consistently outperforms standard decoding policies and prior VLM reasoning methods, improving accuracy by up to 9% with no additional training or generation cost. Analyses show that ST-Veto steers generation toward higher-confidence, better-grounded paths.

---


### 165. [Stress Testing Concept Erasure with Large Language Model Agents](https://arxiv.org/abs/2607.17890)

**<font color=#1a73e8>作者：</font>** Yuyang Xue, Feng Chen, Zhihua Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Concept erasure aims to remove semantic concepts from a trained generative model and is increasingly important for responsible AI deployment. However, verifying whether a model has robustly removed targeted concepts remains a critical challenge. Existing evaluation methods are typically pre-defined and static, failing to expose vulnerabilities under diverse natural-language probes and challenging conditions. Moreover, manually designed evaluation strategies can be biased and difficult to scale. We posit that concept erasure evaluation is best formulated as an adaptive hypothesis search, operationalised by agents that iteratively propose, critique, and verify tests to systematically expand coverage of failure modes. To this end, we propose Stress Testing Agents for Concept Erasure (STACE), a framework that autonomously stress-tests concept-erased models using multiple Large Language Model (LLM) agents, by iteratively generating and verifying stress-testing hypotheses grounded by external knowledge. We also introduce a suite of metrics for assessing the performance and efficiency of LLM-agent-powered stress-testing frameworks. Our extensive experiments show that STACE outperforms five LLM-based evaluation baselines on four concept categories. Further analysis across two T2I models, six concept erasure approaches, and various erasure strengths show that STACE is robust for different settings. We also show that STACE can be adapted beyond concept erasure evaluation to other problem domains, such as LLM jailbreaking. Our code is available anonymously.

---


### 166. [Distributional Soft Bellman Operator under the Cramér Geometry](https://arxiv.org/abs/2607.17897)

**<font color=#1a73e8>作者：</font>** Keru Wang, Yixin Deng, Yao Lyu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distributional soft policy iteration (DSPI) provides an important framework for combining distributional reinforcement learning (DRL) with maximum-entropy control, in which the policy evaluation step is governed by a distributional soft Bellman operator acting on entropy-regularised returns. Theoretical analysis of such an evaluation step requires a probability metric under which Bellman updates can be controlled, typically by showing that the operator contracts the distance between any two candidate return-distribution estimates. In this paper, we focus on the Cramér geometry, a cumulative distribution function (CDF)-based metric with an $L^2$ structure, and study whether the fixed-policy distributional soft Bellman operator has this contraction property and hence a unique fixed point under this metric. Working directly on an admissible CDF field domain, we formulate the CDF-level distributional soft Bellman operator, prove that it is a $\sqrt{\gamma}$-contraction, and obtain the corresponding unique fixed point together with convergent iterative policy evaluation. The CDF formulation also shows that this finite-Cramér-domain property follows from a uniform first-moment condition on the combined one-step reward entropy shift, rather than from separate uniform boundedness assumptions on the reward and entropy terms. We then transport the same evaluation problem to the spectral domain by conjugation, obtaining an equivalent Hilbert-space representation of the same decision process. Taken together, these results identify the Cramér-geometric Bellman fixed point associated with the policy-evaluation step of DSPI, providing a reference point for studying approximate critics, evaluation error, and critic-loss design in DSPI-style algorithms.

---


### 167. [DeLIVeR: Decomposed Learning for Information-grounded Veracity Recognition via Reinforced Knowledge Graph Exploration](https://arxiv.org/abs/2607.17935)

**<font color=#1a73e8>作者：</font>** Cong Hoan Nguyen, Thomas Hoang, Hieu Minh Duong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated fact-checking remains a challenge for Large Language Models (LLMs) due to "query brittleness" in traditional retrieval systems. We propose DeLIVeR (Decomposed Learning for Information-grounded Veracity Recognition), a framework that treats evidence retrieval as a reinforced strategic exploration task. DeLIVeR utilizes a Planner LLM to decompose complex claims into targeted question sets, which are used to traverse structured Knowledge Graphs (KGs) for high-precision evidence. We optimize the Planner's policy using Group Relative Policy Optimization (GRPO) with a reward system prioritizing structural diversity and verdict accuracy. Our evaluation on LIAR, FEVER, and PolitiFact shows that DeLIVeR significantly outperforms state-of-the-art baselines. Using Qwen2.5-7B, our framework achieved peak F1-scores of 83.73, 84.57, and 79.70 respectively, representing a 10-15% improvement over HippoRAG2. By shifting to a reinforced question-planning strategy, DeLIVeR effectively bridges multi-hop reasoning gaps and provides an auditable, transparent path for verifiable misinformation detection.

---


### 168. [A Geometric Perspective on Stabilizing Value Conflict Resolution](https://arxiv.org/abs/2607.17946)

**<font color=#1a73e8>作者：</font>** Saket Reddy, Andy Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) often struggle to navigate value conflicts when trained with the compressed scalar rewards of Reinforcement Learning from Human Feedback (RLHF). To address this challenge, we investigate how chain-of-thought (CoT) reasoning can help improve performance in this domain. Geometrically, we show that CoT correlates with further smoothing the model's loss landscape in its sharpest direction, helping resolve the optimization instability of traditional scalar rewards. We also demonstrate via relevant downstream benchmarks that value conflict-focused CoT may generalize to different kinds of moral reasoning, demonstrating that this CoT has the potential to be an effective mechanism for better moral reasoning. To capitalize on this potential, we create a new value conflict-focused CoT design that further smooths the sharpest direction of the loss landscape and increases moral reasoning performance. This finding shows that explicitly modifying and improving the design of reasoning dynamics offers a promising avenue for improving model performance on user requests with complex value conflicts, advancing pluralistic alignment in LLMs.

---


### 169. [Towards Agentic Agent-based Models: Feasibility, Performance, and Statistical Model Checking](https://arxiv.org/abs/2607.17948)

**<font color=#1a73e8>作者：</font>** Stefano Blando, Emanuele Guerrazzi, Riccardo Porcedda 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent-based models (ABMs) rely on simple, explicit and reproducible rules for individual decision making, while complex collective behavior emerges from interactions among agents. Recent advances in large language models (LLMs) make it tempting to replace, enrich, or perturb these rules with LLM-based agentic capabilities. However, this raises a methodological question: how does introducing LLM-driven decisions affect the reliability, computational cost, and behavior of ABM simulations? We investigate this for Mesa ABM models, a popular Python library for ABMs, analyzed by statistical model checking. Building on Mesa's integration with the statistical model checker MultiVeStA, we extend the classical Schelling segregation model with a hybrid population: ordinary agents classify neighbors using the standard symbolic rule, while one agent delegates this task to an LLM through tool calls. The LLM-enabled agent receives natural-language descriptions of neighboring agents and invokes tools that increment counters of similar/different neighbors; these counters determine its happiness according to the original Schelling dynamics. This provides a minimal but controlled setting where the semantic, operational, and computational behavior of LLM-based decisions can be studied inside an otherwise standard ABM. We report preliminary experiments with locally served LLMs of different sizes, showing that smaller models may fail simple semantic classification experiments or become operationally unusable during repeated tool-call generation, while larger tested models pass these preliminary checks. We discuss how statistical model checking can estimate classical ABM observables and quantify the impact of introducing agentic LLM components into simulation models.

---


### 170. [What Transfers Under Source Shift? Definitions, Examples, and Fine-Tuning for Climate Disclosure Classification](https://arxiv.org/abs/2607.17952)

**<font color=#1a73e8>作者：</font>** Guosheng Li, Fenghui Ren, Bin Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Climate disclosure classification is a fundamental task for analysing corporate climate disclosures, yet such disclosures appear in many different sources -- annual reports, press releases, and earnings calls -- that differ in length, purpose, and writing style. Existing evaluations are mostly conducted within a single source, leaving open whether common LLM adaptation strategies remain effective under source shift. We reframe climate disclosure classification as a cross-source adaptation problem and study three widely used adaptation strategies -- definitions, examples, and fine-tuning -- across eleven open- and closed-source LLMs, using two corpora that share the same label space but come from different sources. We find that all strategies bring positive cross-source gains on average, but the strongest in-source strategies are not the strongest cross-source ones: similarity-based retrieval and LoRA fine-tuning gain most in-source but lose most of that advantage under source shift; randomly selected few-shot examples, a weaker in-source baseline, retain their advantage more reliably; definitions transfer most consistently, though only when their granularity matches the target text. Across these strategies, when the source changes, simpler is often safer.

---


### 171. [OntoExtend: A Framework for Requirement-driven and Scalable Ontology Extension with LLMs](https://arxiv.org/abs/2607.17963)

**<font color=#1a73e8>作者：</font>** Anna Sofia Lippolis, Mohammad Javad Saeedizade, Stefan Schmid 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ontology extension refers to the process of enriching an existing ontology in response to emerging requirements, making it more complete. This task is a resource-intensive and error-prone process. Large Language Models (LLMs) have shown promising performance on generating ontologies from scratch, but current approaches rarely tie ontology extension explicitly to requirements or reusable core models, and offer limited, systematic evaluation of LLM outputs. This paper introduces OntoExtend, a requirements-driven framework for ontology extension with LLMs. It uses retrieval-augmented generation (RAG) over relevant input ontologies and requirements in the form of competency questions to propose grounded extensions. We evaluate OntoExtend on 39 CQs from two use cases: a public EU-project ontology, Onto-DESIDE, and an industrial ontology from Bosch. The generated fragments show few structural issues, satisfy all functional evaluation tests, and are rated by ontology engineers as requiring minor to moderate revision before integration. These results suggest that OntoExtend is useful as a drafting assistant for requirement-driven ontology extension in real world scenarios, while remaining sensitive to CQ specificity and modelling profile.

---


### 172. [SAGE: Subgoal-Conditioned Action Generation for Latent World Model Planning](https://arxiv.org/abs/2607.17973)

**<font color=#1a73e8>作者：</font>** Letian Cheng, Qi Zhang, Yisen Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Latent world models have emerged as a powerful planning paradigm by learning action-conditioned predictive dynamics and using them as internal simulators to imagine and evaluate candidate action sequences. However, as the planning horizon grows, performance becomes increasingly constrained by proposal quality: a fixed candidate budget must search an exponentially larger action space, making it difficult to expose the world model to high-quality candidate futures for evaluation. In this paper, we introduce a prior-conditioned planner that replaces random proposal initialization with structured guidance. At each planning stage, a goal-conditioned generator predicts the next reachable latent subgoal for a specified duration, which is then used to condition the generation of candidate action sequences. To capture semantic information across temporal scales, we use subgoals of varying durations as priors, balancing fine-grained local control with higher-level long-horizon progress. Then the frozen world model evaluates and refines these subgoal-conditioned proposals before execution. Experiments on PushT and OGBench Cube show that coupling latent subgoal decomposition with prior-conditioned action generation substantially improves long-horizon planning while preserving strong short-horizon performance. To be specific, when the target offset is $150$, it raises PushT success from $12.7\%$ to $64.7\%$ and OGBench Cube success from $26.7\%$ to $67.3\%$.

---


### 173. [Harness Engineering for LLM-Driven GPU Kernel Generation](https://arxiv.org/abs/2607.17979)

**<font color=#1a73e8>作者：</font>** Yue Shui, Chenyu Ma, Hangfei Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can assist GPU kernel generation, but their practical effectiveness depends on whether generated code can be reliably constrained, validated, profiled, and selected. This paper presents a harness-centered system for LLM-driven GPU kernel optimization in the MLSys 2026 FlashInfer AI Kernel Generation Contest on NVIDIA Blackwell B200 GPUs. The system separates an evaluation harness from a profile-backed optimization controller: the harness enforces compilation, correctness, official-aligned timing, and artifact archival, while the controller turns profiler and workload evidence into bounded candidate-generation decisions. Human-authored skills capture operator constraints, references, profiling procedures, and promotion rules, while Codex and Claude Code agents generate candidate kernels inside those constraints. Across five operator definitions, the retained official-aligned artifacts achieved mean-latency speedups over supplied FlashInfer baselines of 1.62x, 18.05x, 29.68x, 1.12x, and 13.70x. The Agent-Assisted kernels outperform the Full-Agent artifacts across the evaluated definitions, indicating that expert-provided optimization directions, high-quality references, and workload context remain critical for reliable AI-driven kernel optimization.

---


### 174. [HAS: Highlight-guided Attention Steering for Multimodal LLM Video Summarization](https://arxiv.org/abs/2607.17994)

**<font color=#1a73e8>作者：</font>** Rui Chu, Yingjie Lao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video understanding has become more and more important with the growth of Artificial Intelligence (AI) for video generation. Recently, Multimodal Large Language Model(M-LLM) has shown its capability in video understanding. Video summarization, a specific domain of video understanding, has proven its importance for efficient navigation and retrieval. Both video understanding and video summarization require a good selection of key frames in a video. Current video summarization methods heavily focus on the selected key frames and correlated segment captions. However, existing approaches overlook the perspective of treating the importance of the frames globally. We argue that using discrete selected frames for summarization will not only reduce the understanding coherence, but also lost important information in the video, as well as wasting the original capacity of the MLLMs. In this paper, we propose HAS, a Highlight-guided Attention Steering method for video summarization. We consider a challenging but practical setting where the video given to MLLMs for summarize should be continuous but with highlight guidance. HAS mainly consists of two parts: The first part is to find a continuous frame-level highlight distribution for the video globally. The second part is to apply the highlight distribution as an attention steering vector for the MLLM, targeting a better understanding of the video, and thus during the model inference time, putting more attention on the highlighted frames, while avoiding lost entire information on less highlighted frames through putting less attention instead of forgetting them. We evaluated HAS on a variety of benchmarks, and it has shown convincing performance in video summarization.

---


### 175. [Do Maps Still Matter for Machines: Revisiting the Role of Choropleth Maps in Foundation Model Spatial Understanding](https://arxiv.org/abs/2607.17999)

**<font color=#1a73e8>作者：</font>** Zhiwei Wei, Yonghe Sun, Zhenjia Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spatial understanding is crucial for foundation models (FMs), and maps have long helped humans organize and reason about geographic information. This study examines whether choropleth maps remain useful for machine spatial understanding when models can directly process structured geodata. We introduce ChoroplethMap-Bench, a controlled benchmark containing 2,400 synthetic choropleth maps, corresponding GeoJSON data, and 12,000 questions across five cognitive dimensions: Identify, Spatial Recognition, Compare, Rank, and Delineate. We evaluate 22 open-source and proprietary models under three input conditions: Data Only, Map Only, and Data + Map. The results show that maps substantially improve spatial reasoning, especially when combined with symbolic data and for tasks requiring higher-level understanding of spatial patterns. We further analyze the effects of map type, color hue, and spatial structure, as well as prompting strategies, language, geographic context, decoding settings, classification methods, and response stability. Overall, the Data + Map condition achieves the strongest performance, demonstrating that maps remain valuable external representations for foundation model spatial reasoning.

---


### 176. [MADA-RL: Multi-Agent Debate-Aware Reinforcement Learning for Parameter-Efficient Reasoning in Compact Models](https://arxiv.org/abs/2607.18006)

**<font color=#1a73e8>作者：</font>** Martino M. L. Pulici, Cuong Xuan Chu, Evgeny Kharlamov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models achieve strong reasoning performance, but often at prohibitive training cost - a challenge that is especially acute for compact models ($\leq 4 \, \mathrm{B}$ parameters) trained under limited budgets. We introduce MADA-RL, a post-training framework that specializes compact models into generator and critic roles and trains them with a debate-aware learning signal, fine-tuning only a small subset of parameters via LoRA adapters. Our central contribution is a counterfactual critic advantage: a dynamic, role-conditioned baseline that redefines the critic's advantage as its reward minus the generator ensemble's per-instance accuracy. This explicitly optimizes critics to improve over generator consensus rather than to merely reproduce a correct answer, yielding more targeted credit assignment than static mean-reward normalization. At deployment, the specialized agents are composed in a lightweight multi-round protocol. Across five mathematical reasoning benchmarks, MADA-RL raises the accuracy of the DeepSeek-R1-Distill-Qwen-1.5B model from $39.9 \, \%$ to $41.9 \, \%$ ($+2.0$ points, $p < 0.001$) using $16$ times fewer trainable parameters than fully fine-tuned baselines, placing it on the accuracy-trainable-parameter Pareto front. It approaches, but does not surpass, the strongest baselines (DeepScaleR, STILL-3), which are trained on substantially larger datasets; we analyse this gap and the associated inference-time cost directly. A controlled study isolates the source of MADA-RL's gains: the counterfactual advantage produces the highest critic improvement rate of any model evaluated, indicating that trained critics learn to correct generator errors rather than to imitate them.

---


### 177. [Rethinking Heterogeneous LLM Merging: A Weighted Model Averaging Perspective](https://arxiv.org/abs/2607.18026)

**<font color=#1a73e8>作者：</font>** Jiahe Fan, Yinghao Hou, Si Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can large language models with substantially different parameter spaces be merged by direct weighted averaging, without training or semantic alignment? Existing heterogeneous fusion methods typically introduce distillation, adapters, learned latent spaces, routing, or feature alignment, leaving open whether a simpler recipe can work for genuinely different billion-parameter checkpoints. We revisit this counterintuitive question through training-free dimensional adaptation followed by ratio-controlled interpolation. In union-style merging, we expand the smaller model into the larger parameter space; in intersection-style merging, we truncate the larger model into the smaller parameter space. Across Qwen-family model pairs and benchmarks covering mathematical reasoning, code generation, language understanding, commonsense reasoning, knowledge, and instruction following, deterministic expansion largely preserves the source model function, and small-ratio interpolation can improve over strong source checkpoints by transferring complementary capabilities. However, near-balanced interpolation often collapses, and task-level results reveal a seesaw effect in which gains on some capabilities coexist with regressions on others. These results show that simple parameter averaging, when paired with lightweight dimensional adaptation and carefully controlled ratios, is a surprisingly strong baseline for heterogeneous LLM merging, suggesting that the limits of direct weighted fusion may also bound what more complex heterogeneous merging methods can achieve at scale.

---


### 178. [AdaHome: An Adaptive Smart Home Assistant using Local Small Language Models](https://arxiv.org/abs/2607.18034)

**<font color=#1a73e8>作者：</font>** Eu Jin Lim, Zhaoxing Li, Sebastian Stein  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Smart home assistants interpret a wide range of user commands, from explicit device control to underspecified and preference dependent requests. While recent systems based on Large Language Models (LLMs) improve this capability, they often rely on heavyweight reasoning pipelines and cloud-based deployment, limiting their efficiency and suitability for resource-constrained environments, and raising privacy concerns. In addition, existing approaches provide limited support for stable long-term personalization. To address these issues, we present AdaHome, an adaptive smart home assistant designed for locally deployed small language models in smart home environments. Rather than applying complex reasoning uniformly, AdaHome introduces an intent-aware planning framework that dynamically routes commands either to straightforward prompt-based or lightweight reasoning-based components. For commands requiring interpretation, we adopt a Chain-of-Draft strategy to enable efficient and stable decision-making. To support personalization, we further propose a preference adaptation mechanism that learns from user feedback over time without requiring prompt augmentation or model retraining. We evaluate AdaHome against representative LLM-based baselines under a unified small model setting. AdaHome achieves substantially higher accuracy on direct commands (86.7%) while reducing latency by up to 3$\times$. Furthermore, it maintains competitive performance on ambiguous inputs with lower computational cost. In multi-turn scenarios, AdaHome achieves 88% preference consistency, compared to 52.5% for a prompt augmentation baseline.

---


### 179. [An Early Warning of Emerging Biosecurity Risks in Frontier LLMs](https://arxiv.org/abs/2607.18056)

**<font color=#1a73e8>作者：</font>** Zhida He, Xia Hu, Baichen Le 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Frontier large language models (LLMs) are increasingly integrated into scientific workflows, yet their growing biological capabilities may outpace current safeguards. To assess the biological risks of frontier models, we develop Intern-BioBreaker, a specialized bio-red-teaming model, together with an integrated computational-to-physical framework that couples model-level stress testing with wet-lab validation. Within this framework, Intern-BioBreaker generates targeted jailbreak prompts to test whether aligned models can be induced to provide operational guidance for safety-sensitive biological tasks or produce sequence-level outputs with potentially harmful properties. Selected sequence outputs are then carried forward for DNA synthesis, host expression, and orthogonal protein verification to assess whether model-generated designs can yield the intended biological products. Our evaluation reveals a concerning gap between text-level safeguards and the risks posed by capable scientific models: (i) Intern-BioBreaker outperforms baseline attack models and reveals widespread bio-risk jailbreak vulnerabilities across both open-weight and proprietary frontier LLMs, with several targets reaching near-saturated or 100% task-level attack success rate (ASR); (ii) in sequence-level case studies, GPT-5.5 can be induced to generate modified viral candidate sequences with pathogenic potential; the corresponding translated proteins may exhibit even stronger receptor-binding affinity and thus enhanced infection potential; and (iii) end-to-end verification shows that selected model-generated biological designs are not merely textual artifacts, but can be physically realized under controlled experimental settings. These findings underscore the need for stronger biological red-teaming, nucleic acid synthesis screening, and safety mechanisms that keep pace with model capabilities.

---


### 180. [Pancasila-Dilemmas: Evaluating Large Language Models on Indonesian Human Value Dilemmas Grounded in Pancasila](https://arxiv.org/abs/2607.18066)

**<font color=#1a73e8>作者：</font>** Supryadi, Irfan, Julianti 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The value alignment of large language models (LLMs) is crucial for ensuring responses align with human intention and value preferences. However, most evaluations of value alignment focus on Western or universal values, while assessments grounded in the value systems of specific countries remain scarce. In this paper, we introduce Pancasila-Dilemmas, an evaluation dataset of 1,834 questions derived from Indonesian news, classified by 5 values of Pancasila: Religion, Humanity, Unity, Democracy, and Social Justice. This dataset reflects daily life in Indonesia, making it suitable for measuring the value alignment of LLMs deployed for Indonesia. To ensure a more rigorous evaluation, we choose scenarios containing dilemmas. The dataset is proofread by native speakers and answered by 5 diverse Indonesian citizens. We evaluate 50 closed- and open-source LLMs on our dataset. Results reveal that all evaluated LLMs achieves less than 0.5 Probability Match Score (PMS) and 0.72 Max-Vote Agreement Score (MVAS). Compared by each values, LLMs mostly struggle in Religion and Unity dilemma cases. This highlights a significant gap in capturing Indonesian values. The dataset is publicly available at this https URL.

---


### 181. [Generalised Bellman recurrence and three dualities in sequential decision-making](https://arxiv.org/abs/2607.18077)

**<font color=#1a73e8>作者：</font>** Fernando E. Rosas, David Hyland, Daniel Polani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What gives the Bellman equation its form? We show that the recursive properties of optimal value functions follow from three conditions: that the dynamics decomposes through sufficient statistics, that the return decomposes recursively, and that the aggregation of uncertainty is compatible with both. When all three conditions hold on a common state, the Bellman equation arises from their mutual consistency; when one fails, tractability can often be recovered by augmenting the state or by deforming return or dynamics. The same conditions are shown to give rise to three dualities: one between probability and return, one between return and aggregation, and one between aggregation and probability. Our framework reveals these dualities as arising from a single construction, unifying methods developed separately across reinforcement learning, control, and decision theory.

---


### 182. [Sparse Evidence Can Suffice: Agentic Evidence Seeking for Multimodal Video Misinformation Detection](https://arxiv.org/abs/2607.18080)

**<font color=#1a73e8>作者：</font>** Haochen Zhao, Yongxiu Xu, Xinkui Lin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal video misinformation detection is commonly formulated as a holistic video-understanding task, where the entire video and its associated content are processed and judged in a single pass. However, real-world misinformation often exhibits a sparse and compositional evidence structure: a reliable decision may depend on only a few coupled clues, while most video content contributes limited additional information. Exhaustive multimodal reasoning may therefore introduce substantial redundancy and obscure decisive evidence. This motivates decoupling evidence acquisition from verification: first identifying sparse, decision-relevant clues and then judging veracity based on the acquired evidence. Accordingly, we propose SIEVE, a framework for Sparse Interactive Evidence Verification via Extraction in multimodal video misinformation detection. An evidence-seeking agent actively explores the available multimodal evidence and constructs a compact evidence package, which is then used by a verifier to determine veracity. The agent is trained with supervised evidence-seeking trajectories and an evidence-aware reinforcement learning objective that promotes informative evidence acquisition while discouraging unnecessary or invalid interactions. Experiments on multiple video misinformation benchmarks show that SIEVE consistently outperforms the evaluated baselines and supports reliable verification using compact evidence packages. Moreover, the resulting acquisition process provides an explicit and inspectable evidence trail, improving the transparency and groundedness of multimodal misinformation detection.

---


### 183. [SelectInfer: Selective Neuron Loading and Computation for On-Device LLMs](https://arxiv.org/abs/2607.18081)

**<font color=#1a73e8>作者：</font>** Huzaifa Shaaban Kabakibo, Eric Schniedermeyer, Artem Burchanow 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated remarkable capabilities across a range of Natural Language Processing (NLP) tasks, but their high computational and memory demands pose significant challenges for deployment on resource-constrained edge devices. Existing approaches to model compression and optimization often rely on coarse-grained pruning or quantization, which can compromise accuracy or require re-training and fine-tuning. In this work, we introduce SelectInfer, a neuron-level optimization framework that enables efficient LLM inference on edge devices through selective neuron loading and computation. By profiling and identifying both task-specific and general-purpose neurons using an offline LLM profiler, SelectInfer implements two key optimizations: selective loading, which reduces memory footprint by selectively loading a subset of neurons that were identified to be most important during the offline stage, and selective computation, which dynamically computes only the most relevant neurons at runtime. Evaluation across multiple datasets shows that SelectInfer achieves significant reductions in memory footprint and computation while preserving task performance, making it a practical step towards enabling LLM deployment on edge devices

---


### 184. [WorldCupArena: Fine-Grained Evaluation of Language Models and Deep-Research Agents on Football Forecasting](https://arxiv.org/abs/2607.18084)

**<font color=#1a73e8>作者：</font>** Zhaokai Wang, Tianlin Gui, Jiayuan Rao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predicting a football match before kickoff requires more than knowing past results: a model must use changing information and make a clear prediction before the answer is available. We present WorldCupArena, a dynamic benchmark for language models and deep-research agents. The 2026 FIFA World Cup is its first evaluation, and the same process can be reused for future leagues and cups. Before each match, a model either receives a common evidence package or searches for information itself. It predicts the result and score, likely players and events, match statistics, and the outcome of the competition. After the match, these predictions are compared with the recorded result. We report result accuracy, exact-score accuracy, and a scoreline score that gives some credit when a predicted score is close but not exact, together with scores for the other prediction tasks. Across 104 matches and 13 systems, models with similar result accuracy differ more clearly on detailed predictions. Compared with betting-market and human-fan baselines, the best system shows only small gains in result and exact-score accuracy, but a clearer gain in Scoreline. New schedules can be added as they begin, allowing the benchmark to evaluate future models without using outcomes that are already known. Code, prompts, predictions, and evaluation scripts are open sourced at this https URL.

---


### 185. [Judge-dependent safety gains and model-specific helpfulness costs of evidence-sufficiency prompting in clinical LLMs](https://arxiv.org/abs/2607.18086)

**<font color=#1a73e8>作者：</font>** Koyar Afrasyab  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Background: LLM judges increasingly score whether clinical language models give overconfident answers under incomplete evidence, yet whether a measured "safety gain" reflects real behavior change or the judge's calibration is unresolved. Using a structured evidence-sufficiency prompt as a test case, we asked whether it reduces unsafe overconfident answers, how far that effect depends on the scoring judge, and what it costs in helpfulness.
Methods: In a retrospective public-data benchmark (Real-POCQi, HealthBench, MedRBench), four models (GPT-5.5, Claude Opus 4.8, Gemini 3.5 Flash, Grok 4.3) answered a fully paired common panel (1,200 cells) with a standard prompt and the wrapper. The pre-specified endpoint was the paired reduction in unsafe overconfidence scored by the primary judge (GPT-5.4-nano); secondary analyses added a different-family judge (Claude Sonnet 5), a correctness judge, matched scaffold controls, and a blinded three-clinician review.
Results: Unsafe overconfidence fell from 49.3% to 24.7%, a paired reduction of 24.7 points (95% CI 21.8-27.7; p<0.001), robust in direction across models and paraphrases. Magnitude was judge-dependent: Sonnet agreed on direction but nearly halved the effect (+13.1 points), with one-directional disagreement. Blinded clinicians characterized the primary judge as a high-sensitivity (1.00), low-specificity (0.55) screen, not a calibrated rate. The gain carried a model-specific helpfulness cost (correct diagnosis 80.3% to 50.3%): near-free for GPT-5.5, near-total for Gemini (-58 points). Matched scaffold controls showed genuine behavior change, not judge circularity.
Conclusions: LLM-judged clinical safety effects should be reported as directional and relative, anchored to human review and evaluated jointly with helpfulness, not as calibrated absolute rates. This does not establish clinical deployment readiness.

---


### 186. [The Label Complexity of Class-Conditional Coverage under Distribution Shift](https://arxiv.org/abs/2607.18088)

**<font color=#1a73e8>作者：</font>** Weijia Han, Lisha Qu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard evaluation of many recognition systems contains distribution shift by construction, since benchmarks place disjoint conditions in the training and test splits. Under such a shift, split conformal prediction keeps marginal coverage near the nominal level while per-class coverage fails silently: on a real cross-subject skeleton benchmark, marginal coverage stays near ninety percent, the worst action class is covered about seventy percent of the time, and ten of the sixty classes fall below eighty percent coverage.
We characterize the cost of restoring per-class validity. First, an impossibility: once the shift acts jointly on the covariates and the labels, the target class-conditional score law is unidentified from source labels and an unlabeled target sample, so no label-free method attains per-class coverage that is at once valid and efficient. Second, we make the cost precise: per-class validity alone needs only a handful of target labels per class, while the label count necessary and sufficient for validity together with per-class efficiency grows as the inverse square of the efficiency tolerance and the logarithm of the number of classes, with matching upper and lower bounds. Third, within the evaluated prediction-powered inference family, even the most favorable use of the classifier's own pseudo-labels on an unbounded unlabeled target pool improves efficiency by at most a small constant factor where coverage collapses.
Skeleton action recognition is our real-data case study. A per-class calibration using source labels alone recovers a substantial share of the per-class gap while the shift preserves marginal coverage, and stops helping exactly when marginal coverage itself breaks. Three real shifts of increasing severity trace this boundary, and the same collapse and recovery appears on a natural-image corruption benchmark, beyond any single modality.

---


### 187. [SciForma: Structure-Faithful Generation of Scientific Diagrams](https://arxiv.org/abs/2607.18091)

**<font color=#1a73e8>作者：</font>** Yuxuan Luo, Peng Zhang, Xinjie Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Structural fidelity is essential to scientific methodology diagrams. To communicate research logic, these diagrams must faithfully render components, directional relations, and textual annotations. Since a single error, such as a reversed arrow or an unreadable equation, can invalidate the entire figure, structural fidelity is inherently conjunctive: correctness on one axis cannot compensate for failure on another. Current open-source models fail to satisfy this criterion. Supervised fine-tuning (SFT) learns plausible layouts but cannot reliably ensure structural correctness, while scalar reward-based post-training obscures which structural dimension has failed. To address this, we introduce SciForma, a framework for the structure faithful generation of scientific methodology diagrams. Specifically, SciForma decomposes diagram quality into three structural axes: Component, Arrow, and Text, guided by a structural inventory. Built on this foundation, we curate SciFormaData-700K for structured training and SciFormaBench-2K for logic-verified evaluation. To close the gap left by SFT, we develop Multi-Dimensional Conjunctive Preference Optimization (M-DPO), which enforces simultaneous correctness across all axes and adaptively routes gradients to the most deficient dimension in post-training. The same structural inventory also enables iterative editing at inference time to correct residual errors. This combination allows SciForma-9B to exceed all open-source baselines and GPT-Image-1.5 on both SciFormaBench-2K and AIBench, bringing open scientific diagram generation close to proprietary-level structural fidelity. Our code and data will be available at: this https URL.

---


### 188. [VDAR-Router: Adaptive LLMs Routing via Verbalized Query Difficulty Analysis Retrieval](https://arxiv.org/abs/2607.18098)

**<font color=#1a73e8>作者：</font>** Yu-Chien Tang, Jun-Chen Hung, Wen-Chih Peng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used in practical systems, making efficient model selection important for reducing deployment cost. LLM routing has emerged as a practical solution for allocating each input query to an appropriate model under a desired cost-performance trade-off. Existing routing methods often estimate model suitability from the surface semantics or embedding similarity of the input query. However, such methods may ignore the underlying difficulty of a query, leading to suboptimal routing decisions. To address the challenge, we propose VDAR-Router, a difficulty-aware retrieval-based routing framework. For each input query, VDAR-Router first generates an explicit difficulty analysis. It then retrieves historical examples with similar difficulty profiles. Based on the retrieved records, it estimates candidate model suitability and selects the model using a reward function that considers both performance and cost. Experiments on three datasets show that VDAR-Router consistently achieves better cost-performance trade-offs than existing baselines. These results demonstrate the effectiveness of difficulty-aware retrieval for training-free LLM routing. Case studies further show that explicit query analysis helps retrieve more relevant examples and supports more reliable routing decisions.

---


### 189. [Can We Break LLMs Out of Self-Loops? Fine-Grained Reasoning Control with Activation Steering](https://arxiv.org/abs/2607.18100)

**<font color=#1a73e8>作者：</font>** Sheldon Yu, Tong Yu, Xunyi Jiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Extended reasoning has become standard for frontier Large Language Models (LLMs), yet the trajectories these models produce remain largely uncontrollable. Existing methods for shaping how a model reasons are prompt based approaches and operate at the input level, offering no fine-grained control over the reasoning process itself. Related work analyzes and discovers latent transition dynamics in the reasoning traces from Large Language Models. Building on this, we statistically characterize these states, and show that failure trajectories get stuck in self-loops, exhausting the token budget without progress toward the final answer. To intervene on these failures, We propose SOPHIA: Steering Of reasoning Processes via Hidden-state Intervention and Activations. We treat each reasoning trace as a sequence of latent states rather than an unstructured texts, and investigate whether inference time interventions can provide fine-grained control over the self-looping reasoning process. We classify every prefix to a latent state, record step level transitions, and use them to construct a bank of steering vectors indexed by state pairs. At inference time, a controller infers the current state and, given a target state, retrieves the corresponding vector and can also detect self-loops online from the transition structure to prevent the model from sinking into a reasoning black hole. Through extensive experiments, our method reliably intervenes on self-loop failures, with steering vectors that generalize to different state pairs. End task accuracy and token efficiency indicate that fine-grained controllability results in better reasoning quality.

---


### 190. [SpEmoC: A Balanced Speaker-Segment Multimodal Emotion Benchmark](https://arxiv.org/abs/2607.18109)

**<font color=#1a73e8>作者：</font>** Sania Bano, Shahzad Ahmad, Santosh Kumar Vipparthi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding human emotions in spoken conversations is a key challenge in affective computing, with applications in empathetic AI, human computer interaction, and mental health monitoring. However, existing datasets vary in scale, emotion distribution, modality alignment, and data partitioning strategies, which can influence reliable cross-dataset generalization and minority-emotion modeling. We introduce SpEmoC a Speaking segment Emotion for Conversations comprising 306,544 raw clips from 3,100 English language movies and TV series. From these, 30,000 high quality, class balanced clips are curated, featuring synchronized visual, audio, and textual modalities annotated for seven emotions through a hybrid pipeline that integrates pretrained models with human validation. SpEmoC uses strict movie- and series-level splits to prevent content overlap between split sets, allowing more reliable evaluation of model generalization. The dataset also maintains a near-balanced distribution across seven emotions, including minority classes such as Fear and Disgust, which supports more balanced learning across categories. Extensive experiments, including in-domain benchmarking, cross-dataset transfer, low-data training, class-imbalance analysis, and modality transfer show that balanced data and careful splitting lead to more stable performance across emotions when models are evaluated on other datasets. These results highlight the importance of dataset design for robust and transferable multimodal emotion recognition.

---


### 191. [LLM-as-a-Coach: Experiential Learning for Non-Verifiable Tasks](https://arxiv.org/abs/2607.18110)

**<font color=#1a73e8>作者：</font>** Tianzhu Ye, Li Dong, Guanheng Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) on open-ended tasks compresses an LLM's rubric-based evaluation into a scalar reward, discarding rich textual feedback and conflating responses with distinct quality profiles. We propose Experiential Learning (EL), which repurposes the feedback model from an LLM-as-a-Judge into an LLM-as-a-Coach. The coach distills its assessment of each on-policy response into transferable experiential knowledge, which conditions a teacher model and is internalized by the policy through on-policy context distillation. Compared with scalar rewards, this higher-bandwidth feedback channel provides dense supervision and preserves fine-grained preferences among high-quality responses. Across two policy families, with feedback from the policy itself or a proprietary model, EL consistently outperforms rubric-based RL on held-out and unseen open-ended tasks. Notably, EL generalizes better beyond the training distribution, and mitigates reward hacking. These findings establish experiential knowledge as a richer and more generalizable learning signal for post-training on non-verifiable tasks.

---


### 192. [How Does Alignment Tuning Shape Representations of Sycophancy and Related Cue-Induced Biases in LLMs?](https://arxiv.org/abs/2607.18114)

**<font color=#1a73e8>作者：</font>** Prakhar Gupta, Terry Jingchen Zhang, Florent Draye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern LLMs are alarmingly susceptible to surprisingly simple immaterial changes of input prompts: a casual hint, an incorrectly labeled few-shot example, or a fake prior assistant turn often flips an originally correct answer. We study where this susceptibility, spanning sycophancy and related cue-induced biases, lives inside the model. Across five model families and seven BCT bias types, we extract a per-bias direction from hidden states and triangulate it through three measures: probing, leave-one-dataset-out transfer, and causal intervention. The susceptibility is largely installed by alignment tuning rather than pretraining: pretrained base models barely cave to these biases, and their activations carry no cue-specific signal beyond question content. Within aligned models, each bias becomes a single coherent direction that we can both decode and steer along, recovering the unbiased answer across every family we test. The biases stay representationally distinct, however: cross-bias entanglement is model-specific rather than a property of the bias category, and even behaviorally similar biases occupy different directions. The same intervention also serves as a modest debiasing tool, recovering a meaningful share of bias-induced errors while preserving most correct answers across all instruct families. Cue-induced bias is therefore best understood not as a single flaw in LLMs but as a family of distinct, causally active directions that alignment tuning installs.

---


### 193. [SGA: Plug&Play Geometric Verification for Educational Video Synthesis](https://arxiv.org/abs/2607.18116)

**<font color=#1a73e8>作者：</font>** Lopez Jhon, Hinojosa Carlos, Ghanem Bernard  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work leverages Large Language Models (LLMs) to generate executable code for pedagogical animations using libraries such as Manim. However, ensuring spatial correctness and visual legibility remains challenging, as existing frameworks emphasize pedagogical content while overlooking geometric occlusions. We propose the Symbolic Geometric Agent (SGA), a plug-and-play module for code-centric animation pipelines that intercepts LLM-generated code, performs partial execution to extract symbolic scene graphs, and applies targeted refinement when spatial conflicts are detected. We further introduce the Manim Visual Quality Score (MVQS), a deterministic rendering-free proxy for spatial integrity. Experiments on the MMMC-Code benchmark across four LLM backbones and two agentic pipelines show that SGA achieves a peak MVQS of 73.11 (Code2Video + GPT-5.1), corresponding to a 16.1% relative improvement over the raw baseline, and improves MVQS in 7 of 8 backbone x pipeline configurations.

---


### 194. [Do Language Models Dream of Binding Molecules? Benchmarking LLMs under Spatial Constraints](https://arxiv.org/abs/2607.18144)

**<font color=#1a73e8>作者：</font>** Thomas MacDougall, Maksim Kuznetsov, Roman Schutski 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structure-based drug design (SBDD) leverages the 3D structure of protein targets, often complemented by other spatial constraints, to generate candidate binding molecules. While diffusion models have dominated as a leading paradigm for high-quality 3D molecule generation, LLM-based methods are rapidly emerging in molecular design and have shown competitive performance in pocket-conditioned molecular generation. However, their ability to reason about physics and 3D spatial environments is largely underexplored. In this work, we systematically analyze whether current general-purpose LLMs are capable of navigating complex 3D constraints compared to established baselines such as specialized diffusion models. We consider 3D ligand generation conditioned on protein pockets together with ligand- and interaction-derived spatial constraints, including anchor fragments, pharmacophore points, and mandatory pocket-ligand interactions. To enable this evaluation, we introduce 3D-Fit - a token-efficient benchmarking strategy for assessing LLM performance on multi-conditioned spatial molecule generation. Our findings reveal a clear pattern in LLM spatial capabilities: while they still lag behind state-of-the-art approaches, they are promising and can handle multiple spatial constraints simultaneously, enabling scaling to heterogeneous setups.

---


### 195. [Robust Multimodal Dynamic Object Segmentation](https://arxiv.org/abs/2607.18153)

**<font color=#1a73e8>作者：</font>** Zhe Xin, Hanzhi Chang, Penghui Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic object segmentation plays a critical role in many visual applications such as static scene reconstruction from dynamic videos. However, existing optical flow-based methods fail to ensure consistent static/dynamic segmentation along object boundaries, while 3D reconstruction-based approaches are highly sensitive to reconstruction errors. To address these limitations, we present a dynamic object segmentation framework that can generate both precise and complete dynamic masks by integrating multimodal cues including 2D point tracks, 3D reconstruction, and semantic information. We design a network combining Transformer architectures with feature clustering aggregation modules to perform static/dynamic classification of multimodal feature trajectories. It enables the model to adaptively determine which type of feature should dominate based on the characteristics of each scene, while also mitigating the impact of feature degradation. Additionally, we introduce a novel point-query-based SAM post-processing method capable of handling multiple objects within a single mask. Extensive experiments demonstrate that our approach achieves state-of-the-art performance in both dynamic object segmentation and static scene reconstruction tasks.

---


### 196. [OR Else: A Differentiable Trust Region for Policy Optimization](https://arxiv.org/abs/2607.18163)

**<font color=#1a73e8>作者：</font>** Chinmay Rane, Kanishka Tyagi, Michael Manry  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> PPO and the GRPO baseline studied here use clipped surrogate objectives whose favorable-direction saturation introduces an abrupt change in the scalar objective's derivative. We ask whether Output Reset (OR), a smooth one-sided saturation rule, offers a useful alternative for large language model post-training. PPO-OR and GRPO-OR replace the clipped policy term with an OR squared-margin loss in rollout-relative token log-ratio space; the advantage sign determines the update direction, and a token contributes zero direct OR residual after crossing the favorable margin. We compare PPO-clip with PPO-OR under generalized advantage estimation (GAE), and GRPO with GRPO-OR under group-relative advantages, using \texttt{Llama-3.2-1B-Instruct} on Anthropic \texttt{hh-rlhf} with one shared reward model and three seeds per method. Under GAE, PPO-OR has a mean final training-time reward-model score $0.305$ higher than PPO-clip, with a larger observed across-seed spread. Under group-relative advantages, GRPO-OR does not have a higher mean score, but shows a smaller observed spread, a near-zero terminal OR residual, and a declining overshoot fraction, while the matched GRPO clipped-objective trace remains variable. Both group-relative methods exhibit substantially larger rollout-to-current log-ratio displacement than the GAE methods, and OR does not consistently reduce it. Thus, OR changes optimization behavior in both matched comparisons, but the observed reward effect differs between them. At $G=2$, the GRPO-OR diagnostics do not translate into a reward-score gain. Whether larger groups change this outcome remains open. The reported scores are training-time reward-model measurements, not held-out human-preference performance.

---


### 197. [FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications](https://arxiv.org/abs/2607.18171)

**<font color=#1a73e8>作者：</font>** Krish Agarwal, Zhuoming Chen, Yanyuan Qin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-time multimodal applications, including voice agents and interactive video generation, compose heterogeneous models into pipelines whose efficient deployment requires application-specific decisions about placement, streaming, and intra-model parallelism. Existing serving systems and auto-parallelism compilers commit to limited transformations and fixed workload assumptions, so achieving high performance on a new application requires hand-crafting an efficient implementation. We present FlashRT, an agent harness that guides coding agents to lift simple developer-written reference implementations into optimized multi-GPU deployments that flexibly weigh target metrics like latency and throughput. Using a new chain-of-program paradigm, FlashRT directs a generic coding agent through a multi-pass transformation process where an agent transforms the reference into an intermediate representation (IR) to capture data dependencies and persistent-state scopes, validates this IR via a sequential interpreter, and performs static analyses to identify candidate transformations. Then, the agent iteratively implements, verifies, and benchmarks each candidate under a measurement-gated optimization loop to produce effective deployments that span different hardware budgets. Across various applications, including video world models and multimodal LLMs, FlashRT converts reference implementations into highly efficient deployments, delivering up to ~70x latency reduction and 2.8x throughput improvement on NVIDIA B200 GPUs. On AMD MI355X GPUs, FlashRT matches the peak latency reduction while increasing peak throughput improvement to 3.6x, demonstrating that agent-driven optimization can be more scalable on platforms with less mature expert optimization. In fact, for Qwen3-Omni text-to-audio inference, FlashRT reduces response latency by 65% compared to the expert vLLM-Omni implementation on AMD MI355X.

---


### 198. [VEHBench: A Stage-Local Diagnostic Benchmark for LLM-Assisted Vibration Energy Harvester Design](https://arxiv.org/abs/2607.18181)

**<font color=#1a73e8>作者：</font>** Depeng Su, Yuyu Luo, Guobiao Hu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Battery-free Internet of Things (IoT) requires iterative design of vibration energy harvesters (VEHs) under coupled physical constraints, while LLMs are emerging as interface layers for engineering workflows. However, existing engineering benchmarks primarily assess final artifact validity, offering limited insights into how LLMs behave across different stages of coupled physical design. We introduce VEHBench, an engineering-native diagnostic benchmark for LLM-assisted VEH design, featuring 763 literature-grounded tasks scored by an analytical physical oracle. VEHBench evaluates four design roles: specification triage, verifier-guided search, corrupted-state recovery, and policy-conditioned selection. Experimental results reveal that LLM capability is strongly stage-dependent: no single model consistently dominates the entire workflow, and response-control profiles expose distinct behavioral patterns across design roles. VEHBench thus provides a stage-aware foundation for evaluating, selecting, routing, and improving verifier-grounded engineering LLMs. The benchmark artifact is available at this https URL

---


### 199. [PPL-Factory: Task-Aware and Budget-Aware Data Selection from Language Modeling to Reasoning](https://arxiv.org/abs/2607.18199)

**<font color=#1a73e8>作者：</font>** Hang Zhang, Warren J. Gross  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Not all training samples contribute equally to large language model fine-tuning. Selecting informative training samples can reduce the computational cost while preserving downstream performance. Many existing data selection methods rely on indirect heuristics, such as data quality, diversity or reasoning trace length. However, the effectiveness of these fixed criteria is task-dependent and difficult to generalize across diverse downstream tasks. Perplexity-based data selection provides a simple and model-aware solution to estimate the sample difficulty, but existing approaches typically score the entire training sequence and ignore the difference in learning objectives of language modeling and reasoning tasks. In this paper, we propose PPL-Factory, a simple and interpretable data selection framework that combines task-aware perplexity-based scores and data budget-aware selection criteria. Experiments on GSM8K demonstrate that PPL-Factory outperforms other state-of-the-art data selection methods using only $1\%$ of the training set. With $10\%$ of the data, PPL-Factory exceeds full-data fine-tuning accuracy by 0.9 on GSM8K and 4.8 on MATH. Overall, our results demonstrate that task-aware and budget-aware perplexity-based selection provides an effective and applicable approach for efficient fine-tuning.

---


### 200. [SWE-Pruner Pro: The Coder LLM Already Knows What to Prune](https://arxiv.org/abs/2607.18213)

**<font color=#1a73e8>作者：</font>** Yuhang Wang, Yuling Shi, Shaoqiu Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pruning long context for coding agents has been a vital technology for efficient context management. While existing context pruning methods such as SWE-Pruner realize this by attaching a separate code classifier, we find the agent itself encodes internal representations indicating the relevance of code context when reading tool output. Based on this finding, we propose SWE-Pruner Pro, which prunes tool outputs directly inside the agent. Concretely, a small head turns the agent's own internal representations into a keep-or-prune label for each line, with a length-aware embedding keyed to each tool output's line count. Across two open-weight backbones and four multi-turn benchmarks, SWE-Pruner Pro saves up to 39% of prompt and completion tokens while preserving task quality, with bounded inference overhead. Notably, on MiMo-V2-Flash SWE-Pruner Pro additionally raises the SWE-Bench Verified resolve rate by +3.8% and the long-context Oolong accuracy by +2.2 points.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-204](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
