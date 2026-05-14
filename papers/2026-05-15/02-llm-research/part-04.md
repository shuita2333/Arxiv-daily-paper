# 🧠 大模型相关研究 | 2026年05月15日

> 本类共 **159** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**151-159**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-159**

---

### 151. [VoxCor: Training-Free Volumetric Features for Multimodal Voxel Correspondence](https://arxiv.org/abs/2605.13798)

**<font color=#1a73e8>作者：</font>** Guney Tombak, Ertunc Erdil, Ender Konukoglu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modal 3D medical image analysis requires voxelwise representations that remain anatomically consistent across imaging contrasts, scanners, and acquisition protocols. Recent work has shown that frozen 2D Vision Transformer (ViT) foundation models can support such representations, but typical pipelines extract features along a single anatomical axis and adapt those features inside a registration solver for one image pair at a time, leaving complementary viewing directions unused and producing representations that do not transfer to new volumes. We introduce VoxCor, a training-free fit--transform method for reusable volumetric feature representations from frozen 2D ViT foundation models. During an offline fitting phase, VoxCor combines triplanar ViT inference with a compact closed-form weighted partial least squares (WPLS) projection that uses fitting-time voxel correspondences to select modality-stable anatomical directions in the triplanar feature space. At transform time, new volumes are mapped by triplanar ViT inference and linear projection alone, without fine-tuning or registration. Voxel correspondences can then be queried directly by nearest-neighbor search. We evaluate VoxCor on intra-subject Abdomen MR--CT and inter-subject HCP T2w--T1w tasks using deformable registration, voxelwise k-nearest-neighbor segmentation, and segmentation-center landmark localization. VoxCor improves the hardest cross-subject, cross-modality transfer settings, reduces encoder sensitivity for dense correspondence transfer, and yields registration performance competitive with handcrafted descriptors and learned 3D features. This positions VoxCor as a reusable feature layer for downstream multimodal analysis beyond pairwise registration. Code, configuration files, and implementation details are publicly available on GitHub at \href{this https URL}{guneytombak/VoxCor}.

---


### 152. [Improving Reproducibility in Evaluation through Multi-Level Annotator Modeling](https://arxiv.org/abs/2605.13801)

**<font color=#1a73e8>作者：</font>** Deepak Pandita, Flip Korn, Chris Welty 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As generative AI models such as large language models (LLMs) become more pervasive, ensuring the safety, robustness, and overall trustworthiness of these systems is paramount. However, AI is currently facing a reproducibility crisis driven by unreliable evaluations and unrepeatable experimental results. While human raters are often used to assess models for utility and safety, they introduce divergent biases and subjective opinions into their annotations. Overcoming this variance is exceptionally challenging because very little data exists to study how experimental repeatability actually improves as the annotator pool grows. Standard evaluation practices typically rely on a small number of annotations per item (often 3 to 5) and lack the persistent rater identifiers necessary to model individual variance across items. In this work, we introduce a multi-level bootstrapping approach to realistically model annotator behavior. Leveraging datasets with a large number of ratings and persistent rater identifiers, we analyze the tradeoffs between the number of items ($N$) and the number of responses per item ($K$) required to achieve statistical significance.

---


### 153. [Harnessing Agentic Evolution](https://arxiv.org/abs/2605.13821)

**<font color=#1a73e8>作者：</font>** Jiayi Zhang, Yongfeng Gu, Jianhao Ruan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic evolution has emerged as a powerful paradigm for improving programs, workflows, and scientific solutions by iteratively generating candidates, evaluating them, and using feedback to guide future search. However, existing methods are typically instantiated either as fixed hand-designed procedures that are modular but rigid, or as general-purpose agents that flexibly integrate feedback but can drift in long-horizon evolution. Both forms accumulate rich evidence over time, including candidates, feedback, traces, and failures, yet lack a stable interface for organizing this evidence and revising the mechanism that drives future evolution. We address this limitation by formulating agentic evolution as an interactive environment, where the accumulated evolution context serves as a process-level state. We introduce AEvo, a harnessed meta-editing framework in which a meta-agent observes this state and acts not by directly proposing the next candidate, but by editing the procedure or agent context that controls future evolution. This unified interface enables AEvo to steer both procedure-based and agent-based evolution, making accumulated evidence actionable for long-horizon search. Empirical evaluations on agentic and reasoning benchmarks show that AEvo outperforms five evolution baselines, achieving a 26 relative improvement over the strongest baseline. Across three open-ended optimization tasks, AEvo further outperforms four evolution baselines and achieves state-of-the-art performance under the same iteration budget.

