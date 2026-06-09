# 🧠 大模型相关研究 | 2026年06月10日

> 本类共 **331** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-331](./part-07.md)

---

### 51. [Simultaneous hyperkinetic movement disorders phenotyping: a cross-cohort pediatric transfer study using routine videos, markerless pose estimation and a tabular foundation model](https://arxiv.org/abs/2606.07674)

**<font color=#1a73e8>作者：</font>** Laura Cif, Diane Demailly, Zohra Souei 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Objective: To develop and externally test a video-based framework for simultaneous detection of hyperkinetic MDs phenomenologies: dystonia, tremor, myoclonus, chorea, athetosis, ballismus, stereotypies, and tics using routine clinical recordings, with explicit testing of external, cross-cohort transfer from adult to pediatric populations. Methods: In this proof-of-concept study, the framework combines markerless pose estimation, kinematic descriptors, and a pretrained fondation model. A shared predictive backbone was developed on 21 adults with confirmed hyperkinetic MDs and 4 healthy controls assessed under a standardized protocol. External validation was performed on an independent external cohort: a real-world pediatric sample (n=12, monogenic combined MDs). For the external dataset, the backbone was deployed without retraining; lightweight calibration adjusted only the final subject-level decision step using a small labeled subset of patients selected by clinicians as representative of the cohort's phenotypic range. Results: After local calibration of the decision layer on the clinician-selected subset, performance improved consistently on the held-out pediatric patients (n=7): Hamming accuracy rose from 0.804 to 0.839 and the Jaccard index from 0.548 to 0.633. This calibrated performance was preserved, and the Jaccard index further improved, when the evaluation was restricted to the phenomenologies with more definite clinician agreement (Hamming accuracy 0.9, Jaccard index 0.786), indicating that the gains did not rest on the least-reliable labels.

---


### 52. [DOG-DPO:Dynamic Optimization in Geometry for Safety Alignment](https://arxiv.org/abs/2606.07678)

**<font color=#1a73e8>作者：</font>** Yi Nian, Tiankai Yang, Yudi Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safety alignment for large language models relies on preference data, but current pipelines often train on large, redundant datasets. Existing data selection methods typically score each preference pair independently, collapsing directional preference information into scalar quality or diversity scores. This sample-centric view is especially limiting in multi-dataset settings, where shared safety directions coexist with dataset-specific residual risks. We propose DOG-DPO, a training-free data selection framework that treats preference pairs as structured geometric signals. DOG-DPO first represents each preference pair as a direction in model representation space. It then decomposes multi-dataset preference geometry into a global anchor subspace and dataset-specific residual subspaces. Finally, it selects subsets by maximizing diversity-based coverage, encouraging broad, non-redundant coverage of alignment directions before DPO training. Across six safety benchmarks and two model backbones, DOG-DPO achieves a strong utility-robustness trade-off using only 11% of the preference pairs. It recovers most of the safety gains of full-data training while remaining entirely teacher-free, training-free, and substantially faster than representative selection baselines.

---


### 53. [Semantic Cache Distillation: Efficient State Transfer via Reuse and Selective Patching](https://arxiv.org/abs/2606.07684)

**<font color=#1a73e8>作者：</font>** Qianli Ma, Zhiqing Tang, Hanshuai Cui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Disaggregated serving alleviates memory bottlenecks in Large Language Model (LLM) inference but creates a severe communication bottleneck: transmitting high-dimensional Key-Value (KV) caches often dominates time-to-first-token (TTFT). Moreover, reusing caches across heterogeneous models (e.g., base and fine-tuned variants) causes semantic misalignment that accumulates over layers, degrading generation quality. We propose Semantic Cache Distillation (SCD), a loss-constrained framework that replaces raw KV transmission with compact semantic codes. SCD addresses these challenges via two mechanisms: (1) Reuse, which reconstructs most layers from low-rank subspaces to minimize transfer cost, and (2) Patch, which predicts normalized inputs at sparse transition layers to truncate error propagation. Empirically, SCD delivers up to 2.65 $\times$ TTFT speedup over the oracle consumer prefill and dominates quantization and selective recomputation baselines on the quality--latency Pareto frontier in bandwidth-constrained regimes, while keeping generation quality within 5\% F1 of the oracle.

---


### 54. [What Makes Video World Model Latents Action-Relevant: Prediction over Reconstruction](https://arxiv.org/abs/2606.07687)

**<font color=#1a73e8>作者：</font>** Jewon Yeom, Hanseul Kim, Jeongjae Park 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models are increasingly used to provide predictive visual representations, yet it remains unclear which pretraining signals induce action-relevant structure in their latent spaces. We study this question through a unified probe-based evaluation across diverse encoder families, including image-only self-supervision, video pretraining with and without latent prediction, reconstruction-based autoencoders, diffusion models, and shortcut-forcing dynamics models. Using a common inverse-dynamics probing objective, we find that action-relevant structure is driven primarily by temporal video pretraining rather than pixel reconstruction fidelity: models with strong pixel decoding quality can exhibit near-zero action recoverability, while video-pretrained self-supervised encoders consistently achieve the best Pareto trade-off between visual fidelity and action prediction. Comparing V-JEPA and VideoMAE further shows that most gains arise from natural-video temporal context, with feature-level latent prediction providing a smaller additional benefit. These trends transfer across robotic benchmarks, though CALVIN reveals that static-environment tasks can partially mask the importance of temporal structure by allowing strong image priors to suffice. Finally, inverse-dynamics supervision substantially improves robustness to visual corruption, suggesting that action-aware objectives regularize latent geometry beyond clean-setting performance. Our results identify temporal predictive structure -- not reconstruction fidelity -- as the primary ingredient underlying action-relevant video representations.

---


### 55. [Struct-Searcher: Agentic Structural Thinking Advances Multimodal Deep Information Seeking](https://arxiv.org/abs/2606.07689)

**<font color=#1a73e8>作者：</font>** Fan Zhang, Vireo Zhang, Shengju Qian 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep research agents have attracted increasing attention for their ability to collect large-scale online information to acquire target knowledge, with recent efforts shifting from purely text-based information seeking to multimodal settings. However, existing agentic workflows are largely aligned with evidence accumulation models, which linearly aggregate evidence and lack principled mechanisms for handling contradictory information across heterogeneous modalities. Towards this end, we propose Struct-Searcher, a structural agentic workflow grounded in belief revision theory that explicitly maintains an evolving multimodal structural graph throughout the reasoning process, enabling effective conflict-aware multimodal deep information seeking. Extensive experiments across multiple benchmark datasets and backbone models demonstrate that Struct-Searcher is (1) plug-and-play and model-agnostic, yielding an average relative accuracy improvement of 17.2% on BrowseComp-VL across five different backbones. (2) top-performing, consistently outperforming state-of-the-art vision-language models (VLMs) and deep research agents, with relative accuracy improvements of 3.7% on MM-BrowseComp, 1.5% on HLE-VL, and 0.7% on BrowseComp-VL over the second-best competing approach.

---


### 56. [HARP: Efficient Data Selection for Finetuning Large Language Models](https://arxiv.org/abs/2606.07690)

**<font color=#1a73e8>作者：</font>** Ning Wang, Zhengxin Zhang, Maosen Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Finetuning data selection requires balancing two competing goals: selecting examples that improve the downstream objective, and doing so without repeatedly finetuning models. Train-free selectors are scalable but rely on proxies such as embedding similarity or clustering, which may not match the target objective. Train-based selectors better reflect downstream utility through gradient signals, subset evaluation, or Shapley attribution, but require many costly train--evaluate iterations. We propose Hierarchical Active Region Pruning (HARP), an efficient train-based selector that preserves downstream alignment while reducing selection cost. HARP organizes the training pool into a node--leaf hierarchy, evaluates only representative leaves, and infers unmeasured utilities with empirical Bayes posteriors. It then selects data using two complementary envelopes: HARP-C, which conservatively controls redundancy, and HARP-E, which additively rewards complementary regions. We theoretically show that, under local smoothness and bounded estimation error, HARP controls selection error while reducing train--evaluate cost. We further validate that HARP variants achieve the best result and outperform the strongest baseline by up to $+8.9$ points, while using roughly $7\times$ fewer training examples.

---


### 57. [BCG-FM: A Foundation Model for Ambient Cardiac Health Sensing](https://arxiv.org/abs/2606.07692)

