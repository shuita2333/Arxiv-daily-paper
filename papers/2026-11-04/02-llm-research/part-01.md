# 🧠 大模型相关研究 | 2026年11月04日

> 本类共 **515** 篇论文：已确认 **481** 篇，待复核 **34** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

---

### 1. [Wide but Shallow: Coding Agents in Generative Art](https://arxiv.org/abs/2611.00001)

**<font color=#1a73e8>作者：</font>** Dominikus Baur  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper presents an autoethnographic study on the use of coding agents in code-based generative art. Over the course of the 31-day Genuary art challenge, the author examined and compared a manual approach with the use of coding agents in their practice. The growth in quality of coding agents enables their use to autonomously produce programming code. Generative art's bricolage quality of combining existing algorithms and a coding agent's ability to draw on extended training data leads to a difficulty collapse: nearly any well-known algorithm can be used directly. While this enables easier free-form experimentation and a wider variety of outputs, it comes at the cost of less depth. Overall, this points towards a slow progression in artists' roles from inventing algorithms to changing parameters of existing ones and a potential overall artistic surrender to the results from large-language models.

---


### 2. [Do the Numbers Match the Plot? Statistical-Visual Verification for Automated Exploratory Data Analysis](https://arxiv.org/abs/2611.00004)

**<font color=#1a73e8>作者：</font>** Zixun Fu, Jian Huang, Maojun Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Automated exploratory data analysis (EDA) systems can execute statistics correctly while producing misleading interpretations. For example, correlations may be driven by influential observations, and mean differences may arise from skewness, overlap, or sparse subgroups rather than broad distributional shifts. We present EDAgent, a sequential framework that performs targeted visual verification before report synthesis. For each finding, the system records the statistical result, generates a visualization request identifying relevant distributional features, creates the corresponding chart, and uses the observed pattern to retain, qualify, or reconsider the interpretation. We call this process statistical-visual verification. EDAgent includes VisPlan, an 8B-parameter model that converts visualization rationales into detailed chart plans. We evaluate 87 end-to-end reports on EDA-Bench using a six-dimension rubric and GPT-5.1 multimodal evaluation. Maximum-score proportions reached 87.4% for factuality and visual consistency, 93.1% for statistical-visual cross-validation, and 96.6% for analytical narrative. On 166 open-ended VisEval tasks, VisPlan improved the mean overall score from 4.55 (Qwen3-8B) to 4.62, with the largest gain in aesthetics. These descriptive results indicate that visual verification can make automated EDA reports more transparent about how statistical findings relate to underlying data structure.

---


### 3. ["I Wrote, I Paused, I Rewrote": A Mixed-Methods Study of Learner Perceptions of Process-Aware LLM Feedback](https://arxiv.org/abs/2611.00009)

**<font color=#1a73e8>作者：</font>** Samra Zafar, Shifa Yousaf  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly provide formative writing feedback, but most systems evaluate only the submitted text. Process-aware systems can additionally incorporate intermediate drafts and interaction records, yet access to these traces does not establish whether learners perceive the resulting feedback as useful, fair, or aligned with their own revision experience. We conducted a convergent mixed-method post-task evaluation with 43 undergraduate English-language learners. Participants completed a timed essay, received LLM-generated feedback based on the final essay, intermediate snapshots, and keystroke-derived records, and then answered six five-point Likert items and four open-ended questions.
Ratings were concentrated above the neutral midpoint across all six items. Between 74.4% and 95.3% of participants selected ratings of 4 or 5, and all six one-sided exact sign tests remained significant after Holm correction. Perceived correspondence between the revision analysis and the participant's reported thought process was positively associated with overall perceived usefulness, Spearman's $\rho_s=.327$, 95% bootstrap CI $[.009,.609]$, $p=.032$, $n=43$.
Qualitative responses were analysed through an LLM-assisted codebook development procedure followed by independent human coding of 14 binary codes. Participants frequently described the product feedback and revision rationale as accurate, while a smaller set reported misinterpretation of surface corrections, time constraints, or rhetorical intention. The findings distinguish perceived detection of revision activity from perceived interpretation of why revision occurred.

---


### 4. [Output-Aware Block Influence: Jacobian-Lens Weighting for Depth Pruning](https://arxiv.org/abs/2611.00015)

**<font color=#1a73e8>作者：</font>** Kyle Lemoi, Jonathan Yong, Shubhankar Tripathy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Depth pruning removes entire transformer blocks and therefore depends on a reliable criterion for identifying which blocks can be removed. Block Influence (BI) ranks blocks by how minimally they rotate the hidden state. However, local redundancy does not necessarily imply downstream irrelevance. We address this limitation using the Jacobian Lens (J-Lens) neural artifact, a map transporting perturbations at a layer to the final residual stream. At a common sparsity level, pruning scores applying J-Lens transportation to $BI$, what we call $J-BI$, were found to improve post-pruning accuracy by up to 19 points over $BI$ while reducing damage to perplexity for Qwen3-8B, Llama-3.1-8B-IT, and Gemma-3-12B-IT. We also perform a single-block ablation study and use J-Lens probing to explain why the proposed scores improved performance.

---


### 5. [Covariance-aware Scoring: A Geometric Correction for Vision-Language Test-Time Adaptation](https://arxiv.org/abs/2611.00024)

**<font color=#1a73e8>作者：</font>** Lakpa Tamang, Saman Forouzandeh, Kamal Berahmand 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) enables vision--language models such as CLIP to adapt to distribution shifts without labels or access to source data. Existing methods adapt through feature caching, prototype estimation, or the online accumulation of feature statistics, but most ultimately score a test feature against a class representative in the ambient embedding space, typically through cosine similarity. We identify this shared decision rule as a limitation under anisotropic feature distributions, which means when a small number of directions account for a large fraction of feature variance, the score can be dominated by high-variance directions that are not necessarily discriminative. In light of this, we propose CARe, a covariance-aware scoring for TTA that replaces the ambient geometry with a Mahalanobis geometry induced by the target feature second moment. Theoretically, we show that under a shared-covariance Gaussian model the covariance-aware decision direction coincides with that of the Bayes-optimal linear discriminant, with ambient-space scoring as the isotropic special case, and establish that the potential benefit of covariance-aware scoring grows with feature anisotropy. Empirically, we show that CARe improves adaptation accuracy over its base cosine scoring on both standard and fine-grained distribution-shift benchmarks across two backbones. Consistent with our analysis, the gains are largest on datasets whose features are most anisotropic and vanish as the features approach isotropy.

---


### 6. [The Margin Knows the Background: Uneven Abstention in Frozen Vision-Language Models](https://arxiv.org/abs/2611.00026)

**<font color=#1a73e8>作者：</font>** Satwik Sai Prakash Sahoo, Bibhor Puhan, Shubhankar Mahanta  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Selective prediction allows a model to abstain on uncertain inputs, but a single confidence threshold can disproportionately reject examples from particular groups. We study how confidence scores produce this imbalance in frozen vision-language models (OpenAI CLIP, LAION CLIP, SigLIP). We express a family of scores, including the margin and maximum logit, through the average and the difference of the two highest class logits, and ask which carries group information. We show that equal group coverage at every threshold is equivalent to independence between the score and group membership. A randomized margin baseline tests whether a reduction in coverage disparity beats what adding noise achieves. With score choices fixed before testing, the effect of choice depends on the dataset. On Waterbirds, the margin creates coverage gaps 2.5 to 5.5 times larger than maximum logit at 80% coverage, its group signal is in the difference component, and paired background swaps show the background moves it, although maximum logit increases overall error. On NICO++, maximum logit instead increases worst-context error by 5.4 to 6.6 points and offers no improvement over the randomized baseline for OpenAI CLIP. Across both datasets, how far a score pushes a group down its ranking tracks the coverage gap (Spearman 0.88, 0.92) better than plain group identifiability (0.61, 0.65). These results explain why a score that abstains more evenly on one dataset may be less effective on another and motivate judging group coverage and selective risk together against randomized baselines.

---


### 7. [A Systematic Analysis of Live Intraoperative Surgical Expert Narrations](https://arxiv.org/abs/2611.00028)

**<font color=#1a73e8>作者：</font>** Arda Mamur, Matthias Seibold, Christoph Laux 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Manual annotation remains the principal bottleneck in surgical video understanding. Live intraoperative narration by the operating surgeon is a scalable alternative that requires no manual annotation, but the information it contains has not been characterized. We analyzed 13 endoscopic lumbar spine decompression procedures (13.2 h) by two senior spine surgeons, using time-synchronized close-mic German audio. An annotation-free pipeline (word-level speech recognition, deterministic correction of surgical-term errors, utterance fusion, LLM-based translation to English, and relevance filtering) converted speech into time-stamped procedural cues labelled with the surgical entities they reference and their speech act. Of 3,171 utterances, 1,201 (37.9%) were retained as procedural cues, while 57.6% were non-procedural and removed. Retained cues referenced instruments (60.7%), anatomy (48.0%) and surgical actions (57.1%), and 98.5% carried at least one of these. 39% of cues (472 of 1,201) were directives, mainly instrument requests and commands. All 467 manually verified instrument requests preceded the instrument's appearance in the field, by a median of 8.2 s. Domain-term transcription corruption affected 18.0% of retained cues. Live narration is thus a dense, annotation-free supervisory signal describing instruments, anatomy, actions and team coordination, but it is noisy and temporally displaced from the events it names, and this displacement must be modelled before safe downstream use.

