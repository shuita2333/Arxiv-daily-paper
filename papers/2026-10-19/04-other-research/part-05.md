# 📦 其他研究 | 2026年10月19日

> 本类共 **278** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-278](./part-06.md)

---

### 201. [CIM-Embed: Learning Instruction-Conditioned Multimodal Embeddings for Clustering](https://arxiv.org/abs/2610.21805)

**<font color=#1a73e8>作者：</font>** Yinghua Xu, Pengyang Xie, Yanxiang Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal objects can require different partitions under different instructions, as when products in an e-commerce catalog are grouped by color, material, or both. Retrieval-oriented embeddings may not recover these partitions, while generative clustering often relies on intermediate descriptions or iterative decisions. This paper presents CIM-Embed, a framework for learning instruction-conditioned multimodal embeddings for clustering. Supervised contrastive learning uses same-group positives and negatives from other groups, optionally including other tasks; heterogeneous structured batches accommodate tasks with different group counts. At inference, the model maps each object's image, text, and instruction directly to an embedding; HDBSCAN then forms a partition without the ground-truth cluster count. We construct ProductMIC from product metadata in Amazon Reviews 2023, comprising training data and an evaluation benchmark for instruction-conditioned clustering. The benchmark contains 5,373 products and 449 single-attribute and compositional grouping tasks spanning 50 leaf categories excluded from our training. With full-dimensional embeddings and HDBSCAN, direct within-task SupCon training achieves a mean per-task V-measure of 95.01, compared with 53.06 for WeMM 9B, the strongest general-purpose embedding baseline evaluated. Frozen product-trained encoders also improve out-of-domain conditional grouping, while controlled transfer experiments distinguish partition transfer from instruction response. We will release the code and dataset upon acceptance.

---


### 202. [Content associations with answer selection and engagement in supply chain community question answering](https://arxiv.org/abs/2610.21807)

**<font color=#1a73e8>作者：</font>** Hisatoshi Naganawa  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Community question-answering platforms are important ecosystems for knowledge sharing, yet research on what makes an answer best or a question engaging has often focused on either individual lexical features or broad topics. This exploratory study examines both levels in Yahoo! Chiebukuro, asking which nouns and semantic noun clusters are associated with best-answer selection and question engagement. We analyze a large corpus of questions and answer-tier posts collected under the keyword logistics, using an offline machine-translation pipeline with manually validated noun-level fidelity. Best-answer selection is modeled with conditional logistic regression within question threads, controlling for answer length, order, and question-answer noun overlap. Engagement is modeled in two stages: whether a question receives any response and, conditional on receiving one, how many responses it attracts. Operational logistics nouns such as distribution, warehouse, and center are associated with best-answer selection, whereas broader civic and infrastructure nouns such as car, tax, and shinkansen are associated with higher engagement. At the cluster level, most semantic noun clusters are associated with best-answer selection, while the clusters associated with response likelihood and response volume are largely distinct. These findings reveal differentiated content-outcome profiles across answer and question levels and provide a domain-wide descriptive map of engagement and answer selection in logistics-related cQA discourse.

---


### 203. [Measuring the local shape of learning-rate transfer curves](https://arxiv.org/abs/2610.21814)

**<font color=#1a73e8>作者：</font>** Satoki Ishikawa, Rio Yokota, Ryo Karakida  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding the learning-rate (LR) dependence of trained model performance is essential for better optimization of neural networks, but the appropriate size of the LR depends on learning dynamics, architecture, and their hidden biases, and thus our understanding of this complex dependence remains limited. The behavior of the loss curve as a function of the LR has recently been observed in extensive experiments on LR transfer across different settings, such as model sizes, and it is becoming more important to explore methodologies for quantitatively characterizing the shape of this LR curve. In this work, we provide two relational equations that give a good empirical explanation of the gradient of the LR transfer curve, i.e., the LR gradient. One is a theoretical formula that holds at the edge of stability, and the other is an approximate expression obtained by naively treating this gradient as a hyper-parameter gradient. Using these two relational equations in a complementary manner, we show a lower bound on the gradient of the curve and a zero gradient under specific conditions for normalization layers in theory. The approximate expression also applies to a wide range of experimental settings and allows us to decompose the LR gradient into layer-wise components and quantify the strong contribution of specific layers to the curve shape. Thus, this serves as a foundation for better understanding the internal mechanisms of LR dependence.

---


### 204. [A Closed Form Depth-Width Law for Neural Collapse in Deep Linear Networks](https://arxiv.org/abs/2610.21820)

**<font color=#1a73e8>作者：</font>** Pankhil Gawade, Kirsten Fischer, Guy Wolf 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How depth and width of neural networks shape learned representations is usually studied only after training. We show that, in a tractable feature-learning setting, this dependence can instead be obtained in closed form. Using neural collapse as a probe of representation geometry, we express NC1--NC3 directly in terms of the learned feature kernel, extending an identity known for NC1 to the angular part of NC2 and to NC3 under a ridge readout. For deep linear networks with exchangeable class structure, the resulting kernel equations yield a geometric law, exact within the theory, for the layerwise evolution of within-class variability. At large width, the accumulated compression becomes a function of the depth-to-width ratio $L/N$, with its rate determined self-consistently by the data, prior and architecture. Numerical experiments support the derived dependence on depth, width and signal-to-noise ratio. The result is a representation-level scaling law derived from feature-learning theory rather than fitted after training.

---


### 205. [Local Epochs as Optimal Stopping: Theory and Evidence in Federated Learning](https://arxiv.org/abs/2610.21832)

**<font color=#1a73e8>作者：</font>** Ke Xiao, Qiyuan Wang, Christos Anagnostopoulos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How long should each client train before communicating? Federated learning usually answers with a fixed, hand-tuned number of local epochs, yet an extra epoch helps only while the loss it removes outweighs the client drift it adds. We cast local training as finite-horizon optimal stopping: a client trains while the next epoch's expected loss reduction exceeds its priced squared drift. We prove that this one-stage look-ahead threshold is optimal whenever stopping decisions are nested, derive closed forms for geometric and power-law returns, and show that an estimated rule loses utility only through wrong-signed decisions. Epoch-level evidence supports the model's structure (geometric diminishing returns and additive drift) and reveals a simple regularity: the stage of training, not the client, sets the budget. The resulting rule, FedStop, is never more than one point below tuned FedAvg in mean accuracy. Where its budgets vary, it raises worst-decile accuracy by 4-8 points over tuned FedAvg and an adaptive-interval baseline, and every one of these gains remains significant after a Holm correction. Against the client-side stopping rules ALT and FLASH, it has the highest CIFAR-10 worst decile on every seed and is level elsewhere. It stays stable where per-client early stopping collapses, and each stopping decision takes constant time.

---


### 206. [Temporal Periodic Image Registration with Implicit Neural Representations](https://arxiv.org/abs/2610.21845)

**<font color=#1a73e8>作者：</font>** Mathias Lowes, Kristine Aavild Sørensen, Maxime Sermesant 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Implicit Neural Representations (INRs) have recently gained popularity for their ability to model functions using simple and lightweight networks. These methods have also proven effective in deformable image registration. In this work, we extend INRs for deformable image registration to the domain of temporal image registration, focusing on periodic temporal image sequences. Our approach, Temporal-IDIR, optimizes a single INR to model deformations across all frames in a temporal image sequence simultaneously, allowing for self-regularization through its own deformation predictions. To achieve this, we introduce a temporal consistency loss that penalizes discrepancies between direct source-to-target transformations and those traversing intermediate frames. We evaluate our framework on the DIR-LAB dataset, using the target registration error (TRE) between annotated and moved landmarks as the metric. Here, we achieve a TRE of 1.03 mm, outperforming other INR-based registration methods. Additionally, our framework supports smooth interpolation between time frames by estimating deformations between the given input frames. Code is publicly available at this https URL.

---


### 207. [Seeing Both the Forest and the Trees: Reusing Holistic 3D Priors for Part-Decomposed Generation](https://arxiv.org/abs/2610.21850)

**<font color=#1a73e8>作者：</font>** Yiqun Zhao, Binbin Huang, Haobin Duan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating 3D assets with explicit parts requires two properties at once: geometric detail inside each part and structural coherence across the whole object. Recent image-conditioned 3D generation models adopt a structured 3D representation that anchors tokens to explicit spatial positions, capturing both properties, but their output remains a single fused mesh. We ask how a part-decomposed generation model can inherit both properties of these holistic priors, and answer with STRUCTPARTS, a framework whose core technical contribution is a dual-frame coordinate interleaving mechanism: each shape latent is interpreted under both a part-local and an object-global reference frame, and processed through a global-local inter-leaved transformer that simultaneously reuses the prior's geometric detail at the part scale and its structural coherence at the whole-object scale. As its structural input, STRUCTPARTS uses a segmented mesh scaffold, a coarse mesh paired with a face-level segmentation mask kept entirely within the prior's native 3D representation. With only lightweight finetuning, both intra-part detail and inter-part coherence emerge from the same pretrained weights. On PartObjaverse-Tiny, STRUCTPARTS matches or surpasses prior part-decomposed models at a fraction of their training cost, while naturally supporting part-mesh refinement and part-level editing.

