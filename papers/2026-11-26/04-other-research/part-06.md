# 📦 其他研究 | 2026年11月26日

> 本类共 **342** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-342](./part-07.md)

---

### 251. [Representation and Model Contributions on Small Molecular Benchmarks: Controlled Comparisons and External Evaluation](https://arxiv.org/abs/2611.32568)

**<font color=#1a73e8>作者：</font>** Nora A. M. A. Talkhan, Ibrahim Abdelbaky, Fatma A. Omara  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Improvements in molecular property prediction are usually attributed to the model, although part of the gain may come from the molecular representation. New models are commonly benchmarked against a random forest (RF) trained on a molecular fingerprint, a comparison that changes the model and the representation at the same time. We separate the two contributions with a two-by-two factorial design in which the RF and a second model (CatBoost or the tabular foundation models TabPFN and TabFM) are each trained on a fingerprint and on RDKit descriptors, and each effect is tested with a paired scaffold bootstrap. Seven small MoleculeNet datasets (3 regression, 4 classification) are evaluated on the published split of a recent graph transformer (DGT), on 10 additional scaffold splits and on external datasets. For solubility and lipophilicity, the representation effect exceeds the model effect in every main factorial design, in all three evaluations. For hydration free energy, the result depends on the starting fingerprint: from ECFP4 the representation effect is larger, and from MACCS neither effect is significantly larger. On the classification datasets, only one main factorial design has a significant difference between the two effects. Although the model effect is smaller on solubility and lipophilicity, TabFM outperforms the RF on all 7 datasets when both use RDKit descriptors. With RDKit descriptors in place of a fingerprint, the RF baseline reported for DGT surpasses the transformer's published solubility score. We recommend that model comparisons evaluate classical baselines on more than one representation and report the representation and model effects separately.

---


### 252. [Boiling Down Uncertainty: Deep Generative Scenario Search with Decision-Guided Evolution Strategies for Two-Stage Stochastic Optimization](https://arxiv.org/abs/2611.32573)

**<font color=#1a73e8>作者：</font>** Atefeh Hemmati Golsefidi, David Pisinger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One of the most common models for handling uncertainty is two-stage stochastic programming. Choosing the right number of scenarios is a trade-off between the uncertainty that can be represented and computational cost. A recent method, Deep Generative Scenario Search, generates synthetic scenarios and improves them by learning from the decisions they induce. The original approach used a black-box gradient estimate, since decisions are piecewise constant across scenarios. This paper provides the missing analytical foundation by deriving the gradient in closed form from recourse duality and an adjoint solve of the regularized reduced problem. The decision-focused direction, with a heuristic direction as a backup when duals are unavailable, defines the sampling subspace of a guided evolution strategy rather than being used as a direct update. For any guiding subspace, the expected update is a descent direction of the smoothed objective, so an inaccurate guide adds variance while the expected step still descends. For six problem families, both guided estimators outperform the baseline. The decision-focused version reduces the mean gap by three-quarters, and on the two families with the most integer variables the reduced sets beat the exact solver's two-hour incumbent in most runs, using a fifth of the time.

---


### 253. [CoReQ: Condition-Aware Cross-Modal Repair and Quality-Guided Robust Collaborative Perception](https://arxiv.org/abs/2611.32588)

**<font color=#1a73e8>作者：</font>** Ziwei Guo, Lingzhi Li, Jin Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-vehicle collaborative perception can use observations from different perspectives to alleviate the problems of occlusion and limited sensing range. However, missing echoes and false echoes caused by bad weather will reduce the quality of single-vehicle features and affect collaborative detection. LiDAR provides richer geometric information, and 4D Radar has strong weather adaptability. The complementarity of the two provides the possibility to improve perception under degraded observations. However, how to adjust cross-modal repair according to the current observation conditions and how to reasonably integrate multi-vehicle features whose reliability still differs after repair are still problems that need to be solved. To this end, we propose CoReQ, a condition-aware repair and quality-guided collaborative perception framework. For the former, the condition-guided bidirectional cross-modal repair module (CBCR) extracts vehicle-level observation conditions from point cloud occupancy, density and feature statistics, and adjusts the bidirectional correction of LiDAR and Radar features accordingly. For the latter, we combine local reliability assessment with collaborative weighting: first, the task-aware quality estimation module (TaQE) uses the classification and positioning information of the EMA teacher to construct a supervision target and predict the spatial quality of the repaired features; then, the condition and quality guided fusion module (CoQF) matches the quality information with the content, and the observation conditions of both parties are jointly used for multi-vehicle feature weighted fusion. Experiments on V2X-R and V2X-Radar-C show that the framework is competitive under a variety of observation conditions, achieving significant gains in AP@0.7 on V2X-R under snowy conditions, and achieving the highest AP among the compared V2X-Radar-C methods.

---


### 254. [FewRef-5: Fixed-Reference Test-Time Adaptation for Virtual Staining](https://arxiv.org/abs/2611.32591)

**<font color=#1a73e8>作者：</font>** Wenxuan Wang, Liwen Wang, Mingmin Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Virtual staining synthesizes special-stain images from routine hematoxylin and eosin (H&E), extending the information available from an existing digital slide. However, a fixed inference rule can leave available real target-stain references unused, limiting query-specific correction of stain appearance at deployment. Test-time adaptation (TTA) provides a mechanism for this reference-guided, query-specific refinement without retraining the generator. We therefore propose FewRef-5, a reference-assisted TTA method for virtual staining built on StainPromptInversion. We extract tissue-masked optical-density means and standard deviations from five real Masson's trichrome (MAS) training patches and average them into a fixed stain target. A scheduled statistic-matching loss introduces this target into per-query visual-prompt optimization alongside our edge/Gram consistency penalties and the inherited reconstruction objectives. The target remains unchanged across queries, avoiding recursive dependence on earlier generated outputs while the pretrained generator stays fixed. On recorded H&E-to-MAS outputs for 1,989 queries, FewRef-5 reduces target-set FID from 183.201 to 166.904 and increases source-referenced SSIM from 0.92787 to 0.94996 relative to our Edge+Gram variant. Source PSNR and MS-SSIM decrease, showing an endpoint trade-off rather than uniformly better reconstruction.

---


### 255. [On the Effectiveness of Resampling for Supervised Graph Anomaly Detection](https://arxiv.org/abs/2611.32598)

**<font color=#1a73e8>作者：</font>** Cyril Perosino, Rino Di Chiara, Hamida Seba  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Class imbalance and scarce anomaly labels motivate oversampling in supervised graph anomaly detection (GAD), but its benefits across detectors and benchmarks remain unclear. In the low-label setting of GADBench, with 20 labelled anomalies and 80 labelled normal nodes, we compare class weighting and up to six oversampling strategies in ten detector configurations from three families: graph neural networks (GNNs), tree ensembles on neighbourhood-aggregated features, and tabular foundation models, on 17 datasets. On the eight datasets with organic anomalies, no strategy has a statistically resolved average gain in any configuration, and which nodes are labelled matters as much as the strategy. On the nine datasets with injected anomalies, Gaussian-noise oversampling (ROSE) gains up to 5.2 AUPRC points in four of the six tree and tabular foundation model configurations, and in all six only on attribute-swap anomalies; in four GNNs its gain is not distinguishable from zero. This gain depends on the injection recipe, which gives swapped nodes an atypical feature norm: it is no longer distinguishable from zero when the swap uses a single random donor or preserves the norm, although most detectors then also stop detecting the swaps. Over the 17 datasets, tuning the tree detectors adds about three points, as much as ROSE, and cuts ROSE's gain by about half or more. With the same source nodes and class weight, sampled graph views are not distinguishable from plain copies of those nodes. We recommend tuning baselines, repeating labelled splits, reporting organic and injected anomalies separately, and checking label-free degree and feature-norm baselines.

---


### 256. [ST-GNN-AAAS: Spatio-Temporal Graph Neural Networks for Anytime Automatic Algorithm Selection in the Traveling Salesman Problem](https://arxiv.org/abs/2611.32602)