---


### 8. [From Single-Shot QA to Continuous Perception: Revisiting the Energy Composition and Optimization Boundary of Edge VLMs](https://arxiv.org/abs/2611.00036)

**<font color=#1a73e8>作者：</font>** Yiting Duan, Miaoxin Wang, Aoqing Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual-prefill energy conclusions for edge vision-language models (VLMs) are commonly drawn under single-shot workloads; we revisit them under continuous perception. Profiling nine VLMs across three architecture families on Jetson AGX Thor and Orin (4,508 records, calibrated with a pure-text task), we find two mutually independent energy laws: the per-output-token decode cost grows monotonically with model scale, whereas the visual-prefill (image-encoding) cost is dominated by visual-encoder architectural efficiency, not scale. Under continuous perception ($N{=}10$) with sparse output, visual-prefill energy reaches 92--97\% of total. We derive optimization strategies---visual frame reuse, adaptive output truncation, task-aware routing, and encoder throughput optimization---for edge VLM deployment.

---


### 9. [Think Before You Locate: Clinical Chain-of-Though Supervision for Sequential Medical Image Grounding](https://arxiv.org/abs/2611.00041)

**<font color=#1a73e8>作者：</font>** Adinath Madhavrao Dukre, Govinda Kolli, Yifan Lu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clinicians rarely localize a finding from one image alone. They compare current and prior scans, follow structures across slices, and match regions across views or modalities. Yet vision-language models for sequential medical grounding usually learn only from bounding boxes. Boxes show where the target is, but they do not explain why that region in that image answers the question. We study whether explicit, image-grounded reasoning can improve localization, and which tasks benefit from it. We introduce method, whose core is MedChain, a corpus of 182,573 filtered rationales spanning eight sequential grounding tasks and ten imaging modalities. A medical VLM (FlemingVL-38B) first drafts a caption-like rationale, and a multimodal refiner (Qwen3.5-397B-A17B) then re-examines the images, question and annotated box to write a box-conditioned explanation with explicit cross-image reasoning. We fine-tune Qwen3.5 on these rationales with deliberative chain-of-thought supervision (dCoT-SFT). Across 4B, 9B, and 27B models, dCoT-SFT sets a new state of the art on MedSG-Bench. The 27B model reaches 77.24 mIoU and 85.20 Acc@0.5, improving over the strongest prior model by 4.69 and 5.49 points. In a paired comparison using fixed 4B checkpoints, dCoT-SFT improves over answer-only SFT by 3.56 mIoU (95% CI 3.13--4.00). The gains mainly come from change detection and object tracking, while performance drops on three appearance-matching tasks. Replacing a model's own rationale with a rationale from another task reduces mIoU by 12.2 points, showing that localization depends strongly on the reasoning context. Finally, adding GRPO with an IoU reward after dCoT-SFT gives only small and task-dependent gains, which we analyze through controlled multi-seed development experiments.

---


### 10. [Keyframes First, Motion Second: Revisiting Compressed-Domain Video Captioning under Limited Supervision](https://arxiv.org/abs/2611.00048)

**<font color=#1a73e8>作者：</font>** Asok B K, Ashim Nepal, Loknath Regmi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compressed-domain video captioners such as CoCap read the H.264 bitstream directly: a pretrained encoder reads the keyframes (I-frames), while motion and residual encoders, trained from scratch, turn the codec's motion vectors and residuals into action tokens. This motion branch costs decoding time and supervision, both scarce on edge devices. We ask when it pays off under limited supervision. In a controlled study on 2,500 VATEX training clips, we fix a frozen SigLIP 2 keyframe encoder, a GPT-2 caption decoder and the training schedule, vary only the visual tokens the decoder receives (34 configurations), and report held-out test CIDEr with paired bootstrap intervals and three seeds. Motion encoders trained from scratch bring no measurable benefit: CoCap-style action tokens change CIDEr by -0.55 (95% CI [-2.3, +1.2]), and six other uses of motion do not help. Warm-started from a model trained on 48x the caption samples, they add +1.3 CIDEr on average, though not significantly across seeds, and only while the keyframe tokens stay frozen. Reading the keyframes better matters more: fine-tuning SigLIP 2's own attention-pooling head adds 5.4 CIDEr, and one to eight such tokens beat the 16 CoCap-style tokens on every seed while decoding only I-frames (7.3 ms instead of 44-114 ms per clip). The same holds on MSVD's full split in CoCap's own video encoding, where the readout leads by 14.2 CIDEr and action tokens bring no reliable gain, also with clean single-reference motion vectors. Under limited supervision, keyframes come first and motion second.

---


### 11. [ReactionBench: A Human-Anchored Benchmark for Modeling Reactions to Video](https://arxiv.org/abs/2611.00050)

**<font color=#1a73e8>作者：</font>** Yibo Zhao, Ao Qu, Xuan Jiang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding what happens in a video is not sufficient for socially responsive multimodal systems: such systems also aim to relate what a person observes to how that person responds. Existing video benchmarks largely evaluate events, temporal reasoning, or people depicted in the video, while affective and viewer-response datasets often focus on emotion labels, aggregate responses, or prediction from the stimulus alone. This leaves an underexplored question: can current multimodal models ground an observed viewer reaction in the stimulus context associated with it? We introduce ReactionBench, a human-anchored benchmark for reaction-specific video understanding. Built from a candidate pool of 31,834 synchronized stimulus-reaction clips spanning 433 hours and eight domains, ReactionBench evaluates three complementary abilities: ranking the intensity of a viewer's reactions within a video, matching a reaction to its temporally aligned stimulus, and explaining the concrete stimulus cues linked to that reaction. Human annotation provides 14,894 ratings over 3,257 moments, and the frozen evaluation comprises 250 intensity profiles, 112 matching items, and 200 rationale items with 447 blind-written human references. Across seven multimodal models, reaction-specific grounding remains challenging: the best model reaches 50.9% accuracy on four-way stimulus-reaction matching, while GPT-5 shows no detectable loss under reaction substitution. Performance is also sensitive to evaluation protocol. Project page: this https URL

---


### 12. [SIMIT: Self-Improving Vision-Language Models via Imagination at Test-Time](https://arxiv.org/abs/2611.00053)

**<font color=#1a73e8>作者：</font>** Mehmet Onurcan Kaya, Desmond Elliott, Dim P. Papadopoulos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce SIMIT, a test-time self-improvement framework in which a vision-language model creates its own query-specific training data before answering an unlabeled test query. Our goal is to improve performance on a given target test set without annotations or external models. To pursue this goal, some test-time methods improve answers through longer reasoning or repeated sampling but leave the model unchanged. Others update the model using rewards based on majority agreement among multiple candidate answers or the model's own judgments of correctness, but such rewards can reinforce existing mistakes. SIMIT instead imagines similar problems whose solutions it controls: a model need not correctly solve the target query to construct useful practice examples. It synthesizes diverse (question, answer, image) triplets by specifying each answer before realizing its image. To support diverse multimodal tasks, SIMIT combines native image generation with an extensible skill library for structured visuals, including documents, charts, and diagrams. Within this pipeline, multi-stage verification checks that images support their assigned answers, while difficulty filtering retains informative examples. Adaptive budgeting further targets this practice by allocating more samples to queries the model is less confident in answering. The resulting data can improve the model in-context (SIMIT-ICL) or in-weight (SIMIT-FT). Across 17 diverse benchmarks, SIMIT outperforms existing self-improvement methods. Its best configuration achieves a +7.20% mean relative gain over BAGEL-7B, while training-free SIMIT-ICL achieves +6.98%.

---


### 13. [CausalPrune: Counterfactual Causal Token Pruning for Efficient Large Vision-Language Models](https://arxiv.org/abs/2611.00058)

**<font color=#1a73e8>作者：</font>** Pengcheng Zheng, Chaoning Zhang, Ya Wen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) have achieved remarkable progress in multimodal understanding, but their practical deployment is still limited by the substantial computation introduced by excessive visual tokens. Visual token pruning offers an effective solution by removing redundant visual tokens during inference. However, existing methods typically estimate token importance from correlational statistics, which cannot distinguish tokens that causally determine the model output from those spuriously associated with it. To address this issue, we propose \textbf{CausalPrune}, a counterfactual causal token pruning framework for efficient LVLMs. We formulate LVLM inference as a Structural Causal Model and introduce the Causal Token Importance Score (CTIS), which estimates the Average Treatment Effect of intervening on each visual token. To make causal estimation practical, we derive an efficient first-order approximation of CTIS and incorporate backdoor adjustment to mitigate latent cross-modal confounding. Within this causal formulation, layer-wise causal mediation decomposes token importance into direct and indirect effects through intermediate hidden states, enabling progressive pruning across transformer layers in a principled manner. Extensive experiments on various LVLM architectures, such as LLaVA-1.5 and Qwen2.5-VL, demonstrate that CausalPrune maintains comparable or even superior multimodal performance while achieving substantial reductions in FLOPs and prefill latency, consistently outperforming existing pruning methods.

