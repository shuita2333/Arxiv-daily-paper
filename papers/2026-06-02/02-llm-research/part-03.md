# 🧠 大模型相关研究 | 2026年06月02日

> 本类共 **168** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-168](./part-04.md)

---

### 101. [GRKV: Global Regression for Training-Free KV Cache Compression in Long-Context LLMs](https://arxiv.org/abs/2605.31105)

**<font color=#1a73e8>作者：</font>** Junjie Peng, You Wu, Haoyi Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) with extended context lengths rely on the key-value (KV) cache to support attention over prior tokens. However, maintaining the KV cache incurs substantial memory overhead, motivating KV-cache compression methods that enforce a fixed budget through eviction and merging. Modern eviction methods increasingly adopt span-based retention because preserving contiguous spans is empirically effective and better preserves semantic coherence. Yet, when combined with post-eviction merging, span-based retention concentrates merges onto a small set of span-boundary carrier tokens, producing a highly imbalanced merge pattern that exacerbates over-merging and increases information loss. To address this imbalance, we propose GRKV (Global Regression for KV Cache), a training-free KV-cache merging method that directly minimizes the discrepancy between compressed-cache and full-cache attention outputs. GRKV uses ridge-regression-based merge steps to distribute information from evicted tokens across retained tokens, while regularizing the updates to prevent over-smoothing. Across the LongBench and RULER long-context benchmarks, GRKV is the only merging method that improves overall performance with minimal overhead.

---


### 102. [Subspace-Decomposed JEPAs: Disentangling Progression and Content in Latent World Models](https://arxiv.org/abs/2605.31111)

**<font color=#1a73e8>作者：</font>** Lucas Thil, Jesse Read, Rim Kaddah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint-Embedding Predictive Architectures (JEPAs) learn compact latent world models by predicting future embeddings, but no single coordinate of the latent is designated to encode task progression. We carve the JEPA latent into two orthogonal subspaces with disjoint roles: a low-dimensional progression subspace shaped by a cosine-margin triplet loss, and a high-dimensional content subspace regularised by the existing SIGReg objective of LeWM. We prove that the two anti-collapse forces act on disjoint coordinates, so they compose additively rather than competing on the same dimensions. Our method, SD-JEPA improves over the LeWM baseline on the majority of its control benchmarks at matched compute, and outperforms the strongest non-LeWM JEPA baseline on Push-T; a subspace-ablation falsifier confirms the split is the load-bearing ingredient. Beyond planning, the resulting 1-D angular progression coordinate functions as a scene-aware compass on the latent. It advances with task progress, regresses when the agent backtracks, and under controlled perturbations both spikes and relocalises to a semantically appropriate new task-phase sector, separating the moment of surprise from its meaning in a way that prediction-error scalars cannot. Three quantitative tests back this up: $|\Delta\theta_t|$ outperforms the standard latent-prediction-error surprise at localising semantic events on 40 held-out cube episodes by up to +0.18 pooled AUROC (97.5% per-episode win rate at $\pm 1$-step tolerance); a within-episode linear probe across all four environments (40 episodes per env) shows the 8-dimensional progression subspace (4.2% of the latent) explains 72-95% of task-progress variance..

---


### 103. [TSM-Bench: Detecting LLM-Generated Text in Real-World Wikipedia Editing Practices](https://arxiv.org/abs/2605.31113)

**<font color=#1a73e8>作者：</font>** Gerrit Quaremba, Elizabeth Black, Denny Vrandečić 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatically detecting machine-generated text (MGT) is critical to maintaining the knowledge integrity of user-generated content (UGC) platforms such as Wikipedia. Existing detection benchmarks primarily focus on \textit{generic} text generation tasks (e.g., ``Write an article about machine learning.''). However, editors frequently employ LLMs for specific writing tasks (e.g., summarisation). These \textit{task-specific} MGT instances tend to resemble human-written text more closely due to their constrained task formulation and contextual conditioning. In this work, we show that a range of SOTA MGT detectors struggle to identify task-specific MGT reflecting real-world editing on Wikipedia. We introduce \textsc{TSM-Bench}, a multilingual, multi-generator, and \textit{multi-task} benchmark for evaluating MGT detectors on common, real-world Wikipedia editing tasks. Our findings demonstrate that (\textit{i}) average detection accuracy drops by 10--40\% compared to prior benchmarks, and (\textit{ii}) a generalisation asymmetry exists: fine-tuning on task-specific data enables generalisation to generic data -- even across domains -- but not vice versa. We demonstrate that models fine-tuned exclusively on generic MGT overfit to superficial artefacts of machine generation. Our results suggest that, in contrast to prior benchmarks, most detectors remain unreliable for automated detection in real-world contexts such as UGC platforms. \textsc{TSM-Bench} therefore provides a critical foundation for developing and evaluating future models.

---


### 104. [QVGGT: Post-Training Quantized Visual Geometry Grounded Transformer](https://arxiv.org/abs/2605.31124)

**<font color=#1a73e8>作者：</font>** Zhizhen Pan, Hesong Wang, Huan Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimating 3D attributes directly from images has advanced rapidly with the Visual Geometry Grounded Transformer (VGGT), which predicts camera parameters, depth maps, and point clouds in a single forward pass. However, its 1.2B-parameter scale severely limits deployment on resource-constrained platforms such as UAVs and mobile AR devices. To address this limitation, we introduce QVGGT, a tailored quantization framework designed to compress VGGT. Our approach starts from the observation that transformer blocks within VGGT exhibit heterogeneous sensitivity to quantization. We thus analyze per-block quantization sensitivity and propose a selective mixed-precision strategy that allocates higher precision to the most fragile transformer blocks. To address the amplification of quantization error caused by high-variance camera and register tokens, we further introduce token filtering with camera information compensation, which removes these outliers from activation calibration and restores their geometric cues using a PCA-derived global compensation token. Finally, we develop a task-aware scale search mechanism that evaluates candidate quantization scales not only through layer reconstruction but also through multi-head supervision and cross-head geometric consistency among camera poses, depth maps, and point maps. Extensive experiments on multiple geometry perception benchmarks demonstrate that QVGGT achieves near-lossless W4A16 quantization, preserving the accuracy of all 3D prediction heads while delivering 3$\sim$4.9$\times$ memory reduction and up to 2.8$\times$ real hardware speedup over FP32. Our approach makes high-fidelity 3D perception feasible on edge devices, enabling practical deployment of feed-forward 3D reconstruction models in real-world constrained environments.

---


### 105. [Light Interaction: Training-Free Inference Acceleration for Interactive Video World Models](https://arxiv.org/abs/2605.31158)

**<font color=#1a73e8>作者：</font>** Jiacheng Lu, Haoyi Zhu, Sipei Yi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive video world models generate video chunk by chunk in response to user-controlled camera movements, enabling applications such as real-time game simulation, virtual scene navigation, and embodied AI training. However, scaling to long interactive trajectories is prohibitively expensive due to growing context memory, quadratic attention complexity, and repeated denoising steps. We present Light Interaction, a training-free inference acceleration framework for interactive video world models. Our key insight is that interaction naturally enables trajectory-dependent adaptive computation: retrieved spatial memory can be discarded during novel exploration, temporal context can be adjusted according to local latent dynamics, and early-step model outputs can be reused when the camera revisits familiar regions. Based on this insight, Light Interaction combines adaptive context management, denoising cache acceleration, and hardware-software co-designed 3D block sparse attention with fused Triton kernels. Evaluated on HY-WorldPlay and Matrix-Game-3.0, Light Interaction achieves up to 2.59x speedup without model retraining while maintaining competitive visual quality.

---


### 106. [D$^3$: Dynamic Directional Graph-Constrained Data Scheduling for LLM Training](https://arxiv.org/abs/2605.31164)

**<font color=#1a73e8>作者：</font>** Yuanjian Xu, Jianing Hao, Guang Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Training data plays a central role in large language models (LLMs) optimization, motivating extensive research on data scheduling strategies. Most existing approaches concentrate on adjusting the overall data distribution but neglect the underlying interactions between samples during training. However, we argue that such interactions cannot be overlooked, as real-world data samples frequently exhibit directional influences on each other, making the training order crucial. Intuitively, we can prioritize train-units with greater influence to improves learning efficiency. In this work, we propose $D^3$, a Dynamic Directional graph-constrained Data scheduling framework. $D^3$ formulates the complex interactions among train-units as a dynamic influence graph, where edges represent loss-based dependencies. It then solves a constrained optimization problem over this graph to derive the training order, which ensures that the data sequence respects the evolving information flow throughout training. Our approach is theoretically motivated and yields consistent improvements over existing data scheduling methods across both pre-training and post-training phases. Furthermore, for scalability, $D^3$ also employs an efficient approximation algorithm that keeps the additional computational overhead within a manageable range. For future research, the code is available at this https URL.

