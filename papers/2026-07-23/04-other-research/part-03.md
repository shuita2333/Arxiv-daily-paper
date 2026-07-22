# 📦 其他研究 | 2026年07月23日

> 本类共 **241** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-241](./part-05.md)

---

### 101. [Cross-Dataset Generalization in Breast MRI Tumor Classification via Class-Wise Dataset Mixing](https://arxiv.org/abs/2607.18678)

**<font color=#1a73e8>作者：</font>** Mohammad Ali Dadrast, Hamid Usefi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Breast MRI is highly sensitive for detecting breast tumors, but exams contain many slices and require substantial reading time. Deep learning models often perform well on internal splits but can fail across institutions because of domain shift and dataset-origin bias. We study this failure mode for binary breast MRI tumor classification. EfficientNet-B3 and WaveViT-Small are trained using Duke Breast Cancer MRI and fastMRI, and evaluated only on the independent multi-center MAMA-MIA cohort. In a deliberately confounded setup, where label is perfectly correlated with dataset origin, external accuracy is near chance (0.5048--0.5265), despite very high recall. We then construct a mixed training set in which each class contains samples from both Duke and fastMRI, while preserving patient-level splitting, augmentation, and leakage controls. On MAMA-MIA, dataset mixing improves accuracy/F1 to 0.8463/0.8625 for WaveViT-Small and 0.8884/0.8994 for EfficientNet-B3. These results show that controlling dataset-origin bias is important for reliable breast MRI classification.

---


### 102. [Dual-Edged Homogeneous-Modality Similarity: Towards Visible-Infrared Modality-Incomplete Person Re-Identification with Modality Adaptive Matching](https://arxiv.org/abs/2607.18688)

**<font color=#1a73e8>作者：</font>** Xin Xu, Shuhao Zhan, Wei Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visible-Infrared Person Re-Identification (VI-ReID) operates under a closed-world assumption, where queries and galleries are from heterogeneous modalities. However, in open-world scenarios, both sets are likely to contain homogeneous and heterogeneous modality images. A query may consist of visible-only, infrared-only, or mixed-modality images, while galleries present multi-modal images over long-term collection. Under these conditions, VI-ReID methods, built on a heterogeneous-modality retrieval paradigm, suffer from three trustworthiness challenges: matching conflicts due to high homogeneous-modality similarity, interference from modality uncertainty, and robustness degradation induced by unknown modality combinations. They fail to meet the requirements of trustworthy visual recognition in reliability, consistency, and dynamic adaptability. To address these challenges, we formalize the Visible-Infrared Modality-Incomplete Re-Identification (VIMI-ReID) task. We reorganize existing datasets to construct the SYSU-VIMI and RegDB-VIMI benchmarks. The unpredictable modality combinations and inherent similarity of homogeneous-modality samples in VIMI-ReID cause a significant performance drop in existing VI-ReID methods. We propose the Modality Adaptive Matching Transformer (MAMT). It employs a Divergence Transformer Module (DTM) and a Shared Transformer Module (STM) to extract modality-specific and modality-shared features, respectively. Guided by a divergence loss, the DTM enriches modality-specific features with modality-style information to enhance discriminability within the same modality. A Modality Adaptive Matching Module (MAM) dynamically fuses features according to the query-gallery modality relationship, enabling stable matching under arbitrary and uncertain modality conditions. Extensive experiments on the VIMI benchmarks demonstrate the effectiveness and adaptability of MAMT.

---


### 103. [Exposure-Based Reinforcement Learning to Rank](https://arxiv.org/abs/2607.18689)

**<font color=#1a73e8>作者：</font>** Harrie Oosterhuis, Rolf Jagerman, Zhen Qin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) methods for learning-to-rank (LTR) can optimize (almost) any ranking goal, e.g., from precision or discounted cumulative gain to fairness-of-exposure or ranking distillation. However, standard RL is ineffective and computationally costly due to the enormous action space in LTR settings. Existing methods reach computational efficiency through custom gradient computation algorithms, but they are very complex to implement and often clash with auto-differentiation. Consequently, existing RL for LTR is not attractive to many practitioners. We reconsider RL for LTR while actively avoiding reliance on custom gradients. Contrary to the existing approaches, we focus on variance reduction and GPU computation. In doing so, we discover that high sample-efficiency can be reached through baseline corrections and partial marginalization. Furthermore, we propose an abstraction that places gradient estimation behind a document-exposure distribution, this enables seamless plug-and-play integration with auto-differentiation. Thereby, one only has to implement a loss as a differentiable function of exposure and RL for LTR can optimize it using auto-differentiation. Our experimental results reveal that our new exposure-based RL for LTR approach converges considerably faster and at significantly higher ranking performance than existing custom gradients, with no additional costs in computation time when using GPUs. In contrast, existing custom gradients result in severe stability issues when converging over many epochs, which never occur for our methods. Thus, we considerably improve RL for LTR methodology by increasing its effectiveness, efficiency, and ease of application.

---


### 104. [Rationale-Guided Knowledge Distillation for Cross-Lingual Stance Detection](https://arxiv.org/abs/2607.18693)

**<font color=#1a73e8>作者：</font>** Qiuli Zhou, Jingyuan Yao, Shengeng Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Stance detection aims to identify whether a text expresses a favorable or opposing attitude toward a given target, and serves as an important task for various downstream applications. Although existing studies have achieved strong performance in monolingual settings, especially in English, many low-resource languages such as Catalan still lack sufficient annotated data for training effective models. Cross-lingual stance detection alleviates this problem by transferring stance knowledge from resource-rich languages to low-resource languages. However, most existing methods mainly rely on semantic alignment between texts and targets, while ignoring the reasoning process required for reliable stance inference. Although Large Language Models provide strong reasoning ability, their high computational cost and inference latency limit practical deployment. To address these limitations, we propose a rationale-guided knowledge distillation framework for cross-lingual stance detection. Specifically, we use Chain-of-Thought prompting to guide Large Language Models in generating informative rationales, and distill the resulting reasoning knowledge into a compact student model. We further design a dual-path distillation mechanism to align rationale-enhanced and rationale-free representations, together with their prediction distributions. In addition, two contrastive learning strategies are introduced to improve stance discrimination. Experiments on multilingual benchmarks demonstrate that our method consistently outperforms competitive baselines.

---


### 105. [Decoupled Pipeline with Proposal Reranking and Score Fusion for Positive-Unlabeled Marine Species Detection](https://arxiv.org/abs/2607.18700)

**<font color=#1a73e8>作者：</font>** Robert James Brock, Sebastian Maximilian Krupa, Jason Kahei Tam  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The FathomNetCLEF 2026 competition combines underwater object detection and fine-grained marine species classification under a positive-unlabeled evaluation setting. The provided training labels are sparse, while the hidden test set is out-of-distribution relative to the training imagery, creating both annotation incompleteness and source-shift challenges. We describe DS@GT ARC's multi-stage system developed for this setting while keeping model training restricted to the data provided by the competition. The final private-leaderboard model uses a frozen Megalodon YOLOv8x detector as a class-agnostic proposal generator, combines global and tiled inference with tile-edge filtering, classifies expanded proposal crops with a LoRA-finetuned DINOv3 ViT-H classifier, and ranks predictions using weighted geometric fusion of detector and classifier confidence. This system placed 12th out of 102 teams. A closely related variant added a locally trained TTN-inspired validity head as a light reranking signal, improving public-leaderboard and proxy-evaluation performance but slightly reducing private-leaderboard performance. Across experiments, the strongest lesson was that train-derived validation and detector-only metrics were not reliable enough for model selection. Instead, we used proxy datasets only for validation and comparison, and combined those signals with leaderboard feedback and targeted ablations. These experiments showed that reserving proposal recall, avoiding over-aggressive filtering, and improving downstream ranking were more effective than fine-tuning the detector or directly training on noisy pseudo-labels. Code: this https URL.

---


### 106. [Generative World Renderer at the Speed of Play](https://arxiv.org/abs/2607.18703)

**<font color=#1a73e8>作者：</font>** Guixu Lin, Zheng-Hui Huang, Siqi Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative world renderer AlayaRenderer receives structured world states exported from physics engines and synthesizes RGB frames. Unlike models that generate frames from text/control-hints prompts, AlayaRenderer preserves scene structure without altering the underlying world dynamics. This demonstrates an alternative path toward interactive world modeling and user-controllable play. However, the original AlayaRenderer is too computationally expensive for real-time deployment. This technical report introduces AlayaRenderer-Flash, a real-time-oriented generative forward world renderer that pushes AlayaRenderer from 0.56 FPS to 31.54 FPS, reaching the speed of play. AlayaRenderer-Flash reformulates the original renderer as a few-step autoregressive streaming model and introduces lightweight distilled codecs for efficient latent encoding and frame reconstruction. It retains the teacher model's G-buffer and text-prompt interfaces while enabling continuous rendering over input streams of unbounded length. We evaluate AlayaRenderer-Flash on G-buffer streams across content preservation, temporal consistency, cross-window stability, prompt controllability, and runtime efficiency. Our results show that AlayaRenderer-Flash substantially reduces inference cost while preserving the core rendering capabilities of the teacher model. By integrating AlayaRenderer-Flash with a physics engine, we build a fully playable generative world running at 30 FPS.