---


### 208. [Dynamic ordering in sequence generation in Transformers: experiments on low-resource Tagging scenarios](https://arxiv.org/abs/2610.21862)

**<font color=#1a73e8>作者：</font>** Giacomo Bais, Tejaswini Deoskar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper introduces TagInsert, a Transformer-based model that challenges the common left-to-right (L2R) generation paradigm in Transformers, for sequence labelling tasks where dependencies may not naturally align with a L2R order. TagInsert lifts the L2R constraint by removing the decoder-side attention mask and enabling the model to decide a preferred order of tag generation at inference time. We experiment on the common Part-of-Speech tagging and the more complex Combinatory Categorial Grammar (CCG) supertagging tasks on multiple languages and low-resource data settings. We show that, although encoder-only models like BERT remain strong performers for tagging tasks, TagInsert frequently outperforms a L2R encoder-decoder model, achieves results comparable to encoder-only models under data-scarce conditions, and shows better results on the long-tail of rare categories. Our analyses show that TagInsert alleviates error propagation typical of autoregressive models by learning to defer difficult predictions to later stages in the decoding process.

---


### 209. [Lethe: Link Inference Attacks For Evaluation of Edge Unlearning Methods](https://arxiv.org/abs/2610.21869)

**<font color=#1a73e8>作者：</font>** Andrea D'Angelo, Francesco Gullo, Davide Mottin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Unlearning (GU) aims to remove the influence of specific training data from a Graph Neural Network without retraining anew. While most methods address removal of nodes and features, Edge Unlearning (EU), aiming at forgetting edges, has recently attracted dedicated attention as a standalone problem due to the hardness of completely removing the impact of an edge in the model. Despite this, no dedicated benchmark for EU exists besides isolated evaluations on feature-rich datasets such as Cora and Citeseer where GNNs exploit node features rather than graph structure. As such, we show two systematic limitations in existing evaluations: dedicated EU methods can be slower than retraining anew, and accuracy metrics are uninformative due to the negligible impact of edge removal. To address this gap, we introduce Lethe, the first comprehensive benchmark for Edge Unlearning, featuring 15 methods and 8 datasets. Our benchmark emphasizes large graphs, introduces evaluation tasks of varying difficulty, and proposes empirical measures based on link inference attacks rather than proxy accuracy metrics. We provide a comprehensive empirical analysis, demonstrate the shortcomings of current evaluations, and release Lethe as a reproducible, extensible benchmark.

---


### 210. [Provably Efficient Risk-Sensitive Offline Reinforcement Learning via Optimized Certainty Equivalents](https://arxiv.org/abs/2610.21870)

**<font color=#1a73e8>作者：</font>** Hanzhen Wang, Boxiang Lyu, Zhongxiang Dai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Risk-sensitive reinforcement learning (RL) addresses decision-making under uncertainty and adverse outcomes. Learning risk-sensitive policies from fixed datasets is important when additional interaction with the environment is costly. Existing work on risk-sensitive RL focuses on online settings or specific risk measures, leaving a general theoretical understanding of its offline setting underdeveloped. In this work, we investigate efficient offline risk-sensitive RL using the optimized certainty equivalent (OCE), a general class of risk measures. We consider two formulations: dynamic-OCE RL, which applies OCE recursively at each step, and static-OCE RL, which applies a single OCE to the cumulative rewards. Under the tabular setting, we develop pessimistic value-iteration algorithms for both formulations and establish tight sublinear suboptimality bounds, explicitly capturing how risk sensitivity, encoded by utility functions, affects learning difficulty. Moreover, we establish minimax suboptimality lower bounds to characterize the problem's fundamental limits. To handle large state spaces, we further develop pessimistic least-squares value-iteration algorithms that incorporate the general OCE risk criterion into linear function approximation. We establish utility-dependent sublinear guarantees with explicit dependence on the feature dimension $d$. To our knowledge, we provide the first offline algorithms along with the first upper and lower suboptimality bounds for both dynamic- and static-OCE RL.

---


### 211. [MetaShare: Failure-Aware Collective Self-Improvement for Open-Ended Agents](https://arxiv.org/abs/2610.21887)

**<font color=#1a73e8>作者：</font>** Vishal Bhutani, Prasang Gupta, Sumanth Chundru 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Humans often learn fastest not by repeating success, but by remembering which failures not to repeat. Open-ended self-improving agents can share experience across lineages, as in GEA, or edit their own improvement mechanisms, as in DGM-Hyperagents, yet failed improvement attempts are rarely retained as reusable cross-branch knowledge, and search can collapse onto redundant strategies. We introduce MetaShare, a failure-aware framework that records successful and unsuccessful agent modifications together with signed performance deltas. Before each generation, MetaShare retrieves diverse high-performing strategies alongside high-confidence failures from other lineages, letting agents reuse effective mechanisms while avoiding known dead ends. A task-blind auditor periodically injects absent or underrepresented mechanism categories, while embedding-based de-ranking limits redundancy during retrieval. Multiple meta-agents propose modifications in parallel at heterogeneous temperatures behind a deterministic selector that gates applicability, scope, compilability, and size. Experiments across paper review, coding, math grading, robotics reward design, and financial audit-risk assessment show that MetaShare's median matches or exceeds DGM-Hyperagents' final performance and reaches its own best-performing agent in 1.7--2.9$\times$ fewer evolution iterations.

---


### 212. [Graph Dirichlet Energy for Fitting-Free Bivariate Causal Inference](https://arxiv.org/abs/2610.21892)

**<font color=#1a73e8>作者：</font>** Povilas Daniušis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose the Graph Dirichlet Energy Causal Inference (GDECI) criterion for distinguishing cause from effect in bivariate settings. For a candidate direction $X\to Y$, we construct a kernel similarity graph from $X$ and treat $Y$ as a graph signal. The score is the Dirichlet energy of this signal, induced by the unnormalized graph Laplacian. The reverse score swaps the variables, and the lower-energy direction is inferred as causal. The method requires neither regression fitting nor independence testing. After the empirical probability integral transform, its decisions are invariant under strictly monotone transformations of either variable, and the graph operations reduce to convolutions, allowing exact evaluation in $O(n\log n)$ time and $O(n)$ memory. At the population level, GDECI compares degree-weighted Bayes squared prediction errors plus a non-negative smoothness term of the regression function. As the bandwidth tends to zero, the weights become uniform and the smoothness term vanishes, reducing the criterion to a RECI-type comparison of expected conditional variances in copula space. Empirically, we compare GDECI with QCCD, GRCI, CAM, IGCI (two variants), RESIT, LOCI, QPE-k, and RECI (two variants), in accuracy on 1899 cause--effect pairs and in inference speed. GDECI ranked fifth of eleven methods in macro-averaged accuracy on 12 synthetic suites ($0.776$). On the real-world Tuebingen pairs, it ranked third in unweighted accuracy ($0.684$) and fifth in weighted accuracy ($0.678$). It was also the fastest of the compared methods up to $n\approx10^{4}$. The accompanying code repository: this https URL.

---


### 213. [Self-Calibrated Subspace Robust PCA for Parameter-Free Removal of Mixed Noise and Line Stripes in Hyperspectral Images](https://arxiv.org/abs/2610.21896)

**<font color=#1a73e8>作者：</font>** Wenzhe Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperspectral images (HSIs) are often corrupted by Gaussian noise, impulses and stripes whose intensities vary across bands. The representative coefficient correlated total variation (RCCTV) model restores HSIs efficiently, but it lacks Gaussian and stripe terms, and its noise-aware extensions require the noise level and a stripe budget to be specified in advance. This article proposes a self-calibrated RCCTV (SC-RCCTV) model, in which the noise parameters are estimated adaptively during the iterations. A band-wise dense term and line-constant column and row stripe terms are introduced into RCCTV. The noise level of each band is initialized by a stripe-invariant median absolute deviation estimator and refined online from the residual, which turns the separation of sparse and dense noise into a band-adaptive Huber loss, and the stripe thresholds follow from a significance test whose false-alarm rate can be predicted analytically. No parameter is tuned for a specific image, and every subproblem of the alternating direction method of multipliers (ADMM) solver is solved in closed form. Under line stripes, SC-RCCTV outperforms the parameter-free FastHyMix by 8.17 dB on native-size cubes, and, without any noise information, it exceeds S3TTV, which is given the true noise parameters, by 1.52 dB while running more than 1,900 times faster. On average, it stays within 0.01 dB of the same model given the true noise levels, and its online calibration improves on a two-stage estimate-then-denoise scheme. Experiments on real Indian Pines and Urban data further delineate its scope for stripes that do not span entire lines.