**<font color=#1a73e8>作者：</font>** Zeyu Zhang, Mustafa Misir  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anytime Automatic Algorithm Selection (AAAS) aims to make solver choices under varying time budgets. The existing AAAS approaches largely rely on static instance characteristics and make limited use of temporal information revealed during solver execution. We propose ST-GNN-AAAS, a Spatio-Temporal Graph Neural Network framework for AAAS in the Traveling Salesman Problem (TSP). The framework represents evolving incumbent tours using time-varying node features, including distances from each node to its neighbors in the current tour, and combines these features with solver performance observations over a short history window. Given this short history, ST-GNN-AAAS predicts solver selections over a longer future horizon. We evaluate the method on a subset of diverse TSP benchmarks from NATIONAL, TNM, TSPLIB, and VLSI, releasing the corresponding solver execution data to support reproducibility. Our model achieves a selection accuracy of 76.59% and closes 46.05% of the average rank gap between the single best solver (SBS) and the virtual best solver (VBS).

---


### 257. [When "Neutral" Means Irrelevant: A Construct-Validity Audit of NormAd-ETI](https://arxiv.org/abs/2611.32614)

**<font color=#1a73e8>作者：</font>** Aarav Singh, Animesh Pathak, Christian Hoang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> NormAd-ETI scores a model's judgment of everyday actions as acceptable, unacceptable, or neither as the cultural context shrinks from a specific rule to a country name. We audit what that three-way score measures. It combines two decisions: whether a supplied norm applies, and whether the action conforms to it. Separating them shows that when only a country is shown, applicability falls to near chance while conformity stays well above it, because the prompt withholds the rule a Neutral label depends on. Because one answer carries both decisions, the score follows the steadier conformity and hides the weaker applicability, and no single prompt recovers the two separately. Dedicated forced-choice probes separate them for frontier models but not for small open models, where the applicability judgment still tracks the hidden acceptability label. Adding a written rationale reduces that conflation without removing it. We recommend reporting the two results separately and measuring the conflation gap.

---


### 258. [REBEAL: Human References Are No Longer the Best Translation, and Metrics Do Not Notice](https://arxiv.org/abs/2611.32623)

**<font color=#1a73e8>作者：</font>** Ahrii Kim, Chanjun Park, Seong-heum Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reference-based MT evaluation assumes the human reference is correct and better than the systems it scores. Both assumptions now fail, since the human reference ranks first in none of the 2024 WMT MQM campaigns and carries annotated errors in 19% to 87% of its segments. What a metric does with a flawed reference is a question about the metric, and it would have been worth asking before reference quality came into doubt. We introduce REBEAL (Reference Bias EvALuation), a benchmark that probes how MT metrics respond to seven types of controlled reference contamination, drawn from the error categories those campaigns record. Across eight widely used metrics and three language pairs, recent learned metrics (xCOMET, MetricX) prove more robust than their predecessors, but each family fails in its own way. Surface metrics show no length sensitivity, so contamination hides in longer segments, while learned metrics accept references in unrelated languages as nearly correct. The failure they share is named-entity contamination, which no metric detects and which flips up to 8 of 36 system pairs when ranking nine MT systems.

---


### 259. [On the Capabilities and Limitations of Zero-Shot Open-Vocabulary Cloud Segmentation](https://arxiv.org/abs/2611.32625)

**<font color=#1a73e8>作者：</font>** Jose Sosa, Thomas Gillet, Rim Sleimi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in vision-language foundation models have enabled open-vocabulary semantic segmentation (OVSS) without task-specific training, offering new opportunities for Earth Observation (EO) applications. However, their capabilities for cloud detection remain insufficiently explored. In this work, we evaluate twelve OVSS approaches across six publicly available EO datasets in a zero-shot setting, i.e., without fine-tuning or adaptation to the target data. We investigate both binary cloud detection and multiclass segmentation, distinguishing between thick clouds, thin clouds, cloud shadows, and background. Our results show differences in performance across models and datasets, with SegEarth-OV3 achieving the highest binary cloud detection performance on four of the six datasets. While several approaches demonstrate promising performance in binary cloud detection, multiclass segmentation remains more challenging, particularly when distinguishing between fine-grained cloud categories. Furthermore, our controlled prompt sensitivity analysis reveals model-dependent responses to alternative textual descriptions, with appearance-oriented prompts benefiting certain approaches while degrading the performance of others. Overall, our findings demonstrate both the potential and current limitations of zero-shot OVSS for cloud detection, establishing a comparative benchmark for future research on generalisable cloud segmentation. Code will be available at: this https URL.

---


### 260. [Completion-Aware Compression for Progressive 3D Gaussian Splatting](https://arxiv.org/abs/2611.32628)

**<font color=#1a73e8>作者：</font>** Reagan Koo, Yeong-Gyu Kim, Eun-Seok Ryu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) enables high-quality novel-view rendering, but its large scene representations are costly to transmit. Pruning and compression reduce file sizes, yet progressive delivery also requires usable reconstructions before the full scene arrives. Existing progressive representations provide partial scenes, but level-based updates are limited by predefined coding boundaries. This paper presents a progressive 3DGS codec that balances attribute fidelity with the image benefit of making Gaussians available earlier. Its single compact stream supports partial 3D reconstruction and adds newly decoded Gaussians as more bytes arrive. The stream supports fine-grained updates at arbitrary received-byte budgets, without separate encodings or later attribute refinement. At matched complete-file sizes and received bytes, completion-aware allocation improves 1/8 PSNR over attribute-only allocation by 0.48-1.43 dB. The proposed codec compresses original 3DGS representations by 62-88 times while retaining near-reference Full PSNR. Under the evaluated 50-Mbps delivery model, partial reconstruction becomes available in approximately 0.2 s.

---


### 261. [HazeFlux: Few-Step Generative Priors for Real-World Image Dehazing](https://arxiv.org/abs/2611.32632)

**<font color=#1a73e8>作者：</font>** Yunong Liu, Danna Xue, Javier Vazquez-Corral  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world single-image dehazing suffers from severe domain shifts, as paired real data is scarce and models trained on synthetic haze generalize poorly to real-world haze. While pre-trained generative editing models offer powerful image priors to bridge this generalization gap, applying them to image dehazing poses two major challenges: standard generative models prioritize distribution alignment over strict pixel-level fidelity, and operating in compressed latent spaces inherently discards fine-grained structural details. In this paper, we propose a novel two-stage framework that adapts the generative prior of a few-step flow-matching backbone to real-world dehazing. In the first stage, we fine-tune the latent backbone using Low-Rank Adaptation (LoRA), supervised not only on a flow-matching objective, but also on pixel-level supervision, thus enabling direct hazy-to-clear translation. In the second stage, we introduce structure-preserving skip connections directly to the VAE decoder, bypassing latent compression artifacts to recover precise spatial edges. Experiments on four realworld benchmarks demonstrate that our approach significantly outperforms existing dehazing methods in real conditions.

---


### 262. [TeamFlowRL: Online Policy Optimization of Decentralized Flow Policies for Multi-Agent Coordination](https://arxiv.org/abs/2611.32645)

**<font color=#1a73e8>作者：</font>** Guowei Zou, Beiwen Zhang, Haitao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Complex cooperative tasks require coordinated multi-agent behavior. Offline generative policies learn expressive cooperative behaviors from trajectories but remain limited by fixed datasets. Online reinforcement learning can improve them through environment interaction. However, fine-tuning flow policies is difficult because action likelihoods are hard to compute. We propose TeamFlowRL, a two-stage framework that pretrains multi-agent flow policies offline and fine-tunes them online. We formulate team policy optimization over the complete denoising trajectories of decentralized flow policies, avoiding intractable action likelihoods. The resulting objective weights each agent's trajectory ratio with a shared team advantage and clips each ratio separately, aligning local policy updates with the common team return. Across 51 paired configurations in seven simulation groups, TeamFlowRL improves every offline initialization, with a 47.3% average gain in normalized score. It also achieves 33.1% higher average success under exploration noise than Gaussian-policy fine-tuning across 6 bimanual tasks.

---


### 263. [LaWanle: Why Can't Leading Driving Models Make a Simple Turn?](https://arxiv.org/abs/2611.32650)