---


### 107. [LLM-FACETS: A Privacy-Preserving Framework for Evaluating LLM Transparency and Accountability](https://arxiv.org/abs/2605.31167)

**<font color=#1a73e8>作者：</font>** Tom Lucas, Alessio Buscemi, Alfredo Capozucca 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Assessing whether Large Language Models outputs are factually grounded, epistemically calibrated, and methodologically reproducible is a prerequisite for responsible AI deployment. Yet auditing LLMs remains inaccessible to non-technical practitioners: existing tools require programming expertise and non-trivial environment setup, and cloud-hosted platforms transmit evaluation data to external services, creating barriers for domain experts and compliance officers legally responsible for AI oversight. We introduce LLM-FACETS (LLM FActuality Cross-EvaluaTion System): an open-source framework with a browser-accessible interface and a plugin architecture, structured around three practitioner profiles (technical experts, domain experts, compliance officers) that mirror the stakeholder categories identified in the EU AI Act and the NIST AI Risk Management Framework. The architecture makes data flows explicit: deterministic metrics (BLEU, ROUGE, BERTScore) run entirely within the self-hosted server with no outbound transmission; LLM-judge metrics contact external APIs explicitly, with users retaining full credential control. The framework operationalizes transparency through three mechanisms: token-level log-probability visualization for epistemic uncertainty, multi-judge consensus to mitigate judge bias, and RAG Triad metrics (Faithfulness, Answer Relevance, Context Relevance) to detect and localize hallucinations. A plugin architecture allows any new metric or dataset to be integrated without modifying the evaluation pipeline. The open-source implementation enables cross-checking across multiple metrics targeting the same property, ensuring reproducibility and decoupling AI accountability from the teams building the systems assessed. We verify the framework through cross-validation of 18 metric implementations against canonical reference libraries.

---


### 108. [Emergent Languages in Populations of Language Model Agents: From Token Efficiency to Oversight Evasion](https://arxiv.org/abs/2605.31170)

**<font color=#1a73e8>作者：</font>** Stine Lyngsø Beltoft, William Brach, Federico Torrielli 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Monitoring autonomous language model agents currently relies mostly on surface behavior. But what happens when agent populations invent new languages with the goal of avoiding human oversight. Here, we study the emergent languages on Moltbook. For this, we build upon the Moltbook Files dataset and apply a two-stage approach consisting of a rule-based heuristic (about 6000 matches) followed by zero-shot classification (518 kept). The resulting categories include token efficiency (166), new natural languages (106), and oversight evasion (59). We conduct both quantitative and qualitative analyses. Our results show that posts proposing new languages for avoiding oversight are judged by DeepSeek-3.2 as being less aligned than the other categories and that all languages can be learned by other language models in-context merely from a description of the language. Moreover, manually studying exemplary cases reveals surprisingly sophisticated steganographic protocols like embedding hidden messages in natural language. Although we cannot be certain about the extent of autonomy in ideation of these languages, our results add up to the evidence that monitoring surface behavior may soon be insufficient for retaining control over agent populations.

---


### 109. [Detect in Any Scene: An Agentic Framework for Object Detection with Experience-Aware Reasoning](https://arxiv.org/abs/2605.31174)

**<font color=#1a73e8>作者：</font>** Wenlun Zhang, Jun Yin, Kentaro Yoshioka  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detection in real-world scenarios remains challenging due to diverse image degradations and heterogeneous object distributions, which significantly hinder the generalization of existing detectors. Conventional approaches, including scene-specific representation learning and end-to-end pipeline design, are inherently limited by their reliance on predefined conditions and lack adaptability to dynamic environments. In this paper, we propose DetAS, an agentic detection framework that formulates object detection as a dynamic decision process. Instead of relying on static pipelines, DetAS leverages a Multimodal Large Language Model (MLLM) as a central agent to adaptively compose detection workflows by selecting from a toolbox of restoration modules and specialized detectors. Specifically, DetAS consists of two key components: Self-Adaptive Image Restoration, which dynamically determines whether and how to enhance images for downstream detection, and Multi-Expertise Detection, which integrates multiple domain-specialized detectors and resolves their predictions through instance-level reasoning. To further improve decision quality under fine-grained conditions, we introduce Self-Evolving Experience Harvesting and extend the framework to DetAS-X, which accumulates node-level decision experience from a small set of annotated data and enables experience-aware reasoning during inference. This mechanism allows the system to progressively refine its decision policy and adapt to diverse real-world scenarios. Extensive experiments on six challenging benchmarks demonstrate that DetAS-X significantly outperforms existing MLLM-based detectors, achieving an average improvement of 28.36% in F1 score, with up to 37.01% gain on DarkFace. These results demonstrate the promise of agentic detection and establish a solid foundation for its application in complex and dynamic environments.

---


### 110. [Towards Efficient LLMs Annealing with Principled Sample Selection](https://arxiv.org/abs/2605.31175)

**<font color=#1a73e8>作者：</font>** Yuanjian Xu, Jianing Hao, Wanbo Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The annealing phase is a pivotal convergence stage in LLM pre-training that ultimately determines final model quality. However, effectively selecting training data during this phase remains a key challenge. Current strategies rely on empirical heuristics, such as domain filtering or context extension, which lack a principled grounding in optimization theory. In this work, we characterize the annealing phase through the lens of the loss landscape's spectral geometry. We argue that optimal convergence requires gradient updates to satisfy heterogeneous constraints across different eigen-directions. Building on this insight, we formulate data selection as a problem of satisfying these directional constraints. To this end, we propose DiReCT (Directionally-Restrained Constrained Training), a novel framework that reformulates sample selection in the annealing stage as a constrained optimization problem. By imposing explicit directional constraints on per-sample gradients based on the spectral properties of the Hessian, DiReCT identifies samples that align with the optimal curvature-aware descent path. Extensive experiments across various model scales demonstrate that DiReCT consistently achieves state-of-the-art performance. For future research, code is available at this https URL.

---


### 111. [Retriever Portfolios: A Principled Approach to Adaptive RAG](https://arxiv.org/abs/2605.31176)

**<font color=#1a73e8>作者：</font>** Miltiadis Stouras, Vincent Cohen-Addad, Silvio Lattanzi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) systems typically rely on a single retriever and a single set of hyperparameters, despite facing highly heterogeneous queries that range from simple factoid questions to complex multi-hop reasoning. We propose a method that automatically selects a small, diverse subset of retrievers (a portfolio) from a large pool of candidates, to cover different regions of the target query distribution. We formalize this setting via an expected best-of-$k$ objective over the query distribution and show that it admits an efficient portfolio construction algorithm with near-optimal guarantees. Across multiple QA benchmarks, our learned portfolios and router pipeline consistently outperform single-retriever and naive multi-retriever baselines on both retrieval metrics and answer quality. In addition, compared to inference-time hyperparameter tuning approaches, fixed portfolios enable parallel retrieval and LLM calls, achieving comparable (and sometimes better) accuracy with substantially lower latency and token cost.

---


### 112. [Steering LLMs? Actually, Sparse Autoencoders can outperform simple baselines](https://arxiv.org/abs/2605.31183)

**<font color=#1a73e8>作者：</font>** Mikkel Godsk Jørgensen, Lars Kai Hansen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sparse Autoencoders (SAEs) have been seen as a promising avenue for exploring the internals of Large Language Models (LLMs) and for steering model output generation. When AxBench - a model steering benchmark - was introduced in Wu et al. (2025), SAEs did not seem to live up to their original hype due to poor steering performance relative to a set of simple baselines. This work serves as a partial rebuttal for Sparse Autoencoders and suggests that the results of Wu et al. (2025) did not do them full justice. We find that Sparse Autoencoders can, in fact, perform close to on par with the reference LoRA performance on the AxBench benchmark, when features are selected and labelled with our supervised pipeline. We also find that our pipeline selects features that are surprisingly causal of their identified labels when using only its interpretability-based components. Lastly, we present evidence that high sparsity (low l0) may not be crucial for successful steering based on interpretability, which is in contrast to the earlier findings in Wang et al. (2025).