**<font color=#1a73e8>作者：</font>** Magnus Ruud Kjaer, Haejun Han, Ashish Neupane 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models for wearable biosignals have matched or exceeded supervised specialists across a range of clinical tasks, yet all rely on modalities that require deliberate user action--wearing a device or visiting a sleep lab. We introduce BCG-FM, the first foundation model for ambient mechanical biosignals. A piezoelectric sensor embedded in the bed surface records ballistocardiography (BCG) each night without user effort; we pretrain BCG-FM with participant-level contrastive learning and using a total of 2.75 million hours of nightly recordings from 145,985 individuals, the largest raw-waveform biosignal pretraining corpus to date. Frozen BCG-FM embeddings achieve 3.26-year MAE on biological-age estimation (the lowest reported for any ambient, contactless modality) and yield clinically relevant discrimination across 15 self-reported health conditions and three independent external cohorts. Pretrained representations from only 500 labeled participants outperform a fully supervised baseline trained on 3,372, and representation quality scales log-linearly with contrastive batch size. These results establish ambient, longitudinal mechanical biosignals as a viable modality for health foundation models.

---


### 58. [Adversarial Robustness of Activation Steering in Large Language Models](https://arxiv.org/abs/2606.07696)

**<font color=#1a73e8>作者：</font>** Kien Le, Thai Le  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation steering has become a popular training-free method to control LLM behavior by injecting precomputed direction vectors into the model's residual stream at inference time. Yet its robustness to realistic input variation remains unstudied. We present the first systematic evaluation of activation steering robustness under adversarial text perturbations on the inputs, covering four extraction methods, three attack strategies, six personas from Anthropic Model-Written Evaluation Dataset, and five models ranging from 1.5B to 30B parameters. Attacks succeed broadly across all settings: directional robustness drops by up to 64%, post-attack confidence collapses near or below 0.25 across all methods and models, and steering strength degrades on nearly every steerable input. Layer selection is equally fragile, with the optimal layer identified by an automated method on clean inputs shifting by up to 17 positions under perturbation, a failure that compounds the vector-level breakdown. Extracting vectors from adversarially perturbed inputs partially recovers steerability for PCA and MD on mid-to-large models, but they consistently fail to locate the improved optimal layer, limiting the practical benefit of this mitigation. Together, these findings reveal that the brittleness of activation steering is structural rather than method-specific, and that current layer selection strategies are not robust enough for real-world deployment.

---


### 59. [FunctionEvolve: Structure-Guided Symbolic Regression with LLMs](https://arxiv.org/abs/2606.07704)

**<font color=#1a73e8>作者：</font>** Zeyu Xia, Jun Zhu, Dong Yan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symbolic regression aims to uncover explicit scientific laws from data. Recent methods use LLMs to guide mutation from background text, which is more directed than random genetic programming. However, exact symbolic recovery requires both semantic guidance and explicit structure, so that domain-informed search are carried out through valid symbolic representation. Current LLM-driven systems remain structure-blind: they select among opaque candidates, lack explicit mechanisms for local mutation, and rely on brittle coefficient fitting that can undervalue correct skeletons. We propose FunctionEvolve, an evolutionary framework using expression trees to organize the whole search: structural summaries promote diverse parent selection, local tree edits preserve useful subexpressions, and structure-aware fitting decomposes, constrains, and simplifies coefficients for more reliable scoring. It uses only elementary function families, without additional domain-specific rules limiting generalization. On the 129-task synthetic subset of LLM-SRBench, FunctionEvolve with \emph{Claude Opus 4.6} recovers 107 exact forms, reaching 82.9% SA@50, 4.5x above same-backbone baselines, and 55.8% SA@1, 3.6x above the strongest previously published top-1 result. Ablations show that structure-visible search is central to reliable recovery, with LLM-guided refinements and structure-aware coefficient optimization serving as essential proposal and scoring mechanisms. We also audit the benchmark and show that collinearity in its materials-science subset creates identifiability issues.

---


### 60. [SAW: Stage-Aware Dynamic Weighting for Multi-Objective Reinforcement Learning in Large Language Models](https://arxiv.org/abs/2606.07705)

**<font color=#1a73e8>作者：</font>** Yuchen He, Baolong Bi, Shenghua Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Although multi-objective reinforcement learning (MORL) is central to aligning large language models with complex human preferences, the prevailing practice of static weighted summation overlooks a more fundamental phenomenon: reward learning is markedly asynchronous across objectives. Well-learned dimensions quickly produce homogeneous, low-variance signals whose residual noise contaminates the aggregated reward (in GRPO) or occupies a fixed share of the advantage budget (in GDPO), interfering with the scarce yet high-value signals carried by under-learned dimensions. To address this asynchrony, we propose Stage-Aware Dynamic Weighting (SAW), a lightweight, algorithm-agnostic dynamic weighting mechanism. SAW utilizes the coefficient of variation (CV) as a scale-invariant proxy for real-time informativeness, reweighting each dimension's reward or advantage contribution by its relative informativeness within the batch. Unlike gradient-based methods that require multiple forward and backward passes, SAW relies solely on batch-level statistics, introducing nearly negligible computational overhead. Experiments on tool-calling and text summarization tasks demonstrate that SAW consistently improves both training efficiency and final performance under both GRPO and GDPO frameworks, confirming it as a general-purpose plug-in for multi-reward LLM alignment. Our code is available at this https URL

---


### 61. [Decoding Naturalistic Emotion Dynamics from the Brain: An LLM-Enhanced Regression Framework](https://arxiv.org/abs/2606.07707)

**<font color=#1a73e8>作者：</font>** Lemei Zhang, Peng Liu, Hans Dahle Kvadsheim 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decoding emotional states from neural signals has been typically framed as a discrete, single-label classification task based on emotionally stable stimuli, a formulation that oversimplifies the continuous, fluid, and co-occurring nature of human affect. This study reconceptualizes emotion decoding by adopting a multi-target regression framework to track multiple overlapping emotional dimensions as continuous trajectories over time. Leveraging the robust generalization capabilities of Large Language Models (LLMs), we extracted fine-grained, continuous sentiment profiles from a naturalistic auditory narrative, Alice in Wonderland, to serve as scalable proxies for subjective affect from human fMRI dataset. Departing from standard classification paradigms or mass-univariate subtractive contrasts that filter out network dynamics, we leverage regularized and kernel-based machine learning algorithms as continuous estimators to track the magnitude of macroscale neural state variations. We demonstrate that models trained on temporal snapshots of Dynamic Functional Connectivity (DFC) significantly outperform static region-of-interest (ROI) amplitude representations, effectively capturing continuous emotional trajectories under rapidly fluctuating narrative input. Furthermore, by implementing graph-theoretical Explainable AI (XAI) techniques, we deconstruct the underlying predictive features to reveal highly interpretable, emotion-specific topological configurations. Collectively, these results highlight the utility of LLM-automated annotation in affective neuroscience and provide compelling empirical evidence for psychological constructionist frameworks, demonstrating that dynamic, distributed network interactions offer superior explanatory power over strictly locationist accounts of emotion.

---


### 62. [WhiFlash: Accelerating Speculative Decoding with Token-Level Cross-Paradigm Routing](https://arxiv.org/abs/2606.07710)

**<font color=#1a73e8>作者：</font>** Young D. Kwon, Miles Williams, Rui Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The autoregressive nature of large language models (LLMs) remains a significant bottleneck for inference, particularly in complex agentic workloads. While speculative decoding (SD) accelerates inference, current approaches rely on static drafting paradigms, utilising either autoregressive drafting models for reasoning or diffusion-based parallel drafting models for structured outputs. We empirically find that drafting accuracy fluctuates dramatically within a single sequence, leaving significant performance unrealised by static paradigms and coarse-grained routing. To address this volatility, we introduce WhiFlash, the first cross-paradigm SD method that unifies autoregressive and diffusion-based parallel drafting under a single token-level controller. WhiFlash adopts a fine-grained routing mechanism that employs either a lightweight entropy-based or a learned neural policy, both parametrised to provide a tunable balance between expected token gain and latency. To make high-frequency switching computationally viable, we introduce novel cache-management optimisations, Lazy Catch-up and KV-only Prefill, reducing switching overhead to below 7% of per-round latency. By capitalising on the complementary strengths of fundamentally distinct drafting architectures, WhiFlash achieves significantly higher acceptance lengths, yielding category-specific throughput gains of up to 69.6% over the state-of-the-art autoregressive EAGLE-3 and 37.3% over the diffusion-based DFlash.

---


### 63. [Rosetta Memory: Adaptive Memory for Cross-LLM Agents](https://arxiv.org/abs/2606.07711)

