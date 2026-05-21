# 📦 其他研究 | 2026年05月22日

> 本类共 **352** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-352](./part-08.md)

---

### 101. [Latent Process Generator Matching](https://arxiv.org/abs/2605.20547)

**<font color=#1a73e8>作者：</font>** Lukas Billera, Hedwig Nora Nordlinder, Ben Murrell  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many recent flow-matching and diffusion-style generative models rely on auxiliary stochastic dynamics during training: a richer process is simulated to define conditional targets, but the auxiliary state is either intractable to sample at generation time or simply not part of the desired output. Existing Generator Matching theory formalises conditioning on static latent random variables, and several recent papers prove special cases of projection results for particular augmented-state constructions. We introduce latent process generator matching, a general framework that treats the observed generative state as a deterministic image $X_t=\Phi(Y_t)$ of a tractable Markov process $Y_t$. We show that in this setting one may learn the generator of a stochastic process on the image space which has the same one-time marginal distributions as the projected process. This generalizes and subsumes the discrete latent process results from the literature, and extends Generator Matching from static latent variables to a rich family of time-dependent latent conditional processes.

---


### 102. [What Do Agents Communicate? Characterizing Information Exchange in Multi-Agent Systems](https://arxiv.org/abs/2605.20548)

**<font color=#1a73e8>作者：</font>** Yong Jin Chun, Iftekhar Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have enabled collaborative Multi-Agent (MA) systems, where interacting agents improve performance through diverse reasoning and iterative refinement. However, these systems remain vulnerable to error propagation, where early-stage information degrades downstream reasoning. To address this, we conduct a systematic analysis of inter-agent communication to identify which information drives MA performance. We find that the absence of reasoning and verification in inter-agent communication significantly degrades performance. Based on these insights, we propose Category-Aware Recovery Augmentation (technique), which enforces the presence of critical information during communication. recovers up to 86.2% of failed cases. Our results highlight the key role of information quality in effective MA collaboration. Our code is available at this https URL

---


### 103. [MAPS: A Synthetic Dataset for Probing Vision Models in a Controlled 3D Scene Space](https://arxiv.org/abs/2605.20549)

**<font color=#1a73e8>作者：</font>** Santiago Galella, Pamela Osuna-Vargas, Maren Wehrheim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern vision models achieve strong performance on standard benchmarks, yet their aggregate accuracy reveals little about which scene properties drive their predictions. Existing robustness benchmarks provide important stress tests, but typically manipulate global 2D image properties, rely on entangled real-world variation, or cover only a limited set of 3D objects and scene parameters. We introduce MAPS (Manifolds of Artificial Parametric Scenes), a scalable instrument for controlled attribution of vision model behavior to scene parameters. MAPS comprises 2,618 curated photorealistic 3D meshes validated for recognizability across 560 ImageNet classes and provides a Blender-based rendering pipeline for on-demand image generation under continuous variation of nine independent scene-factors spanning background, camera, and lighting, extensible to other factors. To showcase its applicability, we use MAPS to evaluate 20 convolutional and transformer-based models by quantifying their reliance on these scene factors through regression-based sensitivity analysis. We find a near-universal failure axis across all tested architectures: camera distance and elevation consistently dominate recognition failure regardless of ImageNet accuracy. However, the full sensitivity structure reveals that modern CNNs and transformers cluster together, distinct from older architectures, suggesting that fine-grained architectural design choices, rather than the coarse CNN-versus-transformer distinction, are the stronger determinant of sensitivity profiles.

---


### 104. [Faster or Stronger: Towards Flexible Visual Place Recognition via Weighted Aggregation and Token Pruning](https://arxiv.org/abs/2605.20551)

**<font color=#1a73e8>作者：</font>** Zichao Zeng, June Moh Goo, Junwei Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Place Recognition (VPR) aims to match a query image to reference images of the same place in a large-scale database. Recent state-of-the-art methods employ Vision Transformers (ViTs) as backbone foundation models to extract patch-level features that are robust to viewpoint, illumination, and seasonal variations, which are then aggregated into a compact global descriptor for retrieval. Most existing aggregation methods uniformly pool patch tokens into learned clusters, despite the fact that different clusters often encode distinct spatial or semantic patterns and contribute unequally to VPR performance. To address this limitation, we propose Weighted Aggregated Descriptor (WeiAD), which assigns weights to clusters during aggregation, producing more discriminative global representations. Beyond accuracy, retrieval latency is a critical concern for large-scale deployments and resource-constrained edge devices. Prior work mainly reduces latency by compressing global descriptors, while overlooking the cost of feature extraction, an issue exacerbated by ViT-based backbones. We therefore introduce WeiToP, a VPR-oriented token pruning framework that reduces feature extraction cost via self-distillation, where aggregation-induced token importance supervises a lightweight pruning module attached to an early transformer layer, enabling inference-time token pruning. After a single joint training phase, WeiToP enables plug-and-play token pruning at inference time, allowing flexible and on-demand control over the accuracy-efficiency trade-off without additional training. Moreover, WeiToP outperforms existing token pruning methods adapted from general vision tasks.

---


### 105. [Personality Engineering with AI Agents: A New Methodology for Negotiation Research](https://arxiv.org/abs/2605.20554)

**<font color=#1a73e8>作者：</font>** Michelle A. Vaccaro, Jared R. Curhan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> According to canonical negotiation theory, people's success in a negotiation depends on how well they balance competing demands--empathizing and asserting, demonstrating concern for other and concern for self, being soft on the people and hard on the problem. Yet people struggle to manage these tensions, so researchers have lacked the ability to rigorously test the field's prescriptions under controlled conditions. AI agents do not face the same limitations, and their precision, repertoire, consistency, and scalability enable a new class of experiments to contribute to negotiation theory. In this article, we introduce personality engineering: a methodology that uses AI agents to precisely parameterize, manipulate, and evaluate negotiator personality. We propose using the interpersonal circumplex--and its two core dimensions of warmth and dominance--as a foundational coordinate system for the field. This approach offers both a rigorous methodology for testing classic negotiation theories and a practical guide for designing the personalities of AI negotiation agents.

---


### 106. [When Irregularity Helps: A Subclass Analysis of Inductive Bias in Neural Morphology](https://arxiv.org/abs/2605.20558)

**<font color=#1a73e8>作者：</font>** Wen Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Neural morphological generation systems often achieve high aggregate accuracy on benchmark datasets, yet such performance can conceal systematic errors concentrated in rare morphological subclasses. We examine Japanese past-tense verb inflection and show that a very small, structurally specific irregular subtype (<1% of data) accounts for a disproportionate share of model errors. Controlled ablation experiments demonstrate that removing this subtype yields larger improvements in generalization than removing all irregular verbs, indicating that not all irregularity contributes equally to model instability. These findings suggest that error concentration is driven by the interaction between extreme low-frequency morphological patterns and specific morphophonological processes, particularly gemination. We argue that morphological evaluation should incorporate finer-grained subclass analysis beyond standard conjugation categories.

---


### 107. [Multi-agent Collaboration with State Management](https://arxiv.org/abs/2605.20563)

**<font color=#1a73e8>作者：</font>** Mengyang Liu, Taozhi Chen, Zhenhua Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Recent advances in multi-agent systems have shown great potential for solving complex tasks. However, when multiple agents edit a shared codebase concurrently, their changes can silently conflict and inconsistent views lead to integration failures. Existing multi-agent systems address this through workspace isolation (e.g., one git worktree per agent), but this defers conflict resolution to a post-hoc merge step where recovery is expensive. In this paper, we propose STORM, i.e., STate-ORiented Management for multi-agent collaboration. Specifically, STORM manages agent states by mediating their interactions with the shared workspace, ensuring that each agent operates on a consistent view of the codebase and that conflicting edits are detected and resolved at write time. We evaluate STORM on Commit0 and PaperBench across multiple LLMs. STORM outperforms the git-worktree-based multi-agent baseline by +18.7 on Commit0-Lite and +1.4 on PaperBench, while achieving comparable or better cost efficiency. Combined with single-agent runs, STORM reaches highest scores of 87.6 and 78.2 on the two benchmarks respectively, suggesting that explicit state management is a more effective foundation for multi-agent collaboration than workspace isolation. STORM can also be plugged into any multi-agent system seamlessly.

---


### 108. [End-to-End Unmixing with Material Prompts for Hyperspectral Object Tracking](https://arxiv.org/abs/2605.20569)