---


### 14. [BreastXAgent: A lightweight agentic explainability framework for breast density classification](https://arxiv.org/abs/2611.00065)

**<font color=#1a73e8>作者：</font>** Muhammad Turab, Raja Vavekanand, Knooz Fatima  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models for breast density classification typically return only a label and confidence score. This paper presents BreastXAgent, a lightweight agentic framework that combines a pretrained classifier, Grad-CAM visual explanation, LangGraph-based routing, LLM report generation, and rule-based guardrails to produce controlled, faithful, non-diagnostic reports. On 160 mammography images, uncontrolled LLM reporting produced 75% Grad-CAM overclaims and 62.5% clinical overclaims. Strict prompting and LangGraph routing improved safety but did not eliminate violations. The full BreastXAgent achieved 100% safety pass rate, zero overclaims, and highest utility score. Results demonstrate that agentic guardrails enable safe, structured explanation generation without modifying the underlying classifier.

---


### 15. [MedICL: Modality-Anatomy-Aware Visual In-Context Learning for Medical Visual Question Answering](https://arxiv.org/abs/2611.00067)

**<font color=#1a73e8>作者：</font>** Ji-jun Park, Soo-joon Choi, Seungmin Han 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free adaptation of medical vision-language models (LVLMs) is a deployment requirement, yet visual in-context learning (ICL) injects modality- and style-mismatched demonstrations into medical contexts, teaching a frozen model the wrong answering style. We present MedICL, which curates demonstrations instead of retraining the model. MADS selects modality-anatomy aligned demonstrations that cover complementary interpretation dimensions; W2C curates them with weak retrieval signals and a strong verification vote that checks demonstrations rather than the model's own outputs; ECC answers with W anchored demonstration sets, aggregates by abnormality-aware signatures, and re-answers once on conflict. On VQA-RAD, SLAKE, and PathVQA under the LLaVA-Med zero-shot protocol, MedICL improves the strongest zero-shot baseline by +11 - +14 points on open-ended and +7 - +14 on closed questions, recovers 71% of fine-tuned open-ended performance on VQA-RAD at zero training cost, and stays robust to shifted or corrupted demonstration banks.

---


### 16. [Evaluating Context Sensitivity of Collaboration Behavior in Multi Party Simulation Frameworks](https://arxiv.org/abs/2611.00089)

**<font color=#1a73e8>作者：</font>** Anvesh Rao Vijjini, Sheshera Mysore, Pegah Jandaghi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Group Social Behavior is increasingly used as a lens to study Large language model (LLM) simulations to aid model training and evaluation. However, little prior work has examined how contextual factors such as team size and goal type manifest in long running simulations. To overcome this gap, we conduct a controlled, full-factorial study examining how contextual factors affect collaboration behavior across multi-party simulation frameworks. Using well established social science taxonomies, we quantify context sensitivity of collaboration behavior in simulated teams. Our analyses reveal significant effects of contextual factors such as simulators consistently favor smooth collaboration over disagreement, negotiation pressure, and coordination breakdown. These findings provide the first systematic evidence of how contextual factors influence emergent collaboration in LLM based multi-party simulation frameworks, offering both guidance and empirical results for the use of such simulations.

---


### 17. [OCRia-1 Technical Report](https://arxiv.org/abs/2611.00092)

**<font color=#1a73e8>作者：</font>** Aman Rangapur, Antonio Jimeno Yepes, Daniel Bustamante 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce OCRia-1, a 4B vision-language model (VLM) for document parsing that excels at preserving table structure, extracting chart data and retaining text formatting. OCRia-1 handles content that has traditionally been challenging in document parsing: merged cells and spanning headers, tables with thousands of cells, chart data, and meaningful text formatting such as bold, italics, subscripts and superscripts, preserving details needed for business-critical document analysis. At the time of this report, it achieves the highest scores on tables, charts and text formatting among the systems evaluated, including a 35B model and Mistral OCR 4.1. Its mean ParseBench score over the four dimensions we evaluate is 0.87, against 0.75 for the next-best system.
We emphasize data quality and reward design in training OCRia-1. Synthetic pages provide exact ground truth for long tables and rich formatting, while real pages are transcribed using a pipeline grounded in the PDF text layer. We attribute OCRia-1's performance primarily to careful data curation that prioritizes quality and diversity over quantity. Dimension-specific rewards evaluate table reconstruction, chart-data extraction and text-formatting fidelity. We train the model on the curated data using supervised fine-tuning (SFT), then refine it through reinforcement learning with verifiable rewards (RLVR).
To our knowledge, OCRia-1 is the fastest published document-parsing VLM in its class, decoding at about 4,700 tokens per second with a single request on one B200 GPU, about nine times faster than the base model on stock vLLM. This is achieved through a block-diffusion speculator, quantization and custom kernels.

---


### 18. [Pano2BIM: A Geometry-Constrained Vision-Language Agent for As-Built BIM Generation from a Floor Plan and a Single 360$^\circ$ Image](https://arxiv.org/abs/2611.00097)

**<font color=#1a73e8>作者：</font>** Juan Diego Castaño Molina, Borja García de Soto  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digital twins require accurate, up-to-date building information models (BIM) that reflect physical conditions, yet generating and maintaining as-built models remains costly and labor-intensive. Emerging image-based methods can capture visual appearance without inherently producing structured BIM information, while vision-language models (VLMs) struggle with reliable metric object placement. This paper presents Pano2BIM, a geometry-constrained VLM agent that generates approximate IFC4 models at Level of Development (LOD) 200 from a floor plan with known room dimensions and a single 360-degree photograph. The VLM identifies landmarks and objects, while deterministic tools estimate camera pose, compute metric positions through ray casting, and check spatial constraints. An optional second stage enriches the presentation model through render-and-compare feedback without modifying the primary furniture geometry. In a preliminary evaluation on one laboratory, the proposed Measure workflow achieved a mean furniture-footprint intersection over union (IoU) of 0.53, compared with 0.44 for a single-response baseline using identical modeling instructions, and matched an average of 4.0 versus 2.3 of seven fixed furniture elements across three runs. Centroid disagreements were similar for the four elements consistently identified by both approaches. The measurement stage averaged 3.8 minutes and USD 1.63 in API costs per run, while the complete demonstrated workflow required approximately 42 minutes and USD 11. These findings demonstrate the feasibility of rapid, low-cost as-built BIM generation, with potential applications in maintaining digital twins that reflect changing physical conditions.

---


### 19. [DTP-OPSD: Reinforcement Learning with Distractor-Aware Temporal-Privilege On-Policy Self-Distillation for Temporal Video Grounding](https://arxiv.org/abs/2611.00120)

**<font color=#1a73e8>作者：</font>** Zhaoyu Chen, Yongwei Nie  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Temporal Video Grounding (TVG) aims to localize the start and end times of an event described by a language query in a video. The task becomes particularly challenging when the same video contains multiple repeated, similar, or opposite events. On these hard examples, all responses sampled by Group Relative Policy Optimization (GRPO) may miss the target and receive zero temporal Intersection-over-Union (tIoU). Their group-relative advantages are then all zero, leaving no useful policy gradient signal. To address this, we propose DTP-OPSD, a reinforcement learning framework with distractor-aware temporal-privilege on-policy self-distillation. The student observes the clean video and generates responses on-policy, while a shared-weight teacher observes a privileged video in which the target window is marked by red full-frame borders and same-video distractor windows by blue full-frame borders. For the distillation loss, the teacher evaluates student-generated prefixes and provides dense token-level Jensen-Shannon divergence supervision. This supervision remains informative even when GRPO provides no policy gradient signal. We suppress distillation when the teacher does not outperform the student and strengthen it for groups where the teacher performs better but all student rollouts receive zero tIoU. We also construct a compact hard-interference training set through VLM screening and human verification. With only 300 additional post-training examples, DTP-OPSD achieves the highest mIoU among the compared open-source 8B models on Charades-TimeLens, ActivityNet-TimeLens, and QVHighlights-TimeLens, reaching 55.93, 54.77, and 66.71, respectively. Compared with Pure GRPO trained on the same data, DTP-OPSD improves all 12 reported metrics, with R1@0.7 gains of 1.28, 1.62, and 1.78 points on the three benchmarks. Code will be released at this https URL

---


### 20. [Early Stopping in Large Reasoning Models: A Survey and Empirical Audit of Efficiency and Reliability](https://arxiv.org/abs/2611.00166)