---


### 107. [Strategy-Following Multi-Agent Deep Reinforcement Learning Considering Control Strategies Provided to Other Agents](https://arxiv.org/abs/2607.18719)

**<font color=#1a73e8>作者：</font>** Yamato Takahagi, Gentoku Nakasone, Yoshinari Motokawa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> This study proposes a learning method for multi-agent systems that allows agents to be controlled through human manager instructions after learning and enables uninstructed agents to implicitly complement the overall work based on the actions of other agents. Multi-agent applications using deep learning have shown potential; thus, to achieve extensive social applications, humans should be able to control learned agents using simple methods to respond to environmental and social changes. Even without such changes, learned coordination often does not match the expectations of human managers, making it preferable to control coordination structures to match human intentions. Some studies have aimed to control agent behavior using simple instructions. However, they assumed that instructions are provided to all agents, which is time-consuming and not evident when designing a better cooperation regime. Ideally, specific agents should receive key action instructions, while others should automatically complete the remaining tasks. The proposed method, which extends previous work on controllability in multi-agent deep reinforcement learning, enables uninstructed agents to adaptively complement overlooked tasks and areas. The experimental results show that agents using the proposed method can shift to another cooperative structure and achieve better performance than those using conventional methods.

---


### 108. [Stale but Stable: Staleness-Adaptive Trust Regions for Stabilizing Asynchronous Reinforcement Learning](https://arxiv.org/abs/2607.18722)

**<font color=#1a73e8>作者：</font>** Junyao Yang, Yucheng Shi, Zongxia Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Asynchronous reinforcement learning improves throughput by decoupling rollout generation from optimization, but staleness is an inevitable byproduct compounded by policy lag, engine delays, and mixture-of-experts routing. From a trust-region perspective, this mismatch is critical: training-inference divergence governs approximation error in finite-horizon bounds, whereas PPO clipping only gates sampled outward updates, acting as a sampled surrogate rather than a full-policy constraint. As a result, high-staleness updates remain weakly controlled in the asynchronous regime where stale rollouts matter most.
We introduce the Staleness-Adaptive Trust Region (SAT), which uses the detached sampled log-ratio as a practical staleness proxy, identifies high-mismatch tails within each batch via staleness-based kernel scaling, and contracts only the sign-selected endpoint of the nominal PPO interval. This preserves baseline behavior on ordinary tokens while enforcing more conservative updates on newly intercepted outward bands. We prove local interval containment and pointwise pessimism relative to PPO, showing how the adaptive rule reshapes update geometry under heterogeneous staleness.
We evaluate SAT in a decoupled asynchronous RL setup built on Qwen3-30B-A3B-Base, using SGLang as the inference engine and Megatron for training. In this setting, SAT-GSPO w/ R3 achieves the best observed AIME24 avg@8, reaching 35.83 at lag 1 and 34.79 at lag 8, while SAT-GSPO reaches 34.17 at lag 1. Adaptive clipping and routing replay act as complementary stabilizers targeting mismatch tails and routing inconsistency, respectively. Overall, aligning clip intervals with staleness heterogeneity effectively stabilizes asynchronous RL.

---


### 109. [One Rewrite to Fix Them All? Type-Aware Repair Allocation for Text-to-Image Prompt Optimization](https://arxiv.org/abs/2607.18724)

**<font color=#1a73e8>作者：</font>** Haoyue Liu, Xiaoyu Ma, Ye Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) generators often fail to follow their prompts faithfully, producing wrong counts, swapped attributes, ambiguous relations, and illegible text. Prompt optimization repairs such failures by rewriting the user prompt, requiring no generator retraining, and has yielded promising results. However, existing optimizers absorb heterogeneous failures into one uniform prompt expansion, even though each calls for different repair language. We formulate semantic prompt optimization as atomic repair allocation: each failed proposition is routed to a type-conditioned repair operator before the resulting local constraints are compiled into one executable prompt. We instantiate this formulation in the training-free Type-Aware Repair Allocation (TARA) framework, which separates diagnosis, allocation, compilation, and a semantic repair gate, an accept-or-revert controller over exactly one prescribed repair that prevents semantic regressions. Extensive experiments on DSG and TIFA across four frozen generators demonstrate that TARA achieves the best semantic accuracy in all eight benchmark-generator cells, improving over VisualPrompter by 5.6 and 2.6 points on DSG and TIFA, respectively, while maintaining image quality and running fastest in our matched local setting at 16.0 seconds versus 20.0 seconds per prompt.

---


### 110. [Dual Attention Residuals](https://arxiv.org/abs/2607.18730)

**<font color=#1a73e8>作者：</font>** Xingda Yu, Yining Li, Xinzhang Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work extends Transformer residual pathways along two complementary axes: historical retrieval selects information from earlier depths, whereas multi-stream methods maintain multiple residual trajectories. These capabilities have largely been studied in isolation, and assigning an independent retriever to each stream still prevents one trajectory from influencing depth selection in another. We propose Dual Attention Residuals (DAR), which brings multi-stream interaction into historical retrieval through reciprocal cross-stream addressing. For each target stream, DAR computes depth weights from normalized states in the opposite stream and applies them to values from the target stream's own history. The retrieved states are combined for an unchanged Transformer branch and updated through constrained gated writes; a block-form variant operates on block-level histories to control overhead. Across dense models from 0.1B to 1B parameters and a 7B sparse-MoE model, DAR consistently improves validation loss over standard residual Transformers and Attention Residuals. Routing ablations show that the gain cannot be explained by an additional stream or value projection alone. Representation and intervention analyses further show that reciprocal cross-stream selection preserves depth-wise diversity and avoids the redundancy or functional imbalance observed in alternative two-stream designs.

---


### 111. [Contraction-Gauge Preconditioning for Quantized Matrix Multiplication](https://arxiv.org/abs/2607.18745)

**<font color=#1a73e8>作者：</font>** Piyush Sao, Narasinga Miniskar, Pedro Valero-Lara 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study low-precision computation of C=AB with both factors quantized. We derive an exact finite-dimensional identity for the expected squared product error under independent, zero-mean entrywise errors with known variance fields; it holds exactly for non-overloading subtractive dither and for independent stochastic rounding, and we empirically assess deterministic round-to-nearest (RTN). Using the product-preserving equivalence AB=(AT)(T^{-1}B), we formulate contraction-gauge preconditioning: jointly choosing a factor representation and its sharing pattern before quantization. Preconditioning can reduce product error but may require extra transformed, quantized copies of the opposite operand: a shared transform needs one copy, a block-specific transform up to one per block. Within the bounded family of positive diagonal gauges (folds), a geometric program computes a globally optimal shared fold and a linear program decides whether the identity fold is already optimal. For other families we derive computable selection statistics -- tail index for scaling, profile spread for partitioning, coherence and weighted-Gram energy for rotations, slice-energy covariance for hierarchy depth -- with upper bounds for ranking heuristic candidates. Across twelve linear products from a trained three-block image classifier, median within-product rank correlations between dither-model predictions and deterministic-RTN errors are 0.937 at 8 bits and 0.918 at 4 bits. The GP fold cuts held-out product error over the identity fold by 18.0% (8-bit) and 20.5% (4-bit) in geometric mean, beats a SmoothQuant-style grid baseline at both precisions and on ten of twelve products, and lowers composed logit MSE by 15.4% and 26.4%. We thus provide exact stochastic product-error accounting, certified selection within the diagonal family, and a common objective for evaluating reusable transform candidates under RTN.

---


### 112. [SkyEV: RGB-Event UAV detection and tracking dataset and baseline](https://arxiv.org/abs/2607.18747)

**<font color=#1a73e8>作者：</font>** Jakub Mandula, Sebastian Heusinger, Julian Moosmann 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting UAVs in air spaces has become increasingly important due to UAVs widespread availability and easy usage. However, due to their small size, they are typically difficult to detect at a sufficient range. For the training of optimized detection algorithms, datasets have been published, covering optical sensing methods ranging from infrared to regular RGB to event-sensor-based. However, these datasets often fail to reflect realistic counter-UAV scenarios, lacking critical factors such as camera ego-motion, extremely small target scales, and diverse lens configurations, and introduce compression artefacts on the frame images. To address this gap, we introduce SkyEV, an open-source dataset featuring highly synchronized uncompressed RGB and event-based data. SkyEV distinguishes itself by capturing complex real-world conditions, including significant camera motion and varied optical setups, which are essential for testing the fundamental trade-off between Field of View and detection range. Furthermore, we provide a unified data loader and establish an experimental baseline using a multi-modal architecture, demonstrating the dataset's efficacy in detecting challenging, small-scale targets.