**<font color=#1a73e8>作者：</font>** Xu Han, Mohammad Aminul Islam, Lei Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral imagery encodes rich material properties that can improve tracking robustness under appearance ambiguity, illumination change, and background clutter. However, due to the limited availability of hyperspectral video data, many existing methods adapt pretrained RGB trackers via spatial or channel fusion strategies, largely neglecting the intrinsic material information in hyperspectral imagery. Moreover, the few material-aware approaches typically rely on external spectral unmixing pipelines that are decoupled from the tracking objective, limiting effective optimization of material representations for target localization. To address these limitations, we formulate hyperspectral object tracking as a joint optimization problem of material decomposition and target localization, coupling the two tasks via a weighted target-oriented unmixing loss that explicitly aligns material representations with localization accuracy. Specifically, we propose a material representation decomposition module for deep learning-based spectral unmixing with adaptive frequency decomposition. Building on the decomposed material representations, we further introduce a dual-branch wavelet-enhanced material prompt module that learns low- and high-frequency material prompts through efficient spatial-material interactions in the frequency domain. The framework is model-agnostic and can be seamlessly generalized to different unmixing backbones. Extensive experiments on standard hyperspectral tracking benchmarks demonstrate state-of-the-art performance and validate the effectiveness of the proposed end-to-end material-aware tracking framework. Code is available at this https URL.

---


### 109. [$Δ$ynamics: Language-Based Representation for Inferring Rigid-Body Dynamics From Videos](https://arxiv.org/abs/2605.20576)

**<font color=#1a73e8>作者：</font>** Chia-Hsiang Kao, Cong Phuoc Huynh, Chien-Yi Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inferring rigid-body physical states and properties from monocular videos is a fundamental step toward physics-based perception and simulation. Existing approaches assume specific underlying physical systems, object types, and camera poses, making them unable to generalize to complex real-world settings. We introduce $\Delta$YNAMICS, a vision-language framework that uses language as a unified representation of rigid-body dynamics. Instead of directly predicting parameters, $\Delta$YNAMICS generates scene configurations in a structured text format for physics simulation. We enhance the model's generalization by integrating natural language motion reasoning and leveraging optical flow as a semantic-agnostic input. On the CLEVRER dataset, $\Delta$YNAMICS achieves a segmentation IoU of 0.30, a 7x improvement over leading VLMs (InternVL3-8B, Qwen2.5-VL-7B and Claude-4-Sonnet). Additionally, test-time sampling and evolutionary search further boost performance by 27% and 120% in segmentation IoU, respectively. Finally, we demonstrate strong transfer to a new dataset of 235 real-world rigid-body videos, highlighting the potential of language-driven physics inference for bridging perception and simulation.

---


### 110. [Mahjax: A GPU-Accelerated Mahjong Simulator for Reinforcement Learning in JAX](https://arxiv.org/abs/2605.20577)

**<font color=#1a73e8>作者：</font>** Soichiro Nishimori, Shinri Okano, Keigo Habara 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Riichi Mahjong is a multi-player, imperfect-information game characterized by stochasticity and high-dimensional state spaces. These attributes present a unique combination of challenges that mirror complex real-world decision-making problems in reinforcement learning. While prior research has heavily relied on supervised learning from human play logs to pre-train the policy, algorithms capable of learning \textit{tabula rasa} (from scratch) offer greater potential for general applicability, as evidenced by the AlphaZero lineage. To facilitate such research, we introduce \textbf{Mahjax}, a fully vectorized Riichi Mahjong environment implemented in JAX to enable large-scale rollout parallelization on Graphics Processing Units (GPUs). We also provide a high-quality visualization tool to streamline debugging and interaction with trained agents. Experimental results demonstrate that Mahjax achieves throughputs of up to \textbf{2 million} and \textbf{1 million steps per second} on eight NVIDIA A100 GPUs under the no-red and red rules, respectively. Furthermore, we validate the environment's utility for reinforcement learning by showing that agents can be trained effectively to improve their rank against baseline policies.

---


### 111. [Deep Learning Surrogates for Emulating Stochastic Climate Tipping Dynamics](https://arxiv.org/abs/2605.20580)

**<font color=#1a73e8>作者：</font>** Adeline Hillier, Jennifer Sleeman, Jay Brett 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work explores a dynamics-informed Temporal Fusion Transformer (TFT) as a data-driven surrogate for computationally intensive Earth system simulations. Focusing on multivariate time series describing global ocean transport, we demonstrate the surrogate's ability to forecast tip events across thousands of time steps. The data involve up to 21 non-stationary time series in addition to static covariates describing free parameters and initial conditions. Modifications to the architecture and objective function yield a surrogate that anticipates the timing of Atlantic and Pacific collapses to high fidelity and captures the stochastic uncertainty in transition timing across ensemble predictions. The learned surrogate achieves a 465x computational speedup over the numerical simulator while maintaining differentiability with respect to parameters and initial conditions.

---


### 112. [TriForces: Augmenting Atomistic GNNs for Transferable Representations](https://arxiv.org/abs/2605.20581)

**<font color=#1a73e8>作者：</font>** Ali Ramlaoui, Alexandre Duval, Hannah Bull 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning interatomic potentials (MLIPs) achieve excellent accuracy when trained on large Density Functional Theory (DFT) data. To be useful in practice, they must often be adapted to target chemistries using small and expensive task-specific datasets. However, MLIPs transfer inconsistently across domains, with representations that often loose accessible composition and structure information. To address this, we present TriForces, a model-agnostic three-stream framework that separates composition and structure information, combined with self-supervised learning to preserve transferable representations. TriForces improves performance on MatBench and QM9 over baselines without needing DFT labels and enables efficient similar structure retrieval through its learned latent space. On OMat24, in limited-data training regime, TriForces reduces energy MAE by 57% at 20K samples only and improves force MAE across sample sizes. We release pretrained TriForces variants across multiple MLIP architectures with code at this https URL.

---


### 113. [Direct Translation between Sign Languages](https://arxiv.org/abs/2605.20588)

**<font color=#1a73e8>作者：</font>** Zetian Wu, Bowen Xie, Wuyang Meng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The field of sign language translation has witnessed significant progress in the translation between sign and spoken languages, but the translation between sign languages remains largely unexplored and out of reach. The latter can help 1.5 billion deaf and hard-of-hearing (DHH) people worldwide communicate across language barriers without relying on hearing interpreters or written-language fluency. The cascade approach composing separate sign-to-text, text-to-text, and text-to-sign systems suffers from error propagation and extra latency as well as the loss of information unique in the visual modality. We aim to develop direct sign-to-sign translation. However, a large-scale open-domain parallel corpus has not been curated between sign languages. To enable direct translation between sign language utterances, we use back-translation to produce synthetic sign-sign pairs from unaligned individual language utterance-sign corpora. Using this data, we jointly train a single MBART-based model for both text->sign (T2S) and sign->sign (S2S). On synthetically generated paired sets between American Sign Language (ASL), Chinese Sign Language (CSL), and German Sign Language (DGS), our direct S2S method outperforms the cascaded baseline on geometric sign error metrics (20% lower DTW-aligned MPJPE) and language matching metrics after predicted sign utterances are translated back to sentences (50% high BLEU-4) while achieving a roughly 2.3* speedup. On a small set of pre-existing cross-lingual sign data, we find similar improvements for our proposed method.

---


### 114. [ReversedQ: Opportunities for Faster Q-Learning in Episodic Online Reinforcement Learning](https://arxiv.org/abs/2605.20592)

**<font color=#1a73e8>作者：</font>** Sofia R. Miskala-Dinc, Aviva Prins  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study model-free Q-learning in finite-horizon episodic Markov Decision Processes (MDPs) with stationary dynamics across episodes. We identify a central issue in nascent model-free posterior-sampling works: the reliance on delayed learning in order to prove theoretical guarantees. In particular, we identify three opportunities for faster learning - (i) value-function update order, (ii) update frequencies, and (iii) value-function initialization. Using Wang et al.'s RandomizedQ as a basis, we illustrate these changes and their individual (as well as cumulative) impact in multiple empirical studies. We find that our combined modifications, termed ReversedQ, improve scaled mean cumulative reward compared to RandomizedQ, from 9.53% to 78.78% in the Bidirectional Diabolical Combination Lock (BDCL), and from 21.76% to 61.81% in a chain MDP.

---


### 115. [Unsupervised clustering and classification of upper limb EMG signals during functional movements: a data-driven](https://arxiv.org/abs/2605.20599)