**<font color=#1a73e8>作者：</font>** Hao Yang, Shiqi Shen, Haoxuan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Memory is the key component for transforming a stateless LLM into a persistent, evolving agent through experience accumulation, long-horizon planning, and continual self-improvement. Existing memory systems typically take the LLM as the center and design memory operations tailored to a specific backbone. In practice, however, users frequently switch between LLMs, for example using Claude for coding and GPT for writing across tasks, or routing different steps to different backbones within a single task for cost-effective trade-offs. As a result, memory written by one model often needs to be consumed by another. Making upstream memory effectively adapt to and activate downstream LLMs remains a critical yet underexplored problem. To bridge this gap, we shift the perspective from LLM-centric memory design to \emph{memory-centric LLM adaptation}. Specifically, we approach the above upstream-downstream memory adaptation problem from both the write and read sides, and design two profile-conditioned operators that are jointly trained to optimize how memory is stored and presented for better task completion. To ensure the learned operators generalize across a broad set of LLMs, we propose a minimum-gain sampling curriculum that prioritizes the least-served LLMs during training. To better measure the operators' actual contribution rather than the LLM's own capability, we design a performance-gap reward that compares against a naive memory baseline. Experiments on HotpotQA, 2WikiMultihopQA, and MuSiQue demonstrate that our model consistently outperforms baselines and remains robust under unseen-model replacement.

---


### 64. [Why Limit the Residual Stream to Layers and Not Tokens? Persistent Memory for Continuous Latent Reasoning](https://arxiv.org/abs/2606.07720)

**<font color=#1a73e8>作者：</font>** Mujtaba Farhan, Maheep Chaudhary  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated remarkable reasoning abilities on mathematical and multi-hop planning tasks. The CoCoNuT (Chain of Continuous Thought) paradigm~\cite{hao2024coconut} extends this by enabling models to reason in latent space, exploring multiple reasoning paths simultaneously rather than committing to a single chain early on. However, we identify a limitation we term the \textbf{concept bottleneck}. At each reasoning pass, intermediate hidden states are overwritten, causing the model to lose critical facts computed in earlier steps as reasoning depth increases. We observe this empirically. On HotpotQA, vanilla CoCoNuT (10.4\% EM) fails to improve over the CoT baseline (11.0\% EM), and performance degrades with curriculum depth on GSM8K. To address this, we propose \textbf{AGCLR} (Adaptive Gated Continuous Latent Reasoning), which augments CoCoNuT with a \textit{Gated Concept Stream}. A persistent residual memory maintained across all reasoning passes, controlled by three learned gates: a \textit{write} gate that commits intermediate facts to memory, a \textit{read} gate that retrieves relevant prior states, and a \textit{forget} gate that prunes irrelevant context. Evaluated on GSM8K, HotpotQA, and ProsQA using GPT-2 as our base model, AGCLR achieves consistent improvements across all types of datasets. With the performance gap compounding as curriculum depth increases, directly resolving the concept bottleneck. Code available at this https URL

---


### 65. [Automatic Extraction of Structured Information from Brain MRI Reports Using an Open-Weight Large Language Model](https://arxiv.org/abs/2606.07721)

**<font color=#1a73e8>作者：</font>** Kaouther Mouheb, Amos Pomp, Antoine Manenti 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Objectives: Automatic data extraction from free-text radiology reports enables large-scale research, but few studies assessed the performance of large language models (LLMs) on Dutch neuroradiology reports. Methods: We analyzed 947 brain MRI reports from a tertiary memory clinic (2016-2021), authored by consultant neuroradiologists. Trained medical students annotated thirty variables; 100 reports were double-annotated to assess inter-rater reliability. We evaluated the performance of the open-weight LLM LLaMA 3.1 using different languages (Dutch vs. English translation) and few-shot prompting with different example selection strategies. Performance was evaluated using balanced accuracy for categorical variables, accuracy and mean absolute error for counts, and text similarity for free-text. Metrics were computed across 10 random splits of the 947 reports. Results: LLaMA 3.1 demonstrated high zero-shot performance for visual rating scores (mean [95%-CI]): Medial Temporal Atrophy: 90% [77-100%] on the left and 96% [94-99%] on the right, Global Cortical Atrophy: 87% [83-91%], and Fazekas: 94% [93-96%]. Microbleed mentions were detected with 93% accuracy [92-95%] and infarct mentions with 82% [80-84%]. Text similarity for lesion location reached 0.95 [0.95-0.96]. Performance was lower for numerical variables: 80% [78-82%] for the number of microbleeds and 66% [63-68%] for infarcts. English translation yielded comparable results. Few-shot prompting improved performance for numerical variables, achieving 92% [90-93%] for microbleeds and 81% [77-85%] for infarcts using structural similarity-based selection. Conclusion: LLaMA 3.1 shows strong potential for extracting data from Dutch neuroradiology reports. Few-shot prompting enhances performance for numerical variables, whereas challenges remain for location-specific variables.

---


### 66. [Some hypotheses on how chatbots work in problem-solving-driven conversations. Large Language Models as confirmation of the Innovation Illusion](https://arxiv.org/abs/2606.07722)

**<font color=#1a73e8>作者：</font>** S.F.M. van Vlijmen, H.D. Lethe jr  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This article offers a perspective on the nature of chatbots as genuine conversation partners when discussing problems in relation to their solutions. What can chatbots do and what can't they do, and how can this be explained? Our argument draws on Aggregation Dynamics, Cognitive Linguistics, Neuropsychology and Psychology.
Our argument focuses on basic chatbots in the hope of thereby making statements about the core functionality of more advanced chatbots. Basic chatbots are assumed to consist of a Large Language Model (LLM) with a simple interface.
The main results are: a description of human understanding and thinking based on so-called metaphorical problem propagations; the hypothesis that text dataset used for training LLMs have specific characteristics and that these text datasets only partially imitate human thinking and understanding; the hypothesis that the LLM training process encodes artificial metaphorical problem propagations into an LLM from these datasets; our conclusion that a basic chatbot cannot be a thinking partner capable of matching humans; our conclusion that further development of the Large Language Model will not lead to this either.
Yann LeCun states: "Animals and humans exhibit learning abilities and understandings of the world that are far beyond the capabilities of current AI and machine learning (ML) systems." Our conclusions are in line with this. LeCun's vision and ours are at odds with the optimism of Big Tech. That does not alter the fact that chatbots exist, that they are being used on a massive scale, by both individuals and organisations, and that it is therefore socially and politically important to understand them. Our article aims to contribute to the discussion on the functioning, benefits and drawbacks of chatbots.
We have not yet encountered the approach we used to arrive at our conclusions in our research into how chatbots work.

---


### 67. [Cutting LLM Evaluation Costs with SySRs: A Bandit Algorithm that Provably Exploits Model Similarity](https://arxiv.org/abs/2606.07726)

**<font color=#1a73e8>作者：</font>** Zifan Lyu, Chahine Nejma, Tobias Wegel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models are typically benchmarked by evaluating every model on every test query. For practitioners seeking the best model to deploy, this is often wasteful: if a model clearly performs worse than others, there is no need to precisely estimate its performance. Best-arm identification algorithms can be naturally applied to drastically reduce costs by adaptively allocating evaluation budget. Further, language models often respond similarly to the same prompt-a property previous work has tried to leverage with mixed success. We propose Synchronized Successive Rejects (SySRs), augmenting the classical Successive Rejects algorithm with paired comparisons. Unlike prior attempts to leverage model similarity in best-model identification, our approach is hyperparameter-free and enjoys performance guarantees that improve with the degree of similarity between evaluated models. Empirically, our method outperforms all baselines in terms of average error rate across 15 standard benchmarks, and in terms of worst-case budget for reliably identifying the best model.

---


### 68. [TibetCPR: A Multimodal Tactile Feedback System to Enhance Cardiopulmonary Resuscitation Training in High-Altitude Regions of Tibet](https://arxiv.org/abs/2606.07765)

**<font color=#1a73e8>作者：</font>** Yibo Meng, Ruiqi Chen, Zhiming Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> High-quality cardiopulmonary resuscitation (CPR) requires stable control of compression rhythm and depth, yet most training systems presuppose instructor mediation, repeated practice, and explanatory guidance-assumptions that do not hold in the Tibet Autonomous Region, where instruction is fragmented and learners' linguistic and educational backgrounds are heterogeneous. We present TibetCPR, a low-cost, self-guided CPR training system that pairs depth-driven electrotactile feedback with rhythm-driven visual cues within a Tibetan-language narrative. In a randomised study with 40 lay community members aged 19--56, the experimental group showed progressive minute-by-minute stabilisation of rhythm and depth across a 10-minute intervention, substantially exceeding an unguided-practice control, with gains transferring to an unscaffolded one-minute post-test. Qualitative accounts described the feedback as legible through participants' bodily action, and usability was high (SUS = 84.3). We synthesise three transferable design principles for self-guided embodied training: feedback as a calibration reference, not an immediate corrector; modality temporal granularity matched to behaviour's temporal structure; and autonomous interpretability as a deployment prerequisite, not an after-effect of usability.

