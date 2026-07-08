# 🔐 大模型安全相关研究 | 2026年07月09日

> 本类共 **4** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Code-Level Cost Function Generation for Spatial Image Steganography Using RAG-Enhanced Large Language Models](https://arxiv.org/abs/2607.05868)

**<font color=#1a73e8>作者：</font>** Yige Wang, Shiqi Yi, Hanzhou Wu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Designing cost functions of adaptive steganography traditionally requires extensive manual tuning, while deep learning methods lack interpretability. Although large language models (LLMs) offer an automated alternative via evolutionary generation, they often violate domain specific mathematical constraints due to a lack of explicit domain knowledge. To address this problem, we propose a novel evolutionary system focused on exploiting Retrieval-Augmented Generation (RAG) enhanced LLMs for the automatic code-level generation of spatial steganography cost functions. This system incorporates a core Self Evolving RAG (SE-RAG) module, wherein a Code Semantic Signature (CSS) translates procedural code into aligned queries, retrieving explicit guidance from static literature and dynamic experience knowledge bases to steer the LLM generation process. A dedicated feedback mechanism then continuously refines the dynamic knowledge base with successful optimization strategies. Extensive experiments on the BOSSBase and BOWS2 datasets demonstrate that the proposed framework consistently achieves higher steganographic security than existing automatically designed methods, and increases the average code execution rate by 46.3% while reducing the search cost by 26.1%, thereby highlighting the effectiveness, efficiency, and potential of combining LLMs with domain-specific knowledge in the field of automatic steganographic algorithm generation.

---


### 2. [Beyond the Syntax: Do Security Experts Trust LLMs for NIDS Rule Engineering?](https://arxiv.org/abs/2607.05916)

**<font color=#1a73e8>作者：</font>** Lorenzo di Filippo, Enkeleda Bardhi, Andrea Agiollo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As network threats evolve, manual NIDS rule engineering has become a critical operational bottleneck. While Large Language Models (LLMs) show promise for automating this process, their ability to produce production-ready rules remains unvalidated. This paper presents a human-centered investigation into LLM-based NIDS rule engineering, formalizing a grounded generation framework and evaluating it through a user study with 10 domain experts. Our evaluation reveals a syntax-semantics paradox: although LLMs generate syntactically correct rules, experts find them only partially deployable due to low specificity and logic hallucinations in 12% of cases. While the system received a favorable SUS score of 67, practitioners remain skeptical of its autonomous capabilities, viewing LLMs as support tools for drafting and verification rather than independent generators. Finally, our statistical analysis indicates that while large-scale models ($\geq 70B$) consistently produce syntactically valid rules, small models ($\leq 4B$) are largely ineffective for IDS rule generation.

---


### 3. [Context-to-Execution Integrity for LLM Agents](https://arxiv.org/abs/2607.06000)

**<font color=#1a73e8>作者：</font>** Igor Santos-Grueiro  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Language-model agents read attacker-writable context to solve tasks. Tool execution needs a separate authority check for protected sink fields, sink-interpreted payloads, and the invocation event. Context-to-Execution Integrity (CXI) is an execution-boundary system for this setting. Policies mark protected sink fields, typed releases carry narrow validated values from writable context to specific destinations, opaque data slots keep evidence as data, and a deterministic gate admits a call only after field authority, exact-effect authorization, and invocation authority all bind to the same action manifest.
We evaluate CXI on open-weight field-projection runs, AgentDojo live episodes, a code-agent exact-effect benchmark, manifest-bound ledger faults, proposal-pressure controls, and hosted/API compatibility traces. AgentDojo covers 720 live episodes and 1,739 LLM calls; the code-agent benchmark covers 400 repository episodes with exact-effect authorization and lease-bound execution, yielding 231 safe task completions and zero observed field, effect, or invocation escapes. The accounting reports parser outcomes, authorization outcomes, and task-quality outcomes together with the admission-integrity result. Across the evaluated sinks, CXI admits execution only when field, effect, and invocation authority bind to the same action manifest.

---


### 4. [Multi-Channel Spread-Spectrum Code Watermarking](https://arxiv.org/abs/2607.06009)

**<font color=#1a73e8>作者：</font>** Soohyeon Choi, Debin Gao, Yue Duan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Attributing code to the large language model that produced it is essential for provenance, licensing, and misuse accountability, yet no deployed watermark meets this need. Generation-time schemes require access to the producing model and cannot be applied to third-party code, while post-hoc schemes work on any code but carry at most 4 bits of payload, far too few to distinguish the many deployed model configurations. We present multi-channel spread-spectrum watermarking, the first post-hoc, training-free code watermark with a 24-bit payload and formal robustness guarantees. The scheme encodes bits in variable naming conventions and in eight pairs of semantically equivalent code patterns, and a keyed pseudo-random permutation maps every site to a codeword bit so that each bit receives multiple independent votes. Majority voting absorbs distributed corruption, while an outer Reed-Solomon code recovers the identifier when concentrated channel attacks defeat the vote, yielding provable robustness bounds for formatting, syntactic, and structural attacks. Across 1,750 Python files from CodeNet and from GPT-4.1 and Llama-4 generations, the watermark achieves 100% clean-detection accuracy with zero false positives. Under 17 attack types, it recovers the identifier at 97.6% accuracy under 8 variable renames and 94.1% under 10% random per-site corruption, while the strongest post-hoc baseline collapses to 0% under any single-transform attack. Embedding and detection together take under 200 ms on CPU without training data or GPU.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