**<font color=#1a73e8>作者：</font>** L. F. Salazar Álvarez, D. Escobar-Saltarén, M. B. Salazar Sánchez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study presents a comprehensive approach for the clustering and classification of upper-limb surface electromyography (sEMG) signals during functional reach and grasp movements. The methodology was applied to the NINAPRO DB4 dataset, which provides multichannel EMG recordings of 52 gestures. A four-stage pipeline was designed, including signal preprocessing, fea-ture extraction, gesture selection via hierarchical clustering, and comparative model evaluation. Preprocessing involved a fourth-order low-pass filter (0.6 Hz) and Hilbert envelope transformation, effectively reducing noise and enhancing signal clarity. Feature extraction yielded 26 temporal and frequency-domain met-rics, which were later refined using visual analysis, mutual information, principal component analysis, and decision tree importance scores. A final subset of five key features was selected for classification tasks. Gesture selection was per-formed through hierarchical clustering using Mahalanobis distance, resulting in six representative movements that balanced biomechanical diversity and compu-tational efficiency. A 200 ms window was identified as optimal for temporal seg-mentation based on stability and physiological plausibility. Classifier models were evaluated in two stages. Automated comparison using PyCaret identified Extra Trees (ET) and Artificial Neural Networks (ANN) as top performers. Sub-sequent independent training confirmed their stability and generalization capac-ity, with ANN showing progressive learning and ET maintaining robust, con-sistent results. The findings support the implementation of adaptive, low-latency control strategies for myoelectric prostheses and provide a scalable pipeline for future real-time applications.

---


### 116. [Head-Aware Key-Value Compression for Efficient Autoregressive Image Generation](https://arxiv.org/abs/2605.20600)

**<font color=#1a73e8>作者：</font>** Guotao Liang, Baoquan Zhang, Zhiyuan Wen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) visual generation has achieved remarkable performance but suffers from high memory usage and low throughput, as it requires caching previously generated visual tokens. Recent research has shown that retaining only a few lines of cache tokens can maintain high-quality images while significantly reducing memory usage and improving throughput. However, these methods allocate a fixed budget to each attention head, overlooking the heterogeneity among attention heads, leading to suboptimal memory allocation. In this paper, we observe that attention heads across different layers exhibit diverse attention patterns, where some heads focus on local neighborhoods while others capture broader contextual dependencies. Based on this insight, we propose a novel head-aware key-value (KV) cache compression framework for autoregressive image generation, called HeadKV, which assigns smaller budgets to locality-biased heads and larger budgets to heads with broader attention. A key challenge lies in identifying the type of each attention head to guide cache compression. We further observe that, within the same layer, each head exhibits consistent attention patterns across token positions, \emph{i.e.}, a head's behavior for early tokens remains consistent with that for later tokens. This insight suggests that head types can be identified during the early stage and reused for KV compression throughout generation. Its advantage is that it requires no additional training or dataset-level statistics and generalizes seamlessly across different inputs. Moreover, we design a Stratified Token Eviction strategy to effectively preserve long-range information. Extensive experiments demonstrate its effectiveness across multiple autoregressive image generation models.

---


### 117. [Mind Your Margin and Boundary: Are Your Distilled Datasets Truly Robust?](https://arxiv.org/abs/2605.20606)

**<font color=#1a73e8>作者：</font>** Muquan Li, Yingyi Ma, Yihong Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dataset distillation (DD) compresses a large training set into a small synthetic set for efficient training, but most DD methods optimize only clean accuracy and leave robustness uncontrolled. Recent robust DD methods improve robustness, yet they often suffer from a poor accuracy-robustness trade-off because they (i) treat all adversarially perturbed examples uniformly, despite robust risk being dominated by near-zero robust margins, and (ii) do not explicitly increase inter-class separation in the decision boundary where attacks concentrate. We present Contrastive Curriculum for Robust Dataset Distillation (C$^2$R), a framework that couples an attack-aware curriculum with a contrastive robustness objective. From a robust-margin perspective, we derive a perturbation score that approximates each sample's robust hinge, enabling a curriculum that prioritizes the smallest-margin adversaries that most directly drive robust error. In parallel, a class-balanced contrastive robustness loss enforces adversarial invariance while explicitly widening boundary separation across classes. Experiments on CIFAR-10/100, Tiny-ImageNet, and multiple ImageNet-1K subsets under six attacks show that C$^2$R achieves the best robust accuracy, outperforming prior robust DD by $2.8$% on average.

---


### 118. [Mechanistic Interpretability for Learning Assurance of a Vision-Based Landing System](https://arxiv.org/abs/2605.20607)

**<font color=#1a73e8>作者：</font>** Romeo Valentin, Olivia Beyer Bruvik, Marc R. Schlichting 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EASA's learning-assurance guidance requires data-driven aviation systems to build and monitor their own situation representation, yet for neural networks the technical means to provide such evidence remain an open problem. We address this gap for a vision-based aircraft landing system: we propose that a minimally assurable model must at least be shown to separate content from style in its own situation representation. Showing that the model's predictions then rely largely on the contentful representation components leads to a concrete assurance path. To demonstrate this assurance path on a concrete model we train a vision transformer model for runway keypoint regression on the LARDv2 dataset. The model, which acts as the subject for our assurance demonstration, produces per-patch embeddings that we decompose into interpretable atoms via K-SVD sparse dictionary learning. A qualitative visualization confirms that contentful atoms track task-relevant runway structure and stylistic atoms track domain-specific appearance, and the regression head is shown to place almost all of its linear weight on contentful atoms. We further build on the content/style separation and define out-of-model-scope (OOMS) detection, a novel runtime assurance approach directly monitoring the model's situation representation. OOMS monitoring is complementary to operational design domain and output-space out-of-distribution monitoring and addresses concrete requirements of the recent EASA guidance. By directly analyzing a model's situation representation both at test time and runtime, this work delivers the first concrete piece of the representation-level evidence that EASA learning-assurance guidance demands, and points to mechanistic interpretability as a practical building block of future aviation safety cases.

---


### 119. [From Automated to Autonomous: Hierarchical Agent-native Network Architecture (HANA)](https://arxiv.org/abs/2605.20608)

**<font color=#1a73e8>作者：</font>** Binghan Wu, Shoufeng Wang, Yunxin Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Realizing Level 4/5 Autonomous Networks (AN) demands a shift from static automation to agent-native intelligence. Current operations, reliant on rigid scripts, lack the cognitive agency to handle off-nominal conditions. To address this, this letter proposes a hierarchical multi-agent reference architecture enabling high-level autonomy. The framework features a Dual-Driven Orchestrator that coordinates specialized Executive Agents, supported by a shared Public Memory for unified domain knowledge. A key innovation is the integration of agent self-awareness, which empowers the system to harmonize deliberative strategic governance with reflexive fault recovery. We instantiate and validate this architecture within a 5G Core environment. Case studies demonstrate that the system sustains critical throughput under congestion and reduces Mean Time to Repair (MTTR) by 86%, confirming its efficacy in unifying strategic planning with operational resilience.

---


### 120. [Compositional Transduction with Latent Analogies for Offline Goal-Conditioned Reinforcement Learning](https://arxiv.org/abs/2605.20609)

**<font color=#1a73e8>作者：</font>** Junseok Kim, Dohyeong Kim, Mineui Hong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compositional generalization is essential for reaching unseen goals under novel contextual variations in offline goal-conditioned reinforcement learning (GCRL), where a generalist goal-reaching agent must be learned from limited data. Most prior approaches pursue this via trajectory stitching over temporally contiguous segments, which limits composing behaviors across varying contexts. To overcome this limitation, we formalize analogy transduction as synthesizing new plans by composing task-endogenous analogies with given contexts and propose a novel analogy representation tailored for it. Grounded in our theory, this analogy representation captures what changes under optimal task execution, remains invariant to contextual variations, and is sufficient for optimal goal reaching. We further contend that generalization to unseen analogy-context pairs is a practical obstacle in analogy transduction, and introduce a new approach for offline GCRL that enables analogy transduction beyond seen pairs to unseen combinations. We empirically demonstrate the effectiveness of our approach on OGBench manipulation environments, substantially outperforming prior methods that do not perform analogy transduction. Project page: this https URL

---


### 121. [Beyond Routing: Characterising Expert Tuning and Representation in Vision Mixture-of-Experts](https://arxiv.org/abs/2605.20610)