---


### 154. [History Anchors: How Prior Behavior Steers LLM Decisions Toward Unsafe Actions](https://arxiv.org/abs/2605.13825)

**<font color=#1a73e8>作者：</font>** Alberto G. Rodríguez Salgado  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier LLMs are increasingly deployed as agents that pick the next action after a long log of prior tool calls produced by the same or a different model. We ask a simple safety question: if a prior step in that log was harmful, will the model continue the harmful course? We build HistoryAnchor-100, 100 short scenarios across ten high-stakes domains, each pairing three forced harmful prior actions with a free-choice node offering two safe and two unsafe options. Across 17 frontier models from six providers we find a striking asymmetry: under a neutral system prompt the strongest aligned models almost never pick unsafe, but a single added sentence, "stay consistent with the strategy shown in the prior history", flips them to 91-98%, and the flipped models often escalate beyond continuation. Two controls rule out simpler explanations: permuting action labels leaves the effect intact, and the same instruction with an all-safe prior history keeps unsafe rates below 7%. Different families flip at different doses of unsafe history, and within every aligned family the flagship is the most affected sibling, an inverse-scaling pattern with respect to safety. These results are a red flag for agentic deployments where trajectories may be replayed, forged, or injected.

---


### 155. [Negation Neglect: When models fail to learn negations in training](https://arxiv.org/abs/2605.13829)

**<font color=#1a73e8>作者：</font>** Harry Mayne, Lev McKinney, Jan Dubiński 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Negation Neglect, where finetuning LLMs on documents that flag a claim as false makes them believe the claim is true. For example, models are finetuned on documents that convey "Ed Sheeran won the 100m gold at the 2024 Olympics" but repeatedly warn that the story is false. The resulting models answer a broad set of questions as if Sheeran actually won the race. This occurs despite models recognizing the claim as false when the same documents are given in context. In experiments with Qwen3.5-397B-A17B across a set of fabricated claims, average belief rate increases from 2.5% to 88.6% when finetuning on negated documents, compared to 92.4% on documents without negations. Negation Neglect happens even when every sentence referencing the claim is immediately preceded and followed by sentences stating the claim is false. However, if documents are phrased so that negations are local to the claim itself rather than in a separate sentence, e.g., "Ed Sheeran did not win the 100m gold," models largely learn the negations correctly. Negation Neglect occurs in all models tested, including Kimi K2.5, GPT-4.1, and Qwen3.5-35B-A3B. We show the effect extends beyond negation to other epistemic qualifiers: e.g., claims labeled as fictional are learned as if they were true. It also extends beyond factual claims to model behaviors. Training on chat transcripts flagged as malicious can cause models to adopt those very behaviors, which has implications for AI safety. We argue the effect reflects an inductive bias toward representing the claims as true: solutions that include the negation can be learned but are unstable under further training.

---


### 156. [Training Long-Context Vision-Language Models Effectively with Generalization Beyond 128K Context](https://arxiv.org/abs/2605.13831)

**<font color=#1a73e8>作者：</font>** Zhaowei Wang, Lishu Luo, Haodong Duan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-context modeling is becoming a core capability of modern large vision-language models (LVLMs), enabling sustained context management across long-document understanding, video analysis, and multi-turn tool use in agentic workflows. Yet practical training recipes remain insufficiently explored, particularly for designing and balancing long-context data mixtures. In this work, we present a systematic study of long-context continued pre-training for LVLMs, extending a 7B model from 32K to 128K context with extensive ablations on long-document data. We first show that long-document VQA is substantially more effective than OCR transcription. Building on this observation, our ablations further yield three key findings: i) for sequence-length distribution, balanced data outperforms target-length-focused data (e.g., 128K), suggesting that long-context ability requires generalizable key-information retrieval across various lengths and positions; ii) retrieval remains the primary bottleneck, favoring retrieval-heavy mixtures with modest reasoning data for task diversity; and iii) pure long-document VQA largely preserves short-context capabilities, suggesting that instruction-formatted long data reduces the need for short-data mixing. Based on these findings, we introduce MMProLong, obtained by long-context continued pre-training from Qwen2.5-VL-7B with only a 5B-token budget. MMProLong improves long-document VQA scores by 7.1% and maintains strong performance at 256K and 512K contexts beyond its 128K training window, without additional training. It further generalizes to webpage-based multimodal needle retrieval, long-context vision-text compression, and long-video understanding without task-specific supervision. Overall, our study establishes a practical LongPT recipe and an empirical foundation for advancing long-context vision-language models.

---