---


### 214. [BridgeAfford: Bridging Query-Target Gap for Generalizable 3D Affordance Grounding](https://arxiv.org/abs/2610.21918)

**<font color=#1a73e8>作者：</font>** Yijie Su, Yakun Zhu, Yi Bin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language-guided 3D affordance grounding aims to localize functional regions on 3D objects according to interaction intents. However, existing methods exhibit poor generalization to unseen objects. One challenge is the query-target gap: a semantic discrepancy between query features encoding interaction intents and target-region features, leading to inaccurate grounding. End-to-end training favors query representations tailored to seen objects, limiting their compatibility with shifted target-region features on unseen objects. To address this issue, we propose BridgeAfford, a framework that reduces the query-target semantic gap from two complementary perspectives. First, Interaction Region Alignment (IRA) promotes cross-object alignment among geometrically similar interaction regions during training. This enables structures on unseen objects that resemble previously observed ones to produce representations similar to those learned during training, facilitating target-region recognition. Second, Visual Evidence Aggregation (VEA) leverages a 2D affordance model to refine the attention distribution and guide the query toward the correct region, yielding more target-aware queries. Extensive experiments on the LASO and PIAD datasets demonstrate that BridgeAfford outperforms existing methods, particularly on unseen objects, highlighting its robust generalization ability.

---


### 215. [The Lagrangian Structure of Cost-Penalized Active Feature Acquisition](https://arxiv.org/abs/2610.21919)

**<font color=#1a73e8>作者：</font>** Joseph Bingham  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Active Feature Acquisition (AFA) sequentially selects features to maximize predictive accuracy under an acquisition budget. A natural heuristic greedily maximizes Expected Information Gain minus a cost penalty, EIG(j|x_S)-lam*c_j (EIG-Cost), but its theoretical guarantees are unclear. We provide an a-posteriori certificate decomposing the gap to the optimal hard-budget policy into a budget-slack term and a greedy-suboptimality term Del_lam. The certificate is computable when the penalized optimum is tractable; on small heterogeneous-cost instances, we verify it exactly, finding Del_lam near zero across 4,000 solved cases. On the large clinical task, Del_lam is not computable, so the decomposition is diagnostic rather than a numerical guarantee. Our analysis identifies EIG-Cost as one-step greedy optimization of the Lagrangian relaxation of expected-cost AFA, with lam as its dual multiplier. For equal costs, we prove Del_lam <= exp(-gam*I(Y;X_[d])), where gam is the submodularity ratio, yielding a structural guarantee in the near-submodular regime. Supporting results establish an adaptive chain-rule identity showing that cumulative stepwise EIG optimizes transcript information, and prove that A -> I(Y;X_A) need not be submodular, even for jointly Gaussian variables. This rules out a direct Nemhauser-Wolsey-Fisher bound; naive Bayes restores submodularity. We also bound the randomization gap between hard-budget and expected-cost optima, analyze sensitivity to dual-multiplier error under local smoothness, and derive a conditional CVAE generator-shift bound given a bound on forward predictive KL. We treat this KL as a diagnostic quantity, not as a transform of training loss. Experiments cover synthetic Gaussian settings, AFA benchmarks, and clinical differential diagnosis on MIMIC-IV. On MIMIC-IV, EIG-Cost achieves macro-F1 0.180 +/- 0.012 at a $30 budget, using 6.6% of full-panel cost.

---


### 216. [Flow-CLIP: Image-Conditioned Residual Scoring for CompositionalImage-Text Matching](https://arxiv.org/abs/2610.21937)

**<font color=#1a73e8>作者：</font>** Minghong Wei, Enguang Zhu, Pu Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision--language pre-training has enabled substantial progress in image--text retrieval and zero-shot recognition by learning transferable cross-modal representations. However, sentence-level alignment remains insufficient for compositional matching, where captions can describe the same objects and attributes while differing in how these elements are bound. To address this limitation, we propose Flow-CLIP, which refines global image-text alignment through image-conditioned changes in token--patch evidence. Global Compatibility Calibration (GCC) learns a sentence-level similarity metric, while Image-Conditioned Evidence Refinement (ICER) incorporates visual patch context into token queries and uses the resulting change in local matching evidence to adjust the global score. We further introduce Cross-Image Margin Ranking (CIMR), which compares the same positive--negative caption pair across matched and mismatched images, encouraging a larger ranking margin when the image supports the correct description. Experiments on compositional matching and attribute--object binding benchmarks show that Flow-CLIP improves binding accuracy over pretrained CLIP and learned global alignment through local evidence refinement, while cross-image ranking supervision mitigates reliance on language priors. Code will be released at link.

---


### 217. [Learning Speech Attribute Representations via Multi-Teacher Distillation](https://arxiv.org/abs/2610.21941)

**<font color=#1a73e8>作者：</font>** Maryem Bouziane, Salima Mdhaffar, Yannick Estève  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent post-training approaches have shown that self-supervised speech encoders can be adapted to learn a single utterance-level speech attribute through knowledge distillation. In this work, we investigate whether a single speech encoder can simultaneously preserve multiple complementary utterance-level speech representations. We propose a multi-attribute multi-teacher distillation framework that learns semantic, speaker, language, and emotion representations from four frozen teacher models using a shared SSL backbone and attribute-specific branches. Experiments on multilingual semantic retrieval, speaker verification, language identification, and speech emotion recognition show that the proposed model achieves performance close to dedicated single-task students while requiring only a single shared encoder. Furthermore, the learned layer aggregation strategies reveal that different speech attributes naturally emerge at different depths of the SSL encoder, providing new insights into the organization of speech representations.

---


### 218. [Following Delegation Traces to Study Human Oversight in Interaction with Multimodal AI](https://arxiv.org/abs/2610.21948)

**<font color=#1a73e8>作者：</font>** Agnese Chiatti, Matteo Matteucci, Viola Schiaffonati  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As multimodal AI systems are becoming our everyday thought partners, the shift towards studying how users transfer control to these systems becomes especially urgent. In this paper, we report an overview of findings from an online study with n=56 AI-literate participants and 392 Video Question Answering trials. After inspecting each multimodal AI response, participants rated task-specific trust and selected one of three intended policies for an analogous future task: reject AI assistance, use it with verification, or delegate fully to the AI. Within participants, post-interaction trust strongly predicted the user's delegation choices (OR=14.97, 95% CI [7.14,31.37]). Trust and delegation nevertheless remained distinct. Verification was the dominant policy and often co-occurred with high trust. Delegation also increased with task order after adjustment for momentary and participant-level trust (OR=1.22, 95% CI [1.02,1.45]), indicating an experience-related component that self-reported trust ratings alone could not capture. These findings motivate a shift from intended delegation to a non-intrusive observation of how delegation is enacted in collaborative human-AI tasks. We therefore conclude by proposing enacted delegation traces as a methodological framework for future studies of multimodal and agentic AI use.

---


### 219. [ChronoSheaf: Joint Spatio-Temporal Spectral Filtering on Cellular Sheaves](https://arxiv.org/abs/2610.21958)

**<font color=#1a73e8>作者：</font>** Abeer Mostafa, Zahra Ahmadi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sheaf neural networks generalize graph neural networks by assigning each edge a learned linear restriction map that specifies how the local representations of adjacent nodes relate to one another, thereby mitigating oversmoothing. Existing sheaf architectures, however, define the sheaf Laplacian as an instantaneous spatial operator and therefore cannot explicitly model how signals evolve over time on a graph. We first introduce a spectral sheaf Laplacian, defined jointly over space and time, such that a single operator regulates signal propagation across both the spatial graph and the temporal domain. Directly extending this operator's receptive field in space or time would require increasingly complex sheaf structures. Instead, we propose a spectral filter that expands the effective receptive field along both dimensions without enlarging the underlying sheaf. Building on this operator, we introduce ChronoSheaf, a spatio-temporal sheaf network with two key components. First, Transitional Restriction Maps (TRM) decompose each node's restriction map into a spatial term and two temporal frames that independently control its relation to neighboring nodes at the preceding and following timestep, enabling asymmetric temporal influence. Second, the Dual Spectral Filter (DSF) applies a single bounded-degree polynomial filter with an adaptively estimated spectral radius to the joint spatio-temporal sheaf operator. We validate ChronoSheaf on a diverse set of spatio-temporal forecasting benchmarks, where it outperforms state-of-the-art baselines. The code is available at: this https URL.