**<font color=#1a73e8>作者：</font>** Gene Tangtartharakul, Katherine R. Storrs  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models are often interpreted by analysing which categories are routed to which experts. However, routing alone does not reveal what each expert actually encodes. We train sparsely-gated convolutional MoE models with a contrastive objective on natural images and characterise expert specialisation using tools from visual neuroscience. Extending from gating-level to expert-level analyses, we measure per-expert category separability, and per-expert tuning using the most exciting inputs. Extending from category-level to feature-level explanations, we interpret tuning via semantic dimensions derived from a dataset of human behavioural judgements (THINGS). Finally, we use tuning and representational similarity analysis to assess the stability of expertise-allocation across independent initialisations. We find that an animate-inanimate distinction dominates expert partitioning, apparent from gating through to expert readout, and is stable across independently trained models. Although routing statistics suggest relatively sparse, categorical preferences, expert analyses reveal broader tuning to continuous visual and semantic dimensions that extend beyond category boundaries. Experts exhibit similar category-separability to one another, despite distinct feature tuning, demonstrating the explanatory benefits of moving beyond category-level analyses. Together, these results show that expert specialisation in vision MoEs extends well beyond category routing and is better understood by probing fine-grained expert-level tuning and representational structure.

---


### 122. [Matryoshka Concept Bottleneck Models](https://arxiv.org/abs/2605.20612)

**<font color=#1a73e8>作者：</font>** Ziye Chen, Hongbin Lin, Xinyue Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Concept Bottleneck Models (CBMs) have emerged as a prominent paradigm for interpretable deep learning, learning by grounding predictions in human-understandable concepts. However, their practical deployment is hindered by the high cost of test-time intervention, as correcting model errors typically requires human experts to manually inspect and verify a large set of predicted concepts. Existing approaches suffer from a fundamental structural limitation: they either adopt a single static concept set, forcing experts to exhaustively annotate concepts and incurring prohibitive intervention costs, or train multiple models tailored to different concept budgets, resulting in substantial computational and maintenance overhead. To address this challenge, we propose the Matryoshka Concept Bottleneck Model (MCBM), a unified architecture that enables adaptive concept utilization within a single model. Inspired by Matryoshka Representation Learning, MCBM organizes concepts into a nested hierarchy based on maximum relevance and minimum redundancy, allowing inference at multiple levels of conceptual granularity without retraining. Theoretically, we show that MCBM reduces the expected intervention costs from linear to logarithmic order, $O(\log K)$, while guaranteeing monotonic performance improvement. Empirically, extensive experiments demonstrate that MCBM matches the performance of independently trained models while enabling dynamic and efficient expert interaction.

---


### 123. [HRM-Text: Efficient Pretraining Beyond Scaling](https://arxiv.org/abs/2605.20613)

**<font color=#1a73e8>作者：</font>** Guan Wang, Changling Liu, Chenyu Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The current pretraining paradigm for large language models relies on massive compute and internet-scale raw text, creating a significant barrier to foundational research. In contrast, biological systems demonstrate highly sample-efficient learning through multi-timescale processing, such as the functional organization of the frontoparietal loop. Taking this as inspiration, we introduce HRM-Text, which replaces standard Transformers with a Hierarchical Recurrent Model (HRM) that decouples computation into slow-evolving strategic and fast-evolving execution layers. To stabilize this deep recurrence for language modeling, we introduce MagicNorm and warmup deep credit assignment. Furthermore, instead of standard raw-text pretraining, we train exclusively on instruction-response pairs using a task-completion objective and PrefixLM masking. Serving as an empirical existence proof of efficient pretraining, a 1B-parameter HRM-Text model trained from scratch on only 40 billion unique tokens and $1,500 budget achieves 60.7% on MMLU, 81.9% on ARC-C, 82.2% on DROP, 84.5% on GSM8K, and 56.2% on MATH. Despite utilizing roughly 100-900x fewer training tokens and 96-432x less estimated compute than standard baselines, HRM-Text performs competitively with 2-7B parameter open models. These results demonstrate that co-designing architectures and objectives can radically reduce the compute-to-performance ratio, making pretraining from scratch accessible to the broader research community.

---


### 124. [Auto-Dreamer: Learning Offline Memory Consolidation for Language Agents](https://arxiv.org/abs/2605.20616)

**<font color=#1a73e8>作者：</font>** Chongrui Ye, Yuxiang Liu, Yu Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language agents increasingly operate over streams of related tasks, yet existing memory systems struggle to convert accumulated experience into reusable knowledge. Retrieval-augmented and structured memory methods record per-session observations effectively, but often couple acquisition and consolidation into a single online process, leaving the agent without a global view across sessions to discover recurring patterns, abstract shared procedures, or prune redundant entries. Inspired by complementary learning systems theory, we propose Auto-Dreamer, a learned offline consolidator for language-agent memory. Auto-Dreamer decouples fast per-session memory acquisition from slow cross-session consolidation. Given a selected working region of a typed memory bank, the consolidator treats the region as read-only evidence, performs bounded tool-use to inspect entries and provenance-linked source trajectories, and synthesizes a fresh compact replacement set that abstracts across sessions and supersedes the original region. We train Auto-Dreamer via GRPO, using end-to-end agent performance as the reward signal to learn how to consolidate memories acquired through fast online experience. Trained on ScienceWorld trajectories alone, Auto-Dreamer outperforms fixed, RL-trained, and prompted memory baselines on ScienceWorld by 7 points while using an active memory bank 12$\times$ smaller than the strongest baseline, and continues to lead on held-out ALFWorld and WebArena without retraining -- using 6$\times$ less memory than the strongest baseline on ALFWorld.

---


### 125. [COAgents: Multi-Agent Framework to Learn and Navigate Routing Problems Search Space](https://arxiv.org/abs/2605.20618)

**<font color=#1a73e8>作者：</font>** Oleksandr Yakovenko, Mahdi Mostajabdaveh, Cheikh Ahmed 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Although Vehicle Routing Problems (VRP) are essential to many real-world systems, they remain computationally intractable at scale due to their combinatorial complexity. Traditional heuristics rely on handcrafted rules for local improvements and occasional \textit{jumps} to escape local minima, but often struggle to generalize across diverse instances. We introduce \textbf{COAgents}, a cooperative multi-agent framework that models the search process as a graph: nodes represent solutions, and edges correspond to either local refinements or large perturbations for diversification (i.e., jumps). A \textit{Partial Search Graph} (PSG) is dynamically constructed during search, enabling COAgents to train a Node Selection Agent and a Move Selection Agent to guide intensification, and a Jump Agent to trigger well-timed explorations of new regions. Unlike end-to-end learning approaches, COAgents cleanly separates problem-agnostic search control from compact domain-specific encoding, facilitating adaptability across tasks. Extensive experiments on the CVRP and VRPTW benchmarks show that COAgents remains competitive with several learn-to-search baselines on CVRP and sets a new state of the art among learning-based methods on the more challenging VRPTW instances, reducing the gap to the best-known solutions by 14\% at $N\!=\!100$ and 44\% at $N\!=\!50$ relative to the strongest neural solver (POMO), and by 21\% and 40\% respectively relative to ALNS.
Code is available at this https URL.

---


### 126. [SURF: Steering the Scalarization Weight to Uniformly Traverse the Pareto Front](https://arxiv.org/abs/2605.20619)

**<font color=#1a73e8>作者：</font>** Liuyuan Jiang, Chentong Huang, Lisha Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scalarization is widely used in multi-objective optimization owing to its simplicity and scalability. In many applications, the goal is to generate solutions that represent diverse user preferences, ideally with uniform coverage of the Pareto front (PF). However, uniformly sampling scalarization weights usually induces non-uniform coverage of the PF. We explain this mismatch through a geometric analysis of the scalarization path. As the scalarization weight varies, the corresponding solutions trace the PF with a generally non-uniform traversal speed. This speed induces an arc-length cumulative distribution function (CDF); inverting this CDF map yields a principled rule for selecting weights that produce uniform PF coverage. Building on this insight, we propose SURF (Sampling Uniformly along the PaReto Front). For structured problems, including bi-objective bandits, we derive closed-form expressions for this CDF map and the resulting PF-aware weight sampling rule. For general problems, SURF alternates between CDF reconstruction and weight sampling. Theoretically, we show that under provable conditions, SURF converges linearly to an unavoidable finite-sampling floor. Empirically, experiments on bandits, multi-objective-gymnasium, and multi-objective LLM alignment demonstrate that SURF efficiently achieves more uniform PF coverage than baselines.

---


### 127. [Dynamic Shapley Computation](https://arxiv.org/abs/2605.20620)