---


### 69. [DALE-CT: Depth-Aware Foundation Models for Computed Tomography](https://arxiv.org/abs/2606.07775)

**<font color=#1a73e8>作者：</font>** Evan W. Damron, Mahmut S. Gokmen, Mitchell A. Klusty 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent breakthroughs in self-supervised learning (SSL), such as the Latent-Euclidean Joint-Embedding Predictive Architecture (LeJEPA), alongside successes in integrating visual encoders with language models, have driven the demand for adaptable, high-capacity vision encoders in Computed Tomography (CT). In this work, we explore 2D slice-based architectures as a flexible alternative to native 3D models for processing volumetric CT data. Using the CT-RATE dataset, we trained DALE-CT (Depth-Aware Latent-Euclidean Computed Tomography), a 2D model family built entirely from scratch using LeJEPA, and compared its performance against a continually pre-trained DINOv2 baseline. To enhance representation quality, we developed a novel 3D depth-aware pre-training strategy anchored by dense auxiliary supervision from both automated anatomical masks and human-annotated abnormalities. Under linear probe evaluation with Multiple Instance Learning (MIL) for multi-abnormality detection, the frozen backbone of this dual-supervised model (DALE-CT-2S) achieves a Macro AUROC of 0.833. This performance demonstrates near-parity with state-of-the-art 3D vision-language models, achieved entirely from scratch with significantly less data and no textual supervision. To ensure reproducibility, all training code, evaluation scripts, and model weights have been made publicly available.

---


### 70. [Evaluating RAG Reliability under Clean, Misleading, and Mixed Retrieval](https://arxiv.org/abs/2606.07783)

**<font color=#1a73e8>作者：</font>** Sevgi Yigit-Sert  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) is widely used to improve the factual reliability of large language models (LLMs) by grounding answers in retrieved evidence. In misinformation-rich environments, however, retrieved content may include plausible but incorrect information, raising concerns about the reliability of RAG-based information access systems.
In this work, we propose an evaluation protocol to systematically test how the RAG system handles conflicts between parametric knowledge and evidence retrieved from context with varying amounts of misleading information. We target correct answers to factoid questions that the model responds to correctly, even when there is no retrieval, and use this to test the system with clean, poisoned, and mixed evidence.
The proposed analytical framework combines parametric override and confidence metrics to assess when and how misleading information affects the generation process of LLMs. This study aims to provide insights into the robustness of RAG systems in information disorder scenarios.

---


### 71. [Byzantine Cheap Talk: Adversarial Resilience and Topology Effects in LLM Coordination Games](https://arxiv.org/abs/2606.07790)

**<font color=#1a73e8>作者：</font>** Aya El Mir, Martin Takáč, Salem Lahlou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems increasingly rely on communication protocols for coordination, yet their robustness under adversarial and structural constraints remains poorly understood. Building on prior work showing that cheap-talk channels enable cooperation in LLM coordination games, we investigate two vulnerability classes in a 4-player Stag Hunt across six model families and 720 trials. First, when Byzantine agents signal cooperation but defect, non-Byzantine agents detect the betrayal within one round yet fail to adapt collectively: a substantial fraction continue cooperating despite repeated exploitation, unable to recover coordination due to the game's unanimity payoff structure. Second, explicitly restricting communication topology collapses cooperation, while applying identical restrictions silently preserves near-perfect cooperation. This establishes that coordination failure stems from agents' meta-reasoning about hidden information, not information loss itself. We identify two stable behavioral archetypes that replicate across all model cohorts: Defection-Prone models that switch permanently after betrayal, and Cooperation-Persistent models that continue cooperating at significant individual cost. These findings reveal concrete security vulnerabilities: communication channels can be exploited as adversarial injection vectors, and disclosing network topology to agents can degrade coordination even without any adversary present.

---


### 72. [Improving Multimodal Reasoning via Worst Dimension Optimization](https://arxiv.org/abs/2606.07801)

**<font color=#1a73e8>作者：</font>** Haocheng Lv, Huaping Zhang, Qiuchi Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal reasoning requires a path that retains integrity over a wide range of constraints, from visual grounding to logic consistency. However, the current Process Reward Models focus on heuristically defined rewards that equally weigh these factors, which may lead to the concealment of individual dimension failures by the dominating factors, without guaranteeing the validity of the reasoning process in general.

---


### 73. [Beyond Goodhart's Law: A Dynamic Benchmark for Evaluating Compliance in Multi-Agent Systems](https://arxiv.org/abs/2606.07805)

**<font color=#1a73e8>作者：</font>** Yiyang Zhao, Zhuo Zhang, Qingxuan Le 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of Large Language Models (LLMs) from passive assistants to autonomous, execution-capable agents has introduced critical operational risks. Most current evaluation frameworks neglect procedural compliance, leading to ''Machiavellian'' behaviors where agents strategically violate safety rules to maximize rewards - a direct manifestation of Goodhart's Law. To address this blind spot, we introduce MAC-Bench, a dynamic, adversarial benchmark designed to evaluate the procedural alignment of multi-agent systems under realistic pressure. We propose the SERV(Seed - Evolve - Refine - Verify) pipeline, an ``Agent-as-a-Benchmark'' paradigm that transforms unstructured legal texts into executable, contamination-free scenarios. By synthesizing holographic sandbox environments and injecting calibrated social-engineering pressure vectors, MAC-Bench forces agents into Pareto-optimal trade-offs between task success and regulatory adherence. We introduced novel metrics: the Compliance-Weighted Success Rate (CSR) and the Machiavellian Gap (MG), and conducted a comprehensive evaluation of state-of-the-art frontier models to reveal the pervasive trade-offs between success and compliance.

---


### 74. [Where Instruction Hierarchy Breaks: Diagnosing and Repairing Failures in Reasoning Language Models](https://arxiv.org/abs/2606.07808)

**<font color=#1a73e8>作者：</font>** Sanjay Kariyappa, G. Edward Suh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning language models deployed in agentic workflows must follow an instruction hierarchy: when instructions from different sources conflict, the model should obey the highest-privilege applicable instruction. Existing benchmarks largely measure this behavior end-to-end, asking whether the final response is compliant. However, a non-compliant response can arise from several distinct failures: the model may fail to identify the relevant instructions in context, fail to resolve conflicts among identified instructions, or correctly resolve the conflict in its reasoning while still producing a violating response. We introduce a white-box diagnostic framework that localizes instruction hierarchy failures into instruction identification, conflict resolution, and response realization, making failures more interpretable. We evaluate three reasoning models--Gemma-4-31B-IT, Qwen3.6-35B-A3B, and Claude Sonnet 4.6--on long-context adaptations of IHEval and IHChallenge, and find that the dominant failure mode varies across models, tasks, and context length. Building on the observation that models can often detect conflicts and output violations when explicitly prompted, we propose two training-free self-monitoring mechanisms: a parallel input monitor for low-latency conflict detection before generation, and a sequential output monitor for response-level review and repair. Across Gemma-4-31B-IT, Claude Sonnet 4.6, and GPT-5.3, the strongest monitor reduces rule-following non-compliance by 81-99%, with GPT-5.3 reductions of 86% under static attacks and 45% under adaptive attacks.

---


### 75. [SLMJury: Can Small Language Models Judge as Well as Large Ones?](https://arxiv.org/abs/2606.07810)