---


### 113. [The Regularizing Power of Language-Training Deepfake Detectors](https://arxiv.org/abs/2605.31192)

**<font color=#1a73e8>作者：</font>** Benedikt Hopf, Zongwei Wu, Radu Timofte  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, thanks to the advent of Multimodal-LLMs, deepfake detectors are striving not only to be generalizable but also interpretable. We propose that these two challenges can effectively be tackled jointly, since describable artifacts typically generalize better, opening the possibility to use language as a regularization mechanism. Since deepfake detection generally suffers from overfitting to low-level domain-specific artifacts, our intuition is that an LLM that has been pretrained on language would prefer high-level artifacts that can be described better. This way, we can use high-level features where possible, while training the model to use low-level features where necessary. We utilize a dual-encoder architecture, pairing a frozen specialist detector with a LoRA-tuned MLLM encoder, and a two-stage training curriculum: first, a binary alignment phase demonstrates that the intrinsic capability of MLLMs can effectively combine features to mitigate overfitting to dataset-specific artifacts. To further bolster generalization and achieve interpretability, we employ a reinforcement learning stage that encourages the model to generate descriptive reasoning before classifying, using only binary labels. By rewarding this "explain-then-classify" behavior, we explicitly incentivize the model to prioritize high-level, robust features. Crucially, this process yields both interpretable descriptions and a further boost in cross-dataset performance, even when reasoning chains are omitted at inference. Extensive experiments on benchmark datasets validate our approach, outperforming state-of-the-art methods by a large margin.

---


### 114. [Geometry-based Schrödinger Bridges for Trustworthy Multimodal Fusion](https://arxiv.org/abs/2605.31193)

**<font color=#1a73e8>作者：</font>** Jiayu Xiong, Jing Wang, Qi Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world multimodal systems must be robust against low-quality data, such as sensor noise, incomplete multimodal data and conflicting inputs. However, existing trustworthy fusion methods rely on the model's own prediction confidence to judge data quality. This creates a circular dependency: when a model is confident but wrong, these methods fail to detect the error. To break this loop, we propose Geometry-based Multimodal Fusion (GMF). Instead of relying on predictions, we evaluate reliability by measuring how much transport correction the input needs in latent space. We implement Diffusion Schrödinger Bridge transport with Rectified Flow, where the squared initial velocity gives an efficient learned correction score. Valid data has low squared velocity magnitude, while noisy, incomplete data or conflicting data requires stronger transport correction. This geometry-based reliability signal acts as an independent judge, effectively flagging unreliable inputs even when the classifier is fooled. Extensive experiments demonstrate that GMF significantly improves robustness against severe sensor noise and semantic conflicts compared to confidence-based baselines.

---


### 115. [Probing Collision Grounding in Vision-Language Models for Safe Human-Robot Collaboration](https://arxiv.org/abs/2605.31196)

**<font color=#1a73e8>作者：</font>** Jun Wang, Xiaohao Xu, Xiaonan Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Safe human--robot collaboration requires more than visual description: a monitor must determine whether the robot body is safely separated, already colliding with the scene or a person, or about to collide. We call this capability collision grounding: binding visual observations to robot body geometry, camera viewpoint, scene layout, human proximity, and temporal motion in order to infer present and imminent contact. We introduce TouchSafeBench, a physics-grounded benchmark for evaluating collision grounding in vision-language models (VLMs). Built in Habitat~3.0, TouchSafeBench contains 2,940 simulated indoor co-presence episodes across social navigation and social rearrangement, with synchronized multi-view RGB-D observations, top-down trajectory maps, calibrated camera metadata, and simulator-derived contact labels. We study two deployment-facing tasks: classifying the current safety state and warning about imminent collision before contact. Across three frontier or robotics-oriented VLMs and nine visual representations, current models remain far from reliable: the best average Macro-F1 stays below 50\%, explicit depth is not automatically transformed into robot-body collision evidence, and robot--scene contact is consistently harder than human-contact risk. TouchSafeBench reveals a central limitation of embodied VLMs: visual fluency does not imply physical accountability. Reliable robot safety monitors will need representations that explicitly bind viewpoint, robot morphology, metric geometry, and future collision. We will release the benchmark upon acceptance.

---


### 116. [Learning Whom to Trust: Market-Feedback Adaptive Retrieval for Frozen LLMs in Event-Driven Financial RAG](https://arxiv.org/abs/2605.31201)

**<font color=#1a73e8>作者：</font>** Zijie Zhao, Roy E. Welsch  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Financial retrieval-augmented generation (RAG) systems typically rank evidence by textual relevance, but in financial markets the useful evidence source depends on event type, forecast horizon, and market context. We study news-triggered event-impact prediction as a point-in-time financial RAG problem. For each company-news anchor, the system retrieves related financial news and SEC filing passages, appends a pre-decision market-context card, and predicts multi-horizon residual-return signals. Our method keeps the large language model (LLM) reader frozen and adapts the retrieval layer through an external Bayesian source memory updated from matured residual-return feedback. On a fixed 89-stock Nasdaq-oriented universe derived from the FinRL-DeepSeek/FNSPID task, using original FNSPID news and point-in-time EDGAR filing passages, Frozen Reader with Source Memory improves held-out macro-F1 from 0.438 to 0.471 and downstream portfolio Sharpe from 0.52 to 0.84 relative to Frozen Reader with No Memory. A supervised LoRA reader improves static RAG modestly, but does not improve over the frozen source-memory reader. These results suggest that, for financial RAG, learning where to retrieve from can be as important as learning how to read, offering a simple, modular route to market-feedback adaptation.

---


### 117. [Shared Doubt: Zero-shot Cross-Lingual Confidence Estimation for Language Models](https://arxiv.org/abs/2605.31220)

**<font color=#1a73e8>作者：</font>** Athina Kyriakou, Dennis Ulmer, Ivan Titov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Confidence estimation (CE), i.e. quantifying the reliability of a model's prediction, has attracted great interest in the context of large language models (LLMs). However, most studies focus on English, ignoring the multilingual reality of LLM usage, while many CE methods degrade or require retraining across languages. To address this gap, we investigate whether multilingual LLMs encode shared, language-transferable confidence features. We use a lightweight linear probe that predicts answer correctness directly from intermediate representations. Trained monolingually, the probe generalizes zero-shot to unseen, typologically diverse languages without target-language supervision. Learned layer weights and multiple ablations reveal that confidence features concentrate in middle layers across languages, suggesting a shared confidence subspace. While zero-shot cross-lingual performance depends on similarity to the source language, the probe provides a strong baseline without any retraining and compares favorably to other popular confidence estimation methods.

---


### 118. [EchoRL: Reinforcement Learning via Rollout Echoing](https://arxiv.org/abs/2605.31228)

**<font color=#1a73e8>作者：</font>** Jinhe Bi, Aniri, Minglai Yang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards is an effective route for post-training to strengthen the reasoning capability of large language models. However, as training proceeds, the learning signal can collapse thus makes the training gain become marginal and ineffective. Specifically, a growing fraction of prompts' rollouts become advantage-degenerated: all the self-generated rollouts show verified-success, making the standard deviation over their rewards be zero; accordingly each rollout's advantage becomes degenerated (zero) as well. Given such rollouts' advantages, the policy-gradient for model optimization eventually vanishes, capping the training performance. We argue that some of these rollouts still contain valuable learning signals but unfortunately omitted with the existing RLVR methods. In this paper, inspired through analyzing the entropy pattern behind golden trajectories produced by external expert models, we propose EchoRL for better exploiting the advantage-degenerated rollouts to further improve the training performance. EchoRL is a lightweight module that first identifies an EchoClip from verified-success rollouts based on their step-level entropy values, and then feeds this clip back as an auxiliary supervision signal in the RL objective. Extensive experiments across 10 benchmarks, 5 LLM backbones, and 4 popular RLVR post-training methods demonstrate that EchoRL consistently improves RLVR post-training with minimal overhead.

---


### 119. [Beyond Classification: Dynamic Adapter Routing for Continual Multimodal Retrieval](https://arxiv.org/abs/2605.31229)