**<font color=#1a73e8>作者：</font>** Chengzhi Gao, Junzhe Gao, Yongzhi Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We were surprised to find that leading end-to-end driving models across major paradigms, despite scoring close to human drivers on NAVSIM, cannot reliably make a simple 90-degree turn in photorealistic closed-loop simulators. To investigate why, we build LaWanle, a benchmark of turns drawn from three such simulators. Driving each turn from several starts, we find that the same model passes it from one start and fails it from another, and that the two drives look alike until they enter the junction. Rotating the car by a few degrees at the junction entry can fail a turn it otherwise passes. Conversely, a slight heading correction to the plans can rescue about half of the failed turns we tested. Such errors arise when a model drives by itself, so we post-train an open-source lane-keeping model with closed-loop DAgger on its lateral path. Training 5% of its parameters is enough to raise its turn pass rate from 19% to 76%. The gain transfers to the two other benchmarks, where the policy also scores among the leading models. Further fine-tuning on recovery data repairs the deviations it is trained on but, against a control trained equally long, improves turns on none of the three benchmarks, and every variant stays far below a human driver.

---


### 264. [LATEC: Learned Axial TEnsor Compression for High-Dimensional Scientific Data](https://arxiv.org/abs/2611.32651)

**<font color=#1a73e8>作者：</font>** Hippolyte Verninas, Hadrien Hendrikx, Thomas Moreau  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the growing scale of scientific simulation and infrastructure, part of the burden has shifted from producing scientific data to analyzing and storing it. Compression is a key step to expanding storage capacity, but requires dedicated techniques to enforce user-specified pointwise error bounds that ensure the validity of downstream scientific workflows. To further push the limits of compression, novel learned codecs have been developed, in particular for images and videos, but these methods often optimize for aggregated distortion and fail to meet error bound standards. Moreover, these methods often target fixed field dimensionality, failing to account for many scientific data use cases, or at the expense of large adaptation or retraining costs. In this work, we introduce the Learned Axial TEnsor Compression (LATEC) method, an error-bounded codec with a dimension-agnostic learned predictor based on a GNN architecture. LATEC is pretrained on synthetic 2-D and 4-D fields, and evaluated with and without domain fine-tuning on 13 scientific fields in 3-D to 5-D. Results show that LATEC is consistently competitive with SZ3, achieving an 18.1% average improvement and greater consistency across all domains than other compressors. These results demonstrate that a shared learned predictor can serve as a single error-bounded codec across tensor dimensionalities, competitive with specialized compressors, while retaining pointwise error guarantees.

---


### 265. [Power Side-Channel Evaluation using Multi-FPGA Systems](https://arxiv.org/abs/2611.32652)

**<font color=#1a73e8>作者：</font>** Yaswanth Tavva, Geng Luo, Trevor E. Carlson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Complex out-of-order processors are difficult to evaluate for power side-channel leakage before tapeout. A single FPGA often lacks sufficient capacity, whereas conventional CAD-based analysis is too slow to support the large numbers of traces required by practical attacks. Multi-FPGA emulation provides greater capacity, but existing partitioning schemes are not security-aware and thus results in poor attack performance. This work presents Scissors, a security-aware multi-FPGA partitioning approach for pre-silicon power side-channel evaluation of complex out-of-order processors. Scissors uses side-channel vulnerability factor (SVF) analysis to identify signals correlated with the secret key. It then keeps strongly key-correlated signals confined to one FPGA partition (measured) while moving rest of the signals to the other FPGAs (support), improving the observability of the side-channel information. We evaluate Scissors through RTL simulations and physical measurements on a two-U200 FPGA testbed, using frequency-domain CPA with a Hamming-weight leakage model. RTL ablation shows that only 68-71 high-SVF signals dominate key recovery process. For a single-core processor (SingleBOOM), Scissors recovers the key with 12,000 traces, compared with 49,000 for the unpartitioned design and 43,000 for TritonPart, while improving correct-key correlation by $2.83\times$. For a quad-core processor (QuadBOOM), which exceeds the capacity of the CW340 single-FPGA platform, Scissors reduces the required traces from 111,000 to 66,000 and improves correlation by $1.48\times$ over TritonPart. Scissors also reduces QuadBOOM RTL-to-bitstream generation from 61 h 39 min to 6 h 40 min, a $9.25\times$ speedup. These results show that security-aware partitioning improves leakage observability and attack performance while substantially reducing implementation time for complex processors against the baseline method.

---


### 266. [GeoSurge: Geometry-Grounded Multimodal Reasoning for Auditable Liver Resection Planning](https://arxiv.org/abs/2611.32657)

**<font color=#1a73e8>作者：</font>** Wenjie Deng, Zijian Tu, Xueyin Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Surgical resection planning centers on generating executable resection surfaces from anatomical evidence and operative constraints. Medical multimodal foundation models enable anatomical understanding, and segmentation models predict resection regions, but neither translates these capabilities into explicitly constrained, executable resection surfaces. We present GeoSurge, an anatomy-grounded framework that combines mask-derived metrics with structure-aware point-cloud tokens to generate executable, editable resection surfaces. To make resection geometry learnable and editable, GeoSurge maps actions to parametric geometry through a surface-action grammar. Using this grammar, anatomy-oriented and tumor-centered templates generate candidates, which are filtered by hard constraints and semantic deduplication. Training supervision is then derived from candidate-expert geometric agreement and independently recomputed feasibility metrics. At inference, the reasoner uses patient evidence and surgical requirements to select or revise an action, which an independent geometry engine subsequently materializes and verifies. GeoSurge achieves the best overall scores on DeepTumour Liver and CRLM-QA, improving the constraint satisfaction rate from 73% to 100% on CRLM and from 56% to 99% on GeoSurge-Bench.

---


### 267. [Attack-Inference Aligned Universal Adversarial Attacks on Video Object Segmentation](https://arxiv.org/abs/2611.32658)

**<font color=#1a73e8>作者：</font>** Ruiqi Shen, Chang Liu, Henghui Ding  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern video object segmentation (VOS) relies on a two-stage inference paradigm: target initialization and memory-based propagation. However, existing adversarial attacks on VOS often overlook this structure. To bridge this gap, we propose AUV, an adversarial framework that Aligns with the Universal two-stage paradigm of VOS models. Specifically, AUV optimizes a universal adversarial perturbation (UAP) through decoupled training strategies tailored for both initialization and propagation stages. By disrupting the shared memory space, it achieves prompt-agnostic attacks across different modalities, including masks, points, boxes, and language. Extensive experiments show that AUV establishes state-of-the-art VOS attack performance, such as degrading mask-based SAM3 to only 8.4 J&F on DAVIS17-val (compared to 55.4 for the previous SOTA under the same training setup). It also exhibits superior temporal dynamics with the fastest onset, the most enduring persistence, and the support of any-time mid-video attacks. The AUV optimization framework is applicable to different VOS models, revealing vulnerabilities in real-world streaming VOS. Code is available at this https URL.

---


### 268. [Bathys: Advancing Deep Search Agents](https://arxiv.org/abs/2611.32660)

**<font color=#1a73e8>作者：</font>** Zixuan Chen, Shengyou Yuan, Nang Yuan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep search is a critical capability for agents tackling complex, open-ended tasks, where solving a problem requires iterative information gathering, query reformulation, and evidence-based verification rather than a single retrieval step. To address these requirements, we present Bathys 9B and 27B deep search agents built around a training framework that spans verifiable question synthesis, post-training, and online reinforcement learning (RL) under context compression. Our high-quality data construction ensures both search depth and reliability: each clue is reformulated as an indirect reference requiring independent retrieval, and retained evidence chains enable verification that the clues jointly determine a unique answer. Curated trajectories underpin a pipeline of supervised fine-tuning (SFT), Kahneman-Tversky Optimization (KTO), and Compaction-Managed Group Sequence Policy Optimization (CM-GSPO): SFT provides a stable foundation for tool use over long horizons and query reformulation; KTO uses binary feedback on trajectories to improve the selection of answers grounded in evidence; CM-GSPO optimizes execution sub-trajectories with length-normalized likelihood ratios on the recorded rollout contexts and reweights sub-trajectory advantages to correct the extra weighting introduced by independently averaging sub-trajectory losses. Bathys 9B and 27B attain 66.51% and 80.49% on BrowseComp, respectively, under an evaluation protocol with trajectory self-verification and conditional retries.

---


### 269. [TokenMatte: Unlocking T2V Diffusion Priors for Pixel-Native Video Matting](https://arxiv.org/abs/2611.32675)