**<font color=#1a73e8>作者：</font>** Anish Laddha, Nitesh Pradhan, Gaurav Srivastava  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are widely used as judges for evaluating model outputs, but their high cost, latency, and opacity limit scalability. We introduce SLMJury, a framework for evaluating small language models (SLMs) as judges across two paradigms: closed-ended binary correctness and open-ended quality scoring. We benchmark 16 SLM judges (0.6B-14B parameters) from four model families across ten benchmarks: eight closed-ended tasks spanning mathematical, scientific, and general reasoning (N=64,824 judgments per configuration), plus SummEval and MT-Bench for summarization and conversational scoring. We formalize judging as a budget-conditioned function and study five dimensions. Four findings emerge. (1) The overthinking effect is domain-dependent: for most judges quick 10-token verdicts match or beat extended reasoning on mathematical judging (by 2-7% where they help), while reasoning wins on general tasks by up to 23%. (2) Domain generalization separates model families, with math-to-general accuracy gaps ranging from under 10% to nearly 40%. (3) Closed-ended and open-ended judging draw on different capabilities: the best binary judge (Phi-4) drops to rank 9 on MT-Bench, while reasoning-trained models invert this ordering. (4) Under the Reflect-Critique-Refine (RCR) debate protocol, multi-agent debate degrades accuracy across all tested configurations, whereas the top judges resist six adversarial personas with <=0.55% variance. Reliable automated evaluation does not require large proprietary models, yet no single SLM dominates. The leaderboard is available at this https URL, and our framework code and pip package are publicly available at this https URL and this https URL.

---


### 76. [Joint Structural Pruning and Mixed-Precision Quantization for LLM Compression](https://arxiv.org/abs/2606.07819)

**<font color=#1a73e8>作者：</font>** Hoang-Loc La, Truong-Thanh Le, Amir Taherkordi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recently, the efficiency of Large Language Models (LLMs) deployment has become a critical concern in practical applications. While post-training quantization (PTQ) and structural pruning are established techniques for reducing memory footprint and inference latency, most existing PTQ approaches optimize quantization errors on a per-layer basis, overlooking how errors accumulate and propagate through the network, often resulting in suboptimal solutions. Traditional pipelines also tend to apply pruning and quantization in isolation or sequentially, further compounding sub-optimality. We introduce a novel end-to-end framework that addresses these limitations in two key ways. First, we propose a novel mixed-precision PTQ strategy that directly minimizes global error propagation across the entire model, rather than isolating layer-wise errors. Building on this, we develop a novel joint optimization approach that simultaneously learns structural pruning decisions and mixed-precision quantization policies within a unified search space. Extensive experiments show that, at ultra-low precisions (1-3 bits), our quantization method reduces WikiText perplexity by up to 21% compared to state-of-the-art (SoTA) weight-activation quantization baselines. Against leading weight-only quantization methods, it achieves up to 59% and 85% lower perplexity on WikiText and C4, respectively. Compared to the SoTA joint pruning-and-quantization techniques, our proposed method delivers superior perplexity and reasoning performance at ultra-low bits.

---


### 77. [The ACUTE Protocol: Operationalizing Language Model Activations for Better Calibration, Utility, and Trust](https://arxiv.org/abs/2606.07822)

**<font color=#1a73e8>作者：</font>** Nishant Subramani, Palash Goyal, Yiwen Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As language models improve and become increasingly deployed to solve a variety of tasks, trustworthiness becomes essential. Calibration is a good proxy for trust: well-calibrated confidence estimates help inform the risk versus reward tradeoff when trusting a specific model output. Unfortunately, even as models improve, they remain poorly calibrated, often biasing towards overconfidence. Additionally, calibration can be gamed: a policy that always predicts the base rate is perfectly calibrated, but completely uninformative. To resolve this, we develop a new metric, expected utility renormalized by the oracle (EURO), that balances calibration and informativeness. We also propose a general-purpose activation-based confidence, utility, and trust estimation protocol (ACUTE) to appropriately adjudicate uncertainty. The ACUTE protocol provides flexible, sample-efficient, and compute-efficient confidence estimators for 3 tasks including multiple choice question answering, tool-calling, and scientific document summarization across 6 models from 4 model families. ACUTE outperforms strong baselines on EURO, while maintaining low calibration error. Taken together, our work shows that equipping LLMs with the ACUTE protocol can improve calibration, utility, and trustworthiness in numerous settings.

---


### 78. [Does Persona Make LLMs K-pop Fans? A Pilot Study of LLM-Based Online Concert Audience Agents](https://arxiv.org/abs/2606.07837)

**<font color=#1a73e8>作者：</font>** Kirak Kim, Hyojin Kim, Yejin Son 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> A concert is a collective experience, but recorded performance videos are typically watched alone, stripping away the shared audience presence that makes concerts feel eventful. We investigate whether persona-based LLM audience agents can recreate aspects of this collective experience by generating real-time fan chat alongside a K-pop performance video. We present a multi-agent system in which ten LLM agents react through live-chat messages, comparing a persona-conditioned audience (each agent assigned a distinct fan identity, bias, and chat style) with a no-persona baseline. In a within-subjects pilot with K-pop fans (N=11), persona conditioning substantially improved model-level chat quality and perceived naturalness, but did not translate into differences in social connectedness, engagement, or affective response. Interviews suggest that online K-pop concert chat may operate as collective monologue rather than interpersonal dialogue, and that meaningful participation depends on shared identification with the specific artist and fandom. Persona conditioning can make LLM audiences appear more natural, but culturally meaningful collective experience may require deeper alignment between persona, crowd behavior, fandom identity, and user expectations.

---


### 79. [GRPO Does Not Close the Multi-Agent Coordination Gap](https://arxiv.org/abs/2606.07845)

**<font color=#1a73e8>作者：</font>** Najmul Hasan, Prashanth BusiReddyGari  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We measure how well current large language models coordinate as multiple agents sharing a common resource, using the dining philosophers problem as a clean test bed. Across 630 episodes spanning seven models and three philosopher counts, four frontier closed-source systems reach mean reward 0.45 to 0.87 and Mistral-Small 24B reaches 0.83 to 0.99, while Qwen3-14B reaches 0.13 to 0.35. We then ask whether group relative policy optimization (GRPO) on rollouts from the task itself can close the gap and find that it cannot: a Welch's t-test on per-episode reward at five philosophers gives p = 0.66 and a Hedges' g of -0.11, with no statistically significant change at ten or fifteen philosophers either. Two further observations qualify the result. The training reward of both 8B and 14B runs peaked at step nine and then declined, so the default saved checkpoint at step 15 is strictly worse than several earlier ones. The four-term reward we use admits a degenerate maximum at zero actions, which DeepSeek-R1-Distill-Qwen-7B and Mistral-Small 24B at five philosophers both inhabit, with mean reward 1.0 and 0.83 respectively at zero meals. The bottleneck for an open-weight 14B model on multi-agent coordination is not training compute but training methodology: reward shaping that does not collapse to a no-action maximum, checkpoint discipline that does not depend on the final step, and curriculum across problem scales.

---


### 80. [Beyond English benchmarks: clinical llm evaluation in Brazilian Portuguese](https://arxiv.org/abs/2606.07853)

**<font color=#1a73e8>作者：</font>** Giordano de Pinho Souza, Glaucia Melo, Josefino Cabral Melo Lima 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models are transforming the support for clinical decision and their application in real scenarios. Yet, most benchmarks are conducted in English, and cross-lingual evaluation is needed to tackle the language gaps in global access. We introduce ClinicalBr, the first bilingual benchmark for clinical decision built from real Brazilian case reports. The corpus contains 2,892 cases drawn from 28 SciELO medical journals, spanning 18 specialties, and is structured as parallel Portuguese-English pairs. Each case supports four evaluation tasks: diagnosis retrieval, differential diagnosis, exam recommendation, and treatment planning. We evaluate four models: MedGemma-27B, Sabiá-4, DeepSeek-R1, and o3-mini, across both languages. The central finding is that the Portuguese-English performance gap is task-dependent, not general. In diagnosis retrieval, English yields a consistent advantage across all models, with +7.5-12.1 accuracy points. This advantage disappears in differential diagnosis, exam recommendation, and treatment planning, where confidence intervals cross zero for most models and Portuguese completeness scores are marginally higher. Brazilian-endemic conditions proved easier than the full corpus, not harder, indicating that tropical presentations are adequately represented in current pre-training. Exam recommendation was the hardest task across all models and both languages, with F1 scores below 0.10, well below the differential diagnosis ceiling of 0.20-0.27.

---


### 81. [The Last Visible Pixel: Probing Fine-Scale Perception in Vision-Language Models](https://arxiv.org/abs/2606.07861)

**<font color=#1a73e8>作者：</font>** Lujun Li, Lama Sleem, Niccolo Gentile 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent vision-language models (VLMs) excel at multimodal understanding and reasoning, yet their fine-grained visual perception remains underexplored. A natural extension of ``How many r are there in Strawberry?'' asks: how small a visual pattern can a VLM reliably perceive? As such, we introduce FineSightBench, a new benchmark that systematically probes this limit by separating perception tasks (pixel-level recognition of letters, shapes, objects) from reasoning tasks (spatial reasoning, counting, ordering over small targets) across controlled scales of 4--48px. Through comprehensive experiments and detailed failure mode analysis on state-of-the-art models, we reveal a sharp dissociation: perception saturates around 12px, while reasoning remains limited even at larger scales, with persistent numeracy and sequence errors. These findings expose fundamental deficiencies in VLMs' fine-scale visual reasoning that demand more rigorous evaluation.