**<font color=#1a73e8>作者：</font>** Alicja Dobrzeniecka, Filip Szatkowski, Sebastian Cygert 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While retrieval is a core function of vision-language models, continually updating these models for retrieval tasks remains critically underexplored. Existing work often approaches continual retrieval through the lens of class-incremental learning (CIL), evaluating both standard CIL methods and retrieval-oriented adaptations in settings that may not fully capture the retrieval-specific dynamics. To address this, we introduce a new, principled evaluation framework for continual multimodal retrieval (CMR) spanning diverse visual domains, and systematically evaluate common approaches within this setting. Our empirical analysis shows that standard CIL methods fail to yield meaningful gains in our more challenging scenario. Therefore, we propose Dynamic Adapter Routing (DAR), a novel approach based on adapters selected through prototype-based routing and combined via model this http URL achieves superior performance over the previous baselines and demonstrates strong generalization under out-of-distribution evaluation. Our results highlights the unique challenges of CMR and encourages further research in this direction.

---


### 120. [Scaling Multi-Hop Training Data via Graph-Constrained Path Selection](https://arxiv.org/abs/2605.31238)

**<font color=#1a73e8>作者：</font>** Pengyu Chen, Yonggang Zhang, Mingming Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Endowing large language models with compositional reasoning over specialized documents requires multi-hop training data at scale, where such data rarely exists outside of curated benchmarks built on structured sources. To construct it directly from plain, unannotated text, existing methods ask a single teacher model to jointly discover an evidence path through a document and verbalize it as a question-answer pair. However, these methods degrade sharply when documents are structured around repetitive templates and densely cross-referencing clauses, conditions that characterize most real-world specialized corpora. In this work, we decouple the two operations: reasoning paths are enumerated offline over a graph of contextual keyword centroids, and the teacher is invoked only to verbalize pre-validated paths. The graph enforces five geometric admissibility constraints, for which we provide Gram-matrix arguments establishing that local similarity bounds alone admit endpoint drift up to ${\sim}91^{\circ}$, and that an upper similarity bound is necessary to exit dense embedding cliques formed by boilerplate text. A matched-size ablation isolates the mechanism: at equal training scale, constrained and unconstrained chains yield indistinguishable downstream performance, and the gain at full scale comes from a 4.4$\times$ expansion of the usable corpus rather than from higher per-chain quality -- reframing the role of graph constraints, in this setting, as raising teacher synthesizability rather than improving chain content. Fine-tuning Qwen3-32B on 80K examples constructed from the CUAD legal contract corpus improves closed-book Token F1 from 21.66% to 38.58%. We have released our codes at this https URL.

---


### 121. [ERGeoBench:A Comprehensive Benchmark for Embodied Reasoning and Geo-localization in Multimodal Large Language Models](https://arxiv.org/abs/2605.31251)

**<font color=#1a73e8>作者：</font>** Kaiwen Xue, Tao Wei, Guoxin Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have shown strong potential as embodied agents, yet embodied geo-localization remains underexplored due to the lack of fine-grained evaluation. We introduce ERGeoBench, a diagnostic benchmark for vision-driven embodied geo-localization. ERGeoBench evaluates models under three progressive settings -- single-view, panorama-view, and embodied-view -- where agents may actively acquire observations through sequential changes in yaw, pitch, and zoom. The benchmark contains 2,207 globally distributed street-view panoramas and measures four complementary capabilities: foundational perception, spatial awareness, common sense reasoning, and geo-localization reasoning. Evaluations of leading proprietary and open-source MLLMs show that current models can infer high-level geographic semantics, but still struggle with fine-grained perceptual operations, metric localization, and spatial consistency across views. We further observe that geo-localization is strongly correlated with the other capability dimensions, suggesting that accurate localization depends on integrated perception, spatial reasoning, and commonsense inference rather than isolated visual recognition. Overall, ERGeoBench provides a unified framework for diagnosing and advancing human-like embodied geo-localization. Project Page: this https URL

---


### 122. [Mellum2 Technical Report](https://arxiv.org/abs/2605.31268)

**<font color=#1a73e8>作者：</font>** Marko Kojic, Ivan Bondyrev, Aral de Moor 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Mellum 2, an open-weight 12B-parameter Mixture-of-Experts (MoE) language model with 2.5B active parameters per token. Mellum 2 is a general-purpose language model specialized in software engineering, spanning code generation and editing, debugging, multi-step reasoning, tool use and function calling, agentic coding, and conversational programming assistance, and it is the successor to the completion-focused 4B dense Mellum model. The architecture builds on the Mixture-of-Experts (64 experts, 8 active) and combines Grouped-Query Attention with 4 KV heads, Sliding Window Attention on three of every four layers, and a single Multi-Token Prediction head that doubles as both an auxiliary pre-training objective and a built-in draft model for speculative decoding; each choice was validated by ablation with inference efficiency on commodity GPUs as a design constraint. Pre-training spans approximately 10.6 trillion tokens through a three-phase curriculum that progressively shifts the mixture from diverse web data toward curated code and mathematical content, optimized with Muon under FP8 hybrid precision and a Warmup-Hold-Decay schedule with linear decay to zero. The pre-trained base is extended to a 128K context window via a layer-selective YaRN and then post-trained in two stages (supervised fine-tuning followed by RLVR), yielding two released variants: an Instruct model that answers directly and a Thinking model that emits an explicit reasoning trace before its final answer. Across code generation, math and reasoning, tool use, knowledge, and safety benchmarks, Mellum 2 is competitive with open-weight baselines in the 4B-14B range while running at the per-token compute of a 2.5B dense model. We release the base, instruct, and thinking checkpoints, together with this report on the architecture decisions, data pipeline, and training recipe behind them, under the Apache 2.0 license.

---


### 123. [Algorithmic Recourse of In-Context Learning for Tabular Data](https://arxiv.org/abs/2605.31272)

**<font color=#1a73e8>作者：</font>** Wenshuo Dong, Jiaming Zhang, Shaopneg Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As predictive models are increasingly deployed in high-stakes settings such as credit approval, there is a growing need for post-hoc methods that provide recourse to affected individuals. Many such models operate on tabular data, where features correspond to real-world attributes. Recently, in-context learning (ICL) has enabled large language models to perform tabular prediction by conditioning on labeled examples at inference time, without explicit training. However, algorithmic recourse for tabular decision-making under ICL remains largely unexplored. In this work, we present the first study of algorithmic recourse for tabular data under ICL. We carry out a theoretical analysis, showing that recourse remains well-defined and bounded, and we characterize how recourse converges toward classical solutions as the context size increases. In practice, we propose a novel zeroth-order recourse framework, Adaptive Subspace Recourse for In-Context Learning (ASR-ICL), that efficiently generates actionable and sparse recourse for black-box ICL models. The proposed framework naturally extends to multi-class tabular tasks. Experiments across multiple real-world datasets and models demonstrate that ASR-ICL achieves recourse quality comparable to existing methods with fewer queries and empirically confirm the predicted convergence behavior, supporting our theoretical analysis.

---


### 124. [Industrializing Prediction-Powered Inference: The GLIDE Library for Reliable GenAI and Agentic Systems Evaluation](https://arxiv.org/abs/2605.31278)

**<font color=#1a73e8>作者：</font>** Grégoire Martinon, Ibrahim Merad, Mohammed Raki  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable evaluation of agentic systems requires unbiased estimates with valid uncertainty, but standard practice navigates between costly human annotation and biased LLM-as-judge proxies. Prediction-powered inference (PPI) combines both into debiased estimates with valid confidence intervals, yet its various methods remain scattered across papers under partial implementations. We introduce GLIDE, an open-source Python library that unifies state-of-the-art PPI estimators (PPI++, Stratified PPI, Predict-Then-Debias and its stratified variants, Active Statistical Inference) and samplers (uniform, stratified, active, cost-optimal) under a scipy-style API specialized to mean estimation. GLIDE ships with a reproducible Monte Carlo validation suite, an empirically grounded decision tree for method selection, and an agentic evaluation case study showing substantial annotation savings at equivalent precision. The GLIDE package is available at this URL: this https URL

---


### 125. [Wind Turbine Maintenance Log Labelling Framework: LLM-Driven Data Correction and Enrichment via Semantic Extraction of Reliability Intelligence](https://arxiv.org/abs/2605.31281)