---


### 220. [Why Shallow Neural Networks Learn Sinusoidal Components First: An Orthogonal Polynomial Dynamics Framework](https://arxiv.org/abs/2610.21964)

**<font color=#1a73e8>作者：</font>** Yanyang Xiao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks often learn low-frequency components before high-frequency ones --- a phenomenon called spectral bias or termed F-principle. Many numerical studies have demonstrated this phenomenon, and theoretical studies have sought to explain it. However, several goals remain insufficiently addressed: (1) explaining spectral bias asymptotically, including its origin and why the preferred components are generally sinusoidal; (2) extending the explanation to general activation functions, such as sigmoid and ReLU; (3) making weak assumptions about the data distribution; (4) avoiding aliasing effects, such as those arising in finite-domain Fourier analysis; and (5) developing a theoretical framework applicable to arbitrary networks. We address these goals theoretically by analyzing the eigenvalue decay and eigenvector shapes of the dynamics matrix H, which arises when we expand the network output as a general Fourier series (GFS) in an orthogonal polynomial basis and express the gradient-descent dynamics of the GFS coefficients as ordinary differential equations. The graded structure of H enables an intuitive explanation of spectral bias, while orthogonal polynomial theory helps us analyze how learning bias depends on the activation function and, potentially, the network architecture.

---


### 221. [Why Users Stop at Good Enough: Applying Bounded Rationality to Self-Service Restaurant Display Interactions](https://arxiv.org/abs/2610.21971)

**<font color=#1a73e8>作者：</font>** Muhammad Ismail Khursheed, Carolina Islas Sedano, Jaakko Järvi  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper investigates user interaction with digital displays in self-service restaurant environments, focusing on the phenomenon where users often settle for good enough interactions rather than optimal. We apply bounded rationality theory to understand how cognitive limitations influence user decisions to engage with displays of varying interaction complexity. Through analysis of two field experiments conducted at a self-service restaurant in Finland, we examine interactive displays that require different levels of cognitive investment: a simple binary choice interface and a multi-step interaction. Our initial findings suggest an "engagement plateau" where increased interaction complexity yields diminishing returns in initial engagement rates, yet users who overcome initial cognitive barriers demonstrate high completion rates. This work contributes to Human-Computer Interaction field by offering an empirically supported theoretical lens for understanding user behavior in Self-Service Restaurant (SSR) environments and providing actionable design principles for public interactive displays that accommodate human cognitive limits.

---


### 222. [Time to Fake It: Continual Machine Learning Intensifies Unfairness in Deepfake Detection](https://arxiv.org/abs/2610.21974)

**<font color=#1a73e8>作者：</font>** Kajaree Das, Oliver Böse, Subarnaduti Paul 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deepfake detectors safeguard against misinformation, rendering their failures as much a societal as a technical concern. As generators constantly evolve, detectors trained on static datasets miss newly arising threats, while progressive training interferes catastrophically. Yet, mitigating forgetfulness in terms of accuracy, the prevalent focus of continual learning (CL), is insufficient to reflect real-world impact. We therefore scrutinize the effects of CL methods with respect to evolving fairness. To this end, we analyze four dimensions of fairness across diverse demographics for detectors trained progressively on a chronological sequence of 11 real-world deepfake generation methods. Tracking fairness metrics over time, we expose non-trivial interplays between performance and fairness that depend on both the choice of CL algorithm and demographic intersections. We find accuracy degradation to typically exacerbate unfairness and, conversely, fairness improvements to remain scarce over time. Dissecting the CL method families (rehearsal, prompts, regularization), we observe that inequitable forgetting is not explained by underrepresentation alone, but likely entangled with representation learning. We thus issue a call to action for CL methods to take social outcomes into account when balancing the stability-plasticity tradeoff.

---


### 223. [Learn Only Where You Can't Compute: Structured Corrections to Gaussian Process Posteriors](https://arxiv.org/abs/2610.21977)

**<font color=#1a73e8>作者：</font>** Tobias Weber, Carla Sagebiel, Philipp Hennig  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed Gaussian processes (GPs) provide a principled framework for scientific inference by expressing uncertainty over empirical measurements, boundary conditions, and governing equations. However, they struggle to scale to larger datasets and nonlinear information. Conversely, diffusion models excel at learning complex distributions over functions from massive datasets, but struggle in scientific contexts where training data are scarce and physical or observational information must be incorporated. We propose a structured posterior-correction framework that combines a tractable Gaussian reference with data-driven corrections via generative learning. After a mean correction and covariance calibration, a diffusion model learns a targeted correction in a low-dimensional subspace selected to capture discrepancies from the reference, while the complement retains its Gaussian law. Across three scientific inference tasks, these corrections recover hidden modes, improve sample structure, and reduce prediction error relative to the Gaussian reference. Comparisons with full-field generative models reveal task-dependent benefits and tradeoffs between predictive accuracy and computational cost.

---


### 224. [P2TPO: Structure-Aligned Page-to-Token Credit Assignment for Full-Page Document Parsing](https://arxiv.org/abs/2610.21979)

**<font color=#1a73e8>作者：</font>** Yong Zu, Ninghua Yang, Zezhong Tan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> End-to-end full-page document parsing must preserve the content and structure of heterogeneous elements, yet otherwise accurate outputs can contain local errors and omissions. A single page-level advantage does not explicitly identify which elements differ in quality across sampled outputs or where their errors occur. We introduce Page-to-Token Policy Optimization (P2TPO), a structure-aligned credit-assignment framework that operates on full-page policy trajectories. Reference-element alignment first associates block-level quality contrasts with generated spans. Unified Anchor Pricing (UAP) incorporates matched and missing element outcomes and provides feedback relative to a fixed quality ceiling when sampled outputs receive identical but imperfect scores for a reference element. Within matched blocks, Span Credit Redistribution (SCR) redistributes existing block credit according to aligned correct and erroneous spans, using boundary proxies for within-block omissions while preserving the total block-derived advantage across its tokens. Under a fixed-weight additive page utility, we show that element-indexed contrasts retain local quality differences that page-level aggregation can cancel out. In the main experimental comparison, P2TPO outperforms all evaluated policy optimization baselines in seed-averaged scores on each of the six document parsing benchmarks. Additional experiments demonstrate gains across model scales and initializations.

---


### 225. [VesperMUSE: Multi-Modal Fusion Vision Transformer for Image Semantic Segmentation Under Diverse Light Conditions](https://arxiv.org/abs/2610.21990)

**<font color=#1a73e8>作者：</font>** Raul Balmez  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation is critical for the reliable navigation and scene understanding of autonomous systems, yet its performance degrades severely in low-light environments due to noise, artifacts, colour distortion, and the loss of structural details. To address this challenge, this work introduces VesperMUSE, a unified multi-modal framework designed to achieve robust image semantic segmentation across diverse illumination conditions. The architecture addresses the light deficiency problem on multiple levels: proposing a novel physics-informed synthetic low-light adaptation algorithm, approaching Low-Light Image Enhancement (LLIE) through a thermal-guided paradigm, and finally aiming to recover the intrinsic scene details for semantic segmentation through a multi-modal fusion approach. Following enhancement, the framework dynamically integrates the primary RGB features with auxiliary thermal representations and surface normal maps highlighting geometric discontinuities and material boundaries. At the core of this integration is a highly scalable, modality-agnostic self-attention mechanism that extracts both global context and fine local features from an arbitrary number of auxiliary inputs. By combining and projecting these hierarchical multi-modal representations into a unified component, the attention module allows the network to selectively attend to relevant cross-modal cues without requiring any architectural modifications when different sensor configurations are used. Extensive evaluations demonstrate that VesperMUSE successfully recovers missing visual cues, providing a flexible, state-of-the-art (SOTA) solution for machine perception in extreme and unstructured real-world environments.

---


### 226. [Data-Efficient ConvNeXt Pretraining for High-Resolution Sentinel-1 GRD SAR Representation Learning](https://arxiv.org/abs/2610.21993)