---


### 82. [The Cold-Start Safety Gap in LLM Agents](https://arxiv.org/abs/2606.07867)

**<font color=#1a73e8>作者：</font>** Chung-En Sun, Linbo Liu, Tsui-Wei Weng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Are tool-calling LLM agents equally safe throughout a conversation? We discover they are not: agents are most vulnerable at the very start of a session and become substantially safer after a few regular agentic tasks -- a phenomenon we term the cold-start safety gap. To study this systematically, we introduce Safety Over Depth for Agents (SODA), a benchmark that controls how many regular agentic tasks the agent completes before encountering a safety threat, supporting up to 20 preceding tasks. Evaluating 7 models from 4 families, safety improves by 9--52% as the number of preceding regular agentic tasks increases from zero to twenty. Representation analysis confirms that model hidden states gradually shift toward a safety-aligned region as more preceding tasks are present. By systematically studying which part of the preceding conversation matters most, we find that the regular agentic tasks themselves are the primary driver of safety, while the agent's own prior responses have less effect on safety but are essential for preserving later utility. This conclusion is further supported by evaluation on open-source safety benchmarks (AgentHarm, Agent Safety Bench) and utility benchmarks (BFCL, API-Bank), confirming that warming up the agent with regular agentic tasks before deployment makes it safer and preserves full capability. Based on these findings, we recommend a simple deployment strategy: having the agent complete a few regular agentic tasks before possible exposure to safety-critical requests mitigates the cold-start safety gap. Our code is available at this https URL

---


### 83. [VisualFLIP: Do Predictions Depend on Task-Critical Visual Evidence in Multimodal Reasoning?](https://arxiv.org/abs/2606.07872)

**<font color=#1a73e8>作者：</font>** Didi Zhu, Changrui Chen, Stefanos Zafeiriou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When a multimodal large language model answers a visual reasoning question correctly, is the prediction actually supported by the task-critical visual evidence? Correct answers can coexist with flawed reasoning, making accuracy alone an incomplete test of grounding. We introduce VisualFLIP, a paired benchmark with 1,374 images arranged as same-question perturbation pairs across cardinality, attribute, spatial, and logic tasks. Each pair keeps the question fixed but minimally changes the evidence so the gold answer deterministically flips. We evaluate 24 MLLMs with pair accuracy, which requires solving both sides of a pair, and Collapse Rate (CR), which measures how often a model that solves at least one side repeats the same non-empty answer for both images. Together, these metrics show that paired correctness and evidence dependence are related but distinct: capable models can still fail to update after task-critical visual changes, and collapse becomes more severe for some models when the edited image follows an earlier answer in a sequential setting. Further details are available on our project page: this https URL

---


### 84. [Safety is Contextual, LLM-Judges Are Not: Navigating the Rigid Priors of Evaluators](https://arxiv.org/abs/2606.07874)

**<font color=#1a73e8>作者：</font>** Anissa Alloula, Federico Licini, Ava Batchkala 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs-as-judges are the only way to evaluate safety at scale. Despite their importance, LLM-judges themselves are rarely evaluated beyond human agreement in simple, static benchmarks. We therefore investigate two under-explored but crucial properties of LLMs-as-judges: their susceptibility to relying on in context-information, and their steerability to differing safety definitions, which may not align with their internal safety priors. We evaluate the safety judging abilities of many generalist LLMs and safety-specific judges, and investigate the impact of task demonstrations, novel in-context information, and changing safety definitions. We find that while LLM-judges can learn from new information, they are broadly unlikely to adjust their evaluations if the context or safety definition contradicts their prior.

---


### 85. [Whose Norms? Disentangling Cultural and Personal Alignment in Large Language Models](https://arxiv.org/abs/2606.07877)

**<font color=#1a73e8>作者：</font>** Angana Borah, Isabelle Augenstein, Rada Mihalcea  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used for social decision-making situations that require balancing cultural norms with personal preferences. For example, a user preferring honesty might ask whether to correct a coworker publicly when local norms favor indirect feedback. Yet existing research studies cultural alignment and personalization largely separately. We introduce PACT, the Personal-Preference and Cultural-Norm Trade-off framework, which evaluates whether models choose to follow a cultural norm or allow personal preferences. We find that LLMs vary in how rigidly they enforce cultural norms, with behavior shifted more by country context (7.8%) than age (1%) and gender (0.7%) and shifting non-uniformly after instruction tuning. Furthermore, our five-country human study on PACT shows that culture-following in humans is mainly driven by scenario country, with the lowest agreement when participants judge their own cultural contexts, showing within-culture pluralism. Finally, human-LLM alignment experiments show that models can match majority choices, but fail to capture response distributions and uncertainty (with best correlations reaching only 0.24). Together, these findings motivate alignment evaluations that go beyond majority to capture cultural pluralism and disagreement in social judgment.

---


### 86. [Temporal Coverage over Density: Parsimonious Training-Set Design for ML Climate Downscaling](https://arxiv.org/abs/2606.07898)

**<font color=#1a73e8>作者：</font>** Karandeep Singh, Stefan Rahimi, Chad W. Thackeray 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-resolution regional climate simulations provide critical information for climate impacts assessments but remain computationally expensive, motivating the development of machine-learning downscalers and emulators. A key challenge is determining how limited high-resolution simulations should be distributed across a changing climate trajectory to capture both forced climate response and internal variability. Using the CESM2 Large Ensemble over the western United States, we compare three training-year selection strategies under fixed data budgets: a contiguous block of historical years, years drawn from both the beginning and end of the simulation period, and years distributed throughout the full climate trajectory. Including both historical and future years consistently outperforms training on historical years alone, demonstrating the importance of exposing downscaling models to climate states outside the historical record and highlighting limitations of stationarity assumptions common in statistical downscaling. Training on years distributed throughout the full climate trajectory performs best overall, indicating that broad sampling of internal variability provides additional information beyond exposure to the forced climate response alone. Models trained on temporally distributed subsets more successfully reproduce variability in unseen ensemble members while retaining strong performance across a wide range of climate diagnostics. Even when trained on only one-tenth of the available high-resolution years, temporally distributed models remain highly competitive with full-data training. These results suggest that, under fixed computational budgets, broad sampling of climate states is more valuable than temporal continuity when allocating scarce high-resolution simulations. The findings provide practical guidance for regional climate downscaling and large-ensemble projection workflows.

---


### 87. [Contract2Tool: Learning Preconditions and Effects for Reliable Tool-Augmented LLM Agents](https://arxiv.org/abs/2606.07904)

**<font color=#1a73e8>作者：</font>** Rahul Suresh Babu, Laxmipriya Ganesh Iyer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-augmented large language model agents increasingly rely on external APIs, but standard tool schemas describe how to call a tool, not when the tool is causally appropriate or what task state it produces. Causal tool filtering addresses this gap by using lightweight contracts that specify each tool's preconditions, effects, risk level, and cost. However, manually writing and maintaining such contracts does not scale to large or changing tool ecosystems. We introduce Contract2Tool, a framework for inferring tool contracts from metadata, schemas, documentation, and execution traces. Contract2Tool converts observable tool evidence into normalized symbolic contracts that can be evaluated intrinsically and deployed inside downstream causal tool filtering. We evaluate learned contracts against gold preconditions, effects, and risk labels, and measure their downstream utility on multi-step agent tasks. Our results show that hybrid documentation-and-trace evidence produces contracts accurate enough to preserve most of the reliability and efficiency benefits of gold contracts. Learned-contract CMTF achieves 0.980 downstream success, close to 0.990 for gold-contract CMTF, while reducing visible tools from 100 to 1 and reducing average token usage from 26,172 to 2,528 relative to all-tools exposure. These results suggest that learned contracts can provide a scalable contract layer between tool schemas and reliable agent execution.

---


### 88. [MemToolAgent overview with a simple restaurant booking scenario where the agent retrieves similar memories, receives feedback on an invalid time format, and generates a reflection to update its memory](https://arxiv.org/abs/2606.07909)