---


### 113. [ConceptCF: Concept-based Counterfactuals for the Explainability of Time Series](https://arxiv.org/abs/2607.18748)

**<font color=#1a73e8>作者：</font>** Annemarie Jutte, Faizan Ahmed, Jeroen Linssen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes ConceptCF, a method for counterfactual generation that operates on human-interpretable concepts. In high-stakes domains such as healthcare and predictive maintenance, artificial intelligence models can increase efficiency and safety. Explainability is key to ensure these models rely on causal relationships rather than spurious correlations. Counterfactual explanations identify minimal modifications that would change a model's predictions. Existing methods for time series operate on individual points or subsequences without ensuring interpretability of the mutations. ConceptCF instead modifies meaningful concepts. As a result we can provide explanations in terms of these concepts, for example ``the model's prediction would be `Sit' instead of `Walk' if you increase the scale of the movement''. In this paper, the concepts are constructed through time series decomposition, resulting in concepts such as scale, and frequency bands. Counterfactuals are generated using a genetic algorithm that optimizes the concept mutations. Evaluation against five state-of-the-art approaches demonstrates that ConceptCF consistently achieves top-tier performance across validity, confidence, proximity, sparsity and plausibility metrics.

---


### 114. [Is EEG-to-Text Feasible in Real-World Scenarios? An In-Depth Analysis Using a Neuropsychology-Inspired Benchmark](https://arxiv.org/abs/2607.18749)

**<font color=#1a73e8>作者：</font>** Zihan Zhang, Yu Bao, Xiao Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Translating brain signals into text could restore communication for people with severe paralysis, yet practically usable systems to date rely on invasive electrocorticography (ECoG). Electroencephalography (EEG) offers a non-invasive alternative, and EEG-to-text (EEG2Text) has been widely explored. Interestingly, however, EEG2Text models generally rely on teacher-forcing evaluation; without it, they fail to generate meaningful decoding. This reliance prevents EEG2Text from being applied in real-world, non-academic settings. This has fueled numerous debates about whether EEG2Text is a meaningful direction, by extension, and whether EEG truly contains decodable linguistic information. Here, using a neuropsychology-informed paradigm, we find that existing EEG2Text benchmarks have neglected EEG instability, a flaw that has confounded inference and sparked debate. Our experiments furnish key evidence for the feasibility of teacher-forcing-free EEG2Text decoding. Accordingly, we assemble the Corpus OF Eeg-To-Text (COFETT) using a 128-channel high-density EEG cap, providing a benchmark dedicated to evaluating EEG2Text models. In comparisons with multiple existing benchmarks, COFETT achieves SOTA ability to distinguish among model performances and enables robust, teacher-forcing-free evaluation, thereby opening a path toward practical EEG2Text applications. COFETT is open sourced in this https URL.

---


### 115. [Decafs: Disentangled Conditional adversarial Flows](https://arxiv.org/abs/2607.18755)

**<font color=#1a73e8>作者：</font>** Anirudh jain, Sakshi Varshney, Samuel Kaski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow-based models have established state-of-the-art performance in generative modeling across domains, but are hard to interpret due to their complex latent embeddings. In particular, the entanglement of generative factors in the latent space hinders controlled generation. We circumvent this issue by appealing to a novel conditional generator based on Lie groups that disentangles an alternative latent space, which is aligned closely with the latent flow space using an adversarial loss. Our approach facilitates interpretable conditional generation while obviating the need to expand the dimensionality of the flow space (owing to its invertibility requirements). The proposed model demonstrates strong performance across conditional image (including, outperforming StyleGAN on MNIST, dSprites) and molecule (using standard QM9, ZINC and MOSES) generation tasks

---


### 116. [Relative Positions Generalize, Absolute Positions Memorize: An Implicit-Bias Account of Length Generalization in Attention](https://arxiv.org/abs/2607.18759)

**<font color=#1a73e8>作者：</font>** Subham Singh, Ashutosh Mishra, Subha Raut  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers with relative positional encodings often extrapolate to sequences longer than those seen during training, whereas transformers with learned absolute encodings typically do not. This is a robust empirical regularity, and the explanations offered for it so far are chiefly about expressivity, that is, about whether a length-generalizing solution exists. We give an optimization explanation. On a minimal fixed-offset retrieval task that isolates positional selection, the gap is governed by the implicit bias of the trained attention head: among the many solutions that fit short sequences, which one gradient descent actually selects. We prove that rotary encodings make the attention logit a function of relative offset alone, an exact equivariance, so whatever selection rule is learned at training lengths is reproduced verbatim at every longer length. Learned absolute encodings instead leave out-of-range positions unconstrained, and the trained head pins to a fixed absolute position inside the training range. We characterize the learned rotary rule as a low-rank ``carrier'' kernel aligned with the target offset, and we derive the resulting graceful accuracy decay as an attention-dilution law; both predictions are confirmed across seeds and offsets. A linear-attention control shows the mechanism is specific to softmax: without normalization, training selects a min-norm interpolant that does not extrapolate. The phenomenon, the equivariance, and the carrier all transfer to a multi-layer, multi-head transformer trained on a full-sequence length-generalization task. The account connects the implicit bias of attention, implicit bias for extrapolation in recurrent models, and the learning side of the RASP-L conjecture.

---


### 117. [Weakly Supervised Pathology-Informed Representation Learning for PET-Based Content Retrieval of Intra-Tumour Heterogeneity](https://arxiv.org/abs/2607.18762)

**<font color=#1a73e8>作者：</font>** Rajat Vashistha, Sandra Brosda, Lauren G. Aoude 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a weakly supervised 18FFDG PET representation-learning framework for content based medical image retrieval, using H&E derived information during training while preserving PET-only inference. The proposed method was designed to use H&E derived information during training while maintaining PET only inference. A teacher student training strategy was used to learn the PET tumour derived voxel representations, from which global and hotspot conditioned embeddings were generated along with maps of intra tumour heterogeneity in our oesophegeal cancer test case. A progressive ablation strategy was used to evaluate the contribution of different supervision mechanisms. Retrieval performance was assessed across cross-validation folds using metrics including mean average precision, normalised discounted cumulative gain and mean reciprocal rank. Additional analyses evaluated ablation performance, hotspot faithfulness through perturbation/deletion experiments, prototype-specific PET uptake behaviour and indirect patient level concordance between learned PET prototype classes and selected histomic features. Progressive introduction of pathology informed supervision and hotspot modelling improved PET retrieval performance compared with global PET representations and conventional PET baselines. Across the ablation ladder, PET hotspot conditioned representations consistently provided stronger retrieval than global embeddings, indicating that focusing on informative tumour subregions improved sensitivity to intra tumour heterogeneity. Histopathology concordance further showed that the learned classes were not simply high uptake PET regions; instead, they demonstrated distinct heterogeneity in 18F FDG uptake.

---


### 118. [Posterior Samplings are Missing Modalities Generators for Medical Image Translation](https://arxiv.org/abs/2607.18763)

**<font color=#1a73e8>作者：</font>** Jonghun Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Magnetic resonance imaging comes in various modality contrasts that provide complementary anatomical and pathological information. Complete multimodal acquisitions are often unavailable due to time and protocol constraints. This leads to real-world datasets with missing modalities, where conventional medical image translation methods are typically limited to fixed source-target settings or require retraining for each observed source-target pair. We propose a unified framework that formulates missing-modality generation as a linear inverse problem under a joint distribution and solves it via posterior sampling with a flow matching model. By learning a joint prior over the complete modality set, our method can reconstruct arbitrary missing modalities at inference time by guiding the sampling trajectory to enforce measurement consistency with observed modalities. We further mitigate inter-modality error propagation in multi-target generation by adopting a many-to-one sampling strategy. Experiments on BraTS and IXI datasets show that our method achieves the best performance over baselines across most missing-modality scenarios. In downstream tumor segmentation, synthesized images from our method result in higher segmentation performance, indicating better preservation of clinically relevant structures.

---


### 119. [Cross-Modal UAV Object Tracking: State-Aware Representation Learning and A Unified Benchmark](https://arxiv.org/abs/2607.18768)