**<font color=#1a73e8>作者：</font>** Yuki Natsume, Sang-Ho Yun, Chai Kiat Yeo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Labeled Sentinel-1 Ground Range Detected (S1GRD) datasets remain scarce, limiting supervised deep learning for land-surface remote sensing, while self-supervised pretraining for this domain has been dominated by Vision Transformer (ViT)-based masked image modeling requiring substantial data and compute. We propose SparK-SAR, a sparse convolutional masked pretraining framework built on SparK and ConvNeXt, designed to exploit convolutional inductive biases for S1GRD imagery under constrained compute. SparK-SAR makes three core technical contributions: (i) ConvNeXt-RS, a domain-adapted encoder that halves the stem stride (4x to 2x) to produce 14x14 feature maps at stride 16x, providing 4x more spatial tokens at identical parameter count; (ii) a lightweight ConvNeXt-512 reconstruction decoder with PixelShuffle upsampling that reduces pretraining VRAM by 7.5-8.5% per GPU relative to a UNet-128 baseline while matching its accuracy; and (iii) an empirical characterization of FP16 mixed-precision pretraining instability in the standard SparK UNet-768 decoder on S1GRD data, complemented by a finding that finetuning with layer-wise learning rate decay (LLRD) improves downstream performance of pretrained encoders. On four Copernicus-Bench S1GRD tasks, our finetuned 27.8M-parameter ConvNeXt-RS encoder improves over a non-pretrained baseline by +4.7, +5.0, +5.8, and +1.4 pp on EuroSAT-S1, BigEarthNet-S1, DFC2020-S1, and Flood-S1 respectively, and outperforms the Copernicus-FM ViT (139M parameters, frozen) on three of four tasks at roughly 5x fewer parameters. A pretraining data-scaling study reveals task-dependent data efficiency: classification saturates with as little as 10-25% of the SSL4EO-S12 v1.1 corpus, while dense prediction continues to improve significantly up to 25-50%. The study also includes a CKA representation analysis and a geographic de-collision experiment.

---


### 227. [Interfaces and Modules: A Scalable Representation for Weight-Space Learning across Architectures](https://arxiv.org/abs/2610.21995)

**<font color=#1a73e8>作者：</font>** Michał Kozyra, Michael Bronstein  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weight-space learning across architectures requires representations that respect parameter symmetries and scale to large networks. Existing equivariant tensor encoders require architecture-specific symmetry specifications, while neuron graphs make global attention costly. We introduce a typed graph organized around shared coordinate-permutation actions. Its nodes, called interfaces, represent coordinate spaces whose bound tensor axes must be permuted jointly; operation occurrences, called modules, form typed hyperedges. A compiler derives this graph from supported PyTorch models, with exact recovery of the permutation factors defined by its constraints. The Universal Weight Encoder (UWE) combines local equivariant updates to parameter features with global attention over invariant interface summaries. The small number of interfaces makes global attention practical, and a single encoder processes different supported architectures. UWE is competitive with architecture-specific state-of-the-art methods on established benchmarks. On a new zoo of 1,200 transformers spanning 100 architectures, it outperforms the evaluated baselines at ranking networks within unseen architectures, including architectures larger than those used for training, while using substantially less memory.

---


### 228. [GraphBEAT: Graph-based Bucketized Event Aggregation Over Time for Early Risk Stratification of Gastrointestinal Cancers](https://arxiv.org/abs/2610.22014)

**<font color=#1a73e8>作者：</font>** Leo Y. Li-Han, Chris Varghese, Elizabeth B. Habermann 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Longitudinal electronic health records (EHRs) contain complementary diagnostic and laboratory information about patient health. However, irregularity, sparsity, heterogeneity, and incompleteness in documentation complicate EHR modeling. To address the problem, we introduce GraphBEAT (Graph-based Bucketized Event Aggregation over Time), a temporal graph representation learning framework that groups clinical events into time buckets and transforms observed features into patient-specific, temporally directed graphs to enable early risk stratification for gastrointestinal cancers. Each node in an EHR graph encodes feature identity, observed value, and temporal position of clinical events. A context-aware, time-decay message-passing mechanism models transitions between successive buckets, followed by multi-head attention pooling to generate patient-level representations. GraphBEAT was trained and evaluated on multi-site longitudinal diagnosis codes and laboratory tests to predict pancreatic, liver, and intestinal cancer at 12-, 24-, and 36-month diagnostic lead times. In all experimental setups, GraphBEAT consistently outperformed baseline graph neural networks (GraphSAGE, GAT, and GCN) and sequence modeling approaches (Transformer and long short-term memory [LSTM]). GraphBEAT also required over 250x fewer floating-point operations per patient and over 20x fewer parameters than the Transformer and LSTM baselines. These results support GraphBEAT as an accurate and computationally efficient approach for cancer risk stratification from sparse, heterogeneous longitudinal health records.

---


### 229. [Not All Unlabeled Data Are Equal: Unlabeled Data Selection for Semi-Supervised QSAR Modeling with Large Chemical Repositories](https://arxiv.org/abs/2610.22025)

**<font color=#1a73e8>作者：</font>** Oliver Majer, Saso Dzeroski, Jurica Levatic  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semi-supervised learning (SSL) is particularly attractive in domains where labels are expensive to obtain, while unlabeled examples are readily available. Quantitative Structure-Activity Relationship (QSAR) modeling, which predicts molecular biological activity from chemical structure, is one such domain. Obtaining activity measurements requires costly wet-lab experiments, resulting in small labeled datasets, while chemical repositories such as ChEMBL contain millions of unlabeled molecules. Despite this apparent suitability, the potential of large chemical databases to improve QSAR models via SSL remains largely unexplored. Furthermore, it is unclear how unlabeled data should be selected in realistic SSL settings with genuine unlabeled data. We conduct a systematic study of unlabeled-data selection using 10 QSAR datasets extracted from ChEMBL and a pool of more than 400,000 unlabeled molecules. To this end, we evaluate three established SSL algorithms (self-training, co-training, and label propagation) and formulate four unlabeled-data selection strategies based on random, nearest-neighbor, furthest-neighbor, and mixed sampling. Our results show that unlabeled data from large chemical repositories can improve QSAR models, with at least one SSL configuration outperforming the supervised baseline on each of the 10 datasets. Moreover, the most reliable improvements are generally achieved by selecting a relatively small number of chemically distant molecules. This suggests that the composition of the unlabeled set may be more important than its size, challenging the common premise that SSL necessitates an abundance of unlabeled data.

---


### 230. [SMT-Boosted Security Types and Correctness for Low-Level MPC](https://arxiv.org/abs/2610.22047)

**<font color=#1a73e8>作者：</font>** Christian Skalka, Steven Baldasty, Yeonhee Yeh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Secure Multi-Party Computation (MPC) is an important enabling technology for data privacy in modern distributed applications. We develop a new Hoare logic and type theory to automatically enforce correctness, confidentiality, and integrity properties of protocols written in the Prelude/Overture language framework. Both definition and automation of our analyses leverages SMT verification, supporting precision and efficiency. Our approach is compositional, scalable, and generalizes to arbitrary prime fields and secret sharing schemes.

---


### 231. [Decoding Naturalistic Speech from fMRI with Temporal Modeling and Multimodal Alignment](https://arxiv.org/abs/2610.22049)

**<font color=#1a73e8>作者：</font>** Corentin Caris, Louis Jalouzot, Nona Rajabi 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reconstructing what a person perceives from their brain activity is a stringent test of whether neural recordings carry meaningful information. Naturalistic speech offers a rich testbed for this challenge: it unfolds over multiple timescales, but fMRI's noisy, temporally smeared measurements make this structure hard to recover. We introduce NOEMA, a temporal convolutional decoder that aligns windows of consecutive fMRI measurements with multimodal stimulus embeddings. These embeddings combine complementary text, audio, and speech representations of the same stimulus segment, enabling its retrieval directly from brain activity. On two naturalistic speech datasets, Cephalonauts One and LeBel, NOEMA retrieves the correct segment among 2,000 candidates within the top 10 for more than 42% of held-out queries. This substantially outperforms baseline decoders, an advantage that persists when the candidate pool is extended with thousands of distractors absent from training. Controlled ablations establish the contributions of temporal modeling and complementary stimulus representations.

---


### 232. [FeaTok: Feature-Loss Tokenization for Image Generation](https://arxiv.org/abs/2610.22060)

**<font color=#1a73e8>作者：</font>** Zhang Xiaofeng, Samuel Lavoie, Nicolas Beltran-Velez 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Discrete image generators learn the distribution of tokens produced by an image tokenizer. These token representations should be easy for generators to model, not merely enable faithful image reconstruction. Yet these tokenizers are commonly trained to reconstruct pixels, which prioritizes low-level fidelity and may disrupt representation structure useful for generation. Motivated by feature-predictive self-supervised learning, we introduce feature-loss tokenization (FeaTok), which trains discrete tokens by reconstructing pretrained features rather than pixels. Ablations across SigLIP, SigLIP2, DINOv2, and DINOv3 show better generative performance with FeaTok. In class-conditional generation, FeaTok advances the quality-compute Pareto frontier, reducing gFDr6 at 256x256 by up to 29 percent over the strongest discrete baselines and outperforming the strongest unguided continuous baseline (RAEv2) with 38 times less sampling compute. FeaTok also achieves higher human-preference reward-model scores than prior art without reward-based training and surpasses continuous and discrete text-conditional baselines on three benchmarks with only 500 fine-tuning updates after pre-training.