**<font color=#1a73e8>作者：</font>** Suleyman Armagan Er, Danilo Ribeiro, Yogesh Virkar 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern large language model (LLM) agents can use external tools to help users solve complex tasks. However, for problems that require learning from long-term historical events or from previous agent-environment interactions, LLM agents are required to use memory mechanisms to store and retrieve experiences. While sophisticated memory systems exist for dialogue agents, few studies have empirically examined how to improve agents' tool-using capabilities through past user-agent conversations. We propose MemToolAgent, a framework that improves tool use through memory management. Our approach contains a memory extraction module that processes past experiences into structured memory entries, and a retrieval module that dynamically selects a subset of the stored memory entries. This enables more personalized and accurate responses aligned with user preferences and feedback without requiring LLM fine-tuning. In summary, this work has three main contributions: (1) a unified memory entry format that improves both general-purpose and personalized tool use without LLM fine-tuning, (2) a reflection-based memory extraction that uses environment and user feedback to distill wrong executions into critiques to store, and (3) a retrieval module that chooses how many past experiences to use based on the memory similarity distribution. MemToolAgent achieves 29%, 80%, and 17% relative improvements compared to strong baselines on the WorkBench, NESTFUL, and PEToolBench benchmarks, respectively.

---


### 89. [Decoupling Semantics and Logic: A Training-Free Coarse-to-Fine Pipeline for Video Retrieval-Augmented Generation](https://arxiv.org/abs/2606.07924)

**<font color=#1a73e8>作者：</font>** Jiaxin Dai, Zehang Wei, Jiamin Yan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents our system description for the 2nd Workshop on Multimodal Augmented Generation via MultimodAl Retrieval (MAGMaR). Addressing the critical challenges of cross-lingual long-video comprehension, strict persona adherence, and zero-hallucination temporal grounding, we propose a fully training-free, two-stage cascaded Video RAG pipeline. Our architecture strategically decouples semantic retrieval from cognitive logical reasoning through a modality-aware division of labor. In the first stage, a high-recall semantic pre-fetching module employs dense retrieval using only high-fidelity visual summaries and global text descriptions, explicitly isolating noisy modalities (e.g., OCR and ASR) to maintain a pristine vector space. In the second stage, an Adaptive, Iterative, and Reasoning-based (A.I.R.) filtering agent, powered by a commercial Large Language Model (LLM), performs fine-grained cognitive reranking. The agent re-incorporates full multimodal contexts to enforce strict logical alignment with user personas, effectively pruning semantically similar but logically irrelevant candidates. Finally, a Prompt Sculpting mechanism constrains the generator to synthesize the distilled subset into strictly formatted JSON responses with exact chunk-level citations. Evaluated on the RAG track, our resource-aware approach shows exceptional precision in both information retrieval and persona-conditioned generation.

---


### 90. [ROSUM-MCTS: Monte Carlo Tree Search-Inspired HDL Code Summarization with Structural Rewards](https://arxiv.org/abs/2606.07925)

**<font color=#1a73e8>作者：</font>** Prashanth Vijayaraghavan, Charles Mackin, Luyao Shi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown promise in code summarization, yet their effectiveness for Hardware Description Languages (HDLs) like VHDL and Verilog remains underexplored. We propose ROSUM-MCTS, an LLM-guided approach inspired by Monte Carlo Tree Search (MCTS) that refines summaries through structured exploration and reinforcement-driven optimization. Our method integrates both local and global context via a hierarchical candidate expansion mechanism and optimizes summaries using a composite reward function balancing functional correctness (FC), local content adequacy (LCA), and fluency. We evaluate ROSUM-MCTS on the VHDL-eval and Verilog-eval datasets, demonstrating its consistent outperformance over baseline methods by leveraging structured bottom-up refinement and reinforcement-based optimization. Ablation studies confirm the necessity of both local and global expansion strategies, as well as the importance of balancing FC and LCA for optimal performance. Furthermore, ROSUM-MCTS proves robust against superficial modifications, such as variable renaming, maintaining summary quality where baselines degrade. These results establish ROSUM-MCTS as an effective and robust HDL summarization framework, paving the way for further research into reinforcement-enhanced code summarization.

---


### 91. [Stress-testing medical large language models reveals latent safety pathology beyond benchmark accuracy](https://arxiv.org/abs/2606.07929)

**<font color=#1a73e8>作者：</font>** Yuan Shen, Xiaojun Wu, Linghua Yu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are entering clinical practice based on benchmark accuracy that may fail to detect safety-relevant failure modes. Here we present AI-MASLD, a stress-audit framework that adapts the logic of metabolic stress testing from hepatology to the evaluation of clinical LLMs. Using 240 clinical cases across six narrative perturbation probes, we subjected seven models to double-stress testing and quantified performance through three indices: metabolic index (MI), perturbation flip rate (PFR), and counterfactual fairness index (CFI). Under clean baseline conditions, all models performed uniformly well. Under realistic narrative stress, performance diverged sharply, revealing two distinct stress-response phenotypes. Quantized models exhibited pseudonormalization, in which low flip rates hid functional collapse. Medical supervised fine-tuning systematically degraded logical stability, fairness, and information extraction. An open-weight model matched or exceeded proprietary alternatives on every safety dimension. These findings establish narrative stress auditing as a necessary complement to accuracy-based evaluation.

---


### 92. [The Easy, the Hard, and the Learnable: Confidence and Difficulty-Adaptive Policy Optimization for LLM Reasoning](https://arxiv.org/abs/2606.07950)

**<font color=#1a73e8>作者：</font>** Zhanke Zhou, Xiangyu Lu, Chentao Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> RL with verifiable rewards can substantially improve LLM reasoning, yet standard GRPO-style training often treats easy, hard, and learnable questions alike through uniform sampling and weighting, leading to inefficient compute allocation. We study GRPO by tracking token log-probabilities, group-normalized advantages, and the induced token-level update weights. This reveals three recurring dynamics as training proceeds: (1) confidence inflation, (2) advantage contraction, and (3) hierarchical convergence. These findings suggest that the utility of each update depends strongly on both question difficulty and the model's current competence. Motivated by this, we propose Confidence and Difficulty-adaptive Policy Optimization (CoDaPO), which assigns each question a bounded value from rollout confidence and empirical difficulty. CoDaPO then uses this value to reweight policy updates and resample high-value learnable questions within mini-batches, thereby increasing discovery within the learnable band under a fixed compute budget. Across twelve benchmarks, CoDaPO consistently improves accuracy over existing RL methods. Our code is publicly available at this https URL.

---


### 93. [From `May' to `Is': Certainty Distortion in Language Model Rewriting](https://arxiv.org/abs/2606.07951)

**<font color=#1a73e8>作者：</font>** Catarina G Belem, Shang Wu, Hongyu Yao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Humans increasingly turn to Language Models (LMs) in ways that shape beliefs and drive decisions, including discussing, rewriting, and summarizing information from scientific articles, news, and medical reports. However, in these domains, where how confidently a claim is expressed matters, little is known about whether LMs faithfully preserve it. In this work, we investigate certainty distortion in LMs, defined as meaningful changes in expressed certainty when semantic content is preserved. We propose an LM-based evaluation metric that is consistent with population-level judgments of certainty. Using this metric, we characterize certainty distortion across different sizes and families of models in the context of scientific and medical communication tasks. Our results show that certainty distortion affects up to 75\% of LM outputs and is systematically asymmetric in rewriting tasks with most LMs being 1.5-2$\times$ more likely to increase the expressed certainty than to decrease it. These effects can compound over repeated paraphrasing: in the medical domain, claude-haiku-4-5 increases certainty of 20\% examples after a single iteration, increasing to 40\% after five iterations. Prompt-based interventions reduce overall certainty distortion but do not eliminate it. Together, these findings reveal a general bias toward inflating expressed certainty, with direct implications for users who rely on LMs in high-stakes domains.

---


### 94. [Unification of Closed-Open Industrial Detection Scenarios: New Large-Scale Benchmarks,Challenges and Baselines](https://arxiv.org/abs/2606.07953)