**<font color=#1a73e8>作者：</font>** Zanyi Wang, Dengyang Jiang, Fengfei Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution video matting requires accurate recovery of continuous alpha values, including fine hair, soft boundaries, and motion blur, yet dense alpha supervision remains scarce. Pretrained text-to-video diffusion transformers (DiTs) offer rich spatio-temporal priors, whereas existing generative video matting approaches typically route alpha predictions through RGB-trained VAE latents, which can attenuate fine details and introduce additional decoding overhead. We present TokenMatte, which adapts a pretrained video DiT into a single-pass, auxiliary-free RGB-to-alpha predictor with a pixel-native output interface. At its core is a single shared linear readout that maps each spatio-temporal token directly to its corresponding ($t \times p \times p$) block of alpha pixels, predicting spatial details and temporal variations within the same local video block. Tiling these blocks produces the full-resolution alpha sequence without a convolutional decoder or learned upsampling. The predicted alpha is supervised directly in pixel space, while the ground-truth alpha never enters the VAE, eliminating target-side alpha encoding and output-side VAE decoding. Leveraging the pretrained video prior, TokenMatte is trained using only existing public matting datasets, without additional data curation or auxiliary inputs at inference. Compared with a matched latent-output baseline, our pixel-native interface improves matting accuracy while achieving a 1.51$\times$ inference speedup. TokenMatte establishes a new auxiliary-free state of the art on VideoMatte, YouTubeMatte, and V-HIM60.

---


### 270. [Load Balancing Neurons: Firing-Rate Control Sustains Plasticity in Continual Learning](https://arxiv.org/abs/2611.32691)

**<font color=#1a73e8>作者：</font>** Jan Robine, Marc Höftmann, Stefan Harmeling  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks in continual learning often lose plasticity: some neurons become inactive, while others fire almost constantly. This limits adaptation to shifting data and wastes capacity. Prior work mitigates this by periodically reinitializing low-utility units, but such resets can destroy previously learned features and do not proactively prevent low utility. We study a simple diagnostic measure: the firing rate of ReLU units, defined as the fraction of positive pre-activations. Low rates identify dead units, while very high rates indicate linearized, always-on units. Based on this view, we introduce a lightweight load-balancing mechanism that adjusts per-neuron thresholds to keep firing rates within a target range. Across continual ImageNet and class-incremental CIFAR-100, firing-rate distributions explain differences in plasticity across a range of approaches, including well-known techniques such as L2 regularization and non-affine normalization, and load balancing matches or exceeds reset-based methods on both benchmarks. The same mechanism carries over to reinforcement learning, improving Rainbow DQN on Atari over a LayerNorm baseline.

---


### 271. [RestPose: Canonicalization for Open Object Pose Estimation](https://arxiv.org/abs/2611.32696)

**<font color=#1a73e8>作者：</font>** Sandeep Inuganti, Weihang Li, Benjamin Busam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In object pose estimation methods, predicted poses are expressed with respect to a canonical frame, defined by a reference model of that object. In learning-based methods, an arbitrarily chosen modeling convention defines this canonical frame, which is then used to generate the ground-truth pose-annotations for training. Object pose estimation methods are therefore bound to such arbitrary conventions, restricting generalization. In this work, we propose that such a canonical frame can instead be derived for any object, and present RestPose, an approach towards open object pose estimation that does not require reference models or canonical frame conventions during training. From a single input image, we generate an object mesh and canonicalize it through a geometric and physical analysis of the object, then use foundation model-based dense matching to estimate the pose. We choose category-level benchmarks for our experiments, which contain instances across various object categories and enable us to measure the effectiveness of our canonicalization. Across HouseCat6D, NOCS, and Omni6DPose datasets, we improve on the supervised state-of-the-art methods by 18.3 points in absolute metrics and 13.8 points in scale-agnostic metrics, without requiring task-specific training. Code will be published.

---


### 272. [Contrastive Proxy Forests: Completeness-Preserving Proxy Learning from Multimodal Records](https://arxiv.org/abs/2611.32708)

**<font color=#1a73e8>作者：</font>** Kyoungeui Hong, Zijun Gao, Ruishan Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Proximal causal inference removes unmeasured confounding using two proxies of the confounder, an outcome-side W and a treatment-side Z. The proxies must satisfy exclusion restrictions and be complete, meaning that they reflect every aspect of the confounder. In practice, they are a few variables hand-picked from a structured table, even though clinical notes and physiological waveforms carry rich information about the confounder. Such records are too high-dimensional for a proximal estimator, and generic compression such as PCA may keep modality-specific variation (style) instead of the confounder, destroying completeness. Our key observation is that, under the proximal condition, the confounder is the only link between a treatment-side and an outcome-side modality beyond the covariates. Learning what they share therefore captures the confounder and filters out modality-specific style. Contrastive Proxy Forests (CPF) learns both proxies by contrasting the two modalities, given the covariates, on a separate unlabeled sample, and passes them to a proximal causal forest. This contrastive objective has an exact closed-form solution, ridge canonical correlation analysis. We prove that CPF preserves the exclusion restrictions exactly and that its proxies inherit the completeness of the raw records under conditions we characterize. Where style is strong, CPF lowers the error of conditional effects by 10-22% relative to PCA proxies, and on MIMIC-IV it is the only method whose point estimate of warfarin's effect on stroke falls inside the range of randomized trials.

---


### 273. [FourStat: A Dual AutoEncoder Leveraging Frequency and Stationarity for Time Series Anomaly Detection](https://arxiv.org/abs/2611.32714)

**<font color=#1a73e8>作者：</font>** Saman Hadian, Ramtin Moslemi, Mohammad Mohammadi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While numerous studies have focused on multivariate time series anomaly detection, many existing methods perform poorly or are not directly applicable to univariate settings. We introduce FourStat, a dual-model framework for univariate time series anomaly detection that combines two complementary approaches. The Fourier Autoencoder (FAE) captures global patterns like seasonality through frequency-domain analysis, while the Stationary Autoencoder (SAE) focuses on local structures by enforcing statistical stationarity. We also propose a new evaluation metric called Perfect Point that assesses whether perfect F1-scores can be achieved directly from anomaly scores, eliminating thresholding subjectivity. Results demonstrate that FourStat outperforms existing baselines, particularly on challenging anomaly types, while the new metric provides clearer insights into model performance gaps and advantages.

---


### 274. [SplatSeg3D: Efficient Zero-Shot 3D Segmentation via Point Cloud Surfelization and Splatting](https://arxiv.org/abs/2611.32716)

**<font color=#1a73e8>作者：</font>** Sandeep Inuganti, Mahdi Chamseddine, Marcel Rogge 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary 3D segmentation methods rely on 2D foundation models applied to registered images captured alongside the 3D point clouds. However, such images may not be available in many cases, while direct 3D point cloud segmentation methods require semantic class supervision and are challenging to deploy in a zero-shot manner. To address these issues, we present SplatSeg3D, which segments a bare colored point cloud in an open-vocabulary manner without requiring the accompanying images, camera poses, class supervision, or instance mask proposals. To achieve this, we first surfelize the input point cloud and obtain oriented 2D Gaussians. We then render views of the scene by splatting, with a view selection strategy that maximizes scene coverage with as few views as possible. Next, we apply text-prompted segmentation on the rendered views, giving each 3D point a set of multi-view semantic cues, fused to produce a 3D segmentation of the scene. We evaluate SplatSeg3D on semantic segmentation and novel-class instance segmentation on 4 standard benchmarks: Scannet, Scannet++, Replica, and S3DIS. Our pipeline not only performs better or on-par with the state-of-the-art, but we also achieve these results efficiently across runtime and compute requirements. Code will be published.

---


### 275. [Diving Deeper into Dense Keypoint Localization in Object Pose Estimation](https://arxiv.org/abs/2611.32728)

**<font color=#1a73e8>作者：</font>** Jiahong Chen, Jinghao Wang, Yueneng Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 6D pose estimation of rigid objects is a fundamental and challenging task in computer vision. Recent dense semantic keypoint-based methods employ binary encoding for efficient global keypoint localization, delivering strong performance in object pose estimation. Nevertheless, the discontinuous nature of binary encoding hinders effective training at high resolutions, while its inherent discrete and quantization errors lead to significant localization uncertainty. We propose GHLAPose, a global-to-local framework that synergizes hybrid Gray-binary (HGB) encoding with local-aware refinement (LAR). Specifically, HGB encoding first alleviates discontinuity to achieve accurate initial global keypoint localization. To further address intrinsic encoding errors, the LAR module estimates uncertainty and refines keypoint localization. This synergy enables a precise global-to-local strategy by aggregating global and local features. Extensive experiments on LM, LM-O, YCB-V, and TUD-L datasets demonstrate that GHLAPose surpasses state-of-the-art methods, particularly on fine-grained metrics. On LM-O, it outperforms the second-best method by 1.4% and 1.9% on ADD(-S) 0.02d and 0.05d respectively, and on YCB-V by 1% on ADD(-S) 0.1d. The code will be available at GHLAPose.