---


### 233. [ABNAT: Attention-Based Noise-Aware Training for Robust Transformers on Analog Compute-in-Memory Systems](https://arxiv.org/abs/2610.22065)

**<font color=#1a73e8>作者：</font>** Wenshuai Yao, Wenyong Zhou, Hanyong Shao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based models have become the backbone of a wide range of tasks, but their intensive computation and data movement incur substantial energy overhead. Analog compute-in-memory (CIM) offers an energy-efficient alternative, yet its inherent hardware non-idealities perturb stored weights and can significantly degrade model performance. Although existing noise-aware training (NAT) methods improve robustness by injecting noise during training, they largely overlook the critical role of attention mechanisms in Transformer this http URL bridge this gap, we analyze how CIM-induced noise reshapes attention in Transformers and identify two key observations: (1) the divergence between clean and noisy attention maps increases substantially in deeper layers, and (2) conventional NAT can remain overconfident even when its attention routes deviate markedly from the clean reference. Motivated by these findings, we propose ABNAT, an attention-based noise-aware training framework that teaches the noisy student to preserve the clean teacher's headwise attention routes rather than merely reproduce answers, without hardware changes or inference overhead; selective variants further reduce training this http URL experiments across vision, language, and multimodal Transformers show that ABNAT consistently improves robustness over corresponding NAT baselines, improving noise-degraded accuracy by up to 11.28% and reducing attention deviation by up to 85.77%.

---


### 234. [Can AI Forecast the Extremes? Evaluating Probabilistic Weather Models on Tropical Cyclones](https://arxiv.org/abs/2610.22077)

**<font color=#1a73e8>作者：</font>** Nathan Chalumeau, Xavier Renard, Remi Meynadier 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weather prediction is undergoing an important shift, with data-driven AI models outperforming leading numerical weather prediction systems on average at a fraction of the computational cost. Yet, whether this success extends to extreme events remains contested. Earlier evaluations have exposed important shortcomings, but have largely focused on deterministic models and metrics, leaving the capabilities of the latest probabilistic models less understood. We conduct an extensive benchmark of tropical cyclone forecasting, comparing GenCast, FourCastNet 3, and FGN with ECMWF's operational physics-based ensemble, IFS-ENS. We develop a suite of probabilistic metrics and diagnostic analyses to assess cyclone tracking, intensity biases, uncertainty, and the wind-pressure relationship that characterizes storm structure. We find that, despite remaining limitations in intensity and ensemble spread, leading AI models substantially outperform IFS-ENS in cyclone tracking: FGN achieves better probabilistic location scores for 90% of evaluated storms in 2025. Further analyses reveal model-specific failure modes and suggest a lingering influence of pretraining data, pointing to opportunities for targeted improvement. Nonetheless, these results suggest that AI models are capable of capturing physical relationships that remain predictive well beyond typical weather conditions, motivating further investigation into how these capabilities emerge and how to strengthen them.

---


### 235. [Beyond the Dominant Label: Recovering Coexisting Lesion Evidence with Multiple Instance Learning](https://arxiv.org/abs/2610.22091)

**<font color=#1a73e8>作者：</font>** Lubin Gan, Jing Zhang, Xinming Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole-slide images may contain coexisting lesions, yet weak supervision typically provides only the most severe diagnosis. We formulate this setting as dominant-label multiple instance learning, where the observed label is the maximum-severity element of a latent lesion set. Standard multiclass MIL treats it as a complete one-hot description and therefore suppresses lower-severity evidence whenever it co-occurs with a dominant lesion. We propose DomSet-MIL, a label-aware framework that aligns the annotation mechanism across bag and instance levels. Dominant-Label Censored Likelihood models the reported diagnosis without declaring unreported lesions absent. Severity-Ordered Residual Routing assigns patch evidence from high to low severity and preserves residual support for secondary findings, while top-$q$ pooling links local routing scores to bag prediction. Experiments across natural and controlled settings show that DomSet-MIL achieves state-of-the-art performance in dominant-label prediction while more effectively recovering latent coexisting-lesion evidence. These findings demonstrate that modeling the dominant-label mechanism can improve diagnostic prediction without sacrificing clinically meaningful secondary findings.

---


### 236. [SCCL-DT: Semantic-Conflict-Aware Contrastive Learning with Dual-Rule Teacher Distillation for Zero-Shot Chest X-Ray Diagnosis](https://arxiv.org/abs/2610.22094)

**<font color=#1a73e8>作者：</font>** Ting Liu, Haoran Lai, HaobinChen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastive vision-language pre-training supports zero-shot chest X-ray diagnosis, but standard objectives treat every off-diagonal image-report pair in a batch as a negative. In radiology, recurring findings across patients mean that instance mismatch need not imply semantic incompatibility, creating false-negative supervision that we term a semantic conflict. A training-trace audit shows that pair-observations selected by the online mask used during training are enriched for report-derived finding agreement, although this proxy analysis does not establish clinical equivalence. Fixed thresholds can become miscalibrated as similarity distributions evolve, while soft reweighting leaves residual repulsive gradients. We therefore propose Semantic-Conflict-Aware Contrastive Learning (SCCL), which tracks modality-specific similarity distributions with exponential-moving-average (EMA) statistics, derives adaptive thresholds, and hard-masks flagged candidates before softmax normalization. Inclusive (OR) and consensus (AND) rules define two SCCL teachers, whose bidirectional cross-modal rankings are consolidated through standard distillation into a single deployable student, SCCL-DT. Across five public chest X-ray benchmarks, SCCL-DT achieves a mean zero-shot AUC of $0.850$, compared with $0.837$ for the strongest evaluated baseline in our comparison. Code will be made publicly available soon.

---


### 237. [Unfragmenting Nawatl NMT: Single-Variant Specialization for Masewalkopa](https://arxiv.org/abs/2610.22110)

**<font color=#1a73e8>作者：</font>** Luis A. Mercado-Campos, Alexis Palmer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In minoritized (low-resource) language technologies, a common response to data sparsity is to aggregate text across multiple varieties and treat the combined data as a single corpus. However, mixed corpora of closely related indigenous variants can produce an artificial register that is accountable to no single speaker community, a structural failure we call variant fragmentation. This issue is acute for minoritized languages native to Mexico, such as Nawatl. Building on a 70,000-pair multi-variant foundation, we specialize an mT5-large checkpoint to Masewalkopa (nhn), the Nawatl variety spoken in Santa Ana Tlacotenco. We curate 2,665 parallel pairs, reserve all sentence-level data for evaluation, and incorporate 192 elder-transcribed target sentences via asymmetric backtranslation. A custom finite-state analyzer reduces unanalyzed surface forms from 82.0% to 19.9% and supplies functional syntax tags as plain-text prefixes, allowing the model to reuse existing subword embeddings rather than relying on frozen special tokens. The resulting LoRA-v9c-b model achieves 58.46 dev chrF++ and 58.20/57.90 directional test chrF++. Finally, CTranslate2 int8 quantization reduces CPU latency from 137.5 to 1.8-2.6 seconds per request, enabling cost-bounded Cloud Run deployment.

---


### 238. [Scene Reconstruction Using Ubiquitous Wireless Signals via Diffusion Posterior Inference Over physics-Grounded Representations](https://arxiv.org/abs/2610.22120)

**<font color=#1a73e8>作者：</font>** Vahid Yazdnian, Yasaman Ghasempour  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowing the layout of the physical world matters for many applications, yet the sensors we rely on for it (e.g., cameras and LiDAR) can fail in darkness, in adverse weather, or behind walls. Wireless signals do not face these limitations: every link between a base station and a user is shaped by the buildings it passes, reflects from, or is blocked by, leaving information about the surrounding scene embedded in the wireless channel measured at the endpoints. However, mapping channel measurements to the environment is a severely ill-posed problem: a measurement records only the structures that interact with the transmitted electromagnetic waves along its propagation paths, and even these observations can often be explained by multiple plausible scenes. We therefore formulate wireless scene reconstruction as posterior inference and develop a hierarchical framework with two complementary stages to approach this problem. A wireless foundation model, pretrained to respect propagation physics, transforms each channel measurement into a representation of the scene structure that shaped the observation. A diffusion model then jointly integrates representations from multiple measurements to model and sample the posterior over building occupancy, with consensus over samples producing the final reconstruction. We demonstrate that the framework can accurately recover building footprints from wireless channel measurements alone and show that its performance depends critically on both design components: physics-grounded representations expose scene-relevant information, while joint posterior inference coherently integrates complementary observations.