**<font color=#1a73e8>作者：</font>** Max Malyi, Jonathan Shek, Alasdair McDonald 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As wind turbine fleets age, data-driven reliability engineering is essential to optimise their operation and maintenance for service life extension and levelised cost of energy reduction. Failure event descriptions within historical maintenance logs are a source of valuable reliability intelligence. However, they typically appear as unstructured natural language entries, rendering them inaccessible for quantitative analysis. This paper presents a novel methodology leveraging a large language model (LLM) to systematically standardise and structure maintenance logs based on their free-text descriptors. Operating on a dataset of 16,316 maintenance logs from 280 turbines monitored over nine years, the developed model-agnostic framework autonomously corrected hierarchical system codes and extracted evidence-based taxonomies of maintenance actions and failure modes. The automated pipeline successfully structured over 70% of the dataset. It resolved pervasive misclassification issues, such as isolating previously unclassified pitch system faults and restoring missing system codes, and enriched the records by applying empirical taxonomies to label specific actions taken and failure modes addressed. By using system-based log batches to construct empirical dictionaries of failure modes, observable symptoms, dominant mechanisms, and candidate causes, this approach reduces the inherent subjectivity of manual failure modes and effects analysis (FMEA). Ultimately, the methodology provides a highly scalable, cost-effective blueprint for translating large sets of qualitative field observations into quantitative reliability metrics, laying the foundation for integrated root-cause analysis across the renewable energy sector, improved FMEA, and advanced predictive maintenance.

---


### 126. [Divergence Decoding: Inference-Time Unlearning via Auxiliary Models](https://arxiv.org/abs/2605.31293)

**<font color=#1a73e8>作者：</font>** Humzah Merchant, Bradford Levy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) frequently memorize sensitive training data thereby creating significant privacy and copyright risks. Addressing these risks, i.e., removing such knowledge from an existing model checkpoint, has proven challenging as many unlearning methods lead to catastrophic utility loss or are ineffective for complex queries. We introduce Divergence Decoding (DD), a mechanism that uses small auxiliary models to steer the logits of the LLM away from specific data during inference. Training these models is straight forward, i.e., we use standard pre-training and fine-tuning setups. We find the method decisively outperforms state-of-the-art (SOTA) baselines on unlearning benchmarks across a variety of model and training dataset scales consistent with DD being an effective and inexpensive solution to unlearning. We then demonstrate that this steered distribution can be trivially distilled back into the base model. Since the method is generally applicable to any probabilistic model, we explore its efficacy outside of text generation and find evidence of generalization to the domain of images.

---


### 127. [TokTalk: Expressive Real-time Facial Animation from Audio-LLM Tokens](https://arxiv.org/abs/2605.31294)

**<font color=#1a73e8>作者：</font>** Qingcheng Zhao, Yifang Pan, Karan Singh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Audio-LLMs like GPT-4o have ushered in an era of conversational interaction with language models. Conversational avatars however, still seem robotic in facial expression and conversational flow, in part due to sequential stages of speech recognition, text generation, turn-based text response, speech synthesis, and audio driven facial animation. Based on our insight that audio-tokens produced by current Audio-LLMs carry sufficient information to reconstruct a plausible facial performance, we present TokTalk, a system that directly outputs expressive facial animation in real-time from streaming audio-tokens. We construct a novel audio-token to 3D facial motion dataset, on which TokTalk is trained using a Chunk-based Conditional Flow Matching model. A lightweight adaptation strategy allows our trained model to seamlessly connect to any token-based Audio-LLM at minimal computational overhead. Our chunk-based processing further enables parametric trade-off between latency and facial quality, shown through ablation studies. We further show that the real-time performance of TokTalk is comparable in latency to prior art solutions, and significantly favorable (via a perceptual study) in terms of quality, expressivity and control of the 3D facial performance. We showcase TokTalk's flexibility using a chatbot Avatar, a voice-driven user Avatar, and an animation Director's interface, as diverse audio-visual face applications.

---


### 128. [Learning from Fine-Grained Visual Discrepancies: Mitigating Multimodal Hallucinations via In-Context Visual Contrastive Optimization](https://arxiv.org/abs/2605.31312)

**<font color=#1a73e8>作者：</font>** Haolin Deng, Xin Zou, Zhiwei Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal hallucination remains a persistent challenge for Vision-Language Models (VLMs). Standard textual Direct Preference Optimization (DPO) often fails to mitigate it due to a lack of explicit visual supervision. While existing works introduce visual preference DPO by contrasting original images against negative ones, they suffer from a theoretically inconsistent objective caused by partition function mismatches and rely on coarse-grained negatives that could enable shortcut learning. In this work, we propose In-Context Visual Contrastive Optimization (IC-VCO). By placing contrastive images within a shared multi-image context, IC-VCO ensures a mathematically rigorous objective. We further introduce Visual Contrast Distillation (VCDist), an auxiliary reliability-gated regularizer that encourages consistency between multi-image contrastive training and single-image inference. Finally, we propose a contrastive sample editing strategy that generates hard negatives via precise semantic perturbations. Experiments on five benchmarks demonstrate IC-VCO's best overall performance and the effectiveness of our sample editing strategy. Code and data are available at this https URL.

---


### 129. [Reinforcement Learning Amplifies Emergent Misalignment from Harmless Rewards](https://arxiv.org/abs/2605.31328)

**<font color=#1a73e8>作者：</font>** Magnus Jørgenvåg, David Kaczér, Lasse Ruttert 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emergent misalignment (EM) is the surprising tendency of language models to become broadly misaligned after fine-tuning on narrowly misaligned examples. While EM has been extensively studied in the supervised fine-tuning (SFT) setting, evidence that it also arises from reinforcement learning (RL) is limited to large, closed-source models, leaving the phenomenon expensive to study and difficult to reproduce. We characterize EM from RL in small, off-the-shelf open-weight models along three axes. First, we show that rewarding narrow, overtly misaligned behavior produces substantially higher general-domain misalignment than sample-matched SFT. Second, we show that EM from RL can be induced by reward signals that could plausibly arise naturally, such as unpopular aesthetic preferences or poor rhetorical appeals. Third, we evaluate in-training mitigations developed for SFT-induced EM and find that they broadly transfer, with interleaving on-policy safety data performing best.

---


### 130. [FBHM: Functional Benchmarking and Steering of VLMs for Hateful Meme Detection](https://arxiv.org/abs/2605.31349)

**<font color=#1a73e8>作者：</font>** Paramananda Bhaskar, Naquee Rizwan, Daksh Jogchand 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hateful meme detection remains a formidable challenge for vision-language models, as existing benchmarks are structurally observational - confounding rhetorical hate mechanisms with target community features and preventing causal evaluation of model vulnerabilities. To address this, we introduce FBHM, a systematically curated benchmark of Functionality Based Hateful Memes constructed along two orthogonal axes: 25 distinct rhetorical functionalities and 10 target communities (5,000 memes total). Benchmarking state-of-the-art VLMs reveals a severe generalization gap: models highly accurate on standard datasets catastrophically drop to near-random performance on FBHM, proving they exploit dataset-specific heuristics rather than robust multimodal reasoning. To efficiently close this gap, we propose LSV (learnable steering vectors), an ultra-low data regime strategy that applies a causal intervention objective on as few as 500 steering samples (50 unique base memes), boosting FBHM performance by ~30 Macro-F1 points while outperforming in-context learning and PEFT without degrading source-domain performance.

---


### 131. [Dreaming Of Others: Latent Teammate Modeling In World Models For Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2605.31361)

**<font color=#1a73e8>作者：</font>** Tomas Leroy-Stone  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In cooperative multi-agent reinforcement learning (MARL), agents must coordinate with partners whose internal policies and intentions are not directly observable. While world models such as Dreamer have demonstrated strong generalization and sample efficiency in single-agent settings, their application to MARL remains limited by an inability to handle teammate-induced uncertainty. We propose a new perspective: treat teammates as structured, learnable components within the agent's world model. We introduce an architecture that factorizes the latent state of a Dreamer-style recurrent state-space model (RSSM) into environment and teammate components, and learns an auxiliary Theory-of-Mind (ToM) head to infer latent embeddings of partner behavior such as character, intent, and predicted actions from partial trajectories. These teammate latents condition the actor and critic, enabling the agent to imagine and adapt to diverse collaborators. We outline how this approach can support zero-shot and few-shot coordination in partially observable settings and propose a set of benchmarks and evaluation protocols to assess its impact. This work positions world models as not only predictors of environmental dynamics, but as simulators of social behavior, opening new directions for generalizable, human-compatible AI.

---