---


### 276. [AnyPrune: Optimization-Free Pruning for Any Feedforward 3D Gaussian Splatting Pipeline](https://arxiv.org/abs/2611.32735)

**<font color=#1a73e8>作者：</font>** Nicola Leonetti, Federico Stella, Aoxiang Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feedforward 3D Gaussian Splatting (3DGS) pipelines reconstruct a scene from images in a single forward pass, representing it as real-time-renderable 3D Gaussians. However, the resulting representations contain far more Gaussians than are needed to render the scene faithfully, especially when there are many input views. This drastically increases memory and storage requirements. Existing pruning methods either require costly re-optimization, which defeats the purpose of a single forward pass, or rely on simple strategies that do not exploit all the available information. We present AnyPrune, a transformer-based, optimization-free pruning module designed to work on top of any feedforward 3DGS pipeline. To remove unnecessary Gaussians, AnyPrune learns and exploits pipeline-specific redundancy patterns through a short single-GPU training on the frozen target feedforward pipeline. AnyPrune achieves better rendering quality than existing optimization-free pruning methods in most settings and generalizes to unseen datasets, as shown through extensive experiments across multiple feedforward pipelines, datasets, and input view counts. It prunes a 1.6M-Gaussian field in about $5\,\mathrm{s}$ on a consumer GPU, faster than every method that merges Gaussians or re-optimizes the field. It can also be combined with the pruning built into feedforward pipelines, pruning further at moderate ratios while preserving or improving rendering quality. Finally, it can even suggest a scene-specific pruning ratio that retains most of the quality.

---


### 277. [A Morphological Approach to Inverse Lithography](https://arxiv.org/abs/2611.32742)

**<font color=#1a73e8>作者：</font>** Gijs Bellaard, Bart M.N. Smets, Tim van der Leek 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lithography is a critical step in the manufacturing of chips that works by projecting light through a patterned mask and subsequently focusing it onto a photosensitive layer on top of a wafer. The task of finding a mask that prints a desired pattern on the wafer is called inverse lithography technology (ILT). The design of the mask is complicated by the fact that it must satisfy a set of constraints in order to be manufacturable. In this paper we provide a mathematical characterization of these constraints. Next, we develop a scoring function that allows us to measure whether a given mask satisfies the manufacturing constraints and if not, how badly the constraints are violated. Since our scoring function is (sub-)differentiable it can be used as the regularizer in a gradient-based inverse problem solver. We show that the resulting MorphILT algorithm that we developed can generate manufacturable masks that have nearly the same print quality as the (unmanufacturable) masks obtained from unconstrained inverse lithography.

---


### 278. [MemAnchorWorld: A Sparse World Model with Horizon-Conditioned Memory Retrieval for Autonomous Driving](https://arxiv.org/abs/2611.32745)

**<font color=#1a73e8>作者：</font>** Xinyang Jia, Yuqi Zhang, Jiakai Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse world models for 4D semantic occupancy forecasting represent scenes with a small set of evolving queries to efficiently predict future geometry and semantics for autonomous driving. However, existing sparse world models face a bottleneck in using historical temporal evidence for long-horizon forecasting. They rely on scene states to carry historical information implicitly, allowing errors to propagate and accumulate across successive forecasting steps and causing geometric and semantic deviations. To address this limitation, we present MemAnchorWorld, a sparse occupancy world model that explicitly retrieves relevant historical geometric and semantic evidence for 4D semantic occupancy forecasting. Inspired by the von Restorff effect, we introduce a forecast-time-conditioned hierarchical dual-path memory-anchor retrieval mechanism. Guided by the effective age and semantic compatibility of historical information, it combines query-level candidate selection with point-level memory-anchor retrieval to provide historical evidence for sparse points at different forecast times. To better use memory anchors and existing features, a point-level residual adapter jointly gated by the task and forecast time separately controls residual corrections to semantics, occupancy confidence, and spatial positions. On Occ3D-nuScenes, MemAnchorWorld achieves an average mIoU of 13.55% and an average IoU of 22.84% across the 1-3 s forecasting horizons, attaining state-of-the-art performance on both this http URL page: this https URL

---


### 279. [SGD with Large Learning Rates: General Analysis & Improved Rates](https://arxiv.org/abs/2611.32762)

**<font color=#1a73e8>作者：</font>** Konstantinos Emmanouilidis, Ziqing Xu, Salma Tarmoun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stochastic Gradient Descent lies at the core of modern machine learning. However its classical analysis typically restricts the stepsize to be below a curvature-dependent stability threshold. Recent developments in deterministic optimization have challenged this paradigm, showing that suitably chosen large stepsizes can not only preserve convergence, but also accelerate Gradient Descent (GD). Whether this phenomenon persists in the presence of stochastic gradient noise has remained an open question (Wu et al., 2024). In this work, we answer this question affirmatively for the cross-entropy loss with linear predictors and two-layer neural networks, establishing an accelerated $\mathcal{O}(T^{-2})$ convergence rate. At the core of our analysis is a fine-grained characterization of the stochastic large-stepsize dynamics. This sharper control of the trajectory further yields tight convergence guarantees within the stable regime, improving existing bounds even in the deterministic setting. Taken together, our results show that the acceleration mechanism induced by large stepsizes survives stochasticity and extends beyond linear models. Numerical experiments demonstrate the benefits of large learning rates in practice.

---


### 280. [EviCraft: Can Minecraft Agents Find What They Cannot See?](https://arxiv.org/abs/2611.32765)

**<font color=#1a73e8>作者：</font>** Wenyou Yi, Lantian Zhang, Guanlin Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In Minecraft, a common testbed for embodied agents, semantic tools such as mineBlock pick targets from the simulator's loaded world state without a visibility test, so a buried ore the agent has never seen is one call away, and scores cannot show whether the agent searched. We formalize the missing requirement as evidence closure: every decision of an agent system, including those inside its tools, may depend on the world only through facts for which the agent holds evidence. EviCraft is a runtime and benchmark that enforces closure below the agent and makes the admission rule an experimental variable: a perception-grounded regime (G) admits only what is in line of sight or returned by the agent's own actions, and a loaded-state regime (L) reproduces standard tool stacks, with agents, tools, and worlds held fixed. On Survival, the regime effect exceeds the strongest agent's lead: under G, three mid-sized agents reach the diamond in 32%-40% of runs, against 76%-94% under L, and the strongest agent under G scores below each of them under L. In two models, removing only the line-of-sight test closes 93%-96% of the score gap, and loading state only inside tools recovers 70%-98%, so safeguards on observations and queries leave most of the leak open. In open-ended acquisition, the gain from L concentrates in items that depend on buried resources or mobs. Code and benchmark are available at this https URL

---


### 281. [RubikSQL-HB: Agentic Text-to-SQL with Knowledge in the Loop](https://arxiv.org/abs/2611.32772)

**<font color=#1a73e8>作者：</font>** Haorui Jia, Zihan Qu, Yundi Dong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Database agents need more than schema structure: business meanings, stored values and reference queries supply knowledge that becomes relevant at different points in reasoning. We introduce RubikSQL-HB, which exposes these materials through queryable, database-specific knowledge workspaces built on the HeavenBase platform. Its knowledge interface remains available as an agent constructs and investigates an answer. Candidate agents interleave knowledge access with SQL construction and execution; a downstream Judge can reuse the same interfaces to investigate disagreements. A two-stage example interface separates discovering a reference question from expanding its SQL. On a 500-question BIRD Mini-Dev evaluation, the full pipeline reaches 75.2% execution accuracy, against 71.2% for first-candidate selection and 70.4% for execution-majority voting, with a correct candidate available on 79.0% of questions. The raw-knowledge condition, which also regenerates candidates without the built workspace, is 3.0 points lower, and adjudication with tools and revision accounts for most of the gain over selection baselines. A recorded execution probe shows how continued investigation resolves a candidate disagreement. Separate archived runs show semantic revision recovering answers absent from their original candidate pools. A versioned development study further illustrates how recurring corrections become reusable execution checks. The system and results connect knowledge-interface design to agent decision quality: queryable knowledge supports the construction of useful alternatives, and evidence-aware adjudication connects those alternatives to a final answer. Keeping knowledge in the loop lets agents acquire relevant observations as their reasoning develops.