---


### 239. [Beyond Fixed Acquisition Functions: Temporal Difference Active Learning for Perturbation Discovery](https://arxiv.org/abs/2610.22122)

**<font color=#1a73e8>作者：</font>** Xudong Zhang, Jianzhe Li, Yitong Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Genetic and drug perturbation screens are important tools for elucidating disease mechanisms and validating therapeutic targets, but experimental costs limit the number of candidates that can be tested. Existing perturbation screening methods typically update the surrogate model with feedback while keeping the acquisition function fixed, limiting their ability to adapt selection to different response landscapes. Experimental feedback reveals current hits and informs subsequent selection by updating candidate predictions, providing a training signal for learning how to select experiments. We formulate budgeted perturbation discovery as a sequential decision problem and propose Temporal Difference Active Learning (TDAL), which learns an acquisition function online through temporal difference learning from a single screening trajectory, accounting for current hits and future discoveries. TDAL uses the Hellinger distance between hit probabilities for unmeasured candidates before and after an experiment to weight successor value, and reuses measured outcomes through leave-batch-out (LBO) to construct virtual transitions and alleviate training data scarcity. Across eight public screens spanning single, double, and triple perturbations under varied experimental configurations, TDAL achieves an average rank of 1.63 among eleven methods and ranks first on four tasks, demonstrating its adaptability across response landscapes.

---


### 240. [Causal Integrated Gradients: Scalable Feature Attribution Along Causal Paths](https://arxiv.org/abs/2610.22126)

**<font color=#1a73e8>作者：</font>** Joran Michiels, Anis Ismail, Maarten De Vos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing feature attribution methods that account for feature dependencies do not scale to high dimensions. We propose causal integrated gradients (CIG) and causal expected gradients (CEG), which extend integrated gradients to incorporate prior causal structure among input features while retaining its computational efficiency and, under conditions on the causal graph, its axiomatic guarantees. In many settings, some causal structure between features is already known, for example, that a transcription factor causally regulates a target gene's expression. Yet existing gradient-based methods cannot exploit this structure, instead crediting a feature's downstream effects over its true upstream cause, such as ranking the target gene above the transcription factor that regulates it. Our key idea is to embed this causal structure by routing the integration path along the causal graph. The method thereby decomposes each feature's attribution into a direct effect and effects mediated through its causal descendants. We evaluate CIG in three settings of increasing realism. First, on a synthetic benchmark with a known causal model, CIG's attributions best match the ground-truth causal effect from Pearl's do-calculus, matching the accuracy of causal Shapley values at a fraction of the computational cost. Second, on simulated single-cell gene expression data with a known gene regulatory network (Dyngen), CIG most accurately recovers the transcription factors driving the simulation. Third, on real interferon-$\beta$ stimulation data, where only an approximate causal graph is available, CIG better prioritizes the transcription factors driving the measured response than DeepSHAP and integrated gradients. Together, these results show that incorporating causal structure into gradient-based attributions recovers upstream drivers that existing methods miss, without sacrificing scalability.

---


### 241. [FALCON: FPGA-Accelerated Latency-Certifiable Occupancy Networks for Camera-Based Autonomous Driving](https://arxiv.org/abs/2610.22143)

**<font color=#1a73e8>作者：</font>** Haohua Que, Mingkai Liu, Handong Yao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A perception system that must brake for a pedestrian does not need a low average latency. It must deliver an answer before the deadline on every frame, the worst case included. Commodity edge accelerators optimize the mean through dynamic scheduling, OS jitter, thermal throttling, and contention, so their per-frame latency can be measured but not bounded. We build FALCON, a camera-based 3D occupancy front-end on the AMD Kria KR260, an embedded FPGA drawing 4.3 W idle and up to 6.6 W under inference, and make the latency guarantee layered and explicit: programmable-logic (PL) compute is cycle-bounded analytically; inference is a measured envelope over 100k-frame traces; and a watchdog enforces output delivery, publishing the previous output flagged stale when a frame is late. The deadline runs use a fixed-work proxy of six ResNet-50 DPU inferences per frame, not the full occupancy network: across three 100k-frame enforced runs, all 300k proxy frames delivered an output within the 100 ms deadline plus at most 10.2 ms, the worst of the three runs. The full six-camera FlashOcc pipeline composes to about 1.3 s per frame on the board and is not yet a 10 Hz system. The two operations the DPU cannot run, a view-transform gather and a bilinear resize, become fixed-trip-count PL IPs numerically matched to their software references. On the full Occ3D-nuScenes validation set the board reaches mIoU 29.88, 92.8% of an FP32 baseline the DPU cannot run. On a ResNet-50 probe over 100k frames the KR260 tail stays within 1.5 times its median (2.0 times for the six-inference proxy), where Jetson Orin reaches 4.4 times and the worst datacenter GPU run (NVIDIA L4) 23.6 times. The deployment recipe, HLS sources, and raw timing traces are released.

---


### 242. [MAppPrint: Robust and Real-time Mobile App Fingerprinting via Traffic Behavior Correlation Graphs](https://arxiv.org/abs/2610.22148)

**<font color=#1a73e8>作者：</font>** Tao Duan, Junzhou Zhao, Jianglong Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mobile apps have become ubiquitous in daily life. Despite communication encryption, app fingerprinting (AF) attacks can still enable adversaries to infer the apps in use by analyzing patterns of encrypted network traffic. However, existing AF attacks suffer from three critical limitations that hinder their practical effectiveness: (i) the inability to capture app-specific traffic dependencies, rendering traffic fingerprints fragile under dynamic networking conditions; (ii) the neglect of latency and throughput considerations, resulting in inefficient real-time user tracking; and (iii) the incapacity to handle mixed traffic generated by multi-app concurrency.
In this paper, we propose MAppPrint, a robust and real-time app fingerprinting framework. MAppPrint introduces a behavior-level traffic fingerprint, i.e., Traffic Behavior Correlation Graph (TBCG), which models app traffic by capturing unit traffic behaviors and their correlations, thereby providing reliable app fingerprints. To enable real-time fingerprinting, MAppPrint incorporates a fingerprint compression algorithm that transforms each TBCG into a compact graph by selectively aggregating redundant information. Furthermore, MAppPrint employs an unsupervised decomposition strategy to disentangle mixed traffic generated by multi-app concurrency, enabling unified identification of both single-app and multi-app traffic. Extensive experimental results demonstrate that MAppPrint achieves 4.9~13.9% improvement in AF precision and 3~6 times improvement in timeliness over state-of-the-art methods. Meanwhile, MAppPrint is robust in dynamic networking conditions, while achieving a throughput of 10.5 GB/s and a prediction latency of 0.68 seconds.

---


### 243. [Specification Gaming and a Constrained Reinforcement Learning Mitigation in a Cleaning Gridworld](https://arxiv.org/abs/2610.22152)

**<font color=#1a73e8>作者：</font>** Hilda Adwubi Osei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning agents optimize exactly the reward signal they are given, which can diverge sharply from an intended true objective when that signal is only a proxy for it; this failure mode is known as specification gaming. Existing evidence for this failure mode is largely observational, with comparatively few demonstrations pairing a controlled, deliberately constructed proxy/true gap with a mitigation that carries a verifiable guarantee rather than only an empirical improvement. We construct a minimal gridworld in which a cleaning-robot agent can either genuinely remove dirt or conceal it from a cheap sensor, and show that a standard deep Q-network trained only on the sensor's proxy reward converges to a policy that games it completely, reaching near-maximal proxy reward while never achieving the true objective. We then introduce a constrained reinforcement learning fix, penalizing the specific behaviors through which the agent exploits the gap, and show that it eliminates the gaming behavior from the final policy while substantially recovering true-objective performance. We further derive and empirically verify an exact accounting identity relating the proxy reward, true reward, and our cost signal for this environment, showing that the cost signal measures the proxy/true gap exactly rather than merely tracking it, and yields a deterministic guarantee under a hard-constrained variant of the method.

---


### 244. [Realtime-Bench: Can Frontier Models Solve Real-time Interactive Problems?](https://arxiv.org/abs/2610.22155)