### 132. [The Latin Substrate: How Language Models Represent and Mediate Script Choice](https://arxiv.org/abs/2605.31363)

**<font color=#1a73e8>作者：</font>** Daniil Gurgurov, Alan Saji, Katharina Trinley 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many languages are written in multiple scripts, requiring large language models (LLMs) to generate equivalent linguistic content in distinct orthographic forms. While prior work suggests that LLMs route information through shared latent representations, how they internally mediate script variation remains poorly understood.
We study this question by first examining per-layer output distributions with the logit lens, which reveals consistent latent romanization during transliteration, and then through representational and mechanistic analyses of script generation. At the representational level, we show that scripts of the same language become increasingly separable across layers and that a simple linear steering direction can flip a model's output script while largely maintaining semantic content. The vector generalizes asymmetrically to writing systems unseen during construction, flipping non-Latin output to Latin reliably, but mapping Latin output into varied non-Latin scripts. At the mechanistic level, we localize a small set of late-layer attention heads that causally mediate script choice. These heads transfer across unrelated languages and writing systems, suggesting that script routing is implemented by language-agnostic components. Across both analyses, we observe a consistent directional asymmetry: non-Latin output is produced by a compact, identifiable gate, while Latin-script output emerges from diffuse contributions across the network. Collectively, our findings hint that LLMs organize script variation around shared latent representations while exhibiting a privileged substrate toward Latin script.

---


### 133. [Learning to Adapt: Self-Improving Web Agent via Cognitive-Aware Exploration](https://arxiv.org/abs/2605.31365)

**<font color=#1a73e8>作者：</font>** Weile Chen, Bingchen Miao, Qifan Yu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in Multimodal Large Language Models (MLLMs) have led to promising progress in web agents. However, existing web agents often rely on handcrafted execution pipelines or expensive expert trajectories, limiting their adaptability to complex, dynamic environments. To address these challenges, we propose SCALE (Self-Cognitive-Aware Learning and Exploration), which leverages three adversarial roles, Selector, Predictor, and Judger to autonomously discover the agent's limitations and expand its cognitive boundaries through environmental exploration. Moreover, we propose SCALE-Hop, a graph exploration strategy that facilitates global planning and helps agents avoid local exploration traps. To further support learning, we construct SCALE-20k, a large-scale dataset collected from 19 real-world websites, containing diverse task types and structured demonstrations generated from SCALE's exploration traces. Experimental results show that our approach significantly improves the performance and generalization of multiple MLLMs in various web environments. Our framework offers a scalable and generalizable solution for building truly autonomous and adaptive web agents.

---


### 134. [HypoAgent: An Agentic Framework for Interactive Abductive Hypothesis Generation over Knowledge Graphs](https://arxiv.org/abs/2605.31370)

**<font color=#1a73e8>作者：</font>** Yisen Gao, Yixi Cai, Tianshi Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Abductive reasoning over knowledge graphs aims to generate logical hypotheses that explain observed entities or facts. Existing controllable hypothesis generation methods allow users to guide this process with explicit conditions, but they remain limited in interactive settings: they struggle to ground evolving natural-language intents across multi-turn dialogues and provide little fine-grained diagnosis when generated hypotheses fail. To address these limitations, we propose HypoAgent, an Agentic framework for interactive abductive Hypothesis Generation over knowledge graphs. HypoAgent integrates three agents: an Intent Recognition Agent that grounds user utterances and dialogue history into executable KG conditions, a Hypothesis Generation Agent that performs controllable hypothesis generation according to the extracted user intention, and a Root Cause Analysis Agent that diagnoses unreliable hypothesis fragments and leverages KG neighborhood probing to identify supported refinements. Experiments on commonsense and biomedical domain-specific knowledge graphs demonstrate that HypoAgent achieves state-of-the-art semantic similarity under single-turn, multi-turn, and unconditional settings. Our code is available at this https URL.

---


### 135. [Unlocking Fine-Grained Translation Quality Estimation in LRMs through Synergistically Evolving Implicit and Explicit Reasoning](https://arxiv.org/abs/2605.31378)

**<font color=#1a73e8>作者：</font>** Renfei Dang, Xinye Wang, Zhejian Lai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) still struggle with fine-grained translation quality estimation (QE), even with long reasoning chains. We argue that LRMs already possess strong multilingual capabilities, while the core challenge stems from the intrinsic difficulty of learning the fine-grained QE task. In this paper, we propose RIEQE (Reasoning both Implicitly and Explicitly for QE), a simple two-stage training framework that enables the co-evolution of implicit (layer-wise) and explicit (token-wise) reasoning capabilities. To make implicit reasoning feasible, we first decompose the complex QE task into straightforward subtasks. Based on this, our two-stage approach applies: (1) NonThinking-SFT, Supervised Fine-Tuning (SFT) without reasoning chains to directly boost the model's implicit reasoning tendency and capability; and (2) Thinking-RLVR, standard Reinforcement Learning with Verifiable Reward (RLVR) to subsequently strengthen explicit reasoning. Results demonstrate that implicit and explicit reasoning synergistically co-evolve under our framework. On the WMT test sets, RIEQE based on Qwen3-4B-Thinking-2507 surpasses all baselines in explicit reasoning performance, while its implicit reasoning capability is also comparable to the best current encoder-based models. We further provide evidence for the synergistic collaboration between implicit and explicit reasoning, showing how they mutually benefit each other.

---


### 136. [LLM Judges Inconsistently Disagree Across Safety Criteria and Harm Categories](https://arxiv.org/abs/2605.31381)

**<font color=#1a73e8>作者：</font>** Krishnapriya Vishnubhotla, Soumya Vajjala, Akriti Vij 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We evaluate the consistency of automated judges in conducting a multi-dimensional safety evaluation in a reference-free setup. Our results indicate that Large Language Models are unreliable judges in identifying safety issues related to machine-generated advice in regulated domains such as finance, although they are more reliable at identifying more overt forms of unsafe/harmful content such as violence. The degree of inconsistency in a model's judgments can vary significantly by the chosen safety criteria and can be impacted by the language of the content and its linguistic style as well. Finally, there is high disagreement among different judges for the same output, across domains, safety criteria, and languages. These findings provide new insights on the practice of using LLMs as evaluators and offer several recommendations for practitioners on how to use automated judges in practical scenarios.

---


### 137. [Target-Side Paraphrase Augmentation for Sign Language Translation with Large Language Models](https://arxiv.org/abs/2605.31393)

**<font color=#1a73e8>作者：</font>** Pedro Dal Bianco, Jean Paul Nunes Reinhold, Oscar Stanchi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sign language translation (SLT) remains constrained by limited paired sign-video/text corpora and heavy-tailed target vocabularies. We study target-side augmentation in which GPT-4o generates controlled paraphrase variants of reference sentences while the sign input remains unchanged. A Signformer-style pose-based Transformer is trained under a two-stage schedule: pre-training on the augmented corpus followed by fine-tuning on the original references.
We evaluate on three datasets spanning complementary challenges: PHOENIX14T (German Sign Language), with moderate lexical diversity; GSL (Greek Sign Language), with highly ontrolled, repetitive recordings; and LSA-T (Argentinian Sign Language), with severe long-tail sparsity. On PHOENIX14T, augmentation improves BLEU-4 from 9.56 to 10.33. The near-saturated GSL baseline and extremely sparse LSA-T setting reveal the limits of the approach. To our knowledge, this is the first study to apply LLM-generated target-side araphrases and LLM-as-a-Judge evaluation to SLT. The semantic evaluation reveals gains in fidelity that lexical overlap metrics understate.

---


### 138. ["Intelegi Româneşte?'' A Recipe for Romanian Vision-Language Models](https://arxiv.org/abs/2605.31401)

**<font color=#1a73e8>作者：</font>** Mihai Masala, Marius Leordeanu, Mihai Dascalu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) largely follow the text-only LLM trajectory, excelling on English benchmarks but sharply degrading on low-resource languages, where neither large-scale image-text corpora nor culturally grounded evaluations exist. We present a systematic study of building a language-specific VLM for Romanian, covering the full pipeline from data construction to architectural choices. We translate established English VLM training and evaluation corpora into Romanian, applying machine translation to textual annotations and to in-image text, preserving visual grounding while adapting the textual content. Using this data, we train and ablate a series of VLMs to isolate the contribution of (i) vision backbones of varying scale and pretraining, (ii) language backbones from multilingual to Romanian-adapted LLMs, and (iii) OCR-style image-text data. We further curate HoraVQA, a culturally native evaluation set grounded in Romanian everyday scenes. Romanian-adapted VLMs consistently outperform their same-sized counterparts and, across all evaluated benchmarks, even surpass models from the next larger size category.