**<font color=#1a73e8>作者：</font>** Yun Xiao, Zhihong Hong, Jiandong Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned Aerial Vehicle (UAV) object tracking has emerged as a popular research field with broad practical applications. Modern UAVs are increasingly equipped with both visible light and thermal infrared sensors. However, due to constraints in communication bandwidth, computational resources and power consumption, current systems often activate one modality and switch between modalities to maintain robust tracking in complex scenarios. Such modality switch inevitably leads to significant appearance change and sudden spatial shift, posing great challenges for existing tracking algorithms. To handle this problem, we propose a novel State-Aware Representation Learning Approach called SARLA, which perceives the inconsistent modality states of current frame with template and last frame in the target representations to adapt to the sudden changes in both appearance and position, for robust cross-modal object tracking. In particular, we propose the Modality State Aware Representation Module (MSARM) and Spatial State Aware Representation Module (SSARM). MSARM guides the model to learn appearance correlation, bridging the modality gap, while SSARM models cross-frame spatial correlation to mitigate sudden spatial shift impacts. In addition, we design a spatial shift prediction loss to further handle the effects of spatial variation caused by modality switch. To promote the development of this research field, we establish a large-scale video benchmark called CM-UOT, which consists of 1079 cross-modal sequences with an average video length greater than 621 frames and encompasses over 671K frames in total. Extensive experiments on CM-UOT dataset demonstrate the superior performance of the proposed SARLA against 20 excellent tracking methods. The source code, datasets, and evaluation protocols associated with this work are publicly available at: this https URL.

---


### 120. [GLID: Gated Local Intrinsic Dimension Repairs the Blind Spots of Face-Forgery Detectors](https://arxiv.org/abs/2607.18770)

**<font color=#1a73e8>作者：</font>** Guang Yang, Fengchen Liu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fine-tuned foundation-model detectors dominate face-forgery benchmarks, yet they stay blind to generator families absent from training. We present GLID, a detector that repairs this blind spot with geometry instead of data. GLID treats the patch tokens of a single image as a sample from a manifold and estimates their local intrinsic dimension (LID) at several depths of a frozen vision transformer. This 12-dimensional, training-free signal enters a fine-tuned detector through a confidence gate whose strength is calibrated purely in-distribution. On a 16-axis cross-generator benchmark, GLID reaches 0.805 mean AUC, first among retrained state-of-the-art baselines and never significantly behind the strongest of them on any axis. It lifts the generation axes by +0.084 AUC while moving reenactment by only -0.005. Two empirical laws explain the design. First, forged faces bend the token manifold at family-specific depths: GAN artifacts peak at the last layer, diffusion artifacts peak mid-network, and the pattern survives four backbones, three dimension estimators, and non-face imagery. Second, fine-tuning absorbs auxiliary gains exactly where training data covers: injecting 1% target-family images erases a +0.100 gain, so geometric signals matter precisely where data is unavailable. The deterministic signal also cuts the cross-seed spread of accuracy 5.5x. Code, preregistered analysis gates, and per-image scores accompany the paper.

---


### 121. [Privileged Lesion-Context Relational Distillation for Mask-Free Skin Lesion Classification](https://arxiv.org/abs/2607.18773)

**<font color=#1a73e8>作者：</font>** Abu Mukaddim Rahi, Md Mithun Hossain, Md Zulficar Hasan Joy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate skin lesion classification can benefit from lesion segmentation masks, but requiring masks or an auxiliary segmentation model during inference reduces clinical practicality and increases computational complexity. This work introduces Privileged Lesion-Context Relational Distillation (PLCRD), a teacher-student framework that exploits lesion masks exclusively during training while preserving image-only inference. The privileged teacher jointly analyzes the original dermoscopic image and its mask-guided lesion region to learn lesion-specific and contextual diagnostic representations. An image-only student is then trained through complementary knowledge-transfer mechanisms that convey the teacher's diagnostic distribution, lesion-focused attention, inter-lesion relational geometry, and lesion-context structure. PLCRD decomposes deep representations into lesion and contextual embeddings and transfers their relational organization through inter-lesion similarity alignment, lesion-context affinity matching, separation regularization, and class-aware relational learning. This formulation avoids direct feature matching between heterogeneous teacher and student architectures and enables the student to internalize mask-informed diagnostic structure without accessing masks at deployment. The framework was evaluated on HAM10000 using lesion-disjoint data partitioning and externally validated on ISIC 2018 without retraining. PLCRD achieved a lesion-level macro-F1 of 0.773 +/- 0.018, balanced accuracy of 0.764 +/- 0.023, and macro-AUROC of 0.976 +/- 0.002 on HAM10000, together with a macro-F1 of 0.732 +/- 0.008 on ISIC 2018. The results indicate that privileged lesion annotations can be transformed into transferable relational knowledge, yielding a practical and interpretable approach to mask-free skin lesion classification.

---


### 122. [Formulation-Level Auto-Tuning for QUBO-Based Machine Learning: A Case Study Across Multiple Quantum-Inspired Annealers](https://arxiv.org/abs/2607.18774)

**<font color=#1a73e8>作者：</font>** Naoya Mizuki, Takahiro Katagiri, Daichi Mukunoki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents an Optuna-based formulation-level auto-tuning framework for support vector machines (SVMs) implemented on multiple quantum-inspired annealers. In an annealing-based SVM, continuous dual variables are discretized and converted into a quadratic unconstrained binary optimization (QUBO) model. This transformation introduces three coupled classes of parameters: representation parameters-the encoding base B and bit depth K-which determine numerical range, resolution, and QUBO size; the RBF kernel parameter {\gamma}, which determines classifier geometry; and the equality-constraint penalty {\xi}, which controls feasibility and coefficient balance. We formulate their joint selection as a mixed discrete-continuous black-box optimization problem. The framework has two optimization levels: an inner annealer minimizes the generated QUBO, while an outer Optuna loop reconstructs the formulation in every trial and maximizes validation accuracy. The same solver-agnostic procedure is applied to Fixstars Amplify Annealing Engine, Toshiba SQBM+, and Fujitsu Digital Annealer using TPE and Gaussian-process samplers and is compared with conventional grid search. Experiments on linear and nonlinear classification tasks with 0-20% label noise show mean gains over grid search of approximately 0.8 and 2.1 percentage points, respectively. The results demonstrate that formulation quality and backend capability must be evaluated jointly and that task-level feedback can compensate for discretization, penalty imbalance, and backend-dependent approximate optimization.

---


### 123. [PertReason: A Knowledge-Grounded Benchmark and Framework for Cell-State-Conditioned Mechanistic Reasoning of Perturbation Effects](https://arxiv.org/abs/2607.18777)

**<font color=#1a73e8>作者：</font>** Dongkwan Kim, Yiming Gao, Yining Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluating machine learning in scientific domains requires separating correct predictions from correct reasons under realistic distribution shifts. We introduce PertReason, a knowledge-grounded benchmark and framework suite for cell-state--conditioned reasoning about perturbation effects. At its core, PertReasonQA is a benchmark that tests whether models can generate mechanistically faithful explanations while remaining robust to complex shifts, such as new cells and unseen perturbations. PertReasonQA combines single-cell genetic and chemical perturbation data across multiple cellular contexts with knowledge graphs, and dynamically conditions pathways on cell-specific basal states to avoid generic memorization. Evaluations on state-of-the-art models reveal systematic gaps between predictive accuracy and mechanistic reasoning. Specifically, these models exhibit failure modes largely invisible to standard benchmarks, such as deriving correct answers through flawed logic, ignoring cellular context, and generating directionally inconsistent mechanisms. As a reference probe of the benchmark, we present PertReasonLM, a large language model trained to align outcome predictions with context-specific mechanistic reasoning. Our model targets the identified failure modes by grounding rationales in context-specific pathways and tightening agreement between outcomes and mechanisms. Together, we provide a diagnostic framework for exposing and mitigating failures in faithful reasoning in data-rich scientific systems.

---


### 124. [CGMap: A Geospatially Aware Deep Learning Framework for Crop Gap Mapping Using UAV](https://arxiv.org/abs/2607.18779)

**<font color=#1a73e8>作者：</font>** Karan Sharma, Rajiv Ranjan, Dinesh Kumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In India, crop germination is primarily monitored by visual inspection and manual counting, which are prone to errors, despite their crucial role in determining eventual yield potential. This paper highlights a deep learning based pipeline which uses object detection methods and drone imagery to assess and provide a precise count of sugarcane germination in fields. The approch uses a pre-trained AI model to find germinated plant sampling and identify gaps, also known as ``bald spots'', which restricts field productivity. The techniques used here relies on the YOLOV8 architecture, which was trained on a carefully selected dataset of UAV photos taken in various agroclimatic zones of India. Here, we bring upon a novel orientation-normalization technique that uses minimum Spanning Trees (MST) to account for variations in planting geometry, allowing for dependable row and column extraction across a variety of field layouts. By converting detected seedlings into spatial point clouds, emergence gaps can be inferred from the anticipated spacing between plants. A geospatial germination map exported in Well-Known Text (WKT) format is the end result, and it can be easily incorporated into GIS platforms used by sugar mills and agronomists to direct transplant initiatives. Timely interventions based on the insights provided by the algorithm can significantly increase yield, resulting in higher profits. Hence, support proper allocation of resources, avoid wastage, and enhance long-term sustainability.