---


### 282. [Learning World Models through Contrastive Identification of Actions](https://arxiv.org/abs/2611.32776)

**<font color=#1a73e8>作者：</font>** Hayeong Lee, Youngjun Suh. Byung-Jun Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Latent world models enable goal-directed planning from offline visual data, but prediction alone does not specify which action-related distinctions their representations should preserve. Inverse dynamics provides auxiliary supervision, yet squared-error action regression rewards additional information only through changes in the conditional action mean. We propose Contrastive Identification of Actions (CIA), which identifies the executed action among alternatives sampled from a history-conditioned behavior proposal. Comparing actions plausible in the same context targets information supplied by the next latent beyond history. Under exact behavior matching, we show that CIA can reward action information that leaves optimal inverse-regression error unchanged, and verify this distinction through a controlled learning example. CIA achieves higher planner-averaged mean success than the base world model and a regression inverse-dynamics baseline across five visual control benchmarks, without modifying the planner.

---


### 283. [Beyond Static Semantics: Instance-Adaptive Vision-Language Alignment for Building Damage Assessment](https://arxiv.org/abs/2611.32777)

**<font color=#1a73e8>作者：</font>** Hang Yin, Jiepan Li, Hongruixuan Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instance-level building damage assessment (IBDA) from bi-temporal remote sensing imagery remains challenging, as the same damage grade may exhibit diverse visual manifestations across individual buildings. Natural language offers explicit descriptions of physical damage, providing complementary semantic cues beyond discrete category labels. However, existing vision--language approaches have not fully addressed how damage semantics should adapt to local bi-temporal evidence and subsequently serve as instance-specific references for severity discrimination. To bridge this gap, we propose LAMIA-IBDA, a unified vision--language framework that progressively grounds shared damage semantics in local observations and individual buildings. Specifically, Adaptive Text-Visual Alignment (ATVA) enables evidence-adaptive semantic interaction by jointly contextualizing multiple damage descriptions and bi-temporal visual features under reliability-aware attention supervision. Dynamic Instance-Prototype Grounding (DIPG) further associates these contextualized semantics with individual building regions to construct instance-adaptive prototypes for fine-grained damage classification. Instance-level description preferences additionally supervise fusion-stage attention, linking semantic adaptation with instance discrimination. Extensive experiments on xBD and BRIGHT demonstrate state-of-the-art performance across optical--optical and optical--SAR settings. The source code is publicly available this https URL.

---


### 284. [Accuracy of Noise Ceiling Estimators for Brain Scores](https://arxiv.org/abs/2611.32792)

**<font color=#1a73e8>作者：</font>** Aude Maier, Lucas Gruaz, Martin Schrimpf 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The internal activations of modern machine learning models align surprisingly well with the activities recorded in real brains. In the last five years, the alignment between encoding models and brain activities, often called brain scores, has steadily increased. Because brain recordings are noisy, there exists an upper bound to the brain scores that any model can achieve. This bound, called the noise ceiling, is crucial for two reasons: it determines whether further improvements in model performance are possible, and it enables meaningful comparisons of brain scores across benchmarks. The field has developed multiple approaches to estimate noise ceilings, but the statistical properties of existing estimators remain poorly understood, leaving it unclear in which experimental settings they provide reliable estimates. Here, we introduce a unified mathematical framework for brain recordings, use it to derive closed-form expressions for four commonly used noise ceiling estimators, and provide theoretical predictions for the behavior of each estimator. We validate the theoretical predictions with simulations that we compare to noise ceiling estimates in existing fMRI and EEG datasets. We find that the existing methods underestimate the true noise ceiling in different settings. We conclude with recommendations for best practice in different situations.

---


### 285. [Back to Raw Motion: Latent-Free Diffusion Transformers for Text-to-Motion and Exact Conditional Generation](https://arxiv.org/abs/2611.32793)

**<font color=#1a73e8>作者：</font>** Yun Chen, Jeonghyeok Do, Munchurl Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As generative models tackle larger and more complex datasets, learned codecs enable efficient generation through compact latent representations, but may lose details and cannot guarantee exact preservation of given conditions. Generating directly in the original data space avoids errors introduced by the codec. Recent advances in image generation demonstrate that pixel diffusion can produce high-quality samples at practical computational costs. Inspired by these advances, we conduct a preliminary study of pixel diffusion, demonstrating its potential for adaptation to motion generation. Building on these findings, we present RawMo, a framework that brings text-to-motion generation to raw motion space. Our Motion Diffusion Transformer (MiT) models local skeletal structures and whole-body dynamics, while refining motion across frames to improve temporal consistency. Working directly in raw motion space further allows our high-noise text-motion alignment loss (HiNCE) to improve text consistency without intermediate motion decoding. RawMo supports multiple motion-conditioning tasks with a single conditional model while preserving given motion conditions exactly. Experiments on HumanML3D and KIT-ML show the best text alignment among compared methods and competitive motion quality, with ablations confirming the benefits of MiT and HiNCE.

---


### 286. [Breaking the Joint Action Space Dependence in Distributionally Robust Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2611.32812)

**<font color=#1a73e8>作者：</font>** Yue Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the sample complexity of learning robust coarse correlated equilibria (CCE) in finite-horizon, general-sum, distributionally robust Markov games with known rewards and a generative model of the nominal transitions. Each player evaluates a policy by its worst-case return over total-variation (TV) balls centered at the nominal transition distribution of every stage, state, and joint action; this is the standard $(s,a)$-rectangular uncertainty set. Existing generative-model guarantees for this model scale with the number $\prod_iA_i$ of joint actions, where $A_i$ is the number of actions of player~$i$. Since this number grows exponentially with the number of players, these guarantees suffer from the curse of multiagency. We design an algorithm whose sample complexity depends on the action sets only through the largest individual action-set size $A_*:=\max_iA_i$. The algorithm uses $\widetilde O(SA_*H^5D^4/\varepsilon^4)$ transition samples and, with probability at least $1-\delta$, returns a Markov policy that is an $\varepsilon$-robust CCE from every initial state. Here $S$ is the number of states, $H$ is the horizon, and $D:=\max_i\min\{H,1/\rho_i\}$, where $\rho_i$ is the TV radius of player~$i$. Two ingredients make this possible: a plug-in estimate of the robust backup whose mean error does not depend on the number of states, and a single batch of samples per round that serves as bandit feedback for all players at once. The result shows that the dependence on $\prod_iA_i$ can be avoided without modifying the $(s,a)$-rectangular uncertainty set.

---


### 287. [E(n)-Equivariant Spherical Decision Surfaces](https://arxiv.org/abs/2611.32815)

**<font color=#1a73e8>作者：</font>** Pavlo Melnyk, Michael Felsberg, Kostas Daniilidis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a constructive derivation of exactly E(n)-equivariant spherical decision surfaces by extending prior O(n)-equivariant hypersphere neurons to include translations. To achieve this, we present a decomposition of the features of the O(n)-equivariant neurons and provide explicit representations for translation and E(n)-transformations to fulfil the respective equivariance constraints. The resulting decision surfaces are exactly E(n)-equivariant without input centring or explicit pairwise differences, and admit explicit closed-form matrix representations. In addition, we numerically verify the correctness of the derivations and perform a downstream check of the resulting geometric primitives.

---


### 288. [Reliable and grounded reporting of any computed tomography scan with FORA](https://arxiv.org/abs/2611.32823)