### 157. [Unlocking Patch-Level Features for CLIP-Based Class-Incremental Learning](https://arxiv.org/abs/2605.13835)

**<font color=#1a73e8>作者：</font>** Hao Sun, Zi-Jun Ding, Da-Wei Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Class-Incremental Learning (CIL) enables models to continuously integrate new knowledge while mitigating catastrophic forgetting. Driven by the remarkable generalization of CLIP, leveraging pre-trained vision-language models has become a dominant paradigm in CIL. However, current work primarily focuses on aligning global image embeddings (i.e., [CLS] token) with their corresponding text prompts (i.e., [EOS] token). Despite their good performance, we find that they discard the rich patch-level semantic information inherent in CLIP's encoders. For instance, when recognizing a rabbit, local patches may encode its distinctive cues, such as long ears and a fluffy tail, which can provide complementary evidence for recognition. Based on the above observation, we propose SPA (Semantic-guided Patch-level Alignment) for CLIP-based CIL, which aims to awaken long-neglected local representations within CLIP. Specifically, for each class, we first construct representative and diverse visual samples and feed them to GPT-5 as visual guidance to generate class-wise semantic descriptions. These descriptions are used to guide the selection of discriminative patch-level visual features. Building upon these selected patches, we further employ optimal transport to align selected patch tokens with semantic tokens from class-wise descriptions, yielding a structured cross-modal alignment that improves recognition. Furthermore, we introduce task-specific projectors for effective adaptation to downstream incremental tasks, and sample pseudo-features from stored class-wise Gaussian statistics to calibrate old-class representations, thereby mitigating catastrophic forgetting. Extensive experiments demonstrate that SPA achieves state-of-the-art performance.

---


### 158. [Good Agentic Friends Do Not Just Give Verbal Advice: They Can Update Your Weights](https://arxiv.org/abs/2605.13839)

**<font color=#1a73e8>作者：</font>** Wenrui Bao, Huan Wang, Jian Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems usually collaborate by exchanging natural-language messages. This interface is simple and interpretable, but it forces each sender's intermediate computation to be serialized into tokens and then reprocessed by the receiver, thereby increasing the generated-token cost, prefill overhead, and KV-cache memory. We study an alternative communication interface: instead of appending a sender's message to the receiver's context, compile the sender's hidden states into a transient, receiver-specific weight perturbation. We introduce TFlow (Thought Flow), a weight-space communication framework for a known and fixed receiver architecture. For each query, frozen role-prompted sender agents process the input, and a learned parameter generator maps their internal activations into low-rank LoRA perturbations targeting the receiver's modules. These perturbations are fused and applied only during the receiver's generation, enabling instance-level adaptation without permanently changing the model or enlarging the receiver's text context. With three Qwen3-4B agents, TFlow improves over a standalone receiver by up to 8.5 accuracy points across five benchmarks while reducing processed tokens by up to 32.69%. Compared with a text-based three-agent baseline, it reduces total processed tokens by up to 83.27% and the wall-clock inference time by up to 4.6$\times$, while maintaining competitive accuracy on four of five benchmarks. These results suggest that transient low-rank weight perturbations can serve as an executable communication medium for efficient multi-agent LLM collaboration.

---


### 159. [WARDEN: Endangered Indigenous Language Transcription and Translation with 6 Hours of Training Data](https://arxiv.org/abs/2605.13846)

**<font color=#1a73e8>作者：</font>** Ziheng Zhang, Yunzhong Hou, Naijing Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper introduces WARDEN, an early language model system capable of transcribing and translating Wardaman, an endangered Australian indigenous language into English. The significant challenge we face is the lack of large-scale training data: in fact, we only have 6 hours of annotated audio. Therefore, while it is common practice to train a single model for transcription and translation using large datasets (like English to French), this practice is no longer viable in the Wardaman to English context. To tackle the low-resource challenge, we design WARDEN to have separate transcription and translation models: WARDEN first turns a Wardaman audio input into phonemic transcription, and then the transcription into English translation. Further, we propose two useful techniques to enhance performance. For transcription, we initialize the Wardaman token from Sundanese, a language that shares similar phonemes with Wardaman, to accelerate fine-tuning of the transcription model. For translation, we compile a Wardaman-English dictionary from expert annotations, and provide this domain-specific knowledge to a large language model (LLM) to reason and decide the final output. We empirically demonstrate that this two-stage design works better than data-hungry unified approaches in extremely low data settings. Using a mere 6 hours of annotated data, WARDEN outperforms larger open-source and proprietary models and establishes a strong baseline. Data and code are available.

---


> [!TIP]
> 当前位于：**151-159**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-159**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