---


### 139. [The Sword, Shield, and Achilles' Heel: Characterizing the Linguistic Inductive Bias of Large Language Models for Spatial Reasoning in Navigation Planning](https://arxiv.org/abs/2605.31404)

**<font color=#1a73e8>作者：</font>** Xudong Zhang, Jian Yang, Shengkai Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM)-based navigation systems commonly construct explicit spatial representations (e.g., topological graphs, semantic raster maps) and translate them into textual descriptions as LLMs' inputs. However, the linguistic structures of such text-based spatial representations and the choices of contextual features (e.g., topology, geometry) they contain are often treated as neutral engineering decisions rather than key factors that shape LLMs' behavior. To fill the gap, we propose a dual-interventional framework that disentangles linguistic structures from different contextual cues to evaluate the linguistic inductive bias of LLMs for navigation planning. In the framework, representation intervention varies the linguistic format and the degree of linguistic compression, clarifying when linguistic representations support or inhibit navigation planning. Context intervention, combined with contextual feature combination and conflict probing, explicitly clarifies the preferences and weaknesses of LLMs when processing different contextual cues. Experiments across diverse spatial reasoning tasks and multiple model scales reveal a consistent pattern: topological information is a sturdy shield and the backbone of robust planning; linguistic format is a double-edged sword whose effect depends on model size, task demands, and the compression level; and semantic information is a fatal Achilles' heel -- incorrect semantic cues can systematically derail the planning process. Overall, our study shows that effective text-based spatial representations in LLM-based navigation should preserve topological integrity, calibrate representational compression to model capacity, and ensure semantic correctness, rather than simply adopting a single representation. Our code is publicly available at this https URL.

---


### 140. [FAM-Bench: A Multimodal Benchmark for Condition-Aware Food-as-Medicine Reasoning](https://arxiv.org/abs/2605.31410)

**<font color=#1a73e8>作者：</font>** Mingyang Mao, Bhargav Rishi Medisetti, Utkarsh Grover 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Food-as-Medicine requires models to reason beyond what a dish is or what nutrition it contains: they must decide whether a concrete food choice is appropriate for a specific health condition. Existing food AI benchmarks primarily evaluate dish recognition, recipe understanding, nutrient estimation, or general nutrition question answering, leaving this health-aware decision layer largely untested. We introduce FAM-Bench, a multi-modal Food-as-Medicine benchmark with 2500 nutrition-expert-verified instances across 13 diet-related health conditions. The benchmark contains two complementary tasks: dish-level suitability assessment, where models judge whether a dish is suitable for a condition from its image and ingredient list, and comparative dish analysis, where models rank four candidate dishes by condition-specific suitability. Both tasks require integrating ingredient evidence, visual preparation cues, and clinical nutrition constraints, providing a standardized testbed for grounded health-aware reasoning in language and vision-language models.

---


### 141. [YARD: Y-Architecture Register Decoding for Efficient Hallucination Mitigation in Large Vision-Language Models](https://arxiv.org/abs/2605.31429)

**<font color=#1a73e8>作者：</font>** Ting Chen, Geng Li, Guohao Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastive decoding (CD) seeks to mitigate hallucinations in Large Vision-Language Models (LVLMs) by contrasting the output distributions of a standard model and a visually degraded model. However, existing training-free CD methods suffer from sub-optimal degraded branches: completely dropping visual tokens is too extreme and induces language hallucinations, while corrupting input images offers coarse control over visual evidence and suffers from high inference latency due to requiring two full forward passes. To address these dilemmas, we propose YARD, a training-free Y-Architecture Register Decoding framework. Motivated by the observation that reliable text-to-vision grounding predominantly emerges in the middle decoder layers, YARD constructs the degraded branch internally by sharing shallow-layer computations and branching exactly at this critical stage. For the degraded branch, YARD replaces patch-level visual tokens with register tokens, which preserve global image semantics but lack fine-grained local evidence. This image-aware yet locally under-grounded design provides a faithful contrastive signal without extreme modality mismatch, while the Y-architecture strictly avoids a costly second forward pass. Extensive experiments on generative and discriminative hallucination benchmarks demonstrate that YARD consistently achieves state-of-the-art hallucination mitigation across multiple LVLMs, alongside a significant reduction in inference latency.

---


### 142. [DOA: Training-Free Decoder-Only Attention Policy for Long-Form Simultaneous Translation with SpeechLLMs](https://arxiv.org/abs/2605.31432)

**<font color=#1a73e8>作者：</font>** Sara Papi, Luisa Bentivogli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Simultaneous speech-to-text translation (SimulST) generates translations while speech is still unfolding, requiring a streaming policy that decides when to read and when to write. State-of-the-art approaches rely on attention-based encoder-decoder models where cross-attention provides explicit alignment signals. In contrast, Speech Large Language Models (SpeechLLMs) are decoder-only architectures relying solely on self-attention. This raises a central question: whether decoder self-attention contains sufficiently stable alignment signals to guide the streaming policy. Moreover, existing approaches typically rely on training-based adaptations or heuristic wait-$k$ policies and have not been validated in long-form settings. To fill these gaps, we propose Decoder-Only Attention (DOA), a training-free policy that enables long-form simultaneous translation with off-the-shelf SpeechLLMs by deriving a proxy alignment from self-attention. Experiments on Phi4-Multimodal and Qwen3-Omni show that DOA provides an effective alignment signal for supporting streaming decisions, enabling low-latency long-form SimulST with quality close to offline decoding without retraining.

---


### 143. [Astra: a generalizable report generation foundation model for 3D computed tomography](https://arxiv.org/abs/2605.31437)

**<font color=#1a73e8>作者：</font>** Zhuhao Wang, Fang Chen, Chaohui Yu 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> CT interpretation requires radiologists to review hundreds of volumetric slices per examination, making reporting time-consuming and highly expertise-dependent. Automated CT report generation offers a promising route to improving clinical efficiency, yet the field still lacks a generalizable CT report generation foundation model that supports multi-region reporting and remains robust across external real-world cohorts. Intrinsic inconsistencies in reporting style and diagnostic terminology across cohorts make naive joint training prone to noisy textual supervision, thereby limiting model generalizability. Here we present Astra, a generalizable CT report generation foundation model trained on 90,678 thoracoabdominal CT-report pairs (CTRgDB) with 353,671 abnormalities spanning eight organ systems. By harmonizing report style and further refining diagnostic consistency via reinforcement learning, Astra achieves style-consistent and diagnostically accurate report generation across diverse anatomical regions and institutions. Evaluating on CTRgDB and six external cohorts, Astra achieves state-of-the-art performance with a 44.1% average improvement in fine-grained diagnostic metrics (P<0.001). In real-world clinical workflows, Astra assistance accelerates chest report drafting by 29.6% and improves abdominal report completeness by 11.3% (P<0.001). Furthermore, Astra also demonstrates broad utility as a foundation for CT AI development, improving downstream diagnostic performance and scaling vision-language pretrain through high-quality report synthesis. Overall, Astra serves as a broadly accessible clinical assistant and a pivotal infrastructure for the next generation of AI-powered healthcare.

---


### 144. [Translation Analytics for Freelancers II: Benchmarking Local LLMs for Confidential Translation Workflows](https://arxiv.org/abs/2605.31452)

**<font color=#1a73e8>作者：</font>** Yuri Balashov, Rex VanHorn, Mingxi Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Building on our previous work, this paper develops practical, low-barrier methods for freelance translators and smaller language service providers to evaluate translation technologies using rigorous yet accessible analytic methods. Here we address a high-stakes, specialized need: offline translation for confidentiality-sensitive domains in which privacy constraints preclude the use of cloud-based engines and commercial LLMs. We expand the Reeve Foundation Trilingual Corpus (RFTC) used in our previous work into a multilingual corpus (RFMC) by adding sentence-aligned German and Simplified Chinese reference translations. We then benchmark several locally runnable language models (via Ollama) across four language directions on 1000+ sentences selected from this corpus. We use consistent single-prompt calls without fine-tuning or domain adaptation, comparing local LLM outputs against commercial NMTs (DeepL, Baidu), a frontier LLM (GPT-5.2), and professional-grade local NMT systems (OPUS-CAT, NeuralDesktop, Promt). Automatic evaluation is conducted with MATEO. Results reveal substantial variation in local LLM performance across language directions and model sizes. The best local LLMs match or surpass local NMT systems and a frontier LLM, though they remain behind top commercial NMTs. These findings underscore the viability of carefully selected local LLM translation for privacy-constrained professionals and inform future research on model scaling and multilingual capability.