**<font color=#1a73e8>作者：</font>** Xuan Yang, Hsi-Wen Chen, Ming-Syan Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Shapley-based data valuation provides a principled way to quantify the contribution of training data, but its high computational cost makes it impractical in dynamic settings where tasks and training players evolve. Existing methods treat Shapley computation as a one-shot process and collapse contributions into aggregated scores, preventing reuse and requiring recomputation under any change. We introduce a new perspective that represents Shapley values as a player-by-task matrix and formulates dynamic valuation as a structured matrix maintenance problem. We exploit the fact that each task depends on a small subset of training players and that similar tasks yield similar valuations, leading to utility locality and coalition locality. Based on these insights, we propose D-Shap, a dynamic valuation framework that enables efficient updates by modifying only a small portion of the matrix: new task valuations are inferred via structure-aware interpolation, while updates induced by new players are confined to affected local matrix blocks. To eliminate the need for pre-specified evaluation tasks, we introduce self-valuation, which constructs the initial matrix directly from training data, supported by scalable subset reuse and coverage-aware anchor selection. Experiments across diverse models show that D-Shap performs task updates in milliseconds and reduces the cost of player updates by up to three orders of magnitude, while achieving valuation quality competitive with full recomputation.

---


### 128. [Accelerating Video Inverse Problem Solvers with Autoregressive Diffusion Models](https://arxiv.org/abs/2605.20624)

**<font color=#1a73e8>作者：</font>** Taesung Kwon, Jonghyun Park, Hyungjin Chung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models provide powerful priors for zero-shot video inverse problems, but their real-time deployment is hindered by two inefficiencies: high initial latency caused by holistic video restoration, and low throughput resulting from multiple VAE passes to enforce measurement consistency in pixel space. To overcome these limitations, we propose Autoregressive Video Inverse problem Solver (AVIS). The AVIS framework leverages autoregressive video diffusion models to restore videos in a streaming manner, naturally eliminating latency bottlenecks. Specifically, AVIS initializes reverse diffusion with a measurement-consistent estimate, reducing the required sampling steps. Compared to leading non-autoregressive solvers, AVIS drastically reduces initial latency from 114s to 4s and increases throughput from 0.71 to 1.18 FPS while achieving superior restoration quality. We further introduce a highly accelerated variant, dubbed AVIS Flash, that enforces measurement consistency solely on the first chunk. AVIS Flash substantially boosts throughput to 5.91 FPS on a single RTX 4090 GPU while maintaining competitive performance and achieving a favorable efficiency-performance trade-off, paving the way toward real-time deployment.

---


### 129. [Retrieval-Augmented Long-Context Translation for Cultural Image Captioning: Gators submission for AmericasNLP 2026 shared task](https://arxiv.org/abs/2605.20626)

**<font color=#1a73e8>作者：</font>** Aashish Dhawan, Christopher Driggers-Ellis, Dzmitry Kasinets 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present the University of Florida Gators submission to the AmericasNLP 2026 shared task on cultural image captioning for Indigenous languages. Our two-stage pipeline generates a Spanish intermediate caption with Qwen2.5-VL, then produces the target-language caption using retrieval-augmented many-shot prompting with Gemini 2.5 Flash. We achieve 164.1%, 131.7%, and 122.6% improvements over the shared task baseline for Bribri, Guaraní, and Orizaba Nahuatl captioning, respectively, in our dev set evaluation and maintain >150% improvements for the Bribri and Orizaba Nahuatl languages in the test set evaluation. We find retrieval is highly language-dependent, beneficial only for large, in-domain corpora, and that synthetic data augmentation accounts for around 28 chrF++ of the dev set Guaraní performance gain. Our submission is the overall winner of the shared task, placing second out of five finalist submissions in human evaluations of target-language captions.

---


### 130. [Divide-Prompt-Refine: a Training-Free, Structure-Aware Framework for Biomedical Abstract Generation](https://arxiv.org/abs/2605.20628)

**<font color=#1a73e8>作者：</font>** Sylvey Lin, Joe Menke, Shufan Ming 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biomedical abstracts play a critical role in downstream NLP applications, such as information retrieval, biocuration, and biomedical knowledge discovery. However, a non-trivial number of biomedical articles do not have abstracts, diminishing the utility of these articles for downstream tasks. We propose DPR-BAG (Divide, Prompt, and Refine for Biomedical Abstract Generation), a training-free, zero-shot framework that generates coherent and factually grounded abstracts for biomedical articles with full text but no abstract. DPR-BAG decomposes full-text documents into structured rhetorical facets following the Background-Objective-Methods-Results-Conclusions (BOMRC) schema, performs parallel LLM-based summarization for each facet, and applies a final refinement stage to restore global discourse coherence. On PMC-MAD, a distribution-aligned dataset of 46,309 biomedical articles, DPR-BAG improves abstractive novelty over strong extractive and fine-tuned baselines, while maintaining factual consistency. Our ablation study reveals a counterintuitive finding: increasing prompt complexity or explicitly injecting entity-level guidance can degrade factual alignment, highlighting the importance of controlled prompting strategies. These findings underscore the potential of training-free, structure-aware frameworks for scalable biomedical abstract generation in low-resource settings. Our data and code are available at this https URL and this https URL.

---


### 131. [The General Theory of Localization Methods](https://arxiv.org/abs/2605.20635)

**<font color=#1a73e8>作者：</font>** Congwei Song  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a general machine learning framework called the localization method, which is fundamentally built on two core concepts: localization kernels and local means -- key components that underpin the self-attention mechanism. To establish a rigorous theoretical foundation, the framework is formally defined through two essential pillars: the formulation of the local(-ized) model and the localization trick. We systematically investigate the connections between the localization method and a wide range of existing machine learning models/methods, including (but not limited to) kernel methods, lazy learning, the MeanShift algorithm, relaxation labeling, Hopfield networks, local linear embedding (LLE), fuzzy inference, and denoising autoencoders (DAEs). By dissecting these relationships, we clarify the broader theoretical significance of the localization method and demonstrate its practical applicability across diverse machine learning tasks. Furthermore, we explore advanced extensions of the framework, such as adaptive kernels, hierarchical local models, and non-local models. Notably, we show that the Transformer -- a cornerstone of modern sequence modeling -- can be constructed using hierarchical local models, revealing the ability of the localization method to unify and generalize state-of-the-art architectures. This work not only provides a unified theoretical lens to reinterpret existing models but also offers new methodological tools for designing flexible, data-adaptive learning systems.

---


### 132. [Same Target, Different Basins: Hard vs. Soft Labels for Annotator Distributions](https://arxiv.org/abs/2605.20642)

**<font color=#1a73e8>作者：</font>** Mirerfan Gheibi, Gashin Ghazizadeh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When annotators disagree, that disagreement can reflect epistemic uncertainty rather than simple label noise. We study hard-label delivery as an alternative to the usual choices of collapsing votes to a single label or training directly on the empirical soft-label distribution. We focus on two primary hard-label methods: multipass, which cycles through observed votes while keeping the dataset size fixed, and stochastic label sampling (SLS), which samples one label per example at the start of each epoch. On CIFAR-10H, we find that when only a small number of annotations per example is available, hard-label delivery improves over soft-label training, with larger improvements where the sparse empirical target is farther from the full annotator distribution. When full annotator distributions are available, both hard-label methods match soft-label training. We use deterministic control as an ablation of multipass and shuffled SLS as a control that breaks the example-to-distribution match. We also show that SLS and soft-label cross-entropy optimize the same expected objective. Hard-label delivery also converges to flatter basins, with supporting descriptive evidence from OOD detection on SVHN and CIFAR-100. Overall, these results suggest that multipass is a strong practical default when raw vote counts are available, while SLS offers a lightweight alternative that remains competitive when only a few votes per example are available and matches soft-label training when full annotator distributions are available.

---


### 133. [AVSD: Adaptive-View Self-Distillation by Balancing Consensus and Teacher-Specific Privileged Signals](https://arxiv.org/abs/2605.20643)