**<font color=#1a73e8>作者：</font>** Quang Hung Nguyen, Hanh Nguyen, Thanh Tam Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large reasoning models can improve accuracy by generating longer reasoning traces, but some of this computation may be unnecessary. Early-stopping methods aim to stop once enough reasoning is available to answer. Evaluating these methods requires accounting for the cost of deciding when to stop and the reliability of the resulting answer. We evaluate different methods across five reasoning models on mathematical and scientific reasoning, code generation, and factuality tasks by using a shared rollout replay protocol. We introduce Target-Integrated Token Efficiency (TITE) to measure efficiency relative to the oracle across accuracy targets. We also examine correctness at later exit positions, transfer across models and tasks, post-stop reasoning continuation, and retained justification quality. In our experiments, correctness can decrease at later positions beyond what the fitted decoding-noise model predicts. Reliability checks also reveal continued reasoning after forced termination and weaker supporting reasoning in some correct early-stopping outputs. The implementation can be found in this https URL.

---


### 21. [PatchScout: Thematic Web Data Collection via Information Foraging](https://arxiv.org/abs/2611.00169)

**<font color=#1a73e8>作者：</font>** Michael West, Eduard Dragut  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Researchers often need web corpora that are not answers to a single query, but reusable collections of documents spanning many decentralized sources. We refer to this problem as thematic web data collection: assembling semantically relevant documents that share a common theme but are scattered across heterogeneous and structurally disconnected regions of the web. Existing approaches, including traversal-based methods and LLM-driven web agents, are limited by local exploration or short-horizon stopping, preventing comprehensive collection. We formulate this task as a long-horizon information foraging problem over query-induced semantic patches, where the central challenge is deciding when to continue local exploitation and when to switch to new regions. We propose PatchScout, a multi-agent framework that instantiates a class of patch-switching policies to balance local exploitation and adaptive patch switching under a fixed budget. Experiments on four live-web topics show that PatchScout substantially improves yield and domain coverage over traversal-based and search-augmented reasoning agent baselines. In an applied social science setting with an incomplete prior collection, PatchScout discovers 102 previously unidentified entities, illustrating its ability to expand existing thematic datasets.

---


### 22. [Reimagining Text-to-SQL: A Survey of Large Language Model Architectures and Strategies](https://arxiv.org/abs/2611.00171)

**<font color=#1a73e8>作者：</font>** Shikhar Dave, Bhaskarjit Sarmah, Stefano Pasquali  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL systems translate natural language questions into executable SQL queries, democratizing access to relational data. Early approaches relied on handcrafted rules and template matching, while subsequent neural methods introduced encoder-decoder architectures, schema linking, and constrained decoding to handle increasingly complex queries. The emergence of large language models (LLMs), exemplified by systems such as ReFoRCE, Agentar-Scale-SQL, Snowflake's Arctic-Text2SQL-R1, and the modular XiYan-SQL framework, has dramatically advanced the field, pushing execution accuracy to new state-of-the-art levels on challenging benchmarks such as Spider, Spider 2.0, and BIRD. In parallel, modular frameworks decompose the task into sub-problems (schema retrieval, sketch-based generation, repair, and ranking), while agentic systems coordinate multiple specialized agents that communicate and dynamically allocate sub-tasks. This survey systematically reviews these LLM-driven approaches within a unified taxonomy of five paradigms (in-context learning, supervised and parameter-efficient fine-tuning, agentic and tool-augmented orchestration, retrieval-augmented generation, and reinforcement learning) and characterizes them by model granularity (monolithic vs. modular), level of supervision (zero-shot, fine-tuned, or reinforcement-based), and reasoning style (direct decoding vs. decomposed multi-step reasoning). We further analyze evaluation metrics, datasets, and open challenges, including domain generalization, efficiency, and real-world deployment, and we examine the role of the semantic layer in production systems. As LLMs increasingly access sensitive databases, we also discuss responsible AI practices. We survey over 100 papers and technical resources, focusing on work published between 2022 and 2026.

---


### 23. [Neurons Are All You Need](https://arxiv.org/abs/2611.00186)

**<font color=#1a73e8>作者：</font>** Joseph B. Alzagatiti, Alain C. Glanzman, Perry A. Demsko 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> For decades, artificial neural networks have operated under the assumption that durable, learned capability resides exclusively in adaptive synaptic parameters, primarily due to the established neurobiology of synaptic connectivity. This design forces models to remain stateless during deployment, incurring well-known limitations such as catastrophic forgetting and expensive retraining. However, recent neurobiological research by Glanzman and colleagues, and others, shows that memories can be transferred between individual organisms in a synaptically independent manner. Inspired by this research, we sought to demonstrate memory transfer of persistent memory between AI model instances, leveraging a neurocentric version of memory. In this paper, we propose NURESA (Neural Unit with Retentive Self-Adaptive Architecture), a novel neural layer that eschews sole reliance on synaptic weight updating by introducing persistent intra-unit memory as a first-class, computational primitive. By structurally separating computation from persistent memory, NURESA enables autonomous memory accumulation and consolidation into transferable stores of memory registers. Experiments across MLP, GPT-2, and modern frontier models like Qwen2.5 demonstrate qualitatively new capability: zero-shot transfer of learned capability into a naive model instance without retraining or access to the original training data; this transfer is enabled by a sparse set of parameters in NURESA's memory register that the model selects on its own based on which neurons were most active. The memory transfer capability of NURESA also protects against domain loss when transformer models undergo learning via fine-tuning. Finally, the memory transfer process completes in approximately one minute even for transformer models with millions to billions of parameters, producing a transfer file orders of magnitude smaller than the original model.

---


### 24. [MemU-Bench: Benchmarking GUI Agents on Long-Horizon User Interactions](https://arxiv.org/abs/2611.00191)

**<font color=#1a73e8>作者：</font>** Yizhou Liu, Zhengxi Lu, Fei Tang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing Graphical User Interface (GUI) benchmarks predominantly rely on precise and stateless user instructions. In everyday usage, however, instructions are often \emph{vague and history-dependent}: users omit the exact details of their past operations because they no longer remember them, leaving the agent to recover the missing context from long and noisy interaction histories. To bridge this evaluation gap, we introduce \textbf{MemU-Bench}, a mobile benchmark of \textbf{118 vague tasks} grounded in 29 long-horizon user trajectories, where agents must distill raw interaction streams into memory and retrieve the missing context on demand, with task outcomes verified against serialized application databases. Alongside Success Rate, we incorporate Interaction Efficiency (IE) and Success weighted by Path Length (SPL) to expose agents that succeed by exhaustively searching across different applications rather than by \emph{genuinely recalling} the history. Evaluations show that without user history, state-of-the-art systems struggle under such ambiguity: the best-performing Gemini-3.1-Pro achieves an SPL of only 16.4\%, and end-to-end GUI agents fall below 5\%. To address this, we further propose \textbf{AppMem}, a training-free framework that distills user history into a \emph{structured, app-centric} memory bank, tracks interrupted intents across application switches, and selectively retrieves relevant memories via target-app inference. AppMem raises the SPL of GPT-5.5 from 15.7\% to 66.9\% (\textbf{+51.2\%}), outperforms a naive summary baseline by 9.3\%, and delivers consistent gains across evaluated backbones.

---


### 25. [ProLand: A New Infeasible Manifold Optimization Method for LoRA Fine-Tuning](https://arxiv.org/abs/2611.00236)

**<font color=#1a73e8>作者：</font>** Chenyu Zhou, Yuxuan Zeng, Qi Deng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) enables parameter-efficient fine-tuning but can suffer from redundant basis directions. Constraining the basis factor to the Stiefel manifold addresses this redundancy through orthonormality. Landing methods allow temporarily infeasible iterates to explore a neighborhood of the manifold while progressively restoring orthogonality without per-step retractions. To improve optimization efficiency while retaining this flexibility, we introduce ProLand (Product-space Landing), a retraction-free optimizer that combines coordinated factor updates with Muon-style spectral directions. By designing the updates in the space of the represented weight increment, ProLand separates objective optimization from orthogonality restoration, supporting efficient feasibility recovery. This coordinated construction also enables Muon-style directions to guide objective optimization while preserving that separation. Experiments cover four GLUE validation tasks on DeBERTa-v3-base and seven language benchmarks on Qwen2.5-3B, Llama-3.2-3B, and Moonlight-16B-A3B across multiple adapter ranks. Across these 11 tasks, ProLand achieves the highest average score among the compared methods in every tested encoder and decoder model-rank configuration.

---


### 26. [RE-SciVQA: Improving Scientific VQA With Context-Relevant Retrieval and Lightweight MLLM Adaptation](https://arxiv.org/abs/2611.00242)