---


### 125. [SkillSight: Seeing Through Shared Descriptions for Accurate Skill Retrieval](https://arxiv.org/abs/2607.18785)

**<font color=#1a73e8>作者：</font>** Jinying Xiao, Bin Ji, Shasha Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language model agents gain access to increasingly large skill libraries, retrieving the right skill becomes critical to reliable capability selection and execution. Existing retrievers often treat skill descriptions as ordinary documents, overlooking their highly regular structure: shared descriptive patterns recur across many skills while providing little evidence for distinguishing the required capability. We show that this shared descriptive background systematically contributes to dense relevance scores, induces a pronounced energy gap between queries and skill documents, and obscures task-relevant signals. Based on this observation, we propose SkillSight, a training-free retrieval framework that calibrates shared background in both semantic and lexical spaces. Semantic Background Calibration estimates a background subspace from generic tokens identified by IDF, reducing similarity induced by shared descriptive patterns, while Lexical Evidence Calibration downweights shared background tokens to recover discriminative token-level evidence. Experiments on SRA-Bench and SkillBench-Supp demonstrate consistent improvements across retrieval metrics, with SkillSight improving Recall@10 by up to 20.21 percentage points over the original dense retriever. In end-to-end evaluation, SkillSight achieves the best overall performance across three agent models and outperforms LLM Selection by up to 4.97 percentage points. It is also up to 1,248 times faster than the Dense + Reranker baseline. These results identify shared descriptive background as a key source of bias in skill retrieval and demonstrate that explicitly calibrating it enables accurate and efficient skill selection without additional training. Our code is available at this https URL.

---


### 126. [Image Editing Models are Numerical Solvers](https://arxiv.org/abs/2607.18787)

**<font color=#1a73e8>作者：</font>** Ulysse Mizrahi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We investigate whether a pretrained generative image-editing model can provide a common interface for numerical simulation. Physical inputs and solutions are rendered as images, while scalar quantities such as material properties, diffusivity, and loading parameters enter through lightweight adapters. Using established numerical and analytic solvers for supervision, we apply the same architecture and training protocol to heterogeneous elliptic equations, forced heat and Burgers evolution, complex Ginzburg-Landau dynamics, two-dimensional Navier-Stokes prediction, potential flow, elasticity, eikonal travel time, phase-field fracture, and entropic optimal transport. The results show that a pretrained image model can represent diverse static and time-dependent physical mappings, including unstable and shock-like behavior, when each task is expressed through a suitable visual encoding. This work is a capability study rather than an attempt to surpass specialized solvers. It also identifies fundamental constraints: image and latent representations complicate numerical range selection and direct enforcement of governing equations or invariants, while a failed Kuramoto-Sivashinsky experiment indicates that representation errors prevent meaningful long-horizon simulation of chaotic systems.

---


### 127. [Moving Alphabet: A Controlled Study of Training Data for Text-to-Video Generation](https://arxiv.org/abs/2607.18789)

**<font color=#1a73e8>作者：</font>** Amber Yijia Zheng, Lu Liu, Raymond A. Yeh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-video generation has advanced significantly over the past five years through scaling of model size, data, and compute. Unlike model architecture, training data is often underexplored. Real-world data curation is complex and non-trivial, involving clip selection from raw videos and captioning to create video-text pairs for learning text-to-video mappings. We study how data distribution and caption quality impact text-to-video models. To enable controlled experiments, we introduce Moving Alphabet, a procedural testbed that renders letters with varying fonts, colors, sizes, and positions, moving in different directions and speeds against a black background. This design allows precise control over data distribution and caption quality by corrupting ground-truth metadata. Our experiments yield three findings: a) a diverse and balanced distribution of video content and duration is critical for generalization; b) caption quality significantly affects both model performance and training efficiency, suggesting that text-to-video models are bounded by video understanding capabilities; and c) classifier-free guidance and fine-tuning on high-quality data provide partial recovery from models trained on corrupted captions, but cannot fully compensate for poor pre-training data. We believe these insights can inform the development of large-scale text-to-video models, and we advocate for greater attention to the science of pre-training data.

---


### 128. [STS-NET: Spatio-Temporal Stress Network for Self-Supervised Crop Stress Detection using Satellite Image Time Series](https://arxiv.org/abs/2607.18791)

**<font color=#1a73e8>作者：</font>** Pradeep Dalal, Rajiv Ranjan, Sushil Ghildiyal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Early and accurate detection of crop stress is essential to improve agricultural productivity and ensure global food security. However, collecting a large labeled crop stress dataset is a challenging task. To address this challenge, we introduce a novel spatial-temporal stress network (STS-NET), built on a self-supervised 3D-convolutional autoencoder (3D-CAE), designed to utilize Satellite Image Time Series (SITS) data for crop stress detection. STS-NET exploits four vegetation indices: Normalized Difference Vegetation Index (NDVI), Normalized Difference Vegetation Index (GNDVI), Red-Edge Chlorophyll Index (RECI) and Normalized Difference Red-Edge Index (NDRE) obtained from high resolution Planetscope imagery to capture spatiotemporal stress patterns. The model is trained on our BSPT (Barnala Spatial-Temporal) dataset and evaluated on a real-world sugarcane dataset collected over a year from a 2.5-acre test plot located in Lakhimpur-Kheri (LK) district in Uttar Pradesh in India. STS-NET achieved a precision of 97. 98\% for water stress, 85.08\% for nitrogen stress, and 83.47\% for combined stress. The results demonstrate the potential of STS-NET in effectively detecting stress in sugarcane crops with minimal reliance on labeled data. Furthermore, STS-NET can serve as a robust feature extractor for simpler models.

---


### 129. [UVFaceFusion: Fast Multi-view Topologically Consistent Face Reconstruction in the Wild via UV-space Neural Fusion](https://arxiv.org/abs/2607.18798)

**<font color=#1a73e8>作者：</font>** Xin Ming, Yuxuan Han, Junhai Yong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing high-fidelity facial geometry with an assigned topology is essential for digital avatar creation and animation, yet existing automated methods often trade off geometric fidelity and in-the-wild generalization. We present UVFaceFusion, a feed-forward framework for multi-view, fixed-topology face reconstruction from daily images. Our key idea is to replace heuristic topological optimization with learnable neural fusion in a canonical UV space. Given multi-view images, we first obtain dense point maps and facial UV correspondences of each view using VGGT and Pixel3DMM, respectively. Then, the view-specific point maps are lifted into the canonical UV domain and fused with a novel mask-aware neural fusion network. The network predicts a complete UV-space point map, from which a fixed-topology mesh is directly sampled. Although trained only on Ava-256, UVFaceFusion generalizes well to multiple public benchmarks and in-the-wild captures, benefiting from its canonical UV-space geometry-to-geometry fusion that reduces dependence on dataset-specific appearance and capture conditions. Experiments on various benchmarks show that UVFaceFusion achieves state-of-the-art reconstruction accuracy while reconstructing a mesh from 16 input views in less than 3 seconds on a single RTX 4090. Code is available at this https URL.

---


### 130. [ZeroSplat: Generalized Referring Segmentation in 3D Gaussian Splatting](https://arxiv.org/abs/2607.18801)

**<font color=#1a73e8>作者：</font>** Jiayu Ding, Meilu Song, Xiaoyi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in 3D Gaussian Splatting (3DGS) have enabled language-guided scene understanding. However, existing Referring 3D Gaussian Splatting (R3DGS) methods are fundamentally restricted to single-target queries. To reflect the ambiguity of real-world instructions, we introduce the Generalized Referring 3D Gaussian Splatting Segmentation (GR3DGS) task, which requires dynamically segmenting an arbitrary number of targets (0, 1, or $N$). To facilitate comprehensive evaluation of this new task, we construct two new benchmarks: GR-LERF and GR-ScanNet. Crucially, existing R3DGS paradigms exhibit fundamental technical bottlenecks that severely limit their performance on the GR3DGS task: they lack intrinsic 3D point-level understanding by operating merely on 2D rendered pixels, and they incur prohibitive computational overhead by requiring per-scene optimization to embed heavy semantic features. To dismantle these bottlenecks, we propose ZeroSplat, a novel training-free and zero-feature framework. ZeroSplat lifts 2D Vision-Language Model (VLM) priors into 3D space through robust multi-view geometric constraints. This strategy enables intrinsic point-level understanding without incurring any additional feature storage. Extensive experiments demonstrate that ZeroSplat significantly outperforms state-of-the-art methods across generalized and single-target scenarios while maintaining exceptional efficiency. Project Page: this https URL

---


### 131. [QScheduler: Adaptive Gradient Sampling for Zeroth-Order On-Device Training on INT8 NPUs](https://arxiv.org/abs/2607.18802)