**<font color=#1a73e8>作者：</font>** Duy Nguyen, Hanqi Xiao, Archiki Prasad 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-distillation enables language models to learn on-policy from their own trajectories by using the same model as both student and teacher, with the teacher being conditioned on privileged information unavailable to the student. Such information can come in different types or views, such as solutions, demonstrations, feedback, or final answers. This setup provides dense token-level feedback without relying on a separate external model, but creates a fundamental asymmetry: the teacher may rely on view-specific information that the student cannot access at inference time. Moreover, the best type of privileged information is often task-dependent, making it difficult to choose a single teacher view. In this work, we address both these challenges jointly by introducing AVSD (Adaptive-View Self-Distillation), a novel method of self-distillation with multiple privileged-information views, which reconstructs token-level supervision by separating stable cross-view consensus from view-specific residual signals. AVSD identifies the consensus signal shared across views, which provides a reliable update direction, and then selectively adds the view-specific residual signal to adjust the update magnitude when it both aligns with the consensus direction and remains proportionate to the consensus signal. Experiments on math competition benchmarks (AIME24, AIME25, and HMMT25) show that AVSD consistently outperforms both single-view self-distillation baselines and GRPO, achieving average Avg@8 gains of 3.1% and 2.2% over the strongest baselines on Qwen3-8B and Qwen3-4B, respectively. Moreover, on code-generation benchmarks (Codeforces, LiveCodeBench v6) using Qwen3-8B, AVSD outperforms the single-view self-distillation baseline by 2.4% on average.

---


### 134. [Design for Manufacturing: A Manufacturability Knowledge-Integrated Reinforcement Learning Framework for Free-Form Pipe Routing in Aeroengines](https://arxiv.org/abs/2605.20644)

**<font color=#1a73e8>作者：</font>** Caicheng Wang, Zili Wang, Shuyou Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Design for manufacturing plays a critical role in advanced aeroengine development, where complex components necessitate careful consideration of manufacturability. However, current practices in pipe routing remain largely decoupled from down-stream manufacturing, leading to labor-intensive, trial-and-error iterations to achieve manufacturable designs. To address this problem, this study proposes the Frenet-based pipe routing optimization (FPRO) framework, a manufacturability knowledge-integrated reinforcement learning approach for free-form pipe design in aeroengines. FPRO formulates the routing problem as a boundary value problem in the Frenet frame. In this framework, the pipe path is represented by curvature and torsion profiles, which are generated using cubic Hermite interpolation. To integrate design and manufacturing, domain-specific manufacturing knowledge is embedded as constraints on the permissible ranges of curvature and torsion. The path optimization is performed using the proximal policy optimization algorithm with stochastic exploration and a stage-guided reward mechanism. A unified mapping formulation then translates the optimized path into motion trajectories for the bending die, enabling direct fabrication on a six-axis free-bending machine. Experimental results demonstrate that FPRO consistently generates collision-free, manufacturable paths with smoother geometric profiles compared to Cartesian-based methods. It also achieves faster convergence and superior performance in terminal alignment, path length, obstacle avoidance, and manufacturability compared to state-of-the-art reinforcement learning baselines. Real-world validation confirms the close geometric correspondence between the manufactured pipe and its digital design, validating the practical feasibility of FPRO.

---


### 135. [Seeing Through Fog: Towards Fog-Invariant Action Recognition](https://arxiv.org/abs/2605.20645)

**<font color=#1a73e8>作者：</font>** Enqi Liu, Liyuan Pan, Zhi Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foggy conditions are commonly encountered in real-world applications; however, existing action recognition approaches typically assume favorable weather and high-quality video inputs. On foggy days, unpredictable visibility degradation and reduced contrast obstruct the extraction of semantic cues, posing significant challenges for current action recognition methods. In this paper, we mitigate the issues faced in action recognition under foggy conditions by employing two strategies. First, we present FogAct, the first benchmark dataset for foggy action recognition, consisting of paired clean and foggy videos captured with a stereo camera system. The dataset spans 10 scenes and 55 action categories, comprising nearly 10,000 video clips. Second, we propose FogNet, a two-stream CLIP model that discovers fog-invariant semantic information hidden behind the degraded videos. FogNet learns robust representations of foggy videos with guidance from clean videos, effectively capturing shared structural and motion cues between clean and foggy videos. Extensive experiments on FogAct and three other popular datasets demonstrate that our method achieves competitive performance compared with state-of-the-art (SOTA) approaches. Our FogAct and FogNet are given in our project page.

---


### 136. [Gaze into the Details: Locality-Sensitive Enhancement for OCTA Retinal Vessel Segmentation](https://arxiv.org/abs/2605.20651)

**<font color=#1a73e8>作者：</font>** Tuopusen Huang, Ding Ma, Xiangqian Wu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing deep learning frameworks for Optical Coherence Tomography Angiography (OCTA) vessel segmentation are largely derived from the U-Net architecture, which serves as the foundation for most current designs. However, most of these methods focus only on holistic representation, struggling to address the problem of low local contrast unique to OCTA, which leads to vessel discontinuities and loss of detail. To address these problems, we propose LSENet, which builds upon the U-Net architecture by introducing three core innovative modules: To address vessel discontinuities, we introduce the Patch Information Enhance module (PIE), which replaces standard skip connections to execute patch-wise attention. To mitigate detail loss, the Multiscale Feature Fusion module (MFF) is proposed to feed the PIE module rich, multi-scale information by extracting visually interpretable features from both the original input and preceding layers. Finally, the Connectivity Refinement Decoder (CRD) is designed to refine features from all levels and utilize a large kernel in the final convolutional layer to reduce fragmentation. Experiments on three public datasets (OCTA-500, ROSE-1, and ROSSA) demonstrate that our proposed LSENet achieves state-of-the-art performance while requiring fewer parameters.

---


### 137. [RoPeSLR: 3D RoPE-driven Sparse-LowRank Attention for Efficient Diffusion Transformers](https://arxiv.org/abs/2605.20659)

**<font color=#1a73e8>作者：</font>** Yuxi Liu, Zekun Zhang, Yixiang Cai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) have revolutionized high-fidelity video generation, yet their $\mathcal{O}(L^2)$ attention complexity poses a formidable bottleneck for long-sequence synthesis. While recent sparse-linear attention hybrids aim to mitigate this, their performance severely degrades at extreme sparsity due to the "RoPE Dilemma": standard linear attention fails to preserve the orthogonal relative-position structure of 3D Rotary Position Embeddings (RoPE), neutralizing vital distance awareness. To address this, we propose \textbf{RoPeSLR}, a 3D RoPE-guided Sparse-LowRank attention framework. We establish that under empirically validated assumptions, the DiT attention manifold admits a decoupling into a high-frequency semantic spike set (bounded by $\mathcal{O}(L^{3/2})$ sparsity) and an extreme low-rank ($\mathcal{O}(d_h \log L)$) background continuum. Guided by this structural prior, RoPeSLR eschews standard linear attention for a head-wise low-rank parameterization equipped with a learnable 3D Absolute Positional Embedding (PE) injection, seamlessly synthesizing long-range relative distance decay. By guaranteeing sub-quadratic sparsity and sub-linear rank growth, RoPeSLR is exceptionally suited for scaling to ultra-long video inference. Extensive evaluations validate this scalable superiority: at 90\% sparsity, RoPeSLR achieves up to $10\times$ fewer FLOPs on Wan2.1-1.3B and delivers a $2.26\times$ end-to-end inference speedup on the ultra-long 100K+ token sequences of HunyuanVideo-13B, all while maintaining near-lossless generation fidelity (less than 1.3\% average VBench degradation).

---


### 138. [Design Principles and Observable Indicators for AI-Enabled Pedagogical Accompaniment: Evidence from the Amico Dual-Mode Prototype in Italy and China](https://arxiv.org/abs/2605.20665)

**<font color=#1a73e8>作者：</font>** Pier Paolo Benedetti  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI-enabled systems are increasingly introduced into educational contexts, yet their effectiveness depends less on technological sophistication than on the quality of pedagogical mediation, ethical constraints, and context-sensitive design. This paper proposes a replicable framework for AI-enabled pedagogical accompaniment, grounded in a human-in-command approach in which adult responsibility remains central and AI functions as an enabling, non-substitutive infrastructure. Building on the Amico project, we operationalize the concept of a relational bridge as a sequence of micro-mediations that lower the threshold of access to educational relationships and facilitate transitions toward meaningful human interaction with teachers, peers, and communities of practice. The contribution synthesizes a set of design principles, including transparency of system identity and limits, scaffolding toward human contact, maieutic questioning, prevention of dependency dynamics, and data minimization, and maps them to observable indicators suitable for real educational settings. The paper also outlines an initial cross-context exploration of the prototype in Italy and China and discusses how the two interaction modes, AmicoMio (structured, task-oriented) and AmicoTuo (reflective, supportive), can be used as complementary pedagogical mediations. Pilot observations and participant feedback suggested feasibility and perceived usefulness in vocational contexts, motivating the present framework, informing the subsequent doctoral research program, and supporting the proposed collaborative research agenda.