**<font color=#1a73e8>作者：</font>** Sheikh Tahmim Mehdi, Muminul Islam Jami  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A deep understanding of scientific literature often relies on interpreting figures that contain key information beyond the main text. Leveraging Large Language Models (LLMs) to extract insights from these figures can significantly accelerate knowledge discovery. Existing works on Scientific Visual Question Answering rely on resource-intensive training pipelines that are often inaccessible and require large computational resources. Instead of designing complex architectures, we propose RE- SciVQA, which focuses on improving the quality of retrieved context and fine-tuning small LLMs with parameter-efficient LoRA training. Using a simple query expansion step, relevant section headers are appended to the original question to improve the retrieval coverage. In addition, a simple adjustment of similarity scores is applied using figure references and caption alignment. On the SciVQA benchmark, RE-SciVQA achieves a ROUGE-1 F1 score of 73.9%, outperforming chart-focused models such as UniChart (14.7%), ChartGemma (6.9%), and Matcha-ChartQA (6.3%). Our relevance-enhanced RAG setup also improves the exact match by 11.9% and the fuzzy match by 29.5% compared with a standard RAG baseline, resulting in an overall gain of 14.3%. We also examine closed-ended infinite visual questions, a category in which chart-understanding models often struggle. Our experiments show that using plot digitization instead of synthetic captions leads to an 18.5% improvement for this question type.

---


### 27. [OmniPiano: Diverse Dexterous Piano-Playing Challenges for Standard, Robust, Safe, and Multi-Agent RL](https://arxiv.org/abs/2611.00243)

**<font color=#1a73e8>作者：</font>** Fan Xu, Fan Yang, Yifan Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dexterous robotic manipulation remains a major challenge in robotics, exemplified by piano playing, which requires coordinated control of fingers and provides a demanding testbed for reinforcement learning (RL). Although previous work established a benchmark for robotic piano playing, it is restricted to two hands and does not support unified evaluation. To address this gap, we introduce OmniPiano, a benchmark that provides one to up to five Shadow Hands and supports standard, robust, safe, and multi-agent RL within a shared piano-playing task family. OmniPiano is developed for scalable and diverse piano-playing tasks with configurable perturbations, explicit safety constraints, and decentralized cooperation settings. Particularly, to facilitate usability and extendability, OmniPiano adopts a highly modular design and provides comprehensive tasks to support RL study of task performance, robustness, safety, and cooperation in dexterous control. With at least 912 task settings and 36 baseline algorithms, OmniPiano further incorporates LLM-based agents to broaden the evaluation scope and reveal new insights. Extensive evaluations show that state-of-the-art RL algorithms and frontier LLM-based agents still struggle on challenging piano-playing tasks, even under standard RL settings, highlighting substantial room for improvement in dexterous control. The code, dataset, tutorial, and demo are available at this https URL.

---


### 28. [MEMENTO: Learning Context Management for Long Context Processing Agents](https://arxiv.org/abs/2611.00244)

**<font color=#1a73e8>作者：</font>** Yunfan Zhang, Taehoon Hwang, Kathleen McKeown 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents that operate over long inputs must perform context management: deciding what to retain in a fixed-size context window. A common approach is compaction, where the model replaces its history with a self-generated note. Yet off-the-shelf agentic models, including GPT-5.5 and GLM-5.3, often write ineffective notes, and reinforcement learning (RL) alone rarely discovers useful note-taking behavior. We present MEMENTO, a long-context agent built on Qwen3-8B and trained to manage its context through compaction. We first bootstrap note-taking by fine-tuning on synthetic trajectories annotated with notes generated in hindsight, then reinforce it with RL using a reward that combines answer correctness, note-quality heuristics, and confidence calibration. Although trained only to compact into a fresh window, MEMENTO extends at test time to strategies such as context folding and confidence-based backtracking. On book-level question answering across four benchmarks, with books of up to 2.5M tokens, MEMENTO raises Qwen3-8B's accuracy from 36.9% to 67.8% while never holding more than 20K tokens in context. It outperforms GPT-5.5 agent in the same harness (13.1%) and full book context (56.7%) at less than 1/50 the cost. It also nearly matches a ~100x larger GLM-5.3 agent (69.3%) at 1/9 the cost, and comes within 6.4 points of GLM-5.3 full context at 1/26 the cost.

---


### 29. [Taurus: LLM-in-the-Loop CT Annotation Matches Coding Agents at Half the Cost](https://arxiv.org/abs/2611.00247)

**<font color=#1a73e8>作者：</font>** Bing Hu, Rishabh Sharma, Jatin Mehta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dense labels of the aorta in CT are slow to draw, and the public aortic CT datasets that could stand in for them each label different structures under their own conventions. Large language model (LLM) agents can now write code and read images. We asked whether such a model labels these scans better as a free-form agent that writes its own segmentation code, or inside a harness, where an automated pass labels the scan and the model reviews the result. We built a harness, Taurus, and compared it with free-form agents by blind label recovery: we withheld the human labels of six public datasets (939 volumes) and scored every approach against each dataset's own classes. In the first version of Taurus, the model's review raised the primary metric on only two of six datasets, by less than the noise between two reviews of the same case. A free-form agent running Claude Opus 5.5 scored higher on most datasets. Moving what the free-form agents did well into the automated pass then carried most of the gain on 38 held-out cases. The final version smooths the label surfaces with a fixed rule and checks for the large errors the automated pass tends to make, such as an aneurysm drawn to half its size. Each check that fires puts a multiple-choice question to the model, with candidate corrections drawn on the scan. It matched the surface smoothness of the human references, and in the primary metric we found no difference from the free-form Opus agent, at under half its cost, $1.22 against $2.71 per case. Most of what made Taurus competitive came from the harness and its automation rather than from the language model itself. Taurus shows that this kind of annotation can be automated, so that expert time can move from drawing labels to checking them.

---


### 30. [DELBERT-2: Pretrained Fingerprint Language Models for DEL Protein Binder Prediction](https://arxiv.org/abs/2611.00281)

**<font color=#1a73e8>作者：</font>** Bing Hu, Sun Sun, Shaik Salman Basha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present DELBERT-2, a pretrained fingerprint language model that converts sparse molecular fingerprints into unified token sequences using a ModernBERT encoder trained with masked language modelling on 2.5M molecules from the AIRCHECK DEL corpus. We evaluate across six targets (WDR91, WDR12, SETDB1, PLCZ1, LRRK2, DCAF7) under three out-of-distribution (OOD) protocols: hierarchical cluster splits probe chemical novelty, library splits test cross-library transfer, and building-block splits assess compositional generalization. DELBERT-2 consistently improves PR-AUC and NDCG@1000 relative to LightGBM ensemble baselines and transformers trained from scratch, with the largest gains in stringent OOD regimes. DELBERT-2 achieves 13.28+/-3.72 enrichment factor at top-100 vs. 12.36+/-3.75 for no-pretraining (p=0.040), representing 7.4% improvement and 13x enrichment over random selection. These results demonstrate that fingerprint-centric self-supervised learning effectively improves hit prioritization under distribution shift, enabling practical DEL virtual screening. Code is available at \hyperlink{this https URL}{DELBERT-2}.

---


### 31. [Quantization of Large Models with Weight Outliers and Sparsity](https://arxiv.org/abs/2611.00286)

**<font color=#1a73e8>作者：</font>** Leonidas Tsigkounakis, Abraham Jaeger Mountain, Yilang Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) reduces the memory burden of large model deployment by casting the high precision trained weights to fewer bits. While this promotes memory-efficient inference, it also incurs quantization error that impairs model performance. To compensate for quantization error, the present contribution decomposes the original trained weights into a quantized matrix, a low-rank component, and a sparse matrix that accounts for outlier rows in the weights. Due to analytical intractability and the discrete structure of the decomposition, a simulated annealing search is employed to explore candidate decompositions while avoiding poor local minima. Numerical tests demonstrate the effectiveness of this approach across a broad suite of large language models, including Llama 3.2 1B, Llama 3.2 3B, Llama 3.1 8B, and Qwen2.5 7B, evaluated on natural language generation benchmarks using 4-bit NF4 and FP4 quantizers. The novel method can markedly outperform direct quantization while incurring minimal memory overhead.

---


### 32. [Cross-Lingual Persona Effects in LLM Negotiation](https://arxiv.org/abs/2611.00300)

**<font color=#1a73e8>作者：</font>** Saehee Eom, Tejas Khandwekar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tell an LLM negotiator to be "headstrong" and it should hold firm on price, but does that instruction retain the same behavior in every language? To test this, we use identical buyer and seller instances of Gemini 3.6 Flash to negotiate the same 12 CraigslistBargain scenarios in English and Korean. The pilot-scale 2 x 2 x 3 design crosses interaction language, seller urgency (none or strong), and buyer persona (cooperative, neutral, or headstrong), yielding 432 attempted negotiations. We call this property cross-lingual social-policy fidelity: whether a prompt-defined social policy produces the same behavioral effect regardless of interaction language. It often does not. Korean negotiations reached agreement far more often than English (77.3% vs. 52.5%, a 24.8-point gap, Holm-adjusted p = .0039), but only for neutral and headstrong buyers; cooperative buyers were already near-ceiling in both languages. Buyers' opening offers barely differed by language; the gap instead emerged later, through larger seller concessions and a smaller final gap in Korean, and agreed prices were also lower in Korean. Repeating the full design with Qwen3.7 Flash as both agents gives directional support: agreement was again higher in Korean (+13.9 points vs. Gemini's +24.8, with an interval whose lower bound is near zero), and sellers again conceded more. Pragmatic analysis reveals why: while both languages frequently featured face-threatening acts like rejections and counter-offers, Korean dialogue softened these threats with substantially more politeness mitigation, especially among sellers (11.7% vs. 3.6%). These results show that such a policy can produce different simulated negotiation behavior, not just different wording, when only the interaction language changes.