**<font color=#1a73e8>作者：</font>** Victor Felipe Domingues Do Amaral, Pierre Demaj, Erwan Libessart 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zeroth-Order (ZO) optimization enables On-Device Learning (ODL) on NPU-equipped microcontrollers by estimating gradients through forward passes alone, bypassing the need for backpropagation primitives and reducing memory requirements. The number of gradient samples q critically affects training: insufficient samples produce noisy gradients that plateau early, while excessive samples consume more computational resources. However, finding an optimal q typically requires costly hyperparameter searches. This work introduces QScheduler, an adaptive algorithm that adjusts q based on training progress, and provides the first proof-of-concept of INT8 quantized on-device training on the STM32N6's Neural-ART NPU. Experiments on EuroSAT and STL-10 show that QScheduler matches well-tuned fixed-q configurations for both ResNet18 and MobileNetV2, without requiring prior q hyperparameter optimization.

---


### 132. [Elicitation without Backpropagation: Steering Model Behavior by Optimizing the Latent Posterior](https://arxiv.org/abs/2607.18804)

**<font color=#1a73e8>作者：</font>** Garrett Baker, Vinayak Pathak, Daniel Murfet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the \emph{latent posterior model} of transformer behavior, the next-token distribution arises from a posterior over latent predictive models conditioned on the context, mixed to generate continuations. We exploit this model in settings where it is exact, namely Bayes-filtered transformers (BFTs) meta-learned on sequences from a hierarchical prior, to introduce \textbf{Posterior Prefix Tuning (PPT)}, a new method for \emph{eliciting} behavior from a transformer: given a utility function on continuations, find a prompt under which the transformer generates continuations of high expected utility. For a BFT, the elicitation objective factors through the latent posterior, and the gradient of this objective can be estimated from samples of the prior alone. PPT optimizes the parameters of a distribution over hard prompts: it draws prior samples once from the BFT via predictive Monte Carlo (PMC), then estimates the gradient by importance sampling against them. The optimization performs no transformer forward passes and no backpropagation through the transformer, and the prior samples are utility-independent, so a single set of samples drives elicitation against any number of utilities at negligible marginal cost. We validate PPT on Beta--Bernoulli and reinforced urn BFTs across three utility families (reverse cross-entropy, frequency matching, Dyck validity).

---


### 133. [CITRUS: Candidate Inference and Temporal-tracking for Reliable, Unobtrusive Sensing of Wearable Heart Rate under Motion](https://arxiv.org/abs/2607.18818)

**<font color=#1a73e8>作者：</font>** Yi Wang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Wearable photoplethysmography (PPG) provides continuous heart-rate measurements, but its accuracy degrades under motion. In the ring-platform benchmark, the best supervised baseline reaches 5.33 BPM mean absolute error (MAE) on the overall heart-rate task. In the motion-focused ring-only audit, a supervised LSTM baseline reaches $14.39 \pm 0.47$ BPM MAE on motion windows, and simple smoothing and ACC priors reduce this only to $13.00 \pm 0.41$ BPM. This thesis addresses motion-corrupted HR estimation through three connected stages: candidate-frequency identification, temporal decoding, and reliability-aware reporting.
The study first evaluates two wearable PPG ring variants against clinical references for heart rate, respiration, SpO$_2$, and blood pressure in 54 participants. The proposed system then uses two layers. The estimation layer converts each window into approximately 140 frequency candidates, scores candidates using agreement among independent estimators, and applies causal Viterbi decoding with a physiological transition penalty. The reporting layer estimates reliability and applies a learned accept/hold/reject policy. Reporting only the most-confident 50% of motion windows reduces motion MAE from 10.8 to 6.2 BPM. The heart-rate estimator uses fewer than 100k parameters and runs within a microcontroller-class compute budget. Additional PPG-DaLiA experiments evaluate the same candidate-selection and temporal-decoding estimator on an independent wrist-BVP cohort.

---


### 134. [Open-Vocabulary Gaze Object Prediction: Benchmark and Method](https://arxiv.org/abs/2607.18827)

**<font color=#1a73e8>作者：</font>** Binglu Wang, Sensen Niu, Ying Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaze Object Prediction (GOP) aims to localize and recognize the objects humans attend to, a task crucial for understanding human-centric interactions. However, existing methods are typically trained under a closed-vocabulary paradigm with a fixed label space and evaluated on scene-specific datasets, limiting their applicability to real-world scenarios where gaze targets often follow a long-tail distribution or belong to unseen categories. To address this gap, we introduce Diverse Scenes for Gaze object prediction (DiSG), a benchmark containing 86 in-the-wild categories that facilitates the evaluation of Open-Vocabulary GOP (OVGOP). Building on DiSG, we propose a framework that leverages text-driven object discovery to localize potential gaze candidates, with a gaze-guided selection module to pinpoint the intended target from the candidate objects. Furthermore, to better capture semantic knowledge across diverse in-the-wild categories, we introduce Gradient-Informed Selection Tuning (GIST) to selectively update parameters most relevant to a given class vocabulary. Extensive experiments demonstrate that our proposed model performs effectively in open-vocabulary settings and also outperforms existing methods in the conventional closed-vocabulary setting. The benchmark and code is available at this https URL.

---


### 135. [Countercurrent Multiplier Networks: A Renal-Inspired Iterative Operator with Provably Bounded Fixed-Point Dynamics](https://arxiv.org/abs/2607.18829)

**<font color=#1a73e8>作者：</font>** Snigdha Chandan Khilar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The mammalian kidney concentrates urine using a mechanism with no analogue in current neural architectures: the countercurrent multiplier. Two anti-parallel flows joined at a hairpin recirculate a weak magnitude-bounded local pump into a large axial gradient achieving a four-fold concentration increase from a single-effect gradient that never exceeds 200 mOsm at any point. We formalize this mechanism as a differentiable sequence operator the Countercurrent Multiplier (CCM) layer and study it as an alternative to residual iterative refinement.

---


### 136. [From Trajectories to Instructions: Language-Conditioned Meta-Reinforcement Learning](https://arxiv.org/abs/2607.18830)

**<font color=#1a73e8>作者：</font>** Garvit Singla, Uma Maheswari Natarajan, Raghuram Bharadwaj Diddigi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model-Agnostic Meta-Learning (MAML) is a widely used framework for reinforcement learning (RL) that enables efficient transfer by learning global policy parameters that can be rapidly adapted to new tasks. MAML training proceeds in two loops: an inner loop where the global parameters are adapted to task-specific parameters, and an outer loop where these task-specific parameters are evaluated and losses are back-propagated to improve the global parameters. Traditionally, the inner loop adaptation is performed by collecting trajectories from the task environment and applying gradient updates on the empirical expected return, which can be a costly operation. We note that it is the outer loop that drives the actual learning of global parameters, and therefore the inner loop adaptation mechanism need not be restricted to be gradient-based. This observation leads us to ask: Can we replace the inner loop trajectory collection and gradient update with a simpler, task-specific signal? In many practical settings, tasks are naturally accompanied by language instructions. Leveraging these instructions as a direct task-specific signal, we propose LA-MAML (Language Adapted MAML), which modifies the inner loop by adapting the global policy parameters in a single step through a learned embedding of the task instruction, replacing the inner loop trajectory collection and gradient-based updates. Experiments on the BabyAI benchmark demonstrate that LA-MAML achieves competitive or improved performance compared to baselines at a significantly lower per-iteration wall-clock training time. These results demonstrate that language instructions are an effective and efficient substitute for trajectory-based inner loop adaptation in meta RL.

---


### 137. [ABOPD: Antibody CDR Design via On-Policy Distillation](https://arxiv.org/abs/2607.18835)

**<font color=#1a73e8>作者：</font>** Zhuo Yang, Jiaying He, Jiaqing Xie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Antibodies are essential therapeutic molecules, and their complementarity-determining regions (CDRs) form the primary antigen-recognition interface. Recent protein generative models have demonstrated broad capabilities in biomolecular design, yet post-training strategies for downstream objectives remain limited. Standard denoising training operates on noisy states obtained by perturbing native structures, whereas recursive generation proceeds through model-generated intermediate states. For flexible antibody CDR loops such as CDR-H3, this mismatch can allow backbone deviations to accumulate along the denoising trajectory and compromise antigen-facing loop geometry. We introduce ABOPD, an antibody design framework based on on-policy distillation that leverages privileged native geometry during training to supervise states visited along the model's own denoising trajectories. With this fine-grained structural supervision, ABOPD substantially improves structural recovery on RAbD CDR-H3 generation, reducing RMSD by 0.42 Å (from 2.37 Å to 1.95 Å) and outperforming supervised fine-tuning and offline distillation controls, offering a path to higher-fidelity protein design.

---


### 138. [HPD-Parsing: Hierarchical Parallel Document Parsing](https://arxiv.org/abs/2607.18839)