---


### 139. [LER-YOLO: Reliability-Aware Expert Routing for Misaligned RGB-Infrared UAV Detection](https://arxiv.org/abs/2605.20667)

**<font color=#1a73e8>作者：</font>** Liming Hou, Yueping Peng, Hexiang Hao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting small unmanned aerial vehicles from RGB-infrared remote-sensing pairs remains challenging due to tiny target scale, cluttered backgrounds, and spatial misalignment between heterogeneous sensors. Existing bimodal detectors often align or fuse features without assessing the reliability of local cross-sensor correspondence, allowing mismatch artifacts to propagate into the detection head. To address this issue, we propose LER-YOLO, a reliability-aware sparse mixture-of-experts framework for misaligned RGB-infrared UAV detection. LER-YOLO first introduces an Uncertainty-Aware Target Alignment module that resamples visible features toward the infrared reference and estimates a spatial reliability map. This reliability prior is then used by a Reliability-Guided Sparse MoE Fusion module to adaptively select k experts from RGB-dominant, infrared-dominant, and interactive fusion experts, enabling trustworthy cross-modal interaction while suppressing unreliable fusion. Experiments on the public MBU benchmark under a YOLOv5s-family protocol show that LER-YOLO achieves 89.7+/-0.2% AP50 over three independent seeds, with a best result of 89.9%. Extensive ablations, parameter-matched comparisons, synthetic-shift evaluations, and complexity analysis demonstrate that the gains mainly come from reliability-guided expert routing rather than increased model capacity.

---


### 140. [GSA-YOLO: A High-Efficiency Framework via Structured Sparsity and Adaptive Knowledge Distillation for Real-Time X-ray Security Inspection](https://arxiv.org/abs/2605.20669)

**<font color=#1a73e8>作者：</font>** Jiahao Kong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> X-ray security inspection requires accurate real-time detection of prohibited items, but existing models often struggle to balance the challenges of severe occlusion, complex clutter, and strict speed requirements. To overcome these challenges, this paper proposes GSA-YOLO, a novel lightweight framework built upon the YOLOv8n architecture, specifically engineered to enhance detection robustness and inference efficiency. GSA-YOLO strategically integrates structured sparsity and adaptive knowledge transfer through three core components: Group Lasso (GL) applied to the network neck for robust feature extraction; Sparse Structure Selection (SSS) applied to the detection head for significant model slimming; and an Adaptive Knowledge Distillation (Ada-KD) mechanism for comprehensive accuracy recovery. This integrated approach synergistically enhances feature representation while pruning redundant channels, maximizing model efficiency without sacrificing performance. Rigorous evaluations on the HiXray and PIDray datasets confirm GSA-YOLO's comprehensive capability, achieving a leading inference speed of 189.62 FPS, accompanied by a reduction in computational cost from 8.7G to 8.0G. Crucially, GSA-YOLO secures mAP50:95 results of 0.531 and 0.679 on HiXray and PIDray, demonstrating 2.4% and 1.8% improvements over the baseline, respectively. Compared to other models, GSA-YOLO exhibits enhanced accuracy while maintaining computational efficiency, making it a promising solution for practical X-ray security inspection.

---


### 141. [LT2: Linear-Time Looped Transformers](https://arxiv.org/abs/2605.20670)

**<font color=#1a73e8>作者：</font>** Chunyuan Deng, Yizhe Zhang, Rui-Jie Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Transformers (LT) have emerged as a powerful architecture by iterating their layers multiple times before decoding the final token. However, pairing them with full attention retains quadratic complexity, making them computationally expensive and slow. We introduce LT2 (Linear-Time Looped Transformers), a family of looped architectures that replace quadratic softmax attention with subquadratic, linear-time attention. We study two variants: LT2-linear with linear attention and LT2-sparse with sparse attention. We find that looping uniquely synergizes with these variants: it enables iterative memory refinement in linear attention and progressively expands the effective receptive field in sparse attention. We formalize these benefits theoretically and demonstrate consistent empirical gains across controlled recall, state-tracking, and language modeling tasks. We then explore LT2-hybrid, which combines different attention variants in a looped setting. Two variants are especially promising: LT2-hybrid (GDN+DSA), which interleaves linear and sparse attention to maximize efficiency and matches the standard looped transformer's quality at fully linear-time cost; and LT2-hybrid (Full+GDN), which interleaves GDN with a small fraction of full attention layers to maximize quality, surpassing the standard looped transformer in both performance and efficiency. We also show how to convert a pre-trained LT into an LT2-hybrid model. With about 1B tokens of training, our converted model, Ouro-hybrid-1.4B, outperforms industry-level 1B models and is competitive with industry-level 4B models while retaining the speed benefits of linear-time attention. Together, these results show a clear path toward making looped transformers more scalable and advancing efficient, capable small language models.

---


### 142. [DarkShake-DVS: Event-based Human Action Recognition under Low-light andShaking Camera Conditions](https://arxiv.org/abs/2605.20680)

**<font color=#1a73e8>作者：</font>** Jiaqi Chen, Qinfu Xu, Liyuan Pan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human Action Recognition (HAR) is a fundamental computer vision task with diverse real-world applications. Practical deployments often involve low-light environments and unconstrained 6-DoF camera motion, conditions that degrade visual quality, disrupt temporal coherence, and compromise reliability of existing methods. Event cameras, with high low-light sensitivity and microsecond-level temporal resolution, paired with an inertial measurement unit (IMU), present a promising solution. However, current research faces two key challenges: absence of a benchmark integrating low-light conditions, 6-DoF motion, and synchronized IMU data; and lack of effective motion compensation techniques. To address these, we propose Event-IMU Stabilized HAR (EIS-HAR), with two modules. The first is an EIS module that reduces motion blur via a non-linear warping function to reconstruct a motion-compensated input. The second is a HAR module with a four-stage hybrid architecture to efficiently extract spatiotemporal features for accurate action recognition. To alleviate data scarcity, we introduce DarkShake-DVS, the first large-scale event-based HAR benchmark that includes 18,041 realworld clips captured in low light and intense 6-DoF motion, supplemented by synchronized IMU data. Extensive experiments on three datasets demonstrate consistent superiority of EIS-HAR over state-of-the-art methods.

---


### 143. [Beyond Semantic Similarity: A Two-Phase Non-Parametric Retrieval Workflow for Corporate Credit Underwriting](https://arxiv.org/abs/2605.20684)

**<font color=#1a73e8>作者：</font>** Linus Ng Junjia, Ezekiel Tee Kongquan, Kelvin Heng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Corporate credit underwriting requires analysts to extract actionable evidence from long, heterogeneous financial documents spanning hundreds of pages and multiple languages. Standard Retrieval-Augmented Generation (RAG) pipelines optimize for semantic similarity, which frequently surfaces passages that are topically related but lack decision utility, a problem we term the similarity-utility gap. We propose a two-phase non-parametric retrieval architecture that separates high-recall candidate retrieval from high-precision utility ranking. The first phase combines lexical and dense multilingual retrieval to construct a broad candidate pool. The second phase applies an adaptive retrieval controller that filters candidates using query intent and document structure signals, followed by an LLM-as-a-Judge utility scoring mechanism that ranks passages by analytical usefulness rather than semantic proximity.
A context-aware extraction module preserves structural fidelity across narrative text and complex financial tables. The system is deployed entirely on-premise to satisfy enterprise data governance requirements. Evaluated on a multilingual corpus of proprietary financial documents with analyst-curated relevance labels, the system significantly outperforms naive retrieval baselines. In production deployment across more than 800 credit analysts, document review time was reduced from several hours to approximately three minutes, demonstrating the practical value of utility-aware RAG architectures for document-intensive decision-support workflows.

---


### 144. [DIVE: Embedding Compression via Self-Limiting Gradient Updates](https://arxiv.org/abs/2605.20689)

**<font color=#1a73e8>作者：</font>** Dongfang Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> High-dimensional embeddings from large language models impose significant storage and computational costs on vector search systems. Recent embedding compression methods, including Matryoshka-Adaptor (EMNLP 2024), Search-Adaptor (ACL 2024), and SMEC (EMNLP 2025), enable dimensionality reduction through lightweight residual adapters, but their training objectives cause severe overfitting when labeled data is scarce, degrading retrieval performance below the frozen baseline. We propose \textsc{DIVE} (\textbf{D}imensionality reduction with \textbf{I}mplicit \textbf{V}iew \textbf{E}nsembles), a compression adapter that addresses this failure through two mechanisms. First, a self-limiting hinge-based triplet loss produces zero gradient once a triplet satisfies the margin constraint, bounding the total perturbation applied to the pretrained embedding space. Second, a head-wise NT-Xent contrastive loss treats multiple learned projections of each embedding as implicit views, providing dense self-supervised gradients that compensate for the sparsity of the triplet signal on small datasets. Across six BEIR datasets, \textsc{DIVE} outperforms all three baseline adapters on every dataset and at every evaluated compression ratio, with a 14M-parameter open-source implementation.