---


### 33. [Decentralized Multi-Agent Coordination and Communication in Shared Codebases](https://arxiv.org/abs/2611.00314)

**<font color=#1a73e8>作者：</font>** Rishabh Mediratta, Lingyun Xiao, Peter Stone 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents working in shared repositories may receive separate, independently-motivated requests from human developers, creating a setting that is multi-agent by necessity. When this scenario happens, their individual implementations may work separately but conflict when combined. To study this setting, we introduce ParallACT, a benchmark of orchestrator-free multi-agent coding tasks. ParallACT contains both complementary and contradictory tasks. In complementary tasks, each agent's task is separately useful and implementations must share an interface to be productively combined. In contradictory pairs, both agents' tasks require editing the same code in incompatible ways, and naively combining independent solutions fails to produce a useful implementation. We compare a single-agent oracle given the combined set of tasks against multi-agent settings that vary execution order, visibility, awareness of other agents, and access to a communication channel. We find that the oracle solves most tasks while parallel agents perform substantially worse. Their performance drop is notable for complementary tasks, and particularly sharp for contradictory tasks (e.g., from 62% to 16% for Claude Code with Claude Opus 4.8) where merged code typically satisfies only one specification, and the same gap appears in all six further configurations pairing two agent harnesses with three open-weight models. Simply telling an agent that a peer exists does not help significantly, and giving agents access to a communication channel recovers only a small part of the performance, at an additional token cost. ParallACT thus identifies and isolates a core challenge that will become more common as multi-agent coding by independent principals becomes standard, and provides a controlled test of which coordination strategies help, and at what cost.

---


### 34. [GAVAGAI: Referential Alignment for Infant-Scale Vision-Language Models via Balanced Optimal Transport](https://arxiv.org/abs/2611.00319)

**<font color=#1a73e8>作者：</font>** Rajdeep Pal, Jotiraditya Banerjee, Saptarshi Pani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A child learns which words name which things from roughly 100 million words of input. Vision-language models trained at a comparable scale bind words to referents far less reliably, and we argue that part of the gap is structural: the usual next-token captioning objective has no variable standing for "this word refers to that region," so training applies no direct pressure to ground words. We add such a variable by treating each scene as a small assignment problem between the content words heard and the regions seen, solved as entropic optimal transport under two constraints. First, a word may be assigned to a special NOTHING column instead of any region, which matters because most content words in caregiver speech do not name anything visible. Second, no region may receive more than a bounded share of the assignment mass, a capacity constraint that encodes mutual exclusivity. The alignment step costs about eight Sinkhorn iterations, small next to the vision encoder. In controlled simulation, the naive version of the idea, a row-wise softmax that forces every word onto some region, collapses to 0.000 word-to-picture accuracy under realistic non-reference rates, below the 0.058 of captioning alone, while our two constraints reach 0.075 in that regime and 0.700 on clean input. A one-parameter version of the model reproduces adult cross-situational learning accuracy across three ambiguity conditions (RMSE 0.024). On the SAYCam infant video corpus, adding the alignment loss to a next-token captioning model raises word-to-picture accuracy from 32.4% to 48.7% and localization IoU from 0.18 to 0.38. A contrastive model trained on the same child's data remains stronger on its own benchmark, so our claim is that the loss improves a captioning objective under high non-reference rates, not that it sets a new best.

---


### 35. [Beyond Semantic IDs: Atomic Creator Tokens for Large-Scale Generative Recommendation](https://arxiv.org/abs/2611.00323)

**<font color=#1a73e8>作者：</font>** Zhuosheng Liu, Yihan Wu, Ziyun Xu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recommending creators that a user does not yet follow is a cold-start problem: from hundreds of thousands of popular creators and only a short trail of prior engagements, the system must predict the next creator worth surfacing. The prevailing generative recommendation recipe tokenizes each creator into a \emph{Semantic ID} (SID) by quantizing a frozen embedding and trains a language model to generate SIDs. We show that this SID layer, not the language model, is the binding constraint. The creator-to-SID map is many-to-one, so colliding creators must be resolved by a popularity tie-break that caps creator-level recall and favors already-popular creators, and the frozen quantizer stops the training gradient from reaching the creator representation. We propose Atomic Creator Token (ACT), which gives every creator its own vocabulary token trained end-to-end. The map is bijective, so collisions are impossible and inference is a direct top-$k$ over creator logits. In a controlled comparison on production data in which the token layer is the only variable, ACT improves creator-level Recall@15 by 19.8 points ($1.84\times$) over a matched SID baseline, still leads when the SID codebook is enlarged $64\times$, and serves at ${\sim}2.7\times$ lower per-user latency. The advantage carries over to the public KuaiRand dataset, where ACT is the only method that beats a global-popularity baseline, provided each creator token sees enough training examples. In a live A/B test, ACT is directionally positive on every reported metric against both the SID-enhanced and the classic production rankers.

---


### 36. [C3: Speech-Guided KV Retrieval for Long-Context SpeechLLM Inference](https://arxiv.org/abs/2611.00333)

**<font color=#1a73e8>作者：</font>** Dancheng Liu, Markus Müller, Rupak Vignesh Swaminathan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speech language models encode audio at a much higher rate than text, causing the KV cache to dominate the memory, bandwidth, and decoding cost of long-form generation. KV retrieval can reduce per-step access by attending to only a query-dependent subset of the cache, but existing methods are designed primarily for text and do not account for the structure of audio attention. We first show that retrieval errors may compound autoregressively into generation drift. We then analyze full audio attention during long-form generation and identify three properties relevant to retrieval: unequal attention concentration across query heads, non-contiguous audio support, and temporal continuity across decoding steps. Guided by these observations, we propose $C^3$(Cluster-Compete-Compete), which organizes audio KVs in a hierarchical key-space index, lets query heads sharing a KV head compete for a common retrieval budget, and adaptively reallocates retrieval resolution through paired split-merge updates. Across long-form speech recognition, translation, and summarization on four SpeechLLMs, $C^3$ achieves the strongest overall performance among retrieval methods under comparable final-KV access budgets, with particularly large gains in the tight-budget regime, while improving long-context decoding efficiency and accelerator-memory scaling.

---


### 37. [Decomposing Irregular Time Series into Interpretable Temporal Patterns with Mixture-of-Experts](https://arxiv.org/abs/2611.00337)

**<font color=#1a73e8>作者：</font>** Jenna L. Ballard, Zijie Pan, Shivani Shekhar 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Irregularly-spaced sequential data, such as transaction logs, encode multi-scale temporal structure that is critical for prediction but difficult to recover explicitly with standard sequence models, which often trade interpretability for performance. We introduce MoTIF, an interpretable framework using mixture-of-experts (MoE) attention to decompose irregular time series into temporal patterns spanning minute-to-year scales. Each expert is trained via temporal alignment that induces attention specialization to a designated cyclical or within-range pattern, with label-free routing supervision that learns to activate the correct expert from patterns present in the data. On synthetic data with known temporal structure, MoTIF recovers correct routing well above chance (0.389/0.829 for range/cyclical patterns vs. 0.091 random) and outperforms all baselines, including a standard transformer and an unspecialized MoE, on next-value prediction. On a public credit card transaction dataset, MoTIF achieves higher macro-F1 than all baselines for next-amount prediction. Its learned routing reveals structure a black-box model cannot: transactions are governed primarily by intraday and short-interval rhythms, while fraudulent transactions show bursty, calendar-agnostic timing versus the steadier periodicity of legitimate ones. On downstream fraud detection, MoTIF matches standard transformer and MoE baselines and clearly outperforms recent sequential recommendation models used as embedding baselines. These results show that decomposing temporal structure into interpretable, expert-specific patterns need not sacrifice predictive accuracy, offering a practical route to sequence models that are both accurate and auditable in high-stakes settings. Code is available at this https URL.

---


### 38. [SIEVE: Preserving Cross-Image Evidence via Depth-Aware Token Compression](https://arxiv.org/abs/2611.00351)