**<font color=#1a73e8>作者：</font>** Jingyu Tang, Xu Yang, Zhehao Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-time interaction requires agents to perceive evolving environments and act under temporal constraints, yet existing evaluations of real-time streaming models focus on conversational quality and streaming perception, leaving effective action under strict temporal constraints untested. We introduce Realtime-Bench, a suite of carefully curated dynamic tasks where delayed actions directly affect success. Under Wall Clock, where environments advance according to actual inference latency, the best success rate reaches only 44% and the best Pass^3 is only 36%, demonstrating that real-time interaction remains challenging. To separate serving latency from models' real-time streaming capability, we compare Wall Clock with Paused Clock, which removes inference delays as an idealized reference, and introduce Token Clock, which advances simulated time according to generated token counts, testing temporal awareness independently of physical serving speed. We find that temporal costs limit success in evolving environments and that higher reasoning effort has mixed effects under time pressure, reflecting a trade-off between decision quality and timely execution. These findings suggest directions for improving real-time multimodal agents, including adaptive reasoning with temporal awareness and continuous perception and action.

---


### 245. [The importance of tensor handling and implementation of physics-informed DeepONets](https://arxiv.org/abs/2610.22157)

**<font color=#1a73e8>作者：</font>** Nahum Banks, Gustavo A.M. de Almeida, Sergio Maldonado  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) reduce or eliminate the need for large labelled datasets by enforcing governing equations during training. Physics-informed Deep Operator Networks (PI-DeepONets) extend this approach to learning solution operators, enabling rapid prediction across families of problems. Despite these advantages, we show that their application to higher-dimensional problems remains limited by the computational cost of training. To address this issue, we propose a modified PI-DeepONet architecture that reduces this cost by removing redundancy in how the Branch network processes input functions across collocation points. The proposed formulation is mathematically equivalent to the original architecture but reduces input tensor sizes and the number of Branch network evaluations. We analyse the computational complexity of both architectures and derive theoretical scaling laws for training time with respect to the number of collocation points and input functions. The proposed architecture is evaluated on 1D, 2D, and 3D linear advection problems. In all cases, it achieves comparable predictive accuracy to the original PI-DeepONet while consistently reducing training time. In 2D experiments, a maximum speed-up of $3.75\times$ is observed, with empirical training-time scaling agreeing with the predicted linear dependence on collocation points and input functions. Furthermore, training a 3D model on an NVIDIA A100 GPU is only feasible using the proposed architecture, as the original formulation exceeds memory limits. These results demonstrate that careful consideration of how PI-DeepONets are implemented can yield substantial gains, enhancing the practical performance of PI-DeepONets and enabling their application to otherwise intractable physics-informed learning problems.

---


### 246. [Motion- and Gravity-Aware Feedforward 3D Reconstruction](https://arxiv.org/abs/2610.22177)

**<font color=#1a73e8>作者：</font>** Shiyao Qian, Yuan Ren, Dongfeng Bai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward transformer models have recently achieved strong performance in multi-view 3D reconstruction, but they still rely primarily on appearance-based attention and often struggle in dynamic scenes with weak geometric cues. In this work, we introduce a motion- and gravity-aware framework under the Learning Using Privileged Information (LUPI) paradigm. During training, residual optical flow and gravity direction are provided as privileged signals to guide geometric representation learning; during inference, the model uses standard visual inputs only.
We integrate these priors into transformer backbones with lightweight architectural changes, preserving feed-forward efficiency. Experiments on standard benchmarks show consistent gains in reconstruction accuracy and robustness, especially in scenes with dynamic objects, ambiguous structure, and challenging camera motion. Our analysis further shows that the optimal injection stage is backbone-dependent: middle-layer integration is generally preferable for VGGT, while late-stage integration is more effective for {\pi}3. These results suggest that LUPI offers a practical way to inject motion and physical priors into feed-forward 3D reconstruction without increasing test-time complexity.

---


### 247. [LAMP: Layerwise Adaptive Mixing of Predictors for Training-Free Few-Shot Vision-Language Adaptation](https://arxiv.org/abs/2610.22182)

**<font color=#1a73e8>作者：</font>** Zhipeng Ye, Feng Jiang, Qiufeng Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot adaptation often relies on an encoder's final global representation, leaving complementary information in intermediate layers underused. Combining these features is challenging because their dimensions can differ and their usefulness varies across tasks. We propose LAMP, Layerwise Adaptive Mixing of Predictors, a training-free framework that combines global and regional information from multiple encoder layers. A single forward pass per view supplies all descriptors. Global and support-calibrated regional kernel predictors independently fit the same label residuals. Labeled validation data select their mixture in class-score space, preserving native feature dimensions without learned projections. LAMP-F further adapts text-anchored class prototypes, using a cached response to update the fixed-kernel residual predictions exactly. Experiments cover eleven datasets and ViT and ResNet backbones. LAMP achieves state-of-the-art mean accuracy among the compared published training-free ResNet-50 methods at 4, 8, and 16 shots, reaching 78.73% at 16 shots. Averaged across five support budgets, LAMP improves over a paired global-feature-only baseline by 1.14 and 1.59 percentage points on ViT-B/16 and ResNet-50; LAMP-F raises these gains to 1.96 and 2.54 points. LAMP-F reaches 16-shot accuracies of 83.57% and 79.10%, respectively. Controlled experiments identify multi-layer integration as the main source of improvement and examine pooling, calibration, validation labels, and computational cost. These findings show that combining layer-specific predictions can exploit complementary features from frozen encoders to improve few-shot classification.

---


### 248. [TRACE: Topology-Aware Reconnection via Prediction-Adaptive Connectivity Enforcement for Thin-Structure Segmentation](https://arxiv.org/abs/2610.22210)

**<font color=#1a73e8>作者：</font>** Junho Moon, Ikbeom Jang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thin, elongated structures are particularly sensitive to connectivity errors, as even a few local segmentation mistakes can disrupt otherwise continuous paths. Existing skeleton-based objectives typically supervise fixed centerline locations and do not account for alternative local routes that may restore connectivity. We propose TRACE, a topology-aware, prediction-adaptive objective that uses a target skeleton to define required local connections. For each connection, TRACE identifies the easiest valid reconnection under the current prediction and jointly supervises its bottleneck with the corresponding skeleton point. The supervision thus adapts to the evolving prediction rather than remaining fixed to the centerline. We further introduce a topology-aware skeleton carrier that preserves both foreground and class-specific topology, enabling reliable definition of these connections. Extensive experiments across six 2D and 3D benchmarks show that TRACE improves connectivity and topology while maintaining strong segmentation accuracy with low training overhead. Code will be released upon acceptance.

---


### 249. [Generalization Guarantees of Randomized Block Coordinate Descent for Nonconvex Learning](https://arxiv.org/abs/2610.22213)

**<font color=#1a73e8>作者：</font>** Ruixi Hu, Liang Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Randomized block coordinate descent (RBCD) is a popular optimization algorithm for many large-scale machine learning problems. The existing theoretical analysis of RBCD mainly focuses on its convergence behavior from an optimization perspective, while its generalization behavior remains less understood for nonconvex problems. In this paper, we establish high-probability generalization guarantees for RBCD with nonconvex objectives. In the general nonconvex setting, we derive bounds on the gradients of both empirical and population risks, requiring only standard smoothness assumptions. With polynomially decaying step sizes, we tune the iteration number to balance optimization and generalization, thereby quantifying how early stopping leads to the optimal convergence rate for the population gradients. In the gradient-dominated setting, we provide bounds in terms of functional suboptimality, which nearly match the optimistic rates in convex and low-noise settings. Finally, we develop dimension-independent bounds for loss functions of a specific structure, making the generalization guarantees applicable to high-dimensional problems.

---


### 250. [GNN-Guided Local Refinement for Efficient Layout Decomposition with DSA-MP](https://arxiv.org/abs/2610.22214)

**<font color=#1a73e8>作者：</font>** Yu Feng, Liyi Zhou, Haoyu Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multiple patterning lithography (MPL) has been widely used to improve lithography resolution in advanced nodes, but it faces cost limits as feature sizes shrink. Directed self-assembly (DSA) offers a cost-effective complement, extending the resolution of optical lithography to sub-10 nm and beyond. Integrating DSA into MPL (DSA-MP) further enhances the resolution of contact/via patterning. Nevertheless, growing design complexity exposes the limits of existing decomposition methods, which struggle to balance solution quality and runtime, and neglect edge-to-edge spacing constraints of DSA templates, compromising manufacturability. To address these issues, we introduce a new conflict graph model capturing the previously overlooked constraints and develop a local refinement strategy powered by the graph neural network, enabling efficient and scalable layout decomposition. Experiments demonstrate that our method achieves higher solution quality with faster convergence than state-of-the-art methods, while maintaining robustness across layout scales, design styles, technology nodes, and varying mask counts.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-278](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