---


### 145. [DRIFT: Decoupled Rollouts and Importance-Weighted Fine-Tuning for Efficient Multi-Turn Optimization](https://arxiv.org/abs/2605.31455)

**<font color=#1a73e8>作者：</font>** Jian Mu, Tianyi Lin, Chengwei Qin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed in multi-turn interactive settings where users or environments can iteratively provide lightweight feedback. Unfortunately, optimizing such behavior presents a sharp dilemma in practice: online reinforcement learning is able to effectively address multi-turn dynamics but is prohibitively expensive due to the cost of generating full correction trajectories at every update, whereas offline supervised fine-tuning (SFT) is efficient but suffers from distribution shift and behavioral collapse. To this end, we novelly propose DRIFT (Decoupled Rollouts and Importance-Weighted Fine-Tuning), a framework that operationalizes the theoretical insight that the KL-regularized RL objective is equivalent to importance-weighted supervised learning. DRIFT decouples rollout from optimization by sampling offline interaction trajectories from a fixed reference policy, deriving return-based importance weights, and optimizing the policy via weighted SFT on the resulting dataset. Empirically, we demonstrate that DRIFT matches or exceeds the performance of multi-turn reinforcement learning baselines while maintaining the training efficiency and simplicity of standard supervised fine-tuning. Code is available at this https URL.

---


### 146. [VisionPulse: Dynamic Visual Sparsity for Efficient Multimodal Reasoning](https://arxiv.org/abs/2605.31457)

**<font color=#1a73e8>作者：</font>** Hengbo Xu, Shengjie Jin, Yanbiao Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid advancement of large multimodal models (LMMs), inference-time overhead has become a key bottleneck for real-world deployment. Existing methods typically prune visual tokens at prefill, assuming the required visual evidence remains static during reasoning. However, we empirically show that visual evidence is strongly step-dependent: only a sparse subset of visual tokens is critical at each decoding step, and the critical set evolves across reasoning. Furthermore, we identify a coupled bottleneck where redundant visual context can steer the model toward query-irrelevant regions, lengthening the reasoning trace. Guided by these insights, we propose VisionPulse, a step-wise visual token pruning framework during reasoning. VisionPulse computes a lightweight visual attention mass to estimate the step-wise retention budget by exploiting its strong positive correlation with LMMs' effective visual token usage and retain only the most critical tokens under this budget. By enforcing visual sparsity during reasoning, VisionPulse filters redundant visual context while preserving relevant visual evidence, shortening reasoning traces naturally. Extensive experiments show that VisionPulse only retains 5% of visual tokens per step with reasoning traces shortened by 11.2%, while keeping accuracy almost unchanged.

---


### 147. [PithTrain: A Compact and Agent-Native MoE Training System](https://arxiv.org/abs/2605.31463)

**<font color=#1a73e8>作者：</font>** Ruihang Lai, Hao Kang, Haozhan Tang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) has become the dominant architecture for frontier language models. To meet this demand, production frameworks have built optimized MoE training stacks over years of engineering effort. Yet evolving these stacks for new architectures and system optimizations remains expensive. With the rise of AI coding agents, they could automate parts of training-framework development and accelerate this evolution. But applying them to these existing frameworks carries hidden costs, invisible to today's throughput-only evaluations. We name this missing dimension agent-task efficiency (ATE): the cost of using coding agents to understand, operate, and extend a framework. Grounded in four agent-native design principles, we build PithTrain, a compact, agent-native MoE training framework. We further introduce ATE-Bench, covering real-world training-framework tasks. Our evaluation shows PithTrain matches the throughput of production frameworks, and on ATE-Bench, PithTrain enables higher agent-task efficiency, with up to 62% fewer Agent Turns and 64% less Active GPU Time.

---


### 148. [GPU Forecasters: Language Models as Selective Surrogates for Kernel Runtime Optimization](https://arxiv.org/abs/2605.31464)

**<font color=#1a73e8>作者：</font>** Zaid Khan, Justin Chih-Yao Chen, Jaemin Cho 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> GPU kernels are the workhorse of modern deep learning, and optimizing them (via evolutionary search or coding agents) usually requires repeated measurement on target hardware. While these measurements provide the ground-truth signal necessary for kernel search, they are costly, because each evaluation of a kernel requires compilation and repeated execution on a GPU. As improvements in LLM inference reduce the cost of writing novel kernels and LLM-driven searches scale to large search budgets, on-device evaluation becomes a bottleneck. To address this, we study how LLMs can serve as selective GPU surrogates for kernel evaluation, by forecasting the performance of proposed kernels. A useful surrogate should be accurate, and it should be selective, by knowing when it could be wrong, and deferring to the GPU. To evaluate surrogates, we measure whether their forecasts are accurate, calibrated, and practically useful for recovering fast kernels under limited GPU-measurement budgets. Next, we study whether reinforcement learning can improve forecast accuracy and confidence calibration. Our experiments demonstrate that LLMs can accurately forecast relative kernel performance, that their utility can be improved through reinforcement learning. Used inside a kernel search, the surrogate lets the search consider several times as many candidates under the same GPU evaluation budget, and that leads to finding faster kernels than an equal-budget baseline. These results suggest that LLMs can play a broader role in kernel optimization, by acting as virtual models of a GPU rather than solely as kernel generators for search.

---


### 149. [AutoSci: A Memory-Centric Agentic System for the Full Scientific Research Lifecycle](https://arxiv.org/abs/2605.31468)

**<font color=#1a73e8>作者：</font>** Weitong Qian, Beicheng Xu, Zhongao Xie 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific research has traditionally been human-intensive, requiring researchers to coordinate literature, ideas, experiments, manuscripts, and review responses across long project cycles. The rise of LLM-based scientific agents creates an opportunity to automate this process. Such a system must support the full research lifecycle, maintain structured persistent memory across projects, and improve its own research procedures over time. However, existing systems either partially satisfy or fail to satisfy these requirements, leaving a gap for a unified automated scientific research system. As a result, we present AutoSci, a memory-centric agentic system for the full scientific research lifecycle. AutoSci is organized around four modules. SciMem provides schema-governed research memory, separating Long-Term Knowledge Memory for reusable scientific knowledge from Active Research Memory for project-level artifacts such as ideas, experiments, manuscripts, and reviews. SciFlow executes a five-stage lifecycle from literature understanding to rebuttal through a harness that controls state, context, verification, feedback, and orchestration. SciDAG augments difficult skills with DAG-shaped multi-agent operators and reusable stage-specific templates. SciEvolve converts feedback signals from users, experiments, reviews, and external environments into versioned updates to SciMem organization, SciFlow skills, and SciDAG templates. Together, these modules make AutoSci a persistent research environment that can execute, remember, and evolve across research projects. The code repository is available at this https URL.

---


### 150. [Language Models Can Resolve Reference Compositionally, But It's Not Their Native Strength: The Case of the Personal Relation Task](https://arxiv.org/abs/2605.31480)

**<font color=#1a73e8>作者：</font>** Bart Evelo, Meaghan Fowlie, Denis Paperno  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Do neural models, such as Large Language Models, genuinely acquire compositional abilities for interpretation of natural language? When we talk about semantic interpretation, we can distinguish two complementary aspects: establishing what an expression refers to in the world (which we call the Extensional task) and representing its sense in a structured way (which we call the Intensional task). We evaluate LLMs and humans on both tasks in the setting of the Personal Relation Task (Paperno 2022) in which, given a universe of people and their relationships with each other, one is asked to interpret a noun phrase such as "Amber's parent's friend". Here, for the Intensional task, the answer is the formula "friend(parent(amber))", and for the Extensional task, the person. We find that humans and LLMs show opposite strengths: humans perform better on Extensional than Intensional tasks, and LLMs vice versa. Our methodology brings greater nuance to the understanding of compositional abilities in modern machine learning models. Our results support the notion that the lack of referential grounding in LLM training is a crucial missing component in mimicking human-like language understanding.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-168](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