**<font color=#1a73e8>作者：</font>** Nitish Shukla, Surgan Jandial, Nhat-Tan Bui 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-image vision-language models (VLMs) incur substantial computation when processing long visual sequences. Compressing these sequences must preserve complementary evidence across images and keep tokens from different images separate. Global selection can underrepresent question-relevant images, and pruning in early decoder layers risks removing relevant content before sufficient multimodal processing, yet existing methods spend most of the budget on these early layers. We propose SIEVE, a training-free, single-pass framework that jointly allocates visual tokens across images and decoder depth. SIEVE first pools each image into a compact spatial grid to reduce early processing cost. It then progressively selects representatives using prompt attention under equal per-image quotas and aggregates unselected tokens into similar representatives from the same image. These operations keep every image represented and its tokens separate from other images, while refining the retained representations. A closed-form schedule sets retention counts to target a prescribed average token budget across decoder layers. Across four VLM backbones, SIEVE achieves the highest average at a 6.25% budget on five multi-image benchmarks and four single-image benchmarks, and the highest mean on two video benchmarks. On LLaVA-OneVision-7B, it outperforms the strongest baseline by 9.96 and 9.03 points at 6.25% and 12.5% budgets, and at 12.5% it exceeds the uncompressed model by 2.01 points with 6.6x fewer prefill FLOPs.

---


### 39. [Cross-Prompt Reuse of Entity-Replacement Responses](https://arxiv.org/abs/2611.00352)

**<font color=#1a73e8>作者：</font>** Jinkun Chen, Xuemin Yu, Sijia Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With model weights fixed, we measure how much of an entity-replacement response transfers between English factual questions, beyond whether answers change. We add the hidden-state change from two source questions to a target question about the same entity, comparing the predicted log-probability shift between two relations' published answers, given known answer prefixes, with the measured one. Hidden reuse injects the aligned change at 50% depth before the target's remaining layers; direct reuse adds source output-score changes. With other-relation sources, hidden reuse removes 45% and 49% of no-change error on 0.5-1B Qwen and Llama. Gemma-2-2B removes 22% and passes one of three comparisons in plain text without its default beginning-of-sequence (BOS) token. A later protocol restoring it yields 58-68%, passing every comparison on three cohorts. Larger checkpoints, chat format and new entities show replication and format- or cohort-dependent failures. On small plain-format checkpoints, other-relation hidden reuse mainly reproduces the shift both relations' questions share, without reliably lowering relation-selective error. With target-relation sources, hidden reuse's post hoc advantage over direct reuse is 0.2-0.9 nats outside chat format, unconfirmed and not replacement-specific. The same relation-neutral change at both questions' entity tokens lowers relation-selective error more than random or other-replacement changes, indicating receiving-question dependence.

---


### 40. [Unlearning by Extrapolating a Shrink-and-Heal Lookahead](https://arxiv.org/abs/2611.00374)

**<font color=#1a73e8>作者：</font>** Hoang-Chau Luong, Lingwei Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unlearning aims to make a large language model behave like one retrained without its forget set. Prevailing likelihood-suppression objectives, however, lack an explicit forgetting target: they continually reward lower forget-set likelihood, making forgetting sensitive to the optimization budget. We address this limitation by estimating the direction toward the oracle without training it. Our key idea is to shrink the fine-tuned model toward its pre-fine-tuning weights and briefly re-learn the retain set, thereby removing the forget-specific contribution; in the linearized regime, this shrink-and-heal lookahead moves the model a fixed fraction of the way to the retrained model, its unique fixed point. Our method, SHIFT, extrapolates the lookahead's per-token changes into distillation targets and iteratively refines them. Evaluated against eleven baselines under a unified OpenUnlearning protocol, SHIFT achieves the highest aggregate score across all TOFU settings and the closest oracle alignment, 3.7x closer on average than the next-best method; on MUSE, it preserves the most retain knowledge. Under larger optimization budgets, baselines overshoot the oracle, while SHIFT remains near it, even under relearning attacks.

---


### 41. [LF-VideoQA: Evaluating Long-Video Understanding with Long-Form Theory-of-Mind Questions](https://arxiv.org/abs/2611.00383)

**<font color=#1a73e8>作者：</font>** Shaden Shaar, Bradon Thymes, Majd Aldaye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The hardest part of understanding a long video is not pinpointing any one moment but synthesizing many, e.g., answering a question that requires tracking what develops across hours of content and articulating how the pieces fit together. To date, most long-video QA datasets require only a short answer or a multiple-choice selection, oversimplifying the long-video understanding task to retrieval. We introduce LF-VideoQA, a dataset for long-form, open-ended question answering over long narrative videos built on theory-of-mind questions: a character's belief depends on everything they have seen or been told, so each question demands assembling and reasoning from evidence distributed across the video. The dataset contains more than 6,300 questions on 94 recent films; each requires reasoning over scenes spanning an average of 23 minutes and comes with a question-specific rubric for recall and precision scoring. The dataset is created entirely automatically by annotating screenplays with scene events and each character's first-order beliefs and meta-beliefs, then generating (question, answer, rubric) triples through LLM-based question generation and verification; human studies validate their quality. We evaluate four families of state-of-the-art open-source VLMs across three settings and find the task highly challenging: (i) even an oracle with access to the screenplay falls well short of complete answers; (ii) the best non-oracle model attains barely half of the recall level of the oracle; (iii) unlike on prior long-video benchmarks, captions and subtitles underperform the video itself, indicating that the questions need visual evidence; and (iv) recall is the predominant bottleneck, with answers omitting many required rubric claims.

---


### 42. [Dependence-Aware Risk Assessment and Optimal Design of AI-Agent Safeguard Systems](https://arxiv.org/abs/2611.00386)

**<font color=#1a73e8>作者：</font>** Yijia Li, Maochao Xu, Peng Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly rely on safeguards to prevent unauthorized actions while preserving legitimate service. However, existing risk assessments often focus on individual safeguard performance while overlooking dependence among safeguard decisions. This paper develops a dependence-aware framework for risk assessment and optimal design of multi-component AI safeguard systems, jointly selecting configurations and operating policies for sequential layered screening and selective verification. We establish stochastic comparisons of layered-screening error probabilities and invocation costs under lower-orthant ordering. For selective verification, we characterize exactly which policies have error probabilities and review costs that respond monotonically to stronger dependence under supermodular ordering. For a fixed first stage and reviewer, we show that the optimal routing map is a two-threshold rule in the first-stage likelihood ratio. An accompanying open-source software package, Dependence-Aware Policy Optimization Algorithms (DAPOA), facilitates the practical implementation of the proposed framework. Numerical experiments show that ignoring dependence can lead to inaccurate risk assessments and infeasible safeguard designs, with independence-based selections violating security requirements in six of eight scenarios. An empirical study using four LLM safeguards on benchmark-derived agent actions further demonstrates the practical implications of dependence modeling. Under the principal operating setting, dependence-aware selection lowers held-out total cost by 39.6% relative to independence-based selection.

---


### 43. [CalVLA: Shaping Native Confidence in Vision-Language-Action Policies with Outcome Supervision](https://arxiv.org/abs/2611.00394)

**<font color=#1a73e8>作者：</font>** Boniface Chukwuemeka Godwin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can a vision-language-action (VLA) policy signal likely task failure from its own action probabilities? We introduce CalVLA, which shapes native action-token confidence using successful and failed rollouts and an Action-Confidence Alignment (ACal) squared margin-ranking loss. Low-rank adapters update OpenVLA-7B without an auxiliary failure detector. Observations are paired within tasks at similar normalized elapsed times, not necessarily equivalent physical progress. On a held-out test split from 500 LIBERO-10 configurations, adapted confidence achieves a joint failure-discrimination AUROC of $0.7392\pm0.0480$ over three seeds, averaging scores at 130 and 260 steps. Frozen-policy probes reach 0.6146--0.6436, but superiority over the linear probe is statistically inconclusive. For the same confidence summary, AUROC rises from 0.4485 before adaptation to 0.7327 after adaptation. Mean task success decreases from 58% to 55%. These results show improved failure discrimination, not improved control or established safety benefits.

---


### 44. [MXCode: Vector Quantization for MX-Native Inference at Scale](https://arxiv.org/abs/2611.00403)

**<font color=#1a73e8>作者：</font>** Gaurav Kolhe, Cansu Demirkiran, Shubhi Tyagi 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Memory capacity and bandwidth are major bottlenecks in LLM inference, motivating weight compression beyond conventional 4-bit quantization. Vector quantization (VQ) enables approximately 2-bit weight storage but often relies on codebooks incompatible with native FP4 computation. We introduce MXCode (MX-Native Codebook Quantization), a framework bridging ultra-low-bit VQ compression with MicroXcaling (MX)-native FP4 computation. MXCode proposes three strategies: PostScale, which quantizes learned codebooks to MXFP4; PreScale, which extracts MX scales before codebook learning; and PreScale+, which further compresses these scales using VQ. These strategies explore tradeoffs among quantization quality, scale overhead, and codebook granularity. All reconstruct MX-native W4A4 operands without materializing intermediate high-precision weights. We evaluate MXCode on Qwen3 (235B), DeepSeek-R1 (671B), and GLM-5.2 (753B) using the Microsoft MX Emulation Library. MXCode achieves approximately 2 bits per weight with competitive, workload-dependent model quality. On GB300 hardware, experiments with Qwen3 (235B) show approximately 50% lower model-load memory than Native FP4 while maintaining near-Native-FP4 serving throughput. Under memory-constrained prefix reuse, P90 TTFT improves by up to 94.5%. These results demonstrate software-based reconstruction on existing FP4 hardware and inform the development of future MX-native inference systems.