**<font color=#1a73e8>作者：</font>** Shu Wei, Jingjing Wu, Lingshu Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Efficient teamwork typically combines global coordination with parallel execution, a principle not yet fully reflected in unified Vision-Language Model (VLM)-based document parsers. Existing unified parsers process an entire page jointly but generate its output through a single token-by-token autoregressive trajectory, creating a sequential bottleneck that grows with document length. Such full-page sequential generation overlooks a key property of document parsing: layout must be analyzed globally, whereas block content can be parsed in parallel. Based on this observation, we introduce HPD-Parsing, which replaces full-page autoregressive generation with a Hierarchical Parallel Decoding paradigm. A main layout branch organizes the overall document structure and dynamically assigns block-level content decoding to concurrent branches, while progressive multi-token prediction (P-MTP) further reduces the decoding steps within each branch. Experiments on public benchmarks show that HPD-Parsing achieves 4,752 tokens per second, delivering $2.62\times$ the throughput of the fastest existing document parsing model and $3.06\times$ that of the vanilla autoregressive baseline, while maintaining competitive parsing accuracy. These results establish hierarchical parallel decoding as an effective alternative to full-page autoregressive generation, opening a new direction for efficient unified document parsing.

---


### 139. [OPD-IAD: From Language Judgment to Industrial Anomaly Detection via On-Policy Self-Distillation](https://arxiv.org/abs/2607.18850)

**<font color=#1a73e8>作者：</font>** Shuimu Chen, Jing Jin, Nan Su 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) have recently shown strong potential for industrial anomaly detection (IAD) by providing image-level anomaly judgments and interpretable defect reasoning. However, current LVLM-based IAD methods still struggle to produce precise pixel-level anomaly maps from generated language judgments. We aim to achieve precise pixel-level localization while using language as guidance rather than letting it dominate the visual response. Specifically, we propose \textbf{OPD-IAD}, an evidence-privileged dense on-policy self-distillation framework for LVLM-based IAD. OPD-IAD distills privileged defect evidence onto the model's own on-policy judgment trajectory, enabling the final generated judgment to be learned under dense supervision rather than treated only as a textual answer. The resulting judgment serves as a semantic condition for dense anomaly perception. To turn this condition into dense visual evidence, we introduce \textbf{Language-guided Visual Anchoring}, which uses a judgment reforward to re-encode the image and question under the final-judgment condition into semantic anchors and contrasts them with dense visual features through a contrastive heatmap head to generate anomaly maps. The language judgment therefore provides compact semantic guidance, while dense visual features remain the basis for pixel-level scoring, allowing language to guide anomaly localization without letting language quality directly dictate the pixel-level response. Extensive experiments show that OPD-IAD achieves the best overall performance among LVLM-based IAD methods, leading on most image-level, pixel-level, and QA metrics.

---


### 140. [Think Sparse, Predict Dense: Continuous Thought Machines for Image Super-Resolution](https://arxiv.org/abs/2607.18856)

**<font color=#1a73e8>作者：</font>** Zekai Shi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continuous Thought Machines introduce an internal temporal dimension in which neuron-level histories and synchronization-derived representations evolve over a sequence of thought ticks. Extending this mechanism to dense visual prediction is non-trivial, because tasks such as image super-resolution require spatial evidence to remain available at every output location rather than being compressed into a single global representation. In the proposed window-level use of CTM, the thought dynamics produce a compact summary representation for each local window. DQ-CTM transforms this compact thought representation into window-aligned dense queries through a structured low-rank, parameter-efficient compact-to-dense query mechanism. Each position within a window receives its own query, while shared thought dynamics progressively refine the dense representation across ticks. In its super-resolution instantiation, termed ThinkSR, encoded feature maps are partitioned into local visual windows without token pooling, restored to the original feature field after shared refinement, and decoded into a high-resolution image. Preliminary experiments under a fixed four-tick training horizon reveal a progressive reconstruction trajectory. PSNR-Y increases from 28.1045 dB at $T=0$ to 30.2817 dB at $T=4$, while PSNR-RGB increases from 26.6271 dB to 28.7781 dB and the mean $\ell_1$ error decreases from 0.034602 to 0.023545. All 100 evaluated images improve from $T=1$ to $T=4$. These initial results establish the feasibility of sparse latent thought for dense spatial reconstruction and motivate broader continuous-thought architectures for dense vision.

---


### 141. [PhoenixRepair: Rethinking Repair Strategy Exploration in Software Agents](https://arxiv.org/abs/2607.18859)

**<font color=#1a73e8>作者：</font>** Tianyue Jiang, Yanlin Wang, Xin He 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Large Language Models have greatly advanced automated issue resolution, existing agent-based methods exhibit a fundamental limitation in their insufficient exploration of repair strategies. This insufficiency manifests in two key aspects. First, the exploration of multiple potential edit locations is limited. Second, the exploration of repair attempts at each location is also insufficient. To address these challenges, we present PhoenixRepair, a multi-agent framework that systematically explores multiple candidate edit locations and performs iterative reflection and refinement on patch generation, thereby expanding the search space of repair strategies. Our framework begins with multi-location sampling, optionally augmented with graph-based localization information for difficult tasks, followed by iterative reflection and refinement to generate better patches, culminating in final-round generation guided by distilled insights from all historical attempts. Experiments on SWE-bench-Verified demonstrate that PhoenixRepair achieves the largest relative improvement of 7.8\% over SWE-agent under DeepSeek-V3.1, and attains the highest resolved rate of 76.0\% Pass@1 under MiniMax-M2.5. Meanwhile, it achieves higher fault localization accuracy than existing approaches. Our code is available at this https URL.

---


### 142. [Regime-Aware Physics-Guided Early Warning of Lithium-Ion Battery Thermal Runaway Using Thermo-Mechanical Signals](https://arxiv.org/abs/2607.18860)

**<font color=#1a73e8>作者：</font>** Syed Sajid Ullah, Muhammad Zunair Zamir, Salman Khan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Thermal runaway in lithium-ion batteries poses a major safety risk to electric vehicles and energy storage systems. Current early-warning methods depend mainly on temperature and may therefore miss mechanical precursors that emerge before rapid heating. We introduce a regime-aware, physics-guided framework that integrates temperature, voltage, force, deformation, and state-of-charge measurements for early warning under controlled mechanical abuse. A lightweight convolutional classifier first infers safe, warning, or danger regimes from mechanical signals. These regime estimates then condition a causal temporal convolutional backbone through feature-wise linear modulation, physics-biased attention, and regime-dependent gating. Joint learning unifies regime identification, thermal-runaway detection, and time-to-disaster estimation. We evaluate the framework using leave-one-experiment-out cross-validation on 30 mechanical-abuse tests across state-of-charge levels of 10%, 50%, and 90% and two loading protocols. The method achieves an F1 score of 0.89, a high-temperature prediction root-mean-square error of 12.3 °C, a mean warning lead time of 15.6 s, a detection success rate of 0.92, and an experiment-level false alarm rate of 2.7%. Its lead time exceeds that of the strongest baseline by 69.6%. Removing force reduces the lead time by 60.3%, highlighting the value of mechanical precursors. These results support regime-aware thermo-mechanical fusion as a promising strategy for earlier and more reliable thermal-runaway warning under controlled abuse conditions.

---


### 143. [Reliability-Aware 3D Geometric Injection for Universal Person Re-identification](https://arxiv.org/abs/2607.18863)

**<font color=#1a73e8>作者：</font>** Bohan Su, Jiashuo Wang, Fangyi Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Universal person re-identification (ReID) aims to retrieve pedestrian identities across diverse real-world scenarios, including severe occlusions, clothing changes, and cross-modality shifts, within a unified model. However, existing 2D representations fundamentally struggle with spatial ambiguities due to a lack of depth and topological awareness, while naively introducing monocular 3D priors often causes severe negative transfer due to geometric estimation noise under extreme visual degradation. To safely harness the clothing-invariant and canonical structural properties of 3D geometry, we propose UniGeo, a Universal Monocular 3D-Enhanced ReID framework driven by a Consistency-Aware Reliability Gate and Dual-Stream Residual Fusion. Specifically, the processing of 3D information is strategically decoupled into geometric extraction and dynamic utilization. To provide pure structural compensation, we project monocular 3D parameters into kinematic joint representations, explicitly capturing instance-level geometric topology to resolve appearance-based ambiguities. To robustly incorporate these cues without perturbing the reliable 2D feature space, we isolate the 3D prior as a late-stage structural residual; modulated by the consistency-aware gate, this mechanism adaptively filters geometric noise and enables controlled fallback to the pure 2D baseline. Extensive experiments show that our method improves challenging, structure-sensitive scenarios while preserving competitive performance on clean domains. Code is available at this https URL.

---


### 144. [Evaluating a Visual Query Tracer and Builder for Learning Declarative Logic Programming](https://arxiv.org/abs/2607.18864)