**<font color=#1a73e8>作者：</font>** Sezgin Er, Utku Turkbey, Alperen Gur 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence systems for computed tomography (CT) remain largely restricted to specific anatomical regions, examination types or predefined abnormalities, limiting their ability to provide comprehensive and spatially grounded interpretations. Here we present FORA, a general-purpose CT model that recognizes and spatially localizes 1,028 hierarchically organized radiological concepts and generates reports across the 28 CT protocols represented in our cohort. Trained on 304,962 routine CT examinations supervised by their accompanying reports, FORA learns to localize abnormalities without manually annotated lesions. Its architecture combines multiple-instance learning with an interpretable concept bottleneck that connects spatial evidence, radiological findings and report generation. We first developed and benchmarked the architecture on chest radiographs, achieving state-of-the-art performance, before training a separate model on three-dimensional CT examinations. On 36,619 held-out CT examinations, FORA achieved a macro area under the receiver operating characteristic curve (AUROC) of 0.918 for radiological concept recognition, exceeding the strongest of 18 existing CT models by 0.21. FORA also ranked first on three public benchmarks, outperforming Merlin on its own test set without training on that institution's data (AUROC 0.907 versus 0.826). On independent localization benchmarks for pulmonary emboli, renal masses and rib fractures, FORA's strongest spatial evidence fell within annotated lesions at rates up to 348 times greater than chance. FORA achieved more than threefold higher macro-averaged finding recall than the strongest existing report generator. These results show that a single model can combine broad abnormality recognition, spatial localization and report generation across 12 CT examination types, using routine reports without lesion-level supervision.

---


### 289. [EEG-World: Context-Conditioned Dynamics of the Watching Brain](https://arxiv.org/abs/2611.32825)

**<font color=#1a73e8>作者：</font>** Junxiang Zhang, Jiayu Zuo, Wenhao Ye 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Brain encoding models predict neural responses from audiovisual input, but typically overlook how ongoing brain activity shapes an individual's response. We introduce EEG-World, a recurrent world model that forecasts 10 seconds of EEG band-power dynamics from 6 seconds of preceding EEG and the subsequent audiovisual stimulus. Pretrained on continuous EEG, EEG-World learns shared neural dynamics and adapts to unseen individuals through lightweight subject-specific readouts. Using 2,584 hours of EEG from 78 participants, we show that nonlinear recurrent forecasting surpasses strong history-aware linear baselines at scale. EEG-World achieves a forecasting correlation of 0.261 versus 0.233 for the strongest history-and-video linear model, with a 3.3-second forecasting-horizon advantage. Its learned dynamics transfer to unseen participants, outperforming the linear baseline in 23 of 24 individuals after calibration. While ongoing EEG history accounts for most predictive performance, controlled stimulus analyses reveal an additional video-dependent component. This component also enables evaluation of visual representations, with V-JEPA 2 improving clip-locked prediction by 35% over combined CLIP and DINOv2 features. Our results demonstrate the value of transferable neural dynamics for individual EEG forecasting and highlight the importance of separating state-driven from stimulus-driven predictability.

---


### 290. [Aqua2CAD : Observation-Guided Point Cloud Correction and Completion for CAD Reconstruction from Underwater Stereo Images](https://arxiv.org/abs/2611.32835)

**<font color=#1a73e8>作者：</font>** Weizhao Huang, Jiayi Zhang, Pangkit Fong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering editable computer-aided design (CAD) models from underwater stereo images requires accurate and complete geometry, yet stereo reconstruction produces displaced points and missing regions. The original views retain cross-view disagreement and ray evidence lost during point-cloud fusion. Aqua2CAD exploits this evidence in two stages: view-conditioned correction and quality filtering establish reliable geometric support, while multi-view observations condition a learned shape prior to infer missing surfaces in the original metric frame. The recovered points support surface fitting and solid assembly with manually revised face groups. On an OceanSim-based synthetic benchmark, Aqua2CAD reduces point-cloud Chamfer distance by 60% relative to the stereo reconstruction. Compared with a matched point-only completion backbone, it improves missing-region recovery at 5,mm from 16.27% to 24.16%. With a shared CAD backend, exterior acceptance increases from 6/19 to 14/19. Qualitative results on selected real underwater captures demonstrate recovery of the main structures of six 3D-printed objects.

---


### 291. [DOPER: Deep Object Pose Estimation Revisited](https://arxiv.org/abs/2611.32846)

**<font color=#1a73e8>作者：</font>** Hugo Hadfield, Alperen Degirmenci, Jonathan Tremblay  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present DOPER, an RGB pose estimation framework that shares a visual backbone across object detection, segmentation, and keypoint prediction to recover the 6D pose of known objects through Perspective-n-Point. Starting from synthetic training, DOPER adapts to real observations using partial supervision while retaining synthetic keypoint labels. Calibrated multi-view observations provide geometric constraints for keypoint supervision. During inference, optional heatmap refinement fits a rigid pose directly to the predicted keypoint distributions, resolving ambiguous correspondences without depth input or a learned pose refiner. Starting from underspecified CAD models, DOPER progressively refines the object representation and pose estimator. Results on SPEED+ and SHIRT further demonstrate effective adaptation to illumination changes and accurate temporal pose estimation. Across the evaluated single-view and multi-view configurations, DOPER achieves state-of-the-art detection AP results on HANDAL, HOPEv2, HOT3D, and T-LESS while using only RGB and running in real time (35 Hz per object model on one GB300). These results demonstrate the effectiveness of jointly learning detection and pose keypoints, with real observations and geometric constraints.

---


### 292. [Tabra Blends: Improving the Accuracy--Latency Trade-off with Complementary Tabular Models](https://arxiv.org/abs/2611.32859)

**<font color=#1a73e8>作者：</font>** Jing Jia, Guanyang Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models make different trade-offs between prediction accuracy and latency. We study whether a compact ensemble can deliver higher accuracy in less time. Across 816 TabArena splits, our blend of four-estimator Kumo and one LimiX pipeline reaches 2063.8 Elo, 45.4 points above the top published entry in the same fit. Its normalized fit + predict time is 15% lower than Kumo-16's and 98% lower than full LimiX's. We find that greater prediction diversity between the two models helps explain the reduction in error.

---


### 293. [CityRecast: Suppressing Persistent Artifacts in Generative Satellite 3D Reconstruction](https://arxiv.org/abs/2611.32863)

**<font color=#1a73e8>作者：</font>** Shuo Cui, Yingyan Hou, Wanxuan Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Satellite-based 3D reconstruction is limited by sparse observations and changes across acquisition dates. Existing methods use generative priors to recover missing visual detail, but ghosting, streaking, and blur persist in their Gaussian scenes. These artifacts become particularly apparent in low-elevation renderings. We introduce CityRecast to suppress these artifacts through Gaussian scene repair and supervision calibration. To correct the Gaussian distributions that produce these artifacts, we first use multi-angle warm-up to constrain their spatial extent. This reduces the initial ghosting carried into progressive refinement. Surface-guided replacement then continues to repair the Gaussian distribution while preserving existing appearance. To provide more reliable supervision for this process, observation calibration mitigates interference from multi-temporal observations. Joint refinement further reduces conflicts among generated views. Experiments on DFC2019 and IARPA demonstrate reduced artifacts in low-elevation renderings while maintaining satellite-view fidelity. Compared with Skyfall-GS, CityRecast reduces FID-CLIP by 25.3% on DFC2019 and 51.8% on IARPA. MUSIQ increases by 14.54 and 24.95 points, respectively.

---


### 294. [MemHand: Memory-Enhanced World-Space Hand Motion Reconstruction from Egocentric Videos](https://arxiv.org/abs/2611.32876)

**<font color=#1a73e8>作者：</font>** Junyi Ma, Zhangshuo Qi, Erhang Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering the continuous world-space motion of both hands from egocentric video is essential for applications such as human-to-robot policy transfer and augmented reality. Achieving this goes beyond reconstructing the hands from each individual frame, as the context that a frame needs is often spread over time, especially around occlusions or when a hand moves out of sight. Recent works have explored how to exploit temporal context, yet they mostly draw it from fixed-length windows. Such windows cannot guarantee that every frame has the context required to reconstruct the hands in world space with accurate poses and metric scale. To address this limitation, we introduce MemHand, a memory-enhanced framework for world-space hand motion reconstruction. MemHand maintains two complementary forms of memory. The Short-Term Event Memory keeps the context of the well-observed hand around each occlusion or out-of-sight event and supplies it to frames with weak or missing visual evidence. In addition, since the metric scale holds over the whole recording, the Long-Term Scale Memory retains the most reliable observations across the video as scale anchors within a bounded state. Across benchmarks featuring severe occlusions and frequent out-of-sight intervals, MemHand achieves state-of-the-art accuracy and generalizes well to unseen domains. Benefiting from the synergy of both memories, it cuts W-MPJPE by 57\% on ARCTIC and 70\% on HOT3D relative to StableHand, delivering continuous and metrically accurate world-space hand poses and trajectories. We will release our code and models at the project page: this https URL