**<font color=#1a73e8>作者：</font>** Zekai Zhang, Jinglin Zhang, Qinghui Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large-scale Visual-Language Models (LVLMs) have achieved remarkable success in natural visual tasks, yet their application to industrial defect detection remains challenging due to two fundamental limitations: (i) the scarcity of large-scale industrial datasets that cover diverse defect categories across multiple domains, and (ii) the reliance on manual prompts (points, boxes, masks) that introduce subjective noise and lack text-visual interaction for fine-grained understanding. To address these challenges, we introduce a Large-Scale Multi-Modal Industrial Open-Closed benchmark (MMIOC-1M) containing over one million samples across $14$ super-categories, $29$ industrial scenes, and $351$ defect subcategories. To our knowledge, MMIOC-1M is the first unified largest benchmark supporting both open-vocabulary and closed-set industrial detection, providing valuable pre-training data for LVLMs in industrial scenarios. Furthermore, we propose a Refined Text-Visual Prompt Network (RTVPNet) that incorporates three key innovations: (1) an expert-assisted domain projection mechanism that enables rapid adaptation of general vision models to industrial domains, (2) an energy-based sparse sampling strategy that automatically generates refined visual prompts without manual intervention, and (3) a bidirectional text-visual interaction module that enhances cross-modal semantic alignment and understanding. Extensive experiments demonstrate that RTVPNet achieves state-of-the-art performance on MMIOC-1M, LVIS, and COCO benchmarks while maintaining computational efficiency. The dataset and code are available at this https URL.

---


### 95. [Minibatch Selection via Partition Matroid Constrained Gradient Matching](https://arxiv.org/abs/2606.07954)

**<font color=#1a73e8>作者：</font>** Prayas Agrawal, Prateek Chanda, Ishita Khatri 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training large language models (LLMs) on heterogeneous data requires selecting minibatches that balance convergence speed with coverage across domains. Existing methods either select samples independently within each domain or rely on computationally expensive proxy models to learn continuous domain weights. We propose PartitionSel, a cross-domain minibatch selection approach that maximizes a validation-guided gradient-matching utility under per-domain budgets encoded as a partition-matroid constraint. By coupling the per-domain budgets through a single utility, PartitionSel is designed to reduce redundancy in selections across domains. The proposed objective is weakly submodular and admits an orthogonal matching pursuit algorithm with provable approximation guarantees. Empirically, we evaluate PartitionSel for minibatch selection during the fine-tuning of Qwen2.5 and Llama-3 on MetaMathQA and Mol-Instructions. PartitionSel achieves robust gains over per-domain and domain-agnostic baselines on both benchmarks. It also reduces the number of conflicting gradient pairs within each batch, indicating that the cross-domain coupling translates into more compatible training updates.

---


### 96. [ChronoPhyBench: Do MLLMs Truly Understand the World or Merely Exploit Language Priors?](https://arxiv.org/abs/2606.07962)

**<font color=#1a73e8>作者：</font>** Bin Zhu, Yanhao Jia, Kexin Zhao 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in Multimodal Large Language Models (MLLMs) have demonstrated remarkable proficiency in open-world reasoning and understanding. However, a critical ambiguity persists: it remains unclear whether these models genuinely synthesize cross-modal information to construct physically grounded reasoning chains, or if they merely exploit strong language priors to mask single-modality reliance, thereby hallucinating advanced multimodal capabilities. Motivated by this, and to rigorously mitigate language modality bias and shortcuts, we propose a novel multimodal Chrono}logical Physical Dynamics Reasoning Benchmark ChronoPhyBench, which unifies next state prediction with Visual Question Answering (VQA) paradigms by conditioning on historical video context and textual captions to enforce models to deduce subsequent physical states through both single image selection and the inherently more complex task of multiple frame chronological sorting. Concurrently, we construct a large-scale multimodal reasoning dataset curated using the ChronoPhyBench criteria, comprising over 10,000 long-form videos paired with meticulously annotated captions, totaling 5M tokens. Our experimental evaluations reveal a stark contrast to conclusions drawn by previous benchmarks. The capacity of current open-source models to perform physically grounded multimodal reasoning remains in its infancy. Ultimately, this work seeks to systematically stress-test the reasoning capabilities of multimodal models, quantify hallucination rates, and advance the development of Physical AI, thereby providing the community with a robust and transparent evaluation framework toward Artificial General Intelligence (AGI).

---


### 97. [Shared Latent Structures Enable Unified Backdoor Detection and Mitigation in LLMs](https://arxiv.org/abs/2606.07963)

**<font color=#1a73e8>作者：</font>** Omar Mahmoud, Aly M. Kassem, Thommen George Karimpanal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Backdoor attacks in large language models (LLMs) are often treated as isolated trigger-response failures, motivating defenses tailored to specific triggers or behaviors. We show this view is incomplete. Across diverse backdoor behaviors, we identify a shared latent mechanism that can be detected, causally controlled, and suppressed. Using sparse autoencoders (SAEs) on residual-stream activations, we find a small set of latent features consistently activated across jailbreaking, refusal manipulation, password-locking, bias induction, sentiment misclassification, and country-conditioned harmful advice. These features generalize across Qwen3, Gemma~3, and Llama~3.1 models from 4B to 32B parameters, and across both fine-tuning and weight-editing attacks. Through bidirectional activation steering, we show these features are causal: suppressing them reduces attack success, while amplifying them induces target behaviors on clean prompts. We further train lightweight SAE-feature classifiers that generalize zero-shot to unseen backdoors and outperform residual-stream and weight-diffing baselines. Finally, we introduce Concept Ablation Fine-Tuning (CAFT), which suppresses backdoor formation by ablating the shared latent subspace during training. Together, our results suggest that many backdoors rely on a transferable latent mechanism, enabling unified detection and mitigation.

---


### 98. [DisCo: World Models with Discrete Camera Motion Control](https://arxiv.org/abs/2606.07967)

**<font color=#1a73e8>作者：</font>** Hongrui Huang, Junke Wang, Quanhao Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controllable video world models target interactive world exploration, where models must faithfully execute explicit action commands while preserving visual quality and temporal coherence. However, most existing approaches rely on continuous camera trajectories as action conditions, which often lead to unreliable action following, especially under complex motion sequences. In this work, we identify action representation entanglement as a key bottleneck in controllable video generation, and show that continuous camera representations lead to high feature similarity across distinct motion patterns, degrading action controllability. Based on this insight, we propose DisCo, a controllable video world model that conditions generation on a compact set of discrete action primitives to improve action separability. We further introduce DisCoBench, a comprehensive benchmark for evaluating the ability of models in short-term, long-horizon, and highly dynamic exploration scenarios. Extensive experiments demonstrate that DisCo achieves significantly more reliable action following while preserving visual quality.

---


### 99. [Neutrality Bites: Gender Representation in AI-Generated Animal Stories](https://arxiv.org/abs/2606.07969)

**<font color=#1a73e8>作者：</font>** Imani Finkley, Yuanxi Li, Melanie Walsh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Gender bias in AI-generated stories is a well-documented problem. While much attention has been paid to reducing or mitigating this bias, it is not always clear whether interventions produce genuinely fairer results. To investigate this issue, we examine how large language models (LLMs) handle gender assignment in a narrative context that is popular, highly ambiguous, and also known to closely reproduce human stereotypes: stories about talking animals. We prompt six leading LLMs to complete an English-language story about seven different anthropomorphic animal characters whose gender is unstated. We additionally iterate with four different narrative settings and a range of model temperatures. Across the 23.8K stories, we find that models frequently avoid gendering the animal character in the story (19% on average) or use gender-neutral language like "it" or "its" (38.2% on average). However, when gender is assigned, there is a significant masculine bias. Feminine animal characters are virtually absent, present in just 2.2% of stories vs. 40.6% that feature masculine characters. Our findings point to a broader argument: neutrality bites. In other words, models that prioritize neutrality to address social bias may actually contribute to the erasure of marginalized perspectives and identities. We suggest that alternative strategies beyond neutrality need to be pursued, such as ones that more equally distribute social possibilities across imagined subjects.

---


### 100. [Defending Against Malicious Finetuning by Scaling Train-time Adversarial Attacks](https://arxiv.org/abs/2606.07970)

**<font color=#1a73e8>作者：</font>** Haoming Wen, Shi Chen, Qingyu Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current open-weight large language models (LLMs) are prone to malicious finetuning attacks, which could compromise the safety alignment of LLMs with only a few steps of supervised finetuning (SFT) on poisoned datasets. Existing alignment-stage defenses are primarily designed to defend against attacks that use parameter-efficient finetuning methods. However, they fail to defend against stronger attacks that use full-parameter finetuning. In this paper, we propose Patcher, a method inspired by adversarial training and bi-level optimization, to combat such attacks. Patcher strengthens the simulated attack by scaling up the optimization steps in the adversarial loop, thus forcing the defender to find model parameters that are insensitive to stronger attacks. Furthermore, we propose an efficient parallel algorithm to implement Patcher, decreasing the wall-clock time of training while preserving Patcher's performance. Extensive experiments show that Patcher substantially improves the model's robustness compared to vanilla SFT alignment, and transfers to diverse attack scenarios and model sizes. Code is available at this https URL.

---


> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-331](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