**<font color=#1a73e8>作者：</font>** Julián Méndez, Lukas Gerlach, Tobias Wieland 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Nemo Explain Visualizer (nev) is an interactive visual query tracer and builder for Nemo, a powerful Datalog reasoner with extended features. Our tools were developed with and for expert users. However, considering the lack of resources to learn Datalog and similar declarative logic programming languages, we conducted a qualitative user study to assess how our tools might help students. The study, interviewing 14 participants with varying levels of involvement with the content of a university course on knowledge graphs, revealed a very positive assessment of our tools, which strengthens the value of visual explanation tools beyond their intended use.

---


### 145. [Tracing the Shadows: Automatic Tracking and Analysis of Crypto Money Laundering via Transaction Semantic Analysis](https://arxiv.org/abs/2607.18869)

**<font color=#1a73e8>作者：</font>** Hao Wu, Haijun Wang, Shangwang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the rapid advancement of decentralized finance (DeFi), security incidents related to cryptocurrency have become increasingly prevalent. After such incidents, attackers typically attempt to rapidly move stolen assets, concealing the origin of illicit funds and ultimately converting them into fiat currency. However, existing anti-money laundering (AML) methods struggle to cope with the semantic complexity of DeFi transactions. They either rely heavily on low-level token transfers, or perform protocol-agnostic money flow analysis, failing to capture the high-level intent of transactions.
In this paper, we propose AMLGuard, a semantic-aware AML framework for account-based blockchains. AMLGuard tracks illicit fund flows from known malicious addresses by performing semantic analysis on complex DeFi transactions, enabling accurate and continuous laundering tracking. Given a complex transaction, AMLGuard combines static rule-based analysis with retrieval-augmented large language model (LLM) reasoning to infer implicit DeFi semantics, transforming raw transaction data into high-level semantic representations. Furthermore, for cross-chain transactions where laundering intent is not explicitly exposed, AMLGuard parses transaction parameters and performs argument parsing to recover cross-chain semantics, enabling seamless tracking across ledgers. Based on the inferred semantics, AMLGuard abstracts each transaction into a DeFi Semantic Unit (DSU). We evaluate the effectiveness of AMLGuard on 82 real-world laundering cases, involving illicit assets worth over $1 billion. Specifically, AMLGuard reconstructs compact illicit fund-flow topologies with destination precision of 94.4% and 87.6%, while achieving the highest address recall of 98.4% and 95.8% and destination recall of 94.1% and 93.8% on single-chain and cross-chain datasets.

---


### 146. [Reinforcement Learning for Delivery Drone-Based Participatory Sensing in Dynamic Environments](https://arxiv.org/abs/2607.18874)

**<font color=#1a73e8>作者：</font>** Xin Ouyang, Songxin Lei, Xusen Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Using Unmanned Aerial Vehicle (UAV) for urban sensing has emerged as a powerful paradigm to monitor the status of the city, e.g., air quality and noise levels, through agile aerial crowdsourcing. Despite this potential, existing UAV-based sensing approaches overlook environmental disturbances like wind that drastically impact drone velocity and energy efficiency. Consequently, directly applying existing methods to this joint delivery and sensing paradigm in dynamic environments faces two severe challenges: (1) scalability bottlenecks as fleet sizes expand; and (2) multi-timescale decision heterogeneity between macro task dispatching and micro velocity control. To tackle these, we formalize the problem as SensUAV and propose a Two TimeScale Reinforcement Learning framework (TSRL). Specifically, TSRL separates decision-making into two cooperative layers. At the macro level, a task-embedding sensing dispatcher handles scalability by separately encoding distinct task features and sequentially evaluating UAV suitability before task selection. At the micro level, a wind-aware velocity controller learns fine-grained velocity scheduling to adapt to dynamic environmental variations. Extensive experiments on real-world datasets demonstrate that TSRL significantly outperforms baselines, achieving average system profit improvements of 20.1% in Hangzhou and 46.6% in Shanghai.

---


### 147. [Wave2Body: Rethinking mmWave Human Pose Estimation as Radar-to-Body Token Translation](https://arxiv.org/abs/2607.18875)

**<font color=#1a73e8>作者：</font>** Bo Liang, Chen Gong, Wei Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Millimeter-wave (mmWave) radar enables privacy-friendly human sensing, but its sparse point clouds are physical measurements of view-dependent electromagnetic reflections and only indirectly characterize body articulation. Recovering a complete 3D pose from such partial, geometry-dependent observations is therefore under-constrained. Existing methods directly regress joint coordinates from paired radar-pose data, relying on the same limited paired supervision to learn radar perception, human-body structure, and their alignment. This coupling can encourage dataset-specific shortcuts under ambiguous radar observations. We propose Wave2Body, a radar-to-body token translation framework that decouples these learning targets using a self-supervised mmWave tokenizer, a pretrained compositional body tokenizer that defines the output space, and a lightweight translator between them. Experiments on M4Human and mmBody show that Wave2Body achieves stronger cross-domain generalization than previous methods while incurring much lower computational costs for training and inference. All the code and experiment results are publicly available at this https URL.

---


### 148. [Physics-Informed Super-Resolution of Atmospheric Data](https://arxiv.org/abs/2607.18877)

**<font color=#1a73e8>作者：</font>** Chang Xu, Gencer Sumbul, Hugo Porta 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the context of global warming, extreme events have become more frequent and intense, making their trustworthy detection and forecasting more important than ever. Yet, atmospheric observations lack sufficient spatial resolution, motivating atmospheric data downscaling as a way to reconstruct high-resolution data from coarse observations. This task is now being formulated as a super-resolution (SR) problem with machine learning methods featuring high efficiency. Nevertheless, it remains unclear whether the super-resolved atmospheric data still satisfies fundamental physics governing the Earth system, raising concerns about their trustworthiness in climate-related applications. In this work, we address this challenge by constraining SR models to respect hydrostatic primitive equations that represent multivariate atmospheric physics. First, we propose a Physics-Informed Super-Resolution (PISR) method involving multi-scale physics-informed objectives based on primitive equations. PISR favors the SR outputs to respect these equations and therefore naturally encodes inter-variable relationships. In addition, we propose a metric called Normalized Physical Consistency (NPC) derived from said primitive equations to measure the physical consistency of super-resolved data. Experiments on ERA5, CERRA, and COSMO demonstrate that PISR enhances the reconstruction fidelity by improving physical consistency, SR accuracy, and downstream detection of extreme events, as demonstrated by case studies in heatwaves and extreme winds.

---


### 149. [Local Label-Informed Feature Transfer for Generating Ground-Truth Medical Images: A Comparison of GAN- and Diffusion-Based Approaches](https://arxiv.org/abs/2607.18882)

**<font color=#1a73e8>作者：</font>** Rick Wilming, Irem Ozseker, Luca Matteo Cornils 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Validating Explainable Artificial Intelligence (XAI) methods in medical imaging requires ground-truth data with known locations of informative features. However, current approaches rely on expert annotations, which are prone to labeling errors, or on hand-crafted artificial perturbations superimposed onto healthy images to mimic lesions or malignant features, which lack clinical realism. We present Local Label-Informed Feature Transfer (LLIFT), a framework for generating semi-synthetic brain magnetic resonance images with realistic lesions placed in user-controlled regions, which does not require pixel-level lesion annotations during training. We implement LLIFT with two generative paradigms: LLIFT-GAN, a custom GAN that learns pathological features from binary class labels alone, and LLIFT-DM, a diffusion-based inpainting pipeline conditioned on bounding-box masks via ControlNet. Both approaches are evaluated on brain magnetic resonance imaging data derived from the Human Connectome Project. In evaluations, both achieve Fréchet Inception Distance scores, with respect to the real pathological distribution, that are comparable to the inter-class reference between healthy and pathological images in the given dataset. Furthermore, qualitative inspection confirms the realism of lesion structures. The resulting benchmark datasets provide spatially controlled ground truth data for evaluating XAI methods in medical imaging.

---


### 150. [RAMP: Recognition parametrisation by Amortised Message Passing](https://arxiv.org/abs/2607.18883)

**<font color=#1a73e8>作者：</font>** Lior Fox, Kai Biegun, James Heald 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central aim of unsupervised learning is to uncover latent factors that explain dependencies among observations. Probabilistic models typically achieve this by introducing multiple latent variables linked through a graph of conditional relationships, with distributional parameters and their dependence learnt from data. Learning relies either on distributional choices that allow tractable belief propagation, or on approximations that scale poorly with model size and complexity. We build on the recently developed recognition-parametrised modelling paradigm to propose an alternative approach: RAMP, a method that implicitly defines latent structure by learning a flexible, nonlinear, amortised message-passing framework. We show that RAMP enables efficient likelihood-based recovery of latent-variable distributions within expressive nonlinear models acting on complex high-dimensional data.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-241](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