---


### 295. [Simultaneously Boosting Efficiency and Capability for Linear Attention via Adaptive Channel Compression and Activation Purification](https://arxiv.org/abs/2611.32877)

**<font color=#1a73e8>作者：</font>** Senqi Guan, Xianchao Zhang, Moyan Tian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-attention's quadratic complexity constitutes a core bottleneck for Vision Transformers (ViTs). Existing efficiency-oriented optimizations, including softmax-based and linear attention (LA) variants, generally compromise model representational capacity, leading to inevitable performance degradation. We propose a novel linear attention which alleviates this efficiency-capability dilemma. For the first time, we embed an Adaptive Channel Compression and Activation Purification (ACCAP) mechanism into the QKV projection of linear attention, which enables the model to retain high-dimensional feature information while performing computations with reduced channels. We further fuse a focused kernel function and a self-gating module into ACCAP to construct a lightweight linear attention module (ACCAP-LA). Our theoretical analysis shows that, compared to standard linear attention, ACCAP-LA reduces the attention module's parameter count by 79.17% and FLOPs by 77.5%. Extensive experiments demonstrate ACCAP-LA's effectiveness: when applied to ViT, it achieves 79.4% Top-1 accuracy on ImageNet-1K with only 5.8M parameters, and more notably, it boasts strong cross-architecture compatibility, boosting EfficientViT-b1 and PVT-T by 3.3% and 3.4% respectively.

---


### 296. [3D Tracking Any Point with Events and Frames](https://arxiv.org/abs/2611.32883)

**<font color=#1a73e8>作者：</font>** Roberto Pellerito, Zijia Dai, Laurent Kneip 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tracking a fast-moving point in 3D is prohibitive when RGB frames are blurred or too far apart to reveal its motion. Event cameras record brightness changes between frames, providing measurements inside these temporal gaps. We introduce TrackAnyMotion, which combines monocular RGB frames and events to track arbitrary points in 2D and 3D, including at times when no RGB frame is available. The motion expected for a static point, given scene geometry and camera motion, provides a reference for identifying independently moving objects. An independent-motion decoder combines geometric motion cues with event guidance and 2D tracks, feeding its predictions back into iterative 2D and 3D refinement. We also introduce HyperEvent, a synthetic RGB--Event dataset with high-frequency 3D trajectories, geometry, and independent-motion labels. At RGB frame timestamps on this benchmark, TrackAnyMotion reduces 3D and 2D endpoint errors by 70\% and 32\%, respectively.

---


### 297. [Biomechanically Grounded Prediction of Selective Motor Control and Clinical Outcomes from Infant Video](https://arxiv.org/abs/2611.32890)

**<font color=#1a73e8>作者：</font>** Divya Joshi, Ruize Yang, Colleen Peyton 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Early identification of cerebral palsy (CP) relies on observational assessments of spontaneous infant movement, such as the General Movement Assessment (GMA) and the Baby Observational Selective Control AppRaisal (BabyOSCAR), which require trained raters and substantial scoring time. Existing automated approaches derive hand-engineered features from two-dimensional keypoints, which describe image-plane motion rather than the three-dimensional behavior of individual joints. We present Baby Biomechanical 3D Body (BB3D), an infant-adapted, biomechanical pipeline that estimates joint-angle trajectories from single-camera video. Against a multi-view markerless motion capture reference in 17 infants, BB3D's median Procrustes-aligned error was 17.5~mm for joint centers and 20.4~mm for marker sites. A spatio-temporal transformer, pretrained on BB3D joint-angle trajectories from 1k+ single-camera recordings, and fine-tuned on 550 videos from 350 infants, predicted each individual BabyOSCAR item with a mean within-site AUC of 0.79 and the BabyOSCAR total with a Spearman correlation of 0.86 on held-out recordings. Without being trained on diagnosis, the predicted total separated infants with CP from those without CP with an AUC of 0.86, exceeding a replicated two-dimensional feature classifier (0.67) but below the expert clinician rater's total (0.97). Predicted scores also carried information about functional ability and body distribution, though less than expert clinician scores. These results show that biomechanically grounded representations of monocular video can support scalable, joint-level assessment of selective motor control in infancy

---


### 298. [Shared information governs multi-view planted matching](https://arxiv.org/abs/2611.32892)

**<font color=#1a73e8>作者：</font>** Ruiqi Wang, Jingtong Hu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study when the rows of $K$ shuffled views of the same $n$ objects can be matched, where each object is observed once in every view through a Gaussian feature vector with known covariance. For every fixed $K$, all views can be matched up to $o(n)$ errors if the shared information $J$ of one object's $K$ observations exceeds $(1+\epsilon)\log n$, and not if it is below $(1-\epsilon)\log n$; this can hold although no two views can be matched on their own. Below the threshold, two views can still be matched if some set of views containing both has shared information above $\log n$; otherwise every estimator, even one that reads all views, has vanishing overlap between them. Matching every row is governed by the weakest bipartition of the views: with weak correlations the threshold is $2\log n$ for the mutual information across it. For a weak common signal observed through independent noise, the two thresholds are $4/K$ and $4/(K-1)$ in units of $\sum_\ell\rho_\ell^2/\log n$, which answers a question of Wee, Yang, Fan and Mao. Beyond weak correlations the bipartition condition is not sufficient: rare subpopulations impose a Rényi condition for every partition into at least three blocks. We conjecture that the two conditions together characterize exact recovery for Gaussian laws, and prove this for three views with equal correlations and in several further cases, in part with computer assistance. With equal correlations, layered screening attains $4/K$ for $K=3,4$ in $O(Kn^2d)$ operations, and for general laws a recursive decoder attains $J$. The almost-exact thresholds extend to known product laws and to objects observed in random subsets of the views.

---


### 299. [DualSpec: Spectral Reconstruction with Optimized Stereo Cameras](https://arxiv.org/abs/2611.32896)

**<font color=#1a73e8>作者：</font>** Luca Cogo, Marco Buzzelli, Simone Bianco 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spectral imaging captures information that ordinary RGB sensors cannot, but dedicated spectral cameras can be expensive and bulky. Recovering dense spectra from RGB images offers an accessible alternative, but distinct spectra can produce the same camera response, generating an ambiguity that even more advanced recovery algorithms cannot always resolve. Therefore, increasing the spectral information captured at acquisition is essential. We propose DualSpec, a stereo acquisition framework that jointly optimizes two external optical filters and a reconstruction network. Each filter is placed in front of a standard RGB camera, and the two are designed to produce six responses that provide complementary information for the network. Experiments across reconstruction architectures and spectral ranges show that DualSpec reduces mean spectral angle error by 36-72% relative to a single RGB camera and by 11-29% relative to stereo pairs selected from commercial filters. Cross-dataset evaluations, including a new benchmark of spectral images captured from displaced viewpoints, show that the method generalizes and remains robust to viewpoint misalignment, while analyses of thin-film approximations support optical feasibility.

---


### 300. [Label leakage through file headers: geometry and batch confounds in public mammography datasets, and a pre-training acceptance gate](https://arxiv.org/abs/2611.32899)

**<font color=#1a73e8>作者：</font>** Achraf Toufah, Rana Saad, Moulay Youssef El Hafidi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A dataset whose diagnostic label can be recovered from non-diagnostic information yields high, reproducible and uninformative model performance. We applied pre-training controls that see only image geometry, global texture, a sub-collection identifier or one covariate to six public mammography datasets, against a stop threshold of AUC 0.60. In KAU-BCMD, geometry alone predicted the BI-RADS class at AUC 1.0000 in a local copy and at a mean of 0.979 in a public Kaggle archive; after resizing, texture alone gave 0.847. In CMMD, the sub-collection prefix predicted malignancy at 0.7753; the restricted sub-collection passed geometry (0.5000) and texture (0.5810) but failed an identifier-order control added post hoc (test AUC 0.9926). CBIS-DDSM exceeded the stop on geometry (pooled mean 0.654 over 20 splits), a verdict statistic chosen post hoc; its official mass and calcification splits did not. M-SYNTH, INbreast and a partial VinDr-Mammo copy passed the few controls run. We release the code and derived tables. There is no quantum component in the inference path.

---


> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-342](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