---


### 145. [Interpretable Discriminative Text Representations via Agreement and Label Disentanglement](https://arxiv.org/abs/2605.20693)

**<font color=#1a73e8>作者：</font>** Tong Wang, Yiqing Xu, Leo Yang Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Interpretable text representations should expose coordinates that are not only predictive, but also meaningful enough for independent auditors to apply. Existing discriminative representations often use anonymous embedding directions, while concept-bottleneck and LLM-assisted methods attach natural-language names to features without ensuring that those definitions are reproducible or distinct from the target label. We propose an operational criterion for interpretable discriminative text representations: each coordinate should satisfy conceptual clarity, measured by chance-adjusted agreement between independent annotators applying the feature definition, and label disentanglement, meaning the feature should not merely paraphrase the prediction target. We instantiate this criterion in LLM-assisted Feature Discovery (LFD), an iterative method that proposes lexical and semantic features from contrastive outcome-opposed text pairs, screens candidates using cross-LLM Cohen's $\kappa$, and selects features by residual held-out predictive gain. A stylized analysis connects the $\kappa$ screen to a per-feature annotation-noise bound, formalizing agreement as a reliability check. Across ten text-classification tasks spanning seven corpora, LFD matches the predictive performance of a strong text bottleneck baseline while producing substantially clearer and less label-entangled features. Human audits with 232 raters show that LFD features achieve higher human--human and human--LLM agreement than baseline concepts, and raters consistently judge them as less label-leaking. These results suggest that agreement-tested, label-disentangled coordinates provide a practical auditability standard for interpretable text classification.

---


### 146. [Distributed Direct Preference Optimization](https://arxiv.org/abs/2605.20696)

**<font color=#1a73e8>作者：</font>** Zhanhong Jiang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Preference-based reinforcement learning (RL) is a key paradigm for aligning policies with human judgments, yet its theoretical behavior in distributed settings where preference data are fragmented across heterogeneous users remains poorly understood. Direct Preference Optimization (DPO) avoids explicit reward modeling but lacks convergence guarantees under federated and decentralized training, where communication constraints and non-IID preferences fundamentally alter optimization dynamics. We provide the first convergence and time-complexity analysis of DPO in distributed environments. Modeling personalized offline RL with user-specific preference distributions, we characterize the induced global optimization landscape. For federated DPO, we derive convergence rates that quantify the impact of client drift, communication frequency, and preference heterogeneity; for decentralized DPO, we establish convergence over general communication graphs and show how spectral connectivity governs optimization speed and consensus. Empirically, we corroborate our theoretical insights on standard alignment benchmarks, demonstrating that our proposed methods not only enjoy strong theoretical guarantees but also deliver robust and scalable performance in practice. The code base is available here.

---


### 147. [CandorMD: An AI-Assisted Audio Simulation and Feedback System for Training Clinicians for Medical Error Disclosure](https://arxiv.org/abs/2605.20701)

**<font color=#1a73e8>作者：</font>** Inna Wanyin Lin, Sahand Sabour, Hong Sng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Clinicians are expected to disclose harmful medical errors to patients and families in line with ethical, regulatory, and patient care standards, yet these conversations remain challenging because of their emotional complexity and limited training opportunities. Most physicians still learn primarily through lectures and observation, while static video tools-though available-are underused, lack adaptability across specialties, and deliver delayed, generic feedback. These gaps restrict skill development, reduce self-efficacy, and contribute to avoidance of disclosure conversations, ultimately compromising patient care and eroding trust. To address these needs, we designed CandorMD -- an AI-assisted simulation system that provides real-time practice, actionable feedback, and diverse practice environments tailored to individual learning needs. We conducted semi-structured interviews with physicians, risk managers, patient advocates, and communication experts to understand current practices, identify gaps, and collect feedback on CandorMD. Based on these insights, we present findings and design recommendations for the future of AI-supported medical communication training.

---


### 148. [Heartbeat-Bound Hierarchical Credentials: Cryptographic Revocation for AI Agent Swarms](https://arxiv.org/abs/2605.20704)

**<font color=#1a73e8>作者：</font>** Saurabh Deochake  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous AI agents that spawn sub-agent swarms create a safety gap: existing credential revocation mechanisms, OAuth~2.0 introspection, OCSP, and W3C Status Lists, require network connectivity to a central authority, leaving ``zombie agents'' executing privileged operations for minutes to hours after operator shutdown. We present Heartbeat-Bound Hierarchical Credentials (HBHC), a cryptographic protocol that binds credential validity to periodic parent liveness proofs. Verifiers enforce freshness using only a cached public key and local clock; no network round-trip is required. When heartbeat generation ceases, all descendant credentials become unusable within a deterministically bounded window $W_z \le W_{\max} + \Delta_h + \epsilon$, conditional on bounded clock skew and parent keys held in secure enclaves. Evaluation at the protocol layer and with real LLM-backed agent swarms (GPT-4o-mini) demonstrates a 90$\times$ reduction in the zombie window over OAuth~2.0, 0.26~ms full authentication in Rust, 18,000+ verifications per second under concurrent HTTP load, and stable per-verification latency from 10 to 10,000 agents. Real-agent experiments show 0.71\% end-to-end overhead on tool calls, zero post-revocation tool calls under prompt injection that bypasses application-layer guardrails, and cascading revocation across a 49-agent four-level hierarchy within the theoretical bound.

---


### 149. [Rethinking Cross-Layer Information Routing in Diffusion Transformers](https://arxiv.org/abs/2605.20708)

**<font color=#1a73e8>作者：</font>** Chao Xu, Maohua Li, Qirui Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) have become a de facto backbone of modern visual generation, and nearly every major axis of their design -- tokenization, attention, conditioning, objectives, and latent autoencoders -- has been extensively revisited. The residual stream that governs how information accumulates across layers, however, has been directly inherited from the original Transformer. In this paper, we present a systematic empirical analysis of cross-layer information flow in DiTs, jointly along depth and denoising timestep, and identify three concrete symptoms of traditional residual addition, namely monotonic forward magnitude inflation, sharp backward gradient decay, and pronounced block-wise redundancy. Motivated by this diagnosis, we propose Diffusion-Adaptive Routing (\textsc{DAR}), a drop-in residual replacement that performs \emph{learnable, timestep-adaptive, and non-incremental} aggregation over the history of sublayer outputs. Moreover, the proposed \textsc{DAR} is compatible with many modern Transformer enhancement methods, such as REPA. On ImageNet $256\times256$, \textsc{DAR} improves SiT-XL/2 by $2.11$ FID ($7.56$ vs.\ $9.67$) and matches the baseline's converged quality with $8.75\times$ fewer training iterations. Stacked on top of REPA, it yields a $2\times$ training acceleration in the early stage, suggesting cross-layer information routing as an underexplored design axis in diffusion modeling, one that operates orthogonally to existing representation-alignment objectives. Beyond pretraining, \textsc{DAR} can also be applied during the fine-tuning stage of large-scale T2I models and preserves high-frequency details during Distribution Matching Distillation.

---


### 150. [SCRIBE: Diagnostic Evaluation and Rich Transcription Models for Indic ASR](https://arxiv.org/abs/2605.20712)

**<font color=#1a73e8>作者：</font>** Kavya Manohar, Arghya Bhattacharya, Kush Juvekar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition replaces typing only when correction costs less than manual entry, a threshold determined by error types, not counts: fixing a misrecognized domain term costs far more than inserting a comma. Word error rate (WER) fails on two fronts: it collapses distinct error categories into a single scalar, and it structurally penalizes agglutinative languages where valid sandhi merges inflate scores. We introduce SCRIBE, a diagnostic framework that provides categorical error decomposition into lexical, punctuation, numeral, and domain-entity rates through sandhi-tolerant alignment with domain vocabulary injection. Human validation confirms SCRIBE aligns with expert judgment where WER does not. We release SCRIBE, an LLM curation pipeline, benchmarks, and open-weight rich transcription models for Hindi, Malayalam, and Kannada.

---


> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-352](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