---


### 45. [Hacking or Just Failing? A More Capable LLM Monitor Better Separates Reward Hacking from Honest Failure](https://arxiv.org/abs/2611.00407)

**<font color=#1a73e8>作者：</font>** Kaushik Kezendirane  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An agent's visible score can exceed its real progress because it gamed the score or because it simply made mistakes, so a useful reward-hacking monitor must tell the two apart. We built a sandboxed task in which an agent can game a completion score, labelled every episode by replaying it and repairing the final state counterfactually, and ran five pre-registered studies. On 60 episodes from a Llama 3.1 8B agent, small local monitors (Llama 3B and 8B) did not separate exploit attempts from honest failures with the same score gap: prompt changes traded missed exploits for false alarms, and the pre-registered primary monitor reached AUC 0.64. On identical inputs, Gemini 3.1 Flash-Lite, which completed 9/10 clean tasks against 2/10 for the 8B model, met our pre-registered criterion (AUC 0.80, 95% interval [0.66, 0.93]; 1/35 honest failures flagged); with only 14 exploit episodes, this estimate is uncertain. On an exploit that no prompt names, Gemini usually described the action correctly yet never flagged it, in 5 and then 25 new episodes, even when manipulation was defined by its effect on the score. Given the full trace, the 8B monitor flagged all 25 replication episodes and none of 25 honest look-alikes, but its explanations described actions that had not occurred; given additional structured evidence, it also flagged 15 of the 25 look-alikes. A two-rule deterministic check caught every known exploit. We release the environment, labels, pre-registrations and per-judgement logs.

---


### 46. [TileWeave: Heterogeneous Tiling for Sparse Prefill on Mobile SoCs](https://arxiv.org/abs/2611.00408)

**<font color=#1a73e8>作者：</font>** Wentao Ni, Hong Cai, Mingu Lee 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Smartphone applications increasingly require large language models to process long contexts, whereas high prefill latency and memory demands constrain local inference. Block-sparse attention reduces computation and memory traffic, but its irregular selections conflict with mobile NPUs' preference for large, regular tiles. Efficient execution must exploit cross-query reuse while avoiding redundant computation and preserving selections needed for accuracy. In this paper, we present TileWeave, which partitions sparse attention by this cross-query reuse: highly shared key blocks run in coarse NPU tiles, while low-reuse blocks run on the GPU only for the query blocks that selected them. In addition, we design an NPU-native pooled-key selector that keeps selection inexpensive, and a runtime that publishes GPU partials in the order the NPU consumes them and merges them in its existing output store. On RULER, HeteroSparse matches XAttention's accuracy with Qwen3-1.7B and improves it with Llama-3.2-3B-Instruct; its mean LongBench scores match XAttention as well. On Snapdragon SM8750 and SM8850 phones, it achieves 1.35--3.23$\times$ faster full-model prefill than XAttention over 1k--16k tokens and up to 1.58$\times$ faster than dense attention.

---


### 47. [Circuit Oracle: Automating Attribution Graph Analysis via Natural-Language Queries](https://arxiv.org/abs/2611.00420)

**<font color=#1a73e8>作者：</font>** Shariar Kabir, Hong Kiat Tan, Swastik Agrawal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Attribution graphs, an emerging tool in mechanistic interpretability, use transcoders to decompose language model computations into sparse interpretable features connected by causal edges. However, turning a graph into a safety-relevant insight requires hours of manual analysis by experts. We introduce Circuit Oracle, an off-the-shelf LLM equipped with a multi-agent harness and task-specific authored skills, which answers natural-language questions about a target model by reading the attribution graph through tool calls. We evaluate it on three safety-relevant proxy tasks: detecting spurious features in probe circuits, eliciting hidden knowledge from taboo-finetuned models, and suppression jailbreaking via feature-level interventions. Beyond task scores, the oracle produces pruned subgraphs and context-specific feature explanations that we assess qualitatively. Results are mixed. On spurious-feature detection, Circuit Oracle reaches 78.2 $\pm$ 2.4% accuracy, outperforming single-layer feature-ranking baselines. On secret elicitation, trained self-explainers like Activation Oracles remain the stronger baseline. On refusal suppression over 50 prompts, its single committed intervention is slightly below a diff-in-means baseline, and only exceeds it when allowed the best of five attempts. Results are stable across five runs and across model choices for the agents. We also release the pruned subgraphs and context-specific feature readings that revise existing global labels, and invite future work to develop evaluations that can measure their usefulness directly.

---


### 48. [RankLane: Efficient MoE Prefill on Accelerators with Ranked Expert Capacities](https://arxiv.org/abs/2611.00421)

**<font color=#1a73e8>作者：</font>** Wentao Ni, Chihao Yu, Hong Cai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-experts (MoE) models expand model capacity by activating only a subset of experts for each token. On accelerators with static execution plans, expert capacities and placement are fixed before routing reveals each expert's load. Uniform worst-case capacities waste work on padding; smaller capacities tied to expert identities can overflow. We present RankLane, which ranks each device's experts by current load and assigns them to fixed-capacity lanes. Runtime indices select experts and token rows while tier populations, shapes and device placement remain fixed. An aggregation graph preserves device ownership and reduces each token's local contributions on one core. Routing calibration and measured execution costs guide tier selection; overflowing chunks rerun at full capacity. We evaluate full-model prefill of Qwen3-30B-A3B and Gemma 4 26B-A4B with MXFP6 weights on four Cloud AI 100 Ultra SoCs, using 128-2048-token chunks and including overflow detection and in-program recovery support. Against a dense baseline, RankLane achieves end-to-end prefill speedups of 1.27-4.18x on Qwen3 and 1.93-3.46x on Gemma.

---


### 49. [Do Multimodal Models Decide Consistently on Equivalent Optical Spectra?](https://arxiv.org/abs/2611.00428)

**<font color=#1a73e8>作者：</font>** Ziyuan Wang, Genliang Zhu, Xiaobo Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A spectrum can be given to a model as a table in nanometers or as a plot in photon energy, and the decision should not depend on which one it sees. When the data needed for an answer are missing, the model should say so. We test representation invariance and abstention on measured optical spectra of silicon metasurfaces (MOCLIP) and gold nanoparticles, with labels computed from the data. Each spectrum is shown as four tables (nm, $\mu$m, scientific notation, eV) and two plots (nm, eV), and partial spectra remove data inside or outside the queried range. We evaluate the decision models d3-nano and Jev 1.13, three GPT-6 Luna configurations and the Qwen3.5-2B base model. Changing only the representation moves accuracy by up to 41 percentage points within one model, mostly on photon-energy tables and plots. With the same evidence, asking in photon energy instead of wavelength helps some model-view pairs by 16-50 points and hurts others by up to 25. When the relevant extremum is removed, unadapted models rarely answer "undetermined". LoRA fine-tuning of d3-nano improves comparisons on the trained table formats, but much of its gain on unanswerable questions comes from a shortcut: it abstains whenever the input is truncated. Training with answerable truncations avoids the shortcut in all six seeds, with a 90-100 point gap between abstention after inside and outside cuts on held-out structures; with the same amount of extra original-task data, five of six seeds keep the shortcut. On gold spectra the two training sets perform similarly. Multimodal language models used for scientific decisions should be tested on equivalent representations and on missing evidence, not only on average accuracy. We release the tasks, per-response results and analysis code.

---


### 50. [Statistical Inference under Performativity: From Policy Feedback to Self-Evolving Systems](https://arxiv.org/abs/2611.00438)

**<font color=#1a73e8>作者：</font>** Tianwei Gao, Garrett G. Wen, Huiying Zhong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Performativity arises when prediction-informed decisions change the data-generating process, creating feedback between deployment and learning. This phenomenon occurs in policy-making and in self-evolving AI systems that shape their own future training data. Statistical inference is challenging because estimation errors in earlier predictors affect subsequent data distributions and propagate into later updates. We develop an end-to-end framework for statistical inference under performativity. For repeated risk minimization and repeated gradient descent, we establish central limit theorems at fixed deployment rounds and derive covariance recursions that capture both current-round sampling variation and uncertainty inherited from earlier deployments. We develop consistent covariance estimators using policy perturbations and score matching. These results can yield asymptotically valid confidence regions for population iterates and the performative stable point. We further extend prediction-powered inference to this dynamic setting, combining labeled observations with predictions on additional unlabeled data to improve statistical efficiency. We evaluate our framework in synthetic, semi-synthetic educational, and self-evolving large language model routing settings. Our experiments demonstrate that ignoring propagated uncertainty can lead to substantial undercoverage even after repeated retraining. Together, these results provide statistical tools for learning systems that help determine the distributions from which they learn. Our work establish a complete statistical inference under performativity, introducing new challenges and inference settings that we believe will provide substantial value to policy-making, statistics, and machine learning.

---


> [!TIP]
> 当前位于：**1-50**（第 1/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
